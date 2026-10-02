"""Build the bilingual course website from the course source files.

    python site/build.py

Generates two Quarto website projects, site/en and site/vi, from:
  - Deck_and_Build/deckbuild/content_*.py      -> Neudata revealjs slide decks
  - Course/**/*.md, Course_Preparation/**/*.md  -> pages
  - Course_Preparation/0*/*.Rmd                 -> runnable lesson pages
  - data, scripts, exercises, solutions, PDFs   -> downloads (site/<lang>/files)

Then render with Quarto (see site/README.md). Re-run this script whenever the
course content changes. Instructor-only material (instructor manual, marking
guide, trainer notes, email templates) is deliberately NOT published.
"""
import importlib
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
SHARED = SITE / "_shared"
DECK = ROOT / "Deck_and_Build" / "deckbuild"
COURSE = ROOT / "Course"
PREP = ROOT / "Course_Preparation"

SESSION_DATES = ["08-09-2026", "15-09-2026", "22-09-2026", "29-09-2026", "06-10-2026"]
TRAINERS = "Bernard Osang'ir & My Luong Vuong"
REPO_URL = "https://github.com/neu-data/ClinicalDataAnalysisinR-Phase1"
SITE_URL = "https://neu-data.github.io/ClinicalDataAnalysisinR-Phase1"
# Certificate portal (Google Apps Script web app URL), embedded on the Certificate page.
CERT_PORTAL_URL = ("https://script.google.com/macros/s/"
                   "AKfycbyo0gY-ilc-g2PXHmEszcxyaCy6T1r7cqGhvq6hJSajmUnmvfWfexv5OKcGlbpRVSjaBA/exec")

