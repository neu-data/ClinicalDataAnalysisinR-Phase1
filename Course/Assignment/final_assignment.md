# Final Take-Home Assignment

## Clinical Data Analysis in R — Phase I

**Course:** Clinical Data Analysis in R — Phase I
**Trainers:** Vương Mỹ Lượng (Senior Biostatistician, lead trainer) and Bernard Isekah Osang'ir (Senior Biostatistician)
**Organisation:** Neudata — *#ClearDataClearImpact*
**Assessment type:** Individual take-home assignment (open-book, open-notes)
**Weighting:** 100 marks (see separate marking guide)

---

## 1. Overview

Over the past five days you learned to import, clean, describe, visualise, and model clinical data in R. This assignment asks you to bring those skills together in a single, end-to-end analysis that mirrors a real manuscript workflow — from a messy raw export to a publication-ready Results section.

You will work with a simulated multicentre cross-sectional study:

> **Determinants of Hypertension Treatment Uptake among Adults attending Primary Healthcare Facilities**

The study enrolled **1,500 adult attendees** across **6 primary healthcare (PHC) facilities**. The raw export (`hypertension_phc_raw.csv` / `hypertension_phc_raw.xlsx`) contains **1,503 rows** (3 duplicate records) and **36 variables** covering demographics, anthropometry, behavioural risk factors, comorbidities, laboratory biomarkers, hypertension knowledge, access barriers, and treatment indicators.

The **primary outcome** is `treatment_uptake` (currently on antihypertensive therapy: Yes / No), analysed **only among patients with a hypertension diagnosis** (`htn_diagnosed == "Yes"`, approximately 1,089 patients).

## 2. Rationale

Hypertension is a leading driver of cardiovascular morbidity, yet a large share of diagnosed patients never start or sustain treatment. Understanding *who* takes up treatment — and *which patient, clinical, and access factors* are independently associated with uptake — helps services target outreach and remove barriers. This is exactly the kind of question a clinical analyst is asked to answer from routine PHC data. The dataset deliberately contains the messiness of a real export so that you must make and justify sound data-handling decisions before any modelling.

## 3. Logistics

- **Independent work.** This is completed **on your own**, one week after the course.
- **Effort.** Budget roughly **6–10 hours**.
- **Deliverable.** A **single, fully reproducible** R script **or** Quarto / R Markdown document that runs top-to-bottom without manual intervention, **plus** the exported outputs (Table 1 and figures) and a short written **Results section**.
- **Data.** Start from the **RAW** file (`hypertension_phc_raw.csv` or `.xlsx`). Do **not** start from any cleaned/tidy reference file — cleaning is part of the assessment.
- **Tools.** Base R plus the tidyverse family is expected; you may use `gtsummary`/`gt` or `flextable` for Table 1, `ggplot2` for figures, `broom` for tidy model output, and `pROC` (or equivalent) for discrimination. Use whichever packages you are comfortable with, but **load them explicitly** at the top of your script.

## 4. The Question to Answer

> **Among adults diagnosed with hypertension attending PHC facilities, what patient, clinical, and access-related factors are independently associated with uptake of antihypertensive treatment?**

Your analysis should produce **adjusted odds ratios with 95% confidence intervals** for the determinants of `treatment_uptake`, and a clinical interpretation of which factors matter.

## 5. Tasks

Complete **all** of the following. Number your code sections to match.

1. **Import the raw data.** Read `hypertension_phc_raw.csv` (or the `.xlsx`) into R. Inspect structure, dimensions, and types. Do **not** silently coerce — note what R got wrong on import (e.g. numeric columns read as character because of sentinels).

2. **Remove duplicates.** Identify and drop the duplicate records so that you have **1,500 unique patients** (one row per `patient_id`). Report how many rows you removed.

3. **Handle missing-value sentinels.** Convert disguised missingness — blanks, `NA` strings, `999`, `-99` — to proper `NA` in the affected numeric columns (e.g. cholesterol, LDL, fasting glucose, distance). Do **not** leave sentinel codes as real numbers.

4. **Standardise inconsistent categories.** Harmonise messy text: `sex` (Female/F/female/f, Male/M/male/m → Female/Male); binary fields coded as Yes/No, Y/N and 1/0 (`diabetes`, `family_history_htn`, `health_insurance`, `htn_diagnosed`, `treatment_uptake`); and trim leading/trailing whitespace in `facility`, `residence`, `education`, `occupation`.

5. **Screen and fix impossible values.** Identify and handle biologically implausible entries: `age` (0, 200), `sbp_mmhg` (0, 700), `dbp_mmhg` (5), `weight_kg` (7), `height_cm` (17). Decide and justify whether each becomes `NA` or is corrected. State your rule.

6. **Parse dates.** Convert `enroll_date` (mixed `YYYY-MM-DD`, `DD/MM/YYYY`, `DD-Mon-YYYY` formats) into a proper Date.

7. **Recode and derive variables.** Recompute `bmi` from cleaned `height_cm` and `weight_kg` (do not trust the supplied `bmi`). Set sensible **factor reference levels** for modelling (e.g. `sex` = Female, `residence` = Rural, binaries = No). Set `education` and `physical_activity` as **ordered** factors.

8. **Descriptive statistics.** Summarise the cleaned analysis cohort. Produce a **publication-ready Table 1** of baseline characteristics **stratified by `treatment_uptake`**, with appropriate summaries (mean ± SD or median [IQR] for numeric; n (%) for categorical) and per-variable comparison tests.

