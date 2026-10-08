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
TRAINERS = "Vương Mỹ Lượng & Bernard Osang'ir"
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
        course="Clinical Data Analysis in R - Phase I",
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
                   "of completion, signed by the trainers Vương Mỹ Lượng and Bernard Isekah Osang'ir.\n\n"
                   "**How to get it:** first complete the short [participant feedback survey]"
                   "(https://docs.google.com/forms/d/e/1FAIpQLSc6si0HLATTrUOayWTquPoTHDEcetL15qYjl_vFsKTRlxX-sQ/viewform)"
                   "{target=\"_blank\"} (about 3 minutes, anonymous). When you submit it, you will see a survey "
                   "completion code. Then, in the form below, enter that code and the email you registered with, "
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
        course="Phân tích Dữ liệu Lâm sàng bằng R - Giai đoạn I",
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
                   "Neudata, do giảng viên Vương Mỹ Lượng và Bernard Isekah Osang'ir ký.\n\n"
                   "**Cách nhận:** trước tiên, hãy hoàn thành [khảo sát ý kiến học viên]"
                   "(https://docs.google.com/forms/d/e/1FAIpQLSc6si0HLATTrUOayWTquPoTHDEcetL15qYjl_vFsKTRlxX-sQ/viewform)"
                   "{target=\"_blank\"} (khoảng 3 phút, ẩn danh). Sau khi gửi, bạn sẽ thấy mã hoàn thành khảo sát. "
                   "Sau đó, trong biểu mẫu bên dưới, nhập mã đó và email bạn đã đăng ký, sau đó nhập mã 6 chữ số "
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
            "format:\n  neudata-revealjs:\n    scrollable: true\n"
            "    include-in-header: access-gate.html\n---\n\n")
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


# ----- Free access codes (access.html; checked by the Apps Script portal) --------------------
# The materials are free; a code per person lets us count how many people use them. Emails are
# only used to send the code and are not stored by the portal.
ACCESS_S = {
    "en": dict(title="Free access to the course materials",
               intro=("All course materials are **free**. To open them, request a free access code: enter your "
                      "email and we send you a code. We only count how many people use the materials and roughly "
                      "where from: with each code we record your country and city (looked up in your browser by "
                      "the free GeoJS service) and your browser's time zone and language. **Your email address and "
                      "IP address are not stored.**"),
               step1="1. Get your free access code", email="Your email address", send="Send me a code",
               step2="2. Enter your access code", code="Access code (e.g. ABCD-2345)", unlock="Open the materials",
               forgot="Forgot your code? Request a new one above, it is free.",
               sending="Sending…", checking="Checking…",
               CODE_SENT="Your access code has been sent. Check your inbox (and spam folder), then enter it below.",
               TOO_SOON="A code was sent less than a minute ago. Please check your inbox.",
               BAD_EMAIL="Please enter a valid email address.",
               BAD_CODE="That code is not valid. Check it, or request a new one.",
               ERROR="Something went wrong. Please try again in a moment.",
               done="Access granted, opening the materials…"),
    "vi": dict(title="Truy cập miễn phí tài liệu khóa học",
               intro=("Toàn bộ tài liệu khóa học đều **miễn phí**. Để mở tài liệu, hãy yêu cầu mã truy cập miễn "
                      "phí: nhập email và chúng tôi sẽ gửi mã cho bạn. Chúng tôi chỉ đếm số người sử dụng tài "
                      "liệu và họ ở khu vực nào: với mỗi mã, chúng tôi ghi lại quốc gia và thành phố (do dịch vụ "
                      "miễn phí GeoJS xác định ngay trên trình duyệt của bạn) cùng múi giờ và ngôn ngữ của trình "
                      "duyệt. **Địa chỉ email và địa chỉ IP của bạn không được lưu lại.**"),
               step1="1. Nhận mã truy cập miễn phí", email="Địa chỉ email của bạn", send="Gửi mã cho tôi",
               step2="2. Nhập mã truy cập", code="Mã truy cập (ví dụ ABCD-2345)", unlock="Mở tài liệu",
               forgot="Quên mã? Hãy yêu cầu mã mới ở trên, hoàn toàn miễn phí.",
               sending="Đang gửi…", checking="Đang kiểm tra…",
               CODE_SENT="Mã truy cập đã được gửi. Vui lòng kiểm tra hộp thư (và thư rác), rồi nhập mã bên dưới.",
               TOO_SOON="Mã vừa được gửi chưa đầy một phút trước. Vui lòng kiểm tra hộp thư.",
               BAD_EMAIL="Vui lòng nhập địa chỉ email hợp lệ.",
               BAD_CODE="Mã không hợp lệ. Vui lòng kiểm tra lại hoặc yêu cầu mã mới.",
               ERROR="Đã xảy ra lỗi. Vui lòng thử lại sau giây lát.",
               done="Đã cấp quyền truy cập, đang mở tài liệu…"),
}