# ----- Language strings -----------------------------------------------------------------
L = {
    "en": dict(
        suffix="", lang="en", other="vi", other_label="Tiếng Việt",
        site_title="Clinical Data Analysis in R - Phase 1",
        course="Clinical Data Analysis in R — Phase I",
        home="Home", schedule="Schedule", precourse="Pre-course", sessions="Sessions",
        materials="Materials", certificate="Certificate", slides="Slides",
        day="Day", plan="Plan", section="Section", intro_deck="Course introduction",
        assignment_deck="Final assignment", start_here="Start here", lessons="Lessons",
        open_slides="Open the slides", pptx="Download the slides (PowerPoint)",
        demo="Live-coding demo script", exercise="Practical exercise", solution="Worked solution",
        date_label="Date", time="Tuesday, 8:00–9:30 PM (Vietnam time)", agenda="Agenda",
        materials_label="Materials", downloads="Downloads", data="Course data",
        handbook="Participant handbook", reference="R command reference",
        packages="Package installation guide", assignment="Final assignment",
        install="Install R and RStudio", rstudio="Getting started with RStudio",
        checklist="Preparation checklist", study_guide="Study guide",
        cheatsheet="R cheat sheet", testguide="Choosing a statistical test",
        guides="Guides", precourse_data="Pre-course data", exercises="Exercises and solutions",
        key="Tip", f_press="Press **F** for full screen, **S** for speaker notes, **E** to print.",
        lesson="Lesson", register="Register", free="FREE", beginner="Beginner-friendly",
        online="Online", nocode="No coding experience required",
        hero_promise="A free, hands-on short course for health professionals and researchers in Vietnam",
        cert_title="Certificate of completion",
        cert_body=("Participants who attend **3 to 5 of the 5 sessions** receive a Neudata certificate "
                   "of completion, signed by the trainers My Luong Vuong and Bernard Isekah Osang'ir.\n\n"
                   "**How to get it:** in the form below, enter the email you registered with, "
                   "then the 6-digit code we email you and your official full name. Your certificate is "
                   "emailed to you as a PDF. Each certificate has a unique ID and a QR code that anyone "
                   "can scan to verify it."),
        cert_button="Generate my certificate",
        cert_newtab="Form not showing? Open the certificate portal in a new tab",
        cert_soon="The certificate portal opens after the final session.",
        dl_intro="Everything used in the course, ready to download.",
        col_session="Session", col_date="Date", col_topic="Topic", col_materials="Materials",
        session_page="Session page", files_slides="Slide decks (PowerPoint)",
        files_scripts="Scripts", files_data="Data", files_docs="Documents",
        exercise_file="Exercise", solution_file="Solution",
    ),
    "vi": dict(
        suffix="_VN", lang="vi", other="en", other_label="English",
        site_title="Phân tích Dữ liệu Lâm sàng bằng R - Giai đoạn 1",
        course="Phân tích Dữ liệu Lâm sàng bằng R — Giai đoạn I",
        home="Trang chủ", schedule="Lịch học", precourse="Chuẩn bị",
        sessions="Buổi học", materials="Tài liệu", certificate="Chứng nhận", slides="Bài giảng",
        day="Ngày", plan="Kế hoạch", section="Phần", intro_deck="Giới thiệu khóa học",
        assignment_deck="Bài tập cuối khóa", start_here="Bắt đầu tại đây", lessons="Bài học",
        open_slides="Mở bài giảng", pptx="Tải bài giảng (PowerPoint)",
        demo="Mã minh họa trực tiếp", exercise="Bài thực hành", solution="Lời giải mẫu",
        date_label="Ngày", time="Thứ Ba, 20:00–21:30 (giờ Việt Nam)", agenda="Nội dung",
        materials_label="Tài liệu", downloads="Tải xuống", data="Dữ liệu khóa học",
        handbook="Sổ tay học viên", reference="Tra cứu lệnh R",
        packages="Hướng dẫn cài đặt gói", assignment="Bài tập cuối khóa",
        install="Cài đặt R và RStudio", rstudio="Làm quen với RStudio",
        checklist="Danh sách chuẩn bị", study_guide="Hướng dẫn học tập",
        cheatsheet="Tóm tắt lệnh R", testguide="Chọn kiểm định thống kê",
        guides="Hướng dẫn", precourse_data="Dữ liệu chuẩn bị", exercises="Bài tập và lời giải",
        key="Mẹo", f_press="Nhấn **F** để toàn màn hình, **S** để xem ghi chú, **E** để in.",
        lesson="Bài", register="Đăng ký", free="MIỄN PHÍ", beginner="Dành cho người mới",
        online="Trực tuyến", nocode="Không cần kinh nghiệm lập trình",
        hero_promise="Khóa học ngắn miễn phí, thực hành cho nhân viên y tế và nhà nghiên cứu tại Việt Nam",
        cert_title="Chứng nhận hoàn thành",
        cert_body=("Học viên tham dự **từ 3 đến 5 trên 5 buổi học** sẽ nhận chứng nhận hoàn thành của "
                   "Neudata, do giảng viên My Luong Vuong và Bernard Isekah Osang'ir ký.\n\n"
                   "**Cách nhận:** trong biểu mẫu bên dưới, nhập email bạn đã đăng ký, sau đó nhập mã 6 chữ số "
                   "chúng tôi gửi qua email và họ tên chính thức của bạn. Chứng nhận sẽ được gửi đến email "
                   "của bạn dưới dạng PDF. Mỗi chứng nhận có mã số riêng và mã QR để bất kỳ ai cũng có thể "
                   "quét để xác minh."),
        cert_button="Tạo chứng nhận của tôi",
        cert_newtab="Không thấy biểu mẫu? Mở cổng chứng nhận trong thẻ mới",
        cert_soon="Cổng chứng nhận sẽ mở sau buổi học cuối cùng.",
        dl_intro="Toàn bộ tài liệu dùng trong khóa học, sẵn sàng để tải xuống.",
        col_session="Buổi", col_date="Ngày", col_topic="Chủ đề", col_materials="Tài liệu",
        session_page="Trang buổi học", files_slides="Bài giảng (PowerPoint)",
        files_scripts="Mã R", files_data="Dữ liệu", files_docs="Tài liệu",
        exercise_file="Bài tập", solution_file="Lời giải",
    ),
}

# ----- Markdown helpers ---------------------------------------------------------------------
ESCAPE = set("\\*_$@<>[]~^#|")


