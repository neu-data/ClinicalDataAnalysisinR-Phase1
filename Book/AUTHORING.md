# Authoring guide — *Introduction to Clinical Data Analysis in R*

**Book:** *Introduction to Clinical Data Analysis in R* — subtitle *A Practical Guide to Data Management, Statistical Analysis, and Interpretation*
**Authors:** Bernard Isekah Osang'ir and Vương Mỹ Lượng (Neudata)

This is a **book**, not course material. Each chapter is a self-contained, well-explained
textbook chapter that a reader can study alone. Do **not** mention registration, sessions,
dates, "Day 1", Zoom, trainers, the course portal, the certificate, or "Phase I/II".
Refer to chapters ("in Chapter 3", "the previous chapter"), never to days or sessions.

One source per chapter produces three outputs: the LaTeX book (Overleaf project + PDF),
and the HTML handbook on the course website. Write in the restricted Markdown below so
the converter can handle it.

## Files

```
Book/chapters/en/00-preface.Rmd        (unnumbered front chapter)
Book/chapters/en/01-r-basics.Rmd       Chapter 1
Book/chapters/en/02-data-cleaning.Rmd  Chapter 2
Book/chapters/en/03-descriptive.Rmd    Chapter 3
Book/chapters/en/04-statistical-tests.Rmd  Chapter 4
Book/chapters/en/05-regression.Rmd     Chapter 5
Book/chapters/en/sol-01.Rmd ... sol-05.Rmd   solutions for each chapter (appendix)
Book/chapters/vi/...                   the same names, Vietnamese edition
Book/references.bib                    shared bibliography (cite ONLY keys in this file)
```

Test a file with (from the repository root, Git Bash):

```
"/c/Program Files/R/R-4.6.1/bin/Rscript.exe" Book/tools/knit_chapter.R en 01-r-basics
```

It must finish without error. Then read `Book/_knit/en/01-r-basics.md` and check the output
looks right (tables, figures, widths). R code runs with the working directory `Course/`, so
use paths like `"Data/hypertension_phc_raw.csv"` and `"Data/analysis_data.rds"`.
**Never write into `Course/`** (no `saveRDS("Data/...")`, no `ggsave("Resources/...")`):
when demonstrating saving, write to `tempdir()` or use `eval=FALSE`.

## Markdown you may use (and nothing else)

* Chapter title: one line `# Title {#ch-shortname}` at the very top (preface: `# Preface {.unnumbered}`).
* Sections `##`, subsections `###`, sub-subsections `####`. Optional label: `## Title {#sec-name}`.
* Paragraphs; **bold**, *italic*, `inline code`, links `[text](https://...)`.
* Bullet lists (`- `) and numbered lists (`1. `), one level of nesting (indent 2 spaces).
* Maths: inline `$\bar{x}$`, display on separate lines:
  ```
  $$
  s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2}
  $$
  ```
  Use standard LaTeX maths only (amsmath). No `\begin{align}` — use `\begin{aligned}` inside `$$`.
* Citations: `[@altman1991]`, `[@altman1991; @kirkwood2003]`, page `[@altman1991, p. 45]`,
  in-text `@welch1947 showed ...`. Only keys that exist in `Book/references.bib`.
  Cite the theory: every statistical method and key concept should have at least one reference.
* Cross-references: write plain text ("see Section 3.4", "Chapter 2"), no `\ref`.
* Pipe tables written by hand, with an optional caption line before them: `Table: Caption text`.
* Callout boxes (exactly this syntax; types: `note`, `tip`, `warning`, `important`):
  ```
  ::: {.callout-note title="Clinical interpretation"}
  Text, lists and inline code are fine inside. No R chunks inside callouts.
  :::
  ```
  Use them consistently:
  - `callout-note`  → *Clinical interpretation* (what the result means for patients/practice)
  - `callout-tip`   → *Good practice* / *Tip*
  - `callout-warning` → *Common mistake*
  - `callout-important` → *Key points* (end-of-chapter summary)
* Learning objectives (first thing after the chapter's short introduction):
  ```
  ::: {.objectives}
  - Explain ...
  - Use ...
  :::
  ```
* Exercises (at the end of each chapter, under `## Exercises`), numbered by chapter:
  ```
  ::: {.exercise title="Exercise 3.1"}
  Question text. May contain lists and `code`. No R chunks.
  :::
  ```
  5–8 exercises per chapter, from easy to challenging, all answerable with the course data.

### R chunks

```{r chunk-label}
code
```

* Unique chunk labels, lowercase-with-dashes, prefixed by the chapter (`c3-age-summary`).
* Figures: give `fig.cap="..."` (a full sentence caption) and, if needed,
  `fig.width=`, `fig.height=` (inches; default 7 × 4.3). One figure per chunk.
* Tables: produce them with `knitr::kable(x, digits = 2, caption = "...")`; for gtsummary
  use `tbl |> gtsummary::as_kable(caption = "...")`. Keep tables ≤ 7 columns so they fit
  the page; abbreviate column names if needed.
* Hidden setup code (e.g. loading packages a second time): `include=FALSE`.
  Code that should be shown but not run (installing packages, `View()`, saving files into the
  project): `eval=FALSE`.
* Keep printed output short and meaningful: use `head()`, `select()`, `glimpse()` with
  care, `print(n = 6)`; output lines must stay ≤ 80 characters (already set via `options(width = 80)`).
* Comment code generously but concisely (comments are part of the teaching).
* Each chapter file is knitted in a **fresh R session**: load packages and data at the top of
  every chapter (and every solutions file).

## Content of a chapter

1. A short opening paragraph: why this matters in clinical research (the motivating question).
2. Learning objectives box.
3. Theory explained properly — definitions, intuition, formulas where useful, assumptions,
   when to use / not use — **with references**. Then the R implementation on the case-study
   data, the real output, and a careful line-by-line reading of that output.
4. Clinical interpretation callouts, good-practice tips and common-mistake warnings.
5. Figures and tables generated from the data — they make the book interesting.
6. A `## Summary` section ending with a `callout-important` *Key points* box.
7. `## Further reading` — 3–5 cited sources with one line each on why to read them.
8. `## Exercises` with 5–8 exercise boxes.

Length is not limited: be thorough and genuinely explanatory (aim for roughly
6,000–10,000 words per chapter excluding code). British English spelling.

## Solutions file (`sol-0X.Rmd`)

* No `#` chapter heading. Start with `## Chapter X: <chapter title>` and then one
  `### Exercise X.Y` per exercise with a short explanation, the R code (executed) and the
  interpretation of the output. Load packages and data at the top (chunk `include=FALSE`
  is fine, then show the essential code). Chunk labels prefixed `s3-...`.

## The case study

All examples use the course dataset: a multicentre cross-sectional study, *Determinants of
hypertension treatment uptake among adults attending primary healthcare facilities*
(1,500 adults, 6 facilities). Files in `Course/Data/`:

* `hypertension_phc_raw.csv` / `.xlsx` — raw, messy (used for import and cleaning)
* `analysis_data.rds` — clean analysis-ready data (38 variables; factors already set)
* `data_dictionary.csv` / `.md` — variable definitions and known data problems

Primary outcome `treatment_uptake` (Yes/No, reference "No") is analysed among patients with
`htn_diagnosed == "Yes"`. The data are simulated for teaching; say so where results are
interpreted (results illustrate methods, not real clinical findings).

The existing course scripts show the analyses the book must cover (and can reuse):
`Course/Scripts/day1_demo.R` … `day5_demo.R`, exercises in `Course/Practicals/`, solutions in
`Course/Solutions/`, and `Course/References/participant_handbook.md`.