def access_page(lang, out):
    A = ACCESS_S[lang]
    msgs = {k: A[k] for k in ("CODE_SENT", "TOO_SOON", "BAD_EMAIL", "BAD_CODE", "ERROR", "done",
                               "sending", "checking", "send", "unlock")}
    import json
    html = f"""```{{=html}}
<div class="access-box">
  <h3>{A['step1']}</h3>
  <form id="acc-req" class="acc-row">
    <input id="acc-email" type="email" required autocomplete="email" placeholder="{A['email']}" aria-label="{A['email']}">
    <button id="acc-send" class="btn btn-primary" type="submit">{A['send']}</button>
  </form>
  <h3>{A['step2']}</h3>
  <form id="acc-ver" class="acc-row">
    <input id="acc-code" type="text" required autocomplete="one-time-code" placeholder="{A['code']}" aria-label="{A['code']}" style="text-transform:uppercase">
    <button id="acc-unlock" class="btn btn-primary" type="submit">{A['unlock']}</button>
  </form>
  <p class="acc-hint">{A['forgot']}</p>
  <div id="acc-msg" class="acc-msg" role="status"></div>
</div>
<style>
.access-box {{ max-width: 560px; }}
.acc-row {{ display:flex; gap:.5rem; flex-wrap:wrap; margin-bottom:1rem; }}
.acc-row input {{ flex:1 1 260px; padding:.55rem .7rem; border:1.5px solid #c9d6dc; border-radius:8px; font-size:1rem; }}
.acc-hint {{ color:#5f6f78; font-size:.92rem; }}
.acc-msg {{ display:none; padding:.7rem .9rem; border-radius:8px; margin-top:.5rem; }}
.acc-msg.ok {{ display:block; background:#EAF2F5; border-left:5px solid #055F56; }}
.acc-msg.err {{ display:block; background:#FEF3F2; border-left:5px solid #B42318; color:#7A271A; }}
</style>
<script>
(function () {{
  var API = "{CERT_PORTAL_URL}";
  var KEY = "neudata-cdar-access";
  var M = {json.dumps(msgs, ensure_ascii=False)};
  var lang = "{lang}";
  var MAX_AGE = 7 * 24 * 60 * 60 * 1000, IDLE = 2 * 60 * 60 * 1000;   // 7 days, 2 hours idle
  function fresh() {{
    try {{
      var r = JSON.parse(localStorage.getItem(KEY) || "null");
      if (!r || !r.t) return false;
      var now = Date.now();
      return (now - r.t < MAX_AGE) && (now - (r.last || r.t) < IDLE);
    }} catch (e) {{ return false; }}
  }}
  function show(kind, key) {{ var m = document.getElementById("acc-msg"); m.className = "acc-msg " + kind; m.textContent = M[key] || M.ERROR; }}
  // Approximate location for the usage counts: browser time zone and language, plus country and
  // city from GeoJS (looked up here in the browser). The IP address is never sent to Neudata.
  var geo = Promise.race([
    fetch("https://get.geojs.io/v1/ip/geo.json").then(function (r) {{ return r.json(); }})
      .then(function (g) {{ return {{ country: g.country || "", city: g.city || "" }}; }}),
    new Promise(function (res) {{ setTimeout(function () {{ res({{}}); }}, 3000); }})
  ]).catch(function () {{ return {{}}; }});
  function call(body) {{
    var tz = ""; try {{ tz = Intl.DateTimeFormat().resolvedOptions().timeZone || ""; }} catch (e) {{}}
    return geo.then(function (g) {{
      body.tz = tz; body.blang = navigator.language || ""; body.country = g.country || ""; body.city = g.city || "";
      return fetch(API, {{ method: "POST", headers: {{ "Content-Type": "text/plain;charset=utf-8" }}, body: JSON.stringify(body) }});
    }}).then(function (r) {{ return r.json(); }});
  }}
  function go() {{
    var next = new URLSearchParams(location.search).get("next") || "index.html";
    if (!/^[\\w.\\-]+\\.html/.test(next)) next = "index.html";
    location.replace(next);
  }}
  if (fresh() && new URLSearchParams(location.search).get("next")) go();
  document.getElementById("acc-req").addEventListener("submit", function (ev) {{
    ev.preventDefault();
    var b = document.getElementById("acc-send"); b.disabled = true; b.textContent = M.sending;
    call({{ action: "request", email: document.getElementById("acc-email").value.trim(), lang: lang }})
      .then(function (r) {{ show(r.ok ? "ok" : "err", r.code); if (r.ok) document.getElementById("acc-code").focus(); }})
      .catch(function () {{ show("err", "ERROR"); }})
      .finally(function () {{ b.disabled = false; b.textContent = M.send; }});
  }});
  document.getElementById("acc-ver").addEventListener("submit", function (ev) {{
    ev.preventDefault();
    var b = document.getElementById("acc-unlock"); b.disabled = true; b.textContent = M.checking;
    var code = document.getElementById("acc-code").value.trim().toUpperCase();
    call({{ action: "verify", code: code }})
      .then(function (r) {{
        if (!r.ok) {{ show("err", r.code); return; }}
        try {{ var _n = Date.now(); localStorage.setItem(KEY, JSON.stringify({{ code: code, t: _n, last: _n }})); }} catch (e) {{}}
        show("ok", "done"); setTimeout(go, 700);
      }})
      .catch(function () {{ show("err", "ERROR"); }})
      .finally(function () {{ b.disabled = false; b.textContent = M.unlock; }});
  }});
}})();
</script>
```"""
    (out / "access.qmd").write_text(
        f"---\ntitle: {yaml_str(A['title'])}\ntoc: false\n---\n\n{A['intro']}\n\n{html}\n", encoding="utf-8")