def esc(text):
    """Escape prose for Pandoc markdown, keeping `code spans` intact."""
    parts = str(text).split("`")
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            out.append("`" + part + "`")
        else:
            out.append("".join("\\" + ch if ch in ESCAPE else ch for ch in part))
    return "".join(out)


def fmt_line(line):
    if isinstance(line, dict):
        t = esc(line.get("text", ""))
        if line.get("color"):
            t = f'[{t}]{{style="color:#{line["color"]}"}}'
        if line.get("bold"):
            t = f"**{t}**"
        return t
    return esc(line)


def yaml_str(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def notes(spec):
    n = spec.get("notes")
    if not n:
        return ""
    paras = "\n\n".join(esc(p) for p in str(n).split("\n") if p.strip())
    return f"\n::: {{.notes}}\n{paras}\n:::\n"


CALLOUT = {"tip": "tip", "warning": "warning", "mistake": "important",
           "interpretation": "note", "note": "note"}


def block_md(b):
    lines = b.get("lines", [])
    if "callout" in b:
        kind = CALLOUT.get(b["callout"], "note")
        body = "\n\n".join(fmt_line(x) for x in lines)
        return f"::: {{.callout-{kind}}}\n## {esc(b.get('header', ''))}\n{body}\n:::\n"
    out = []
    if b.get("header"):
        out.append(f"### {esc(b['header'])}\n")
    if b.get("bullets"):
        out += [f"- {fmt_line(x)}" for x in lines]
    else:
        out += [f"| {fmt_line(x)}" for x in lines]
    return "\n".join(out) + "\n"


def column_md(col):
    out = []
    if col.get("header"):
        out.append(f"### {esc(col['header'])}\n")
    lines = col.get("lines", [])
    if col.get("bullets", True):
        out += [f"- {fmt_line(x)}" for x in lines]
    else:
        out += [f"| {fmt_line(x)}" for x in lines]
    return "\n".join(out)


def slide_md(spec, lang):
    t = spec["type"]
    S = L[lang]
    title = esc(spec.get("title", ""))
    if t == "divider":
        md = f"# {title}\n"
        if spec.get("agenda"):
            plan = esc(spec.get("plan_title") or S["plan"])
            items = "\n".join(f"- {fmt_line(a)}" for a in spec["agenda"])
            md += f"\n## {plan}\n\n{items}\n"
        return md + notes(spec)
    if t in ("title", "closing"):
        return ""

    heavy = False
    body = ""
    if t == "content":
        blocks = spec.get("blocks", [])
        n_lines = sum(len(b.get("lines", [])) + 1 for b in blocks)
        heavy = n_lines > 9
        body = "\n".join(block_md(b) for b in blocks)
    elif t == "bullets":
        items = []
        for it in spec.get("items", []):
            if isinstance(it, dict):
                items.append("    " * int(it.get("level", 0)) + f"- {fmt_line(it)}")
            else:
                items.append(f"- {fmt_line(it)}")
        heavy = len(items) > 7
        body = "\n".join(items) + "\n"
    elif t == "two_column":
        heavy = max(len(spec["left"].get("lines", [])), len(spec["right"].get("lines", []))) > 6
        body = (":::: {.columns}\n::: {.column width=\"50%\"}\n" + column_md(spec["left"]) +
                "\n:::\n::: {.column width=\"50%\"}\n" + column_md(spec["right"]) + "\n:::\n::::\n")
    elif t == "code":
        body = f"```r\n{spec['code']}\n```\n"
        if spec.get("output"):
            body += f"\n```{{.text .code-output}}\n{spec['output']}\n```\n"
        if spec.get("note"):
            body += f"\n::: {{.code-note}}\n{esc(spec['note'])}\n:::\n"
        heavy = spec["code"].count("\n") + str(spec.get("output", "")).count("\n") > 10
    elif t == "image":
        img = f"![](images/resources/{spec['image']}){{width=100%}}"
        if spec.get("side_notes"):
            side = (f"### {esc(spec.get('side_header', ''))}\n\n" +
                    "\n".join(f"- {fmt_line(x)}" for x in spec["side_notes"]))
            body = (":::: {.columns}\n::: {.column width=\"38%\"}\n" + side +
                    "\n:::\n::: {.column width=\"62%\"}\n" + img + "\n:::\n::::\n")
        else:
            cap = esc(spec.get("caption", ""))
            body = f"![{cap}](images/resources/{spec['image']}){{fig-align=\"center\" width=\"75%\"}}\n"
    elif t == "table":
        hdr = "| " + " | ".join(esc(h) for h in spec["headers"]) + " |"
        sep = "|" + "|".join(":---" for _ in spec["headers"]) + "|"
        rows = ["| " + " | ".join(fmt_line(c) for c in r) + " |" for r in spec["rows"]]
        body = "\n".join([hdr, sep] + rows) + "\n"
        if spec.get("caption"):
            body += f"\n: {esc(spec['caption'])}\n"
        heavy = len(spec["rows"]) > 5
    intro = f"[{esc(spec['intro'])}]{{.slide-intro}}\n\n" if spec.get("intro") else ""
    cls = " {.smaller}" if heavy else ""
    return f"## {title}{cls}\n\n{intro}{body}{notes(spec)}"


def load_slides(module, lang):
    sys.path.insert(0, str(DECK))
    name = module + L[lang]["suffix"]
    mod = importlib.import_module(name)
    return [v for k, v in vars(mod).items() if k.startswith("SLIDES")][0]


def deck(path, lang, title, subtitle, date, slides):
    S = L[lang]
    head = (f"---\ntitle: {yaml_str(title)}\nsubtitle: {yaml_str(subtitle)}\n"
            f"author: {yaml_str(TRAINERS)}\ninstitute: \"Neudata Consulting Ltd\"\n"
            f"date: {yaml_str(date)}\nlang: {S['lang']}\nsection-label: {yaml_str(S['section'])}\n"
            "format:\n  neudata-revealjs:\n    scrollable: true\n---\n\n")
    body = "\n".join(slide_md(s, lang) for s in slides)
    path.write_text(head + body, encoding="utf-8")


# ----- Pages from markdown documents ---------------------------------------------------------
def md_page(src, dest, title=None, extra_top="", link_map=None):
    text = src.read_text(encoding="utf-8")
    m = re.search(r"^#\s+(.+)$", text, flags=re.M)
    if title is None:
        title = re.sub(r"[*`]", "", m.group(1)).strip() if m else src.stem.replace("_", " ")
    if m:
        text = text[:m.start()] + text[m.end():]
    text = re.sub(r'<div align="center">\s*', "", text)
    text = re.sub(r"\s*</div>", "", text)
    for old, new in (link_map or {}).items():
        text = text.replace(f"]({old})", f"]({new})")
    dest.write_text(f"---\ntitle: {yaml_str(title)}\n---\n\n{extra_top}{text.lstrip()}", encoding="utf-8")


def rmd_page(src, dest):
    """Convert a pre-course R Markdown lesson into a runnable Quarto page."""
    text = src.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, flags=re.S)
    yaml, body = (m.group(1), text[m.end():]) if m else ("", text)
    keep = [ln for ln in yaml.splitlines() if re.match(r"^(title|subtitle|author|date):", ln)]
    # Run the code from the lesson's original folder, so its "../Data/..." paths work and the
    # code shown on the page is exactly what learners type in their own course project.
    lesson_dir = Path("..", "..", src.parent.relative_to(ROOT)).as_posix()
    head = ("\n".join(keep) + "\nexecute:\n  echo: true\n  warning: false\n  message: false\n"
            f"knitr:\n  opts_knit:\n    root.dir: \"{lesson_dir}\"\n")
    dest.write_text(f"---\n{head}---\n{body}", encoding="utf-8")


