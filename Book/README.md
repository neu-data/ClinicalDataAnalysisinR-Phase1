# Introduction to Clinical Data Analysis in R

*A Practical Guide to Data Management, Statistical Analysis, and Interpretation* — Bernard Isekah Osang'ir and Vương Mỹ Lượng (Neudata)

The participant handbook, written as a book: each chapter explains the theory, shows the R code
with its real output, figures and tables on the case-study data, and ends with exercises;
worked solutions are in the appendix and every method is referenced. English and Vietnamese.

| | English | Tiếng Việt |
|---|---|---|
| PDF | [Introduction_to_Clinical_Data_Analysis_in_R_EN.pdf](Introduction_to_Clinical_Data_Analysis_in_R_EN.pdf) | [Introduction_to_Clinical_Data_Analysis_in_R_VN.pdf](Introduction_to_Clinical_Data_Analysis_in_R_VN.pdf) |
| Overleaf project | [EN zip](Introduction_to_Clinical_Data_Analysis_in_R_EN_overleaf.zip) | [VN zip](Introduction_to_Clinical_Data_Analysis_in_R_VN_overleaf.zip) |
| Online (website) | [Handbook](https://neu-data.github.io/ClinicalDataAnalysisinR-Phase1/en/handbook.html) | [Sổ tay](https://neu-data.github.io/ClinicalDataAnalysisinR-Phase1/vi/handbook.html) |

## Open in Overleaf

Upload the zip (**New Project → Upload Project**), then set **Menu → Compiler → LuaLaTeX**.
`main.tex` is the main file; the book uses the Neudata book class `neudatabook.cls`
(same house style as the Neudata report template) and biber for the references.

## How it is made

```
chapters/en/*.Rmd, chapters/vi/*.Rmd     the sources (one per chapter + solutions)
        │  tools/knit_chapter.R          runs the R code on Course/Data (real output, figures)
        ▼
_knit/<lang>/*.md + figures              knitted Markdown (also used by the website)
        │  tools/md2tex.py               converts to LaTeX for neudatabook.cls
        ▼
overleaf/<lang>/                         Overleaf project → zip, and LuaLaTeX → PDF
```

Rebuild everything (needs R 4.x with the course packages and a TeX Live/TinyTeX with LuaLaTeX):

```bash
python Book/tools/build_book.py            # both languages; --force to re-run all R code
python site/build.py                       # then refresh the website pages
```

Writing rules: [AUTHORING.md](AUTHORING.md). Vietnamese translation rules and terminology:
[TRANSLATION_VI.md](TRANSLATION_VI.md). References: [references.bib](references.bib).

The data are simulated for teaching; results illustrate methods, not clinical findings.