# ----- Final-assignment submission form (Apps Script web app, ?page=submit) ----------------
SUBMIT_S = {
    "en": dict(title="Submit your assignment",
               lead=("When your analysis is ready, upload it with the form at the bottom of this page. It goes "
                     "straight to the trainers, and you receive a confirmation email."),
               button="Submit",
               intro=("Upload one `.zip` file (`Surname_Phase1_Assignment.zip`) containing your script or "
                      "Quarto/R Markdown file, Table 1, figures and Results section. Maximum 20 MB."),
               newtab="Form not showing? Open the submission page in a new tab"),
    "vi": dict(title="Nộp bài tập",
               lead=("Khi bài phân tích đã sẵn sàng, hãy tải lên bằng biểu mẫu ở cuối trang này. Bài được gửi "
                     "thẳng đến các giảng viên, và bạn sẽ nhận email xác nhận."),
               button="Nộp bài",
               intro=("Tải lên một tệp `.zip` (`Surname_Phase1_Assignment.zip`) gồm script hoặc tệp "
                      "Quarto/R Markdown, Bảng 1, các hình và phần Kết quả. Tối đa 20 MB."),
               newtab="Không thấy biểu mẫu? Mở trang nộp bài trong thẻ mới"),
}


# ----- The book:"Introduction to Clinical Data Analysis in R" as the handbook -------------------
BOOK = ROOT / "Book"
BOOK_TITLE = {"en": ("Introduction to Clinical Data Analysis in R",
                     "A Practical Guide to Data Management, Statistical Analysis, and Interpretation"),
              "vi": ("Nhập môn Phân tích Dữ liệu Lâm sàng bằng R",
                     "Hướng dẫn thực hành về quản lý dữ liệu, phân tích thống kê và diễn giải kết quả")}