9. **Figures.** Create **at least two publication-quality figures** exported at **300 dpi** (e.g. a labelled bar chart of uptake by a key determinant; a boxplot/violin of a numeric predictor by uptake; or a forest plot of the adjusted model). Figures must have titles, axis labels with units, and legible fonts.

10. **Restrict the analysis population.** Filter to **diagnosed hypertensives** (`htn_diagnosed == "Yes"`) before any inferential analysis. Report the resulting sample size.

11. **Bivariable statistical tests.** For each candidate determinant, test its unadjusted association with `treatment_uptake` using an appropriate test (chi-square / Fisher for categorical; t-test / Wilcoxon for numeric). Report test statistics and p-values.

12. **Simple (univariable) logistic regression.** Fit a logistic regression of `treatment_uptake` on each candidate predictor separately and report **crude odds ratios** with 95% CIs.

13. **Multiple (adjusted) logistic regression.** Fit a multivariable logistic model including the pre-specified determinants (age, sex, education, residence, diabetes, family history, health insurance, knowledge score, distance to facility). Report **adjusted odds ratios (aORs) with 95% CIs** and p-values on the **odds-ratio scale** (exponentiated — not log-odds). Report the number of complete cases used.

14. **Model assessment.** Report model discrimination (e.g. AUC / C-statistic) and comment briefly on fit and on any precision issues (wide CIs).

15. **Clinical interpretation.** Interpret the adjusted results clinically: which factors are independent determinants, the direction and magnitude of effect, and what is *not* significant. Avoid over-claiming.

16. **Results section.** Write a **~250–400 word** Results section in manuscript style, integrating the sample flow, Table 1 highlights, and the adjusted model. State numbers with CIs.

17. **Reproducibility.** Your script must run end-to-end from the raw file on a clean session. Use **relative paths**, set a seed if randomness is used, and capture your environment (e.g. `sessionInfo()`).

## 6. Submission Instructions

- Submit **one** analysis file: a `.R` script **or** a `.qmd` / `.Rmd` document.
- **File-naming convention:** `Surname_Phase1_Assignment.R` (or `.qmd` / `.Rmd`). Example: `Osangir_Phase1_Assignment.R`.
- Bundle your file together with exported outputs (Table 1 and the figures) and the Results section into a single `.zip` named `Surname_Phase1_Assignment.zip`.
- Email your `.zip` file to the lead trainer, **Vương Mỹ Lượng**, at **myluong.1710@gmail.com** by the stated deadline (one week after the course).

## 7. What to Submit — Checklist

- [ ] Reproducible analysis file (`Surname_Phase1_Assignment.R` / `.qmd` / `.Rmd`) that runs from the **raw** data.
- [ ] Exported **Table 1**, stratified by `treatment_uptake` (e.g. `.docx`, `.html`, or `.png`).
- [ ] **At least two figures** exported at **300 dpi** (`.png` / `.tiff` / `.pdf`).
- [ ] **Results section** (~250–400 words), as a separate file or a clearly marked section in your document.
- [ ] A short note of the **sample sizes** at each step (rows imported → after de-duplication → diagnosed → complete cases in the model).
- [ ] `sessionInfo()` output (or equivalent) for reproducibility.

## 8. Academic Integrity

This is an **individual** assessment. You may consult the course materials, the demo scripts, R help, and package documentation. You may **not** share code or written results with other participants, submit another person's work, or have someone complete it for you. If you use AI assistance or any external snippet, you must understand it, adapt it to this dataset, and be able to explain every line. Identical submissions or code you cannot explain will be treated as a breach of integrity.

---

> ### Hints — where to look (no answers given)
>
> - **Importing & first inspection:** revisit the **Day 1** demo for `read_csv()` / `readxl`, `glimpse()`, `str()`, and spotting columns read as the wrong type.
> - **Cleaning, sentinels, duplicates, dates:** the **Day 2** demo covers `distinct()`, `na_if()`, recoding with `case_when()` / `fct_recode()`, `str_trim()`, and date parsing (`lubridate`). The data dictionary's *"Known data-quality issues"* box tells you exactly which problems exist — but you must write the code.
> - **Factors & derived variables:** see the **Day 2–3** material on `factor()` levels, `relevel()`, ordered factors, and computing BMI.
> - **Table 1 & descriptives:** the **Day 3** demo shows `gtsummary::tbl_summary()` / `add_p()` (or `flextable`) and choosing the right summary per variable type.
> - **Figures:** the **Day 3–4** `ggplot2` demos cover themes, labelling, and `ggsave(..., dpi = 300)`.
> - **Tests & regression:** the **Day 4–5** demos cover `chisq.test`/`fisher.test`, `t.test`/`wilcox.test`, `glm(..., family = binomial)`, exponentiating coefficients with `broom::tidy(..., exponentiate = TRUE, conf.int = TRUE)`, and AUC with `pROC`.
> - **Reference sheet:** keep the course **R reference sheet / cheat-sheet** open for syntax reminders.
> - **Data dictionary:** `Course/Data/data_dictionary.md` defines every variable, its coding, and its role — read it before you start.
>
> *Tip:* think about your analysis as a pipeline — import → clean → derive → restrict → describe → test → model → interpret. Get each stage right before moving on, and re-run from the top often.
