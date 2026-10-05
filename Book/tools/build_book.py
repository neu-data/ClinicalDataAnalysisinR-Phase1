"""Build "Introduction to Clinical Data Analysis in R" (EN and VN).

    python Book/tools/build_book.py              # knit changed chapters, build both editions
    python Book/tools/build_book.py en --force   # re-knit everything, English only
    python Book/tools/build_book.py --no-pdf     # skip the local LuaLaTeX compile

For each language:
  1. knit Book/chapters/<lang>/*.Rmd -> Book/_knit/<lang>/*.md (real R output + figures)
  2. convert to LaTeX -> Book/overleaf/<lang>/ (a complete Overleaf project)
  3. zip it -> Book/Introduction_to_Clinical_Data_Analysis_in_R_<EN|VN>_overleaf.zip
  4. compile with latexmk/LuaLaTeX -> Book/Introduction_to_Clinical_Data_Analysis_in_R_<EN|VN>.pdf
Run from the repository root.
"""
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BOOK = ROOT / "Book"
sys.path.insert(0, str(BOOK / "tools"))
from md2tex import convert  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RSCRIPT = r"C:/Program Files/R/R-4.6.1/bin/Rscript.exe"
CHAPTERS = ["01-r-basics", "02-data-cleaning", "03-descriptive", "04-statistical-tests", "05-regression"]
TITLE = "Introduction to Clinical Data Analysis in R"
SUBTITLE = "A Practical Guide to Data Management, Statistical Analysis, and Interpretation"
AUTHORS = r"Bernard Isekah Osang'ir \\[0.35em] Vương Mỹ Lượng"

TEXT = {
    "en": dict(code="EN", title=TITLE, subtitle=SUBTITLE, references="References",
               solutions="Solutions to the Exercises",
               solutions_intro=("This appendix gives worked solutions to the exercises at the end of each "
                                "chapter. Try each exercise yourself before reading the solution: there is "
                                "often more than one correct way to write the code, and comparing your "
                                "approach with ours is part of the learning."),
               colophon=("The data used throughout this book are simulated for teaching: they resemble a "
                         "real multicentre study of hypertension care, but the results illustrate methods "
                         "and are not clinical findings.\\par\\medskip Every result, table and figure in this "
                         "book was produced by the R code printed alongside it, using R, knitr and the "
                         "tidyverse, and the book was typeset with LuaLaTeX.")),
    "vi": dict(code="VN", title="Nhập môn Phân tích Dữ liệu Lâm sàng bằng R",
               subtitle="Hướng dẫn thực hành về quản lý dữ liệu, phân tích thống kê và diễn giải kết quả", references="Tài liệu tham khảo",
               solutions="Lời giải bài tập",
               solutions_intro=("Phụ lục này trình bày lời giải chi tiết cho các bài tập ở cuối mỗi chương. "
                                "Hãy tự làm từng bài trước khi đọc lời giải: thường có nhiều cách viết mã "
                                "đúng, và việc so sánh cách làm của bạn với cách làm của chúng tôi là một "
                                "phần của quá trình học."),
               colophon=("Bản tiếng Việt của \\textit{Introduction to Clinical Data Analysis in R: A Practical Guide to Data Management, Statistical Analysis, and Interpretation}.\\par\\medskip Dữ liệu dùng trong cuốn sách này là dữ liệu mô phỏng phục vụ giảng dạy: chúng "
                         "giống một nghiên cứu đa trung tâm thực tế về chăm sóc tăng huyết áp, nhưng các kết "
                         "quả chỉ minh họa phương pháp, không phải phát hiện lâm sàng.\\par\\medskip Mọi kết "
                         "quả, bảng và hình trong sách đều được tạo ra từ mã R in kèm, sử dụng R, knitr và "
                         "tidyverse; sách được dàn trang bằng LuaLaTeX.")),
}


def bib_keys():
    return set(re.findall(r"@\w+\{([^,\s]+),", (BOOK / "references.bib").read_text(encoding="utf-8")))


ONLY = None   # set with --only=name1,name2 to build a subset (e.g. while chapters are being written)