BOOK_CHAPTERS = ["01-r-basics", "02-data-cleaning", "03-descriptive", "04-statistical-tests", "05-regression"]
BOOK_S = {
    "en": dict(chapter="Chapter", solutions="Solutions to the exercises", objectives="Learning objectives",
               note="Clinical interpretation", tip="Good practice", warning="Common mistake",
               important="Key points", prev="Previous", next="Next", contents="Contents",
               authors="Bernard Isekah Osang'ir and Vương Mỹ Lượng",
               intro=("The participant handbook is our book **{t}**, *{s}*. Each chapter explains the "
                      "theory behind a method, shows the R code and its real output on the case-study "
                      "data, with figures and tables, and ends with exercises. Worked solutions are at the "
                      "end of the book."),
               pdf="Download the book (PDF, English)", pdf_other="Tiếng Việt (PDF)",
               overleaf="LaTeX source for Overleaf (zip)", read="Read online"),
    "vi": dict(chapter="Chương", solutions="Lời giải bài tập", objectives="Mục tiêu học tập",
               note="Diễn giải lâm sàng", tip="Thực hành tốt", warning="Lỗi thường gặp",
               important="Điểm chính", prev="Trước", next="Tiếp", contents="Mục lục",
               authors="Bernard Isekah Osang'ir và Vương Mỹ Lượng",
               intro=("Sổ tay học viên là cuốn sách **{t}**, *{s}*. Mỗi chương giải thích lý thuyết của "
                      "phương pháp, trình bày mã R và kết quả thực tế trên dữ liệu nghiên cứu tình huống, "
                      "kèm hình và bảng, và kết thúc bằng bài tập. Lời giải chi tiết nằm ở cuối sách."),
               pdf="Tải sách (PDF, tiếng Việt)", pdf_other="English (PDF)",
               overleaf="Mã nguồn LaTeX cho Overleaf (zip)", read="Đọc trực tuyến"),
}


def number_headings(md, num):
    """Prefix ## / ### headings with the book's section numbers (3.1, 3.1.1), skipping code."""
    out, fence, sec, sub = [], False, 0, 0
    for line in md.split("\n"):
        if line.lstrip().startswith("```"):
            fence = not fence
        m = None if fence else re.match(r"^(##|###)\s+(.*)$", line)
        if m and "{.unnumbered}" not in line:
            if m.group(1) == "##":
                sec, sub = sec + 1, 0
                line = f"## {num}.{sec} {m.group(2)}"
            else:
                sub += 1
                line = f"### {num}.{sec}.{sub} {m.group(2)}"
        out.append(line)
    return "\n".join(out)


def book_md_to_qmd(md, B):
    """Knitted book Markdown -> Quarto page body (callouts, figures)."""
    md = re.sub(r"^::: \{\.objectives\}\s*$", f'::: {{.callout-note .nb-objectives icon=false title="{B["objectives"]}"}}',
                md, flags=re.M)
    md = re.sub(r'^::: \{\.exercise title="([^"]*)"\}\s*$', r'::: {.callout-tip .nb-exercise icon=false title="\1"}',
                md, flags=re.M)
    for kind in ("note", "tip", "warning", "important"):
        md = re.sub(rf"^::: \{{\.callout-{kind}\}}\s*$", f'::: {{.callout-{kind} title="{B[kind]}"}}', md, flags=re.M)
    md = md.replace("](figures/", "](images/book/")
    return md