def copy(src, dest):
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)


# ----- Build one language -----------------------------------------------------------------
def build(lang):
    S = L[lang]
    sfx = S["suffix"]
    out = SITE / lang
    for sub in ("files", "images"):
        shutil.rmtree(out / sub, ignore_errors=True)
    for f in out.glob("*.qmd"):
        f.unlink()
    out.mkdir(exist_ok=True)

    # shared look
    shutil.rmtree(out / "_extensions", ignore_errors=True)
    shutil.copytree(SHARED / "_extensions", out / "_extensions")
    copy(SHARED / "course.scss", out / "course.scss")
    copy(SHARED / "neudata-logo.png", out / "images" / "neudata-logo.png")
    copy(SHARED / "lang-switch.html", out / "lang-switch.html")
    for png in (COURSE / "Resources").glob("*.png"):
        copy(png, out / "images" / "resources" / png.name)
    copy(COURSE / "Images" / "Course_Poster.png", out / "images" / "course-poster.png")

    # downloads
    F = out / "files"
    for f in (COURSE / "Data").iterdir():
        if f.suffix in (".csv", ".xlsx", ".rds", ".pdf"):
            copy(f, F / "data" / f.name)
    for folder in ("Scripts", "Practicals", "Solutions"):
        for f in (COURSE / folder).glob("*.R"):
            copy(f, F / folder.lower() / f.name)
    for pdf in ("Participant_Handbook.pdf", "R_Command_Reference_Sheet.pdf", "Package_Installation_Guide.pdf"):
        copy(COURSE / "References" / pdf, F / "docs" / pdf)
    copy(COURSE / "Assignment" / "Final_Assignment.pdf", F / "docs" / "Final_Assignment.pdf")
    copy(COURSE / "Course_Orientation_EN.pdf", F / "docs" / "Course_Orientation_EN.pdf")
    pptx = f"Clinical_Data_Analysis_in_R_Phase1{sfx}.pptx"
    copy(ROOT / "Deck_and_Build" / "Slides" / pptx, F / "slides" / pptx)
    for f in (PREP / "Data").iterdir():
        if f.suffix in (".csv", ".xlsx"):
            copy(f, F / "precourse" / "data" / f.name)
    for folder in ("Exercises", "Solutions"):
        for f in (PREP / folder).glob("*.R"):
            if f.stem.endswith("_VN") == (lang == "vi"):
                copy(f, F / "precourse" / folder.lower() / f.name)
    for ext in ("pdf", "docx"):
        g = PREP / "00_READ_ME_FIRST" / f"Study_Guide_{'VN' if lang == 'vi' else 'EN'}.{ext}"
        copy(g, F / "precourse" / g.name)
    copy(PREP / "01_Install_R_and_RStudio" / "installation_test.R", F / "precourse" / "installation_test.R")

    # ---- slide decks
    sub = S["course"]
    front = load_slides("content_front", lang)
    t = front[0]
    deck(out / "slides-intro.qmd", lang, " ".join(t["title"]), t["subtitle"][0],
         SESSION_DATES[0], front)
    day_titles = []
    for d in range(1, 6):
        sl = load_slides(f"content_day{d}", lang)
        day_titles.append(sl[0]["title"])
        deck(out / f"slides-day{d}.qmd", lang, sl[0]["title"], sub, SESSION_DATES[d - 1], sl)
    asg = load_slides("content_assignment", lang)
    deck(out / "slides-assignment.qmd", lang, asg[0]["title"], sub, SESSION_DATES[4], asg)

    # ---- home
    hero = (
        "::: {.course-hero}\n"
        f"# {S['site_title']}\n{S['hero_promise']}\n\n"
        "::: {.badges}\n"
        f"[{S['free']}]{{}} [{S['beginner']}]{{}} [{S['online']}]{{}} [{S['nocode']}]{{}}\n"
        ":::\n\n"
        f"[{S['schedule']}](schedule.qmd){{.btn .btn-light role=\"button\"}}\n"
        ":::\n\n"
    )
    readme = ROOT / ("README_VN.md" if lang == "vi" else "README.md")
    text = readme.read_text(encoding="utf-8")
    text = re.sub(r'^<div align="center">.*?</div>\s*(---\s*)?', "", text, flags=re.S)
    (out / "index.qmd").write_text(
        f"---\npagetitle: {yaml_str(S['site_title'])}\ntoc: false\n---\n\n{hero}"
        f"![](images/course-poster.png){{.float-end width=\"34%\" style=\"margin:0 0 1rem 1.5rem\"}}\n\n"
        f"{text}", encoding="utf-8")

    # ---- schedule
    rows = []
    for d in range(1, 6):
        topic = day_titles[d - 1].split(":", 1)[-1].strip()
        rows.append(f"| {d} | {SESSION_DATES[d - 1]} | {esc(topic)} | "
                    f"[{S['session_page']}](day{d}.qmd) · [{S['slides']}](slides-day{d}.qmd) |")
    (out / "schedule.qmd").write_text(
        f"---\ntitle: {yaml_str(S['schedule'])}\n---\n\n**{S['time']}**\n\n"
        f"| {S['col_session']} | {S['col_date']} | {S['col_topic']} | {S['col_materials']} |\n"
        "|:--:|:--|:--|:--|\n" + "\n".join(rows) + "\n\n"
        f"- [{S['intro_deck']}](slides-intro.qmd)\n- [{S['assignment_deck']}](slides-assignment.qmd)"
        f" · [{S['assignment']}](assignment.qmd)\n", encoding="utf-8")

    # ---- session pages
    for d in range(1, 6):
        sl = load_slides(f"content_day{d}", lang)
        agenda = "\n".join(f"- {fmt_line(a)}" for a in sl[0].get("agenda", []))
        md = (f"---\ntitle: {yaml_str(day_titles[d - 1])}\n---\n\n"
              f"**{S['date_label']}:** {SESSION_DATES[d - 1]} · {S['time']}\n\n"
              f"## {S['agenda']}\n\n{agenda}\n\n## {S['materials_label']}\n\n"
              f"| | |\n|:--|:--|\n"
              f"| 🎞️ **{S['slides']}** | [{S['open_slides']}](slides-day{d}.qmd) — {S['f_press']} |\n"
              f"| 📥 **PowerPoint** | [{S['pptx']}](files/slides/{pptx}) |\n"
              f"| 💻 **{S['demo']}** | [day{d}_demo.R](files/scripts/day{d}_demo.R) |\n"
              f"| 🧪 **{S['exercise']}** | [day{d}_exercise.R](files/practicals/day{d}_exercise.R) |\n"
              f"| ✅ **{S['solution']}** | [day{d}_solution.R](files/solutions/day{d}_solution.R) |\n"
              f"| 📁 **{S['data']}** | [{S['data']}](data.qmd) |\n")
        (out / f"day{d}.qmd").write_text(md, encoding="utf-8")

    # ---- course documents
    md_page(COURSE / "References" / f"participant_handbook{sfx}.md", out / "handbook.qmd", S["handbook"],
            f"📥 [PDF](files/docs/Participant_Handbook.pdf)\n\n")
    md_page(COURSE / "References" / f"R_command_reference_sheet{sfx}.md", out / "reference.qmd", S["reference"],
            f"📥 [PDF](files/docs/R_Command_Reference_Sheet.pdf)\n\n")
    md_page(COURSE / "References" / f"package_installation_guide{sfx}.md", out / "packages.qmd", S["packages"],
            f"📥 [PDF](files/docs/Package_Installation_Guide.pdf)\n\n")
    md_page(COURSE / "Assignment" / f"final_assignment{sfx}.md", out / "assignment.qmd", S["assignment"],
            f"📥 [PDF](files/docs/Final_Assignment.pdf) · 🎞️ [{S['slides']}](slides-assignment.qmd)\n\n")
    md_page(COURSE / "Data" / "data_dictionary.md", out / "data.qmd", S["data"],
            "📥 " + " · ".join(f"[{f.name}](files/data/{f.name})" for f in sorted((F / "data").iterdir())) + "\n\n")

    # ---- pre-course module
    precourse_links = {"00_READ_ME_FIRST/README.md": "precourse-guide.qmd",
                       "Data/data_dictionary.md": "precourse-data.qmd",
                       "Data/Data_Quality_Problems.md": "precourse-data.qmd"}
    md_page(PREP / f"README{sfx}.md", out / "precourse.qmd", S["precourse"], link_map=precourse_links)
    md_page(PREP / "00_READ_ME_FIRST" / f"README{sfx}.md", out / "precourse-guide.qmd", S["study_guide"],
            f"📥 [PDF](files/precourse/Study_Guide_{'VN' if lang == 'vi' else 'EN'}.pdf) · "
            f"[Word](files/precourse/Study_Guide_{'VN' if lang == 'vi' else 'EN'}.docx)\n\n")
    md_page(PREP / "00_READ_ME_FIRST" / f"Preparation_Checklist{sfx}.md", out / "precourse-checklist.qmd",
            S["checklist"])
    md_page(PREP / "01_Install_R_and_RStudio" / f"Install_R_and_RStudio{sfx}.md", out / "install.qmd",
            S["install"], "📥 [installation_test.R](files/precourse/installation_test.R)\n\n")
    md_page(PREP / "02_Getting_Started_with_RStudio" / f"RStudio_Beginner_Manual{sfx}.md", out / "rstudio.qmd",
            S["rstudio"])
    md_page(PREP / "Cheat_Sheets" / f"R_Cheat_Sheet{sfx}.md", out / "cheatsheet.qmd", S["cheatsheet"])
    md_page(PREP / "Cheat_Sheets" / f"Statistical_Test_Decision_Guide{sfx}.md", out / "test-guide.qmd",
            S["testguide"])
    for i, g in enumerate(("Analytical_Thinking_Framework", "Examples_by_Profession", "From_R_Output_to_Paper"), 1):
        md_page(PREP / "Guides" / f"{g}{sfx}.md", out / f"guide{i}.qmd")
    dd = PREP / "Data" / f"data_dictionary{sfx}.md"
    md_page(dd, out / "precourse-data.qmd", S["precourse_data"],
            "📥 " + " · ".join(f"[{f.name}](files/precourse/data/{f.name})"
                              for f in sorted((F / "precourse" / "data").iterdir())) + "\n\n")
    dq = (PREP / "Data" / f"Data_Quality_Problems{sfx}.md").read_text(encoding="utf-8")
    with open(out / "precourse-data.qmd", "a", encoding="utf-8") as fh:
        fh.write("\n\n" + re.sub(r"^#\s", "## ", dq, flags=re.M))
    ex = sorted((F / "precourse" / "exercises").glob("*.R"))
    so = sorted((F / "precourse" / "solutions").glob("*.R"))
    rows = "\n".join(f"| [{e.name}](files/precourse/exercises/{e.name}) | [{s.name}](files/precourse/solutions/{s.name}) |"
                     for e, s in zip(ex, so))
    (out / "precourse-exercises.qmd").write_text(
        f"---\ntitle: {yaml_str(S['exercises'])}\n---\n\n| {S['exercise_file']} | {S['solution_file']} |\n|:--|:--|\n{rows}\n",
        encoding="utf-8")
    lessons = sorted(PREP.glob(f"0[3-7]_*/*.Rmd"))
    lessons = [p for p in lessons if p.stem.endswith("_VN") == (lang == "vi")]
    for i, p in enumerate(lessons, 1):
        rmd_page(p, out / f"lesson{i}.qmd")

    # ---- certificate and downloads
    if CERT_PORTAL_URL:
        portal = f"{CERT_PORTAL_URL}?lang={lang}"
        title = S["cert_button"]
        # button opens the portal in this page's language; the same form is embedded below it
        action = (f"[{title}]({portal}){{.btn .btn-primary .btn-lg role=\"button\" target=\"_blank\"}}\n\n"
                  f'```{{=html}}\n<iframe src="{portal}" title="{title}" '
                  'style="width:100%;height:860px;border:1px solid #d6e2e7;border-radius:12px;margin-top:1rem;" '
                  'loading="lazy"></iframe>\n```\n\n'
                  f"[{S['cert_newtab']}]({portal}){{target=\"_blank\"}}")
    else:
        action = f"*{S['cert_soon']}*"
    (out / "certificate.qmd").write_text(
        f"---\ntitle: {yaml_str(S['cert_title'])}\n---\n\n{S['cert_body']}\n\n{action}\n", encoding="utf-8")
    sections = [(S["files_slides"], "slides"), (S["files_scripts"], "scripts"),
                (S["exercise"], "practicals"), (S["solution"], "solutions"),
                (S["files_data"], "data"), (S["files_docs"], "docs")]
    dl = [f"---\ntitle: {yaml_str(S['downloads'])}\n---\n\n{S['dl_intro']}\n"]
    for label, folder in sections:
        dl.append(f"\n## {label}\n")
        dl += [f"- [{f.name}](files/{folder}/{f.name})" for f in sorted((F / folder).iterdir())]
    (out / "downloads.qmd").write_text("\n".join(dl) + "\n", encoding="utf-8")

    # ---- project config
    lesson_titles = []
    for i, p in enumerate(lessons, 1):
        m = re.search(r'^title:\s*"?(.*?)"?\s*$', p.read_text(encoding="utf-8"), flags=re.M)
        lesson_titles.append((f"lesson{i}.qmd", m.group(1).replace('"', "'") if m else f"{S['lesson']} {i}"))
    guide_titles = []
    for i in range(1, 4):
        m = re.search(r'^title:\s*"(.*)"\s*$', (out / f"guide{i}.qmd").read_text(encoding="utf-8"), flags=re.M)
        guide_titles.append((f"guide{i}.qmd", m.group(1).replace('\\"', "'") if m else f"{S['guides']} {i}"))
    menu = lambda items: "\n".join(f"          - href: {h}\n            text: {yaml_str(t)}" for h, t in items)
    cfg = f"""project:
  type: website
  output-dir: _site

lang: {S['lang']}

execute:
  freeze: auto

website:
  title: {yaml_str(S['site_title'])}
  site-url: "{SITE_URL}/{lang}/"
  repo-url: "{REPO_URL}"
  favicon: images/neudata-logo.png
  search: true
  page-navigation: true
  navbar:
    logo: images/neudata-logo.png
    logo-alt: "Neudata Consulting Ltd"
    title: false
    background: "#04242F"
    foreground: "#FFFFFF"
    left:
      - href: index.qmd
        text: {yaml_str(S['home'])}
      - href: schedule.qmd
        text: {yaml_str(S['schedule'])}
      - text: {yaml_str(S['precourse'])}
        menu:
{menu([("precourse.qmd", S['start_here']), ("precourse-guide.qmd", S['study_guide']),
       ("precourse-checklist.qmd", S['checklist']), ("install.qmd", S['install']),
       ("rstudio.qmd", S['rstudio'])] + lesson_titles +
      [("precourse-exercises.qmd", S['exercises']), ("precourse-data.qmd", S['precourse_data']),
       ("cheatsheet.qmd", S['cheatsheet']), ("test-guide.qmd", S['testguide'])] + guide_titles)}
      - text: {yaml_str(S['sessions'])}
        menu:
{menu([("slides-intro.qmd", S['intro_deck'])] + [(f"day{d}.qmd", day_titles[d - 1]) for d in range(1, 6)] +
      [("slides-assignment.qmd", S['assignment_deck'])])}
      - text: {yaml_str(S['materials'])}
        menu:
{menu([("handbook.qmd", S['handbook']), ("reference.qmd", S['reference']), ("packages.qmd", S['packages']),
       ("data.qmd", S['data']), ("assignment.qmd", S['assignment']), ("downloads.qmd", S['downloads'])])}
      - href: certificate.qmd
        text: {yaml_str(S['certificate'])}
    right:
      - href: ../{S['other']}/index.html
        text: {yaml_str(S['other_label'])}
      - icon: globe
        href: https://www.neu-data.com
        aria-label: Neudata
  page-footer:
    left: "**Neudata Consulting Ltd** · *Insight. Impact. Innovation.*"
    center: "Neudata | #ClearDataClearImpact"
    right: "[www.neu-data.com](https://www.neu-data.com) · [contact@neu-data.com](mailto:contact@neu-data.com)"

format:
  html:
    theme: [cosmo, course.scss]
    toc: true
    code-copy: true
    code-overflow: wrap
    include-after-body: lang-switch.html
"""
    (out / "_quarto.yml").write_text(cfg, encoding="utf-8")
    print(f"{lang}: {len(list(out.glob('*.qmd')))} pages")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for lang in ("en", "vi"):
        build(lang)