def knit(lang, name, force):
    src = BOOK / "chapters" / lang / f"{name}.Rmd"
    if ONLY is not None and name not in ONLY:
        return None
    md = BOOK / "_knit" / lang / f"{name}.md"
    if not src.exists():
        return None
    if force or not md.exists() or md.stat().st_mtime < src.stat().st_mtime:
        print(f"  knitting {lang}/{name}")
        r = subprocess.run([RSCRIPT, str(BOOK / "tools" / "knit_chapter.R"), lang, name], cwd=ROOT,
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        if r.returncode != 0:
            sys.exit(f"knit failed for {lang}/{name}:\n{r.stdout[-3000:]}\n{r.stderr[-3000:]}")
    return md.read_text(encoding="utf-8")


def build(lang, force=False, pdf=True):
    T = TEXT[lang]
    keys = bib_keys()
    proj = BOOK / "overleaf" / lang
    if proj.exists():
        shutil.rmtree(proj)
    (proj / "chapters").mkdir(parents=True)
    (proj / "figures").mkdir()
    print(f"[{lang}] knitting and converting")

    included = []
    md = knit(lang, "00-preface", force)
    if md:
        (proj / "chapters" / "00-preface.tex").write_text(convert(md, keys), encoding="utf-8")
        front = [r"\include{chapters/00-preface}"]
    else:
        front = []
    for ch in CHAPTERS:
        md = knit(lang, ch, force)
        if md:
            (proj / "chapters" / f"{ch}.tex").write_text(convert(md, keys), encoding="utf-8")
            included.append(rf"\include{{chapters/{ch}}}")
    sol_parts = []
    for n in range(1, 6):
        md = knit(lang, f"sol-0{n}", force)
        if md:
            sol_parts.append(convert(md, keys, unnumbered_sections=True))
    if sol_parts:
        sol = (rf"\chapter{{{T['solutions']}}}" + "\n\\label{ch-solutions}\n\n" + T["solutions_intro"]
               + "\n\n" + "\n\n".join(sol_parts))
        (proj / "chapters" / "solutions.tex").write_text(sol, encoding="utf-8")

    # figures (vector PDF versions)
    for f in (BOOK / "_knit" / lang / "figures").glob("*.pdf"):
        shutil.copy2(f, proj / "figures" / f.name)
    shutil.copy2(BOOK / "latex" / "neudata-logo.png", proj / "figures" / "neudata-logo.png")
    shutil.copy2(BOOK / "latex" / "neudatabook.cls", proj / "neudatabook.cls")
    shutil.copy2(BOOK / "references.bib", proj / "references.bib")
    (proj / "latexmkrc").write_text("$pdf_mode = 4;\n$postscript_mode = $dvi_mode = 0;\n", encoding="utf-8")

    appendix = "\\appendix\n\\include{chapters/solutions}\n" if sol_parts else ""
    main = rf"""% {T['title']} — {T['subtitle']}
% Compile with LuaLaTeX and biber (Overleaf: Menu > Compiler > LuaLaTeX).
\documentclass[{lang}]{{neudatabook}}
\usepackage[backend=biber, style=authoryear, maxcitenames=2, maxbibnames=10, giveninits=true,
            uniquename=false, uniquelist=false, dashed=false, doi=true, url=false]{{biblatex}}
\addbibresource{{references.bib}}

\title{{{T['title']}}}
\subtitle{{{T['subtitle']}}}
\authorlist{{{AUTHORS}}}
\date{{2026}}

\begin{{document}}
\frontmatter
\maketitle
\copyrightpage{{{T['colophon']}}}
\tableofcontents
{chr(10).join(front)}

\mainmatter
{chr(10).join(included)}

{appendix}
\backmatter
\printbibliography[heading=bibintoc, title={{{T['references']}}}]
\end{{document}}
"""
    (proj / "main.tex").write_text(main, encoding="utf-8")
    (proj / "README.md").write_text(
        f"# {T['title']} ({T['code']})\n\nOverleaf project. Upload this folder (or the zip) to Overleaf, then set "
        "**Menu → Compiler → LuaLaTeX**. `main.tex` is the main document; chapters are in `chapters/`, "
        "figures in `figures/`, references in `references.bib` (biber).\n", encoding="utf-8")

    zpath = BOOK / f"Introduction_to_Clinical_Data_Analysis_in_R_{T['code']}_overleaf.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(proj.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(proj).as_posix())
    print(f"[{lang}] Overleaf project -> {zpath.name}")

    if pdf:
        print(f"[{lang}] compiling with LuaLaTeX")
        # XeTeX on some Windows/TinyTeX setups crashes at random while loading fonts (no LaTeX
        # error in the log); retry a few times, starting clean after a crash.
        for attempt in range(6):
            r = subprocess.run(["latexmk", "-lualatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
                               cwd=proj, capture_output=True, text=True, encoding="utf-8", errors="replace")
            log = (proj / "main.log").read_text(encoding="utf-8", errors="replace") if (proj / "main.log").exists() else ""
            if r.returncode == 0 or any(l.startswith("!") for l in log.splitlines()):
                break
            print(f"[{lang}] TeX engine crashed, retrying ({attempt + 1})")
            for f in proj.glob("main.xdv"):
                f.unlink()
        if r.returncode != 0 or not (proj / "main.pdf").exists():
            errs = [l for l in log.splitlines() if l.startswith("!")][:10]
            sys.exit(f"LaTeX failed for {lang}:\n" + "\n".join(errs) + "\n" + r.stdout[-2500:])
        out = BOOK / f"Introduction_to_Clinical_Data_Analysis_in_R_{T['code']}.pdf"
        shutil.copy2(proj / "main.pdf", out)
        missing = sorted(set(re.findall(r"Missing character: There is no (.) ", log)))
        print(f"[{lang}] PDF -> {out.name}" + (f"  (missing glyphs: {''.join(missing)})" if missing else ""))
        for f in proj.glob("main.*"):
            if f.suffix not in (".tex",):
                f.unlink()


if __name__ == "__main__":
    args = sys.argv[1:]
    langs = [a for a in args if a in ("en", "vi")] or ["en", "vi"]
    for a in args:
        if a.startswith("--only="):
            ONLY = set(a[7:].split(","))
    for lang in langs:
        if (BOOK / "chapters" / lang).exists() and any((BOOK / "chapters" / lang).glob("*.Rmd")):
            build(lang, force="--force" in args, pdf="--no-pdf" not in args)