def build_book_pages(lang, out, S):
    """Write handbook.qmd (book landing page) and one page per chapter. Returns the page list."""
    B = BOOK_S[lang]
    t, s = BOOK_TITLE[lang]
    knit = BOOK / "_knit" / lang
    code = "EN" if lang == "en" else "VN"
    other = "VN" if lang == "en" else "EN"
    if not knit.exists():
        return []
    for png in (knit / "figures").glob("*.png"):
        copy(png, out / "images" / "book" / png.name)
    copy(BOOK / "references.bib", out / "references.bib")
    docs = out / "files" / "docs"
    for c in (code, other):
        pdf = BOOK / f"Introduction_to_Clinical_Data_Analysis_in_R_{c}.pdf"
        if pdf.exists():
            copy(pdf, docs / pdf.name)
    zipf = BOOK / f"Introduction_to_Clinical_Data_Analysis_in_R_{code}_overleaf.zip"
    if zipf.exists():
        copy(zipf, docs / zipf.name)

    pages = []                                    # (file, title, md)
    if (knit / "00-preface.md").exists():
        md = (knit / "00-preface.md").read_text(encoding="utf-8")
        title = re.match(r"#\s+(.*?)\s*(\{.*\})?\s*$", md.splitlines()[0]).group(1)
        pages.append(("book-preface.qmd", title, md.split("\n", 1)[1], None))
    for n, ch in enumerate(BOOK_CHAPTERS, 1):
        f = knit / f"{ch}.md"
        if f.exists():
            md = f.read_text(encoding="utf-8")
            title = re.match(r"#\s+(.*?)\s*(\{.*\})?\s*$", md.splitlines()[0]).group(1)
            pages.append((f"book-chapter{n}.qmd", f"{B['chapter']} {n}: {title}", md.split("\n", 1)[1], n))
    sols = [knit / f"sol-0{n}.md" for n in range(1, 6) if (knit / f"sol-0{n}.md").exists()]
    if sols:
        md = "\n\n".join(p.read_text(encoding="utf-8") for p in sols)
        pages.append(("book-solutions.qmd", B["solutions"], md, None))

    for k, (fname, title, md, num) in enumerate(pages):
        nav = []
        if k > 0:
            nav.append(f"[← {B['prev']}: {pages[k - 1][1]}]({pages[k - 1][0]})")
        nav.append(f"[{B['contents']}](handbook.qmd)")
        if k + 1 < len(pages):
            nav.append(f"[{B['next']}: {pages[k + 1][1]} →]({pages[k + 1][0]})")
        if num:
            md = number_headings(md, num)
        head = (f"---\ntitle: {yaml_str(title)}\nsubtitle: {yaml_str(t)}\nbibliography: references.bib\n"
                f"link-citations: true\n---\n\n")
        (out / fname).write_text(head + book_md_to_qmd(md, B) + "\n\n---\n\n" + " · ".join(nav) + "\n",
                                 encoding="utf-8")

    links = [f"| **PDF** | [{B['pdf']}](files/docs/Introduction_to_Clinical_Data_Analysis_in_R_{code}.pdf)"
             f" · [{B['pdf_other']}](files/docs/Introduction_to_Clinical_Data_Analysis_in_R_{other}.pdf) |",
             f"| **Overleaf** | [{B['overleaf']}](files/docs/{zipf.name}) |"]
    toc = "\n".join(f"{i + 1}. [{p[1]}]({p[0]})" for i, p in enumerate(pages))
    landing = (f"---\ntitle: {yaml_str(t)}\nsubtitle: {yaml_str(s)}\n---\n\n"
               f"*{B['authors']}* · Neudata\n\n" + B["intro"].format(t=t, s=s) + "\n\n"
               "| | |\n|---|---|\n" + "\n".join(links) + f"\n\n## {B['read']}\n\n" + toc + "\n")
    (out / "handbook.qmd").write_text(landing, encoding="utf-8")
    return pages


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
    copy(SHARED / "access-gate.html", out / "access-gate.html")
    access_page(lang, out)
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
              f"| **{S['slides']}** | [{S['open_slides']}](slides-day{d}.qmd), {S['f_press']} |\n"
              f"| **PowerPoint** | [{S['pptx']}](files/slides/{pptx}) |\n"
              f"| **{S['demo']}** | [day{d}_demo.R](files/scripts/day{d}_demo.R) |\n"
              f"| **{S['exercise']}** | [day{d}_exercise.R](files/practicals/day{d}_exercise.R) |\n"
              f"| **{S['solution']}** | [day{d}_solution.R](files/solutions/day{d}_solution.R) |\n"
              f"| **{S['data']}** | [{S['data']}](data.qmd) |\n")
        (out / f"day{d}.qmd").write_text(md, encoding="utf-8")

    # ---- course documents
    book_pages = build_book_pages(lang, out, S)
    if not book_pages:
        md_page(COURSE / "References" / f"participant_handbook{sfx}.md", out / "handbook.qmd", S["handbook"],
                f"[PDF](files/docs/Participant_Handbook.pdf)\n\n")
    md_page(COURSE / "References" / f"R_command_reference_sheet{sfx}.md", out / "reference.qmd", S["reference"],
            f"[PDF](files/docs/R_Command_Reference_Sheet.pdf)\n\n")
    md_page(COURSE / "References" / f"package_installation_guide{sfx}.md", out / "packages.qmd", S["packages"],
            f"[PDF](files/docs/Package_Installation_Guide.pdf)\n\n")
    md_page(COURSE / "Assignment" / f"final_assignment{sfx}.md", out / "assignment.qmd", S["assignment"],
            f"[PDF](files/docs/Final_Assignment.pdf) · [{S['slides']}](slides-assignment.qmd)\n\n")
    if CERT_PORTAL_URL:                                   # submission form (same Apps Script web app)
        submit_url = f"{CERT_PORTAL_URL}?page=submit&lang={lang}"
        A = SUBMIT_S[lang]
        _, head, body = (out / "assignment.qmd").read_text(encoding="utf-8").split("---\n", 2)
        box = (f"::: {{.callout-tip title=\"{A['title']}\"}}\n{A['lead']}\n\n"
               f"[{A['button']}](#submit){{.btn .btn-primary .btn-lg role=\"button\"}}\n:::\n\n")
        form = (f"\n\n## {A['title']} {{#submit}}\n\n{A['intro']}\n\n"
                f'```{{=html}}\n<iframe src="{submit_url}" title="{A["title"]}" '
                'style="width:100%;height:1050px;border:1px solid #d6e2e7;border-radius:12px;" '
                'loading="lazy"></iframe>\n```\n\n'
                f"[{A['newtab']}]({submit_url}){{target=\"_blank\"}}\n")
        (out / "assignment.qmd").write_text("---\n" + head + "---\n" + box + body + form, encoding="utf-8")
    md_page(COURSE / "Data" / "data_dictionary.md", out / "data.qmd", S["data"],
            "" + " · ".join(f"[{f.name}](files/data/{f.name})" for f in sorted((F / "data").iterdir())) + "\n\n")

    # ---- pre-course module
    precourse_links = {"00_READ_ME_FIRST/README.md": "precourse-guide.qmd",
                       "Data/data_dictionary.md": "precourse-data.qmd",
                       "Data/Data_Quality_Problems.md": "precourse-data.qmd"}
    md_page(PREP / f"README{sfx}.md", out / "precourse.qmd", S["precourse"], link_map=precourse_links)
    md_page(PREP / "00_READ_ME_FIRST" / f"README{sfx}.md", out / "precourse-guide.qmd", S["study_guide"],
            f"[PDF](files/precourse/Study_Guide_{'VN' if lang == 'vi' else 'EN'}.pdf) · "
            f"[Word](files/precourse/Study_Guide_{'VN' if lang == 'vi' else 'EN'}.docx)\n\n")
    md_page(PREP / "00_READ_ME_FIRST" / f"Preparation_Checklist{sfx}.md", out / "precourse-checklist.qmd",
            S["checklist"])
    md_page(PREP / "01_Install_R_and_RStudio" / f"Install_R_and_RStudio{sfx}.md", out / "install.qmd",
            S["install"], "[installation_test.R](files/precourse/installation_test.R)\n\n")
    md_page(PREP / "02_Getting_Started_with_RStudio" / f"RStudio_Beginner_Manual{sfx}.md", out / "rstudio.qmd",
            S["rstudio"])
    md_page(PREP / "Cheat_Sheets" / f"R_Cheat_Sheet{sfx}.md", out / "cheatsheet.qmd", S["cheatsheet"])
    md_page(PREP / "Cheat_Sheets" / f"Statistical_Test_Decision_Guide{sfx}.md", out / "test-guide.qmd",
            S["testguide"])
    for i, g in enumerate(("Analytical_Thinking_Framework", "Examples_by_Profession", "From_R_Output_to_Paper"), 1):
        md_page(PREP / "Guides" / f"{g}{sfx}.md", out / f"guide{i}.qmd")
    dd = PREP / "Data" / f"data_dictionary{sfx}.md"
    md_page(dd, out / "precourse-data.qmd", S["precourse_data"],
            "" + " · ".join(f"[{f.name}](files/precourse/data/{f.name})"
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
    include-in-header: access-gate.html
"""
    (out / "_quarto.yml").write_text(cfg, encoding="utf-8")
    print(f"{lang}: {len(list(out.glob('*.qmd')))} pages")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for lang in ("en", "vi"):
        build(lang)
