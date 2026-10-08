# Marking Guide (Instructor Use)

## Final Take-Home Assignment: Clinical Data Analysis in R, Phase I

**Course:** Clinical Data Analysis in R - Phase I, Vương Mỹ Lượng (Senior Biostatistician, lead trainer) and Bernard Isekah Osang'ir (Senior Biostatistician), Neudata (*#ClearDataClearImpact*)
**Total:** 100 marks

This guide gives a weighted rubric, an answer key with canonical results, a common-errors penalty list, and grade bands. Mark on **correct method and sound interpretation**, not on exact second-decimal matches, package and R versions shift decimals trivially. Reward justified, well-documented decisions even where they differ slightly from the model answer.

### Weighting summary

| # | Component | Marks |
|---|-----------|------:|
| 1 | Data import & cleaning | 20 |
| 2 | Descriptive statistics & Table 1 | 15 |
| 3 | Figures | 10 |
| 4 | Statistical tests | 15 |
| 5 | Regression modelling | 20 |
| 6 | Interpretation & Results writing | 15 |
| 7 | Reproducibility & code quality | 5 |
| | **Total** | **100** |

---

## Component rubrics

### 1. Data import & cleaning: 20 marks

| Sub-criterion | Marks | Full credit | Partial | Zero |
|---|---:|---|---|---|
| Import raw file & inspect | 3 | Reads the **raw** csv/xlsx; inspects structure/dims; notes columns mis-typed by sentinels | Imports but no inspection / no comment on types | Starts from a cleaned file, or import fails |
| Remove 3 duplicates → 1,500 | 3 | Drops duplicates, confirms **1,500 unique** patients, reports count removed | De-duplicates but doesn't verify/report | Duplicates left in (1,503 rows) |
| Missing-value sentinels → NA | 4 | All of blank/`NA`/`999`/`-99` converted to `NA` in the right columns | Some sentinels handled, others missed | Sentinels left as numbers (e.g. 999 in glucose) |
| Inconsistent categories standardised | 4 | `sex`, all mixed binaries, and whitespace fields harmonised consistently | Partial harmonisation; residual variants remain | No recoding; F/Male/1/0 left mixed |
| Impossible values screened | 3 | Identifies & justifiably handles age 0/200, SBP 0/700, DBP 5, weight 7, height 17 | Handles some; rule unstated | Implausible values left in analysis |
| Dates parsed | 1 | `enroll_date` parsed to Date across all 3 formats | Partial parsing | Not parsed |
| Recode/derive + factor reference levels | 2 | BMI recomputed; sensible reference levels; education/PA ordered | Some done | None |

**Earns marks:** `na_if()` / `case_when()` used cleanly; counts reported at each step; a documented rule ("values outside physiological range set to NA").
**Loses marks:** dropping whole rows with any NA before cleaning; "fixing" by guessing values without justification; trusting the supplied `bmi`.

---

### 2. Descriptive statistics & Table 1, 15 marks

| Sub-criterion | Marks | Full credit | Partial | Zero |
|---|---:|---|---|---|
| Appropriate summaries by type | 4 | Mean±SD or median[IQR] for numeric; n(%) for categorical | Mixed/inappropriate choices | Raw dumps only |
| Table 1 stratified by `treatment_uptake` | 5 | Clean, labelled table stratified by outcome | Built but not stratified, or unlabelled | No Table 1 |
| Comparison test column | 3 | Sensible per-variable p-values included | Some tests wrong/missing | None |
| Publication quality & export | 3 | Readable units/labels; exported (docx/html/png) | Rough formatting | Not exported |

**Earns marks:** `gtsummary::tbl_summary() |> add_p()` (or flextable) with clear labels and units.
**Loses marks:** Table 1 built on all 1,500 instead of the cleaned cohort; percentages that don't account for missing; unrounded values (e.g. 47.382%).

---

### 3. Figures: 10 marks

| Sub-criterion | Marks | Full credit | Partial | Zero |
|---|---:|---|---|---|
| Two relevant figures | 4 | ≥2 figures that address the question | Only one figure | None |
| Quality (titles, axis labels, units, legibility) | 3 | Fully labelled, legible, sensible chart type | Missing labels/units | Unlabelled |
| Exported at 300 dpi | 3 | `ggsave(..., dpi = 300)` (or equivalent) evidenced | Exported but dpi not set | Not exported |

**Earns marks:** forest plot of aORs; uptake-by-determinant bar chart with counts/%; boxplot of knowledge score by uptake.
**Loses marks:** default ggplot with no labels; screenshots instead of exported files; 3-D / pie charts.

---

### 4. Statistical tests: 15 marks

| Sub-criterion | Marks | Full credit | Partial | Zero |
|---|---:|---|---|---|
| Restrict to diagnosed (`htn_diagnosed=="Yes"`) | 4 | Filters to ~**1,089**; reports n | Filters but doesn't report | Tests run on all 1,500 |
| Correct test choice | 5 | Chi-sq/Fisher for categorical; t/Wilcoxon for numeric; assumptions considered | Some mismatches | Wrong tests throughout |
| Correct execution & reporting | 4 | Statistics + p-values reported clearly | Incomplete reporting | Not reported |
| Sensible variable screening | 2 | Candidate determinants tested | Ad hoc selection | None |

**Earns marks:** Fisher used where a cell is sparse (e.g. diabetes × uptake); Wilcoxon when distribution is skewed.
**Loses marks:** chi-square on tiny expected counts without comment; using the full sample; p-values with no test named.

---

### 5. Regression modelling: 20 marks

| Sub-criterion | Marks | Full credit | Partial | Zero |
|---|---:|---|---|---|
| Univariable logistic models | 4 | Crude ORs + 95% CIs per predictor | ORs without CIs | Not done |
| Multivariable model specification | 5 | `glm(..., family=binomial)` with the pre-specified determinants, on diagnosed cohort | Some predictors missing/mis-specified | Wrong outcome/population |
| Results on OR scale | 5 | Coefficients **exponentiated** to aORs with 95% CIs | ORs without CIs | **Log-odds reported as if ORs** |
| Complete-case reporting | 2 | States ~**992** complete cases used | Not reported |, |
| Model discrimination | 4 | AUC/C-statistic reported (~**0.71**) with brief comment | Reported without comment | Absent |

**Earns marks:** `broom::tidy(model, exponentiate = TRUE, conf.int = TRUE)`; reference levels chosen so ORs read intuitively; AUC via `pROC`.
**Loses marks:** linear regression on a binary outcome; outcome reversed (No as event); reading raw `coef()` as odds ratios; dropping `diabetes` because the CI is wide.

---

### 6. Interpretation & Results writing, 15 marks

| Sub-criterion | Marks | Full credit | Partial | Zero |
|---|---:|---|---|---|
| Correct clinical reading of aORs | 6 | Direction + magnitude right; names independent determinants | Some misreads | Reversed/incorrect throughout |
| Handles non-significance correctly | 3 | Distance described as NS / inconclusive, **not** "no effect" | Loosely worded | "Distance has no effect" |
| Results section (250–400 words, manuscript style) | 4 | Integrates sample flow, Table 1, model; numbers with CIs; within word count | Present but thin / off length | Missing |
| Precision / limitations awareness | 2 | Notes wide CI on diabetes (small subgroup), confounding (residence crude vs adj) | Mentions vaguely | None |

**Earns marks:** "Diabetes was associated with over three-fold higher odds of uptake (aOR 3.56, 95% CI 1.46–9.61), though the wide CI reflects a small diabetic subgroup."
**Loses marks:** causal language ("urban residence causes uptake"); interpreting NS as proof of no association; reporting ORs without CIs in the prose.

---

### 7. Reproducibility & code quality, 5 marks

| Sub-criterion | Marks | Full credit | Partial | Zero |
|---|---:|---|---|---|
| Runs end-to-end from raw, clean session | 2 | Top-to-bottom run, no manual steps | Runs with minor fixes | Fails to run |
| Relative paths / portability | 1 | Relative paths; no machine-specific paths | Mixed | **Absolute paths** (`C:\Users\...`) |
| Readability | 1 | Commented, sectioned, libraries loaded up top | Sparse | Unstructured |
| Environment captured | 1 | `sessionInfo()` / seed where needed | Partial | None |

**Loses marks:** hard-coded absolute paths; `rm(list=ls())`/`setwd()` to a personal folder; packages used but never loaded.

---

## Model answer / answer key

> Mark for **correct method + interpretation**. CIs and directions are stable; second-decimal differences across R/package versions are **acceptable**.

**Expected sample flow**
- Imported: **1,503** rows →
- After removing 3 duplicates: **1,500** unique patients →
- Restricted to diagnosed hypertensives (`htn_diagnosed == "Yes"`): **≈ 1,089** →
- Complete cases in the adjusted model: **≈ 992**.
- Overall treatment uptake among diagnosed: **≈ 47%**.

**Canonical adjusted odds ratios (final multivariable model)**

| Predictor | aOR | 95% CI | p | Direction |
|---|---:|---|---|---|
| Age (per year) | **1.03** | 1.02–1.04 | <0.001 | ↑ uptake |
| Sex: Male (vs Female) | **0.74** | 0.56–0.97 | 0.031 | ↓ uptake (female favoured) |
| Education (linear trend) | **1.96** | 1.39–2.77 | <0.001 | ↑ with higher education |
| Residence: Urban (vs Rural) | **1.87** | 1.41–2.49 | <0.001 | ↑ uptake |
| Diabetes: Yes | **3.56** | 1.46–9.61 | 0.007 | ↑ uptake (largest effect, widest CI) |
| Family history of HTN: Yes | **1.91** | 1.44–2.54 | <0.001 | ↑ uptake |
| Health insurance: Yes | **2.05** | 1.54–2.74 | <0.001 | ↑ uptake |
| Knowledge score (per point) | **1.10** | 1.06–1.14 | <0.001 | ↑ uptake |
| Distance to facility (per km) | **0.98** | 0.96–1.01 | 0.128 | **NS** (trend ↓) |

**Model discrimination:** AUC ≈ **0.71** (acceptable).

**A correct interpretation should state:**
- Independent determinants of uptake: older age, **female** sex, higher education, urban residence, diabetes, family history, health insurance, and greater hypertension knowledge.
- **Diabetes** has the largest effect (>3× odds) but the **widest CI** (small subgroup), a precision teaching point.
- **Distance** is in the expected (protective-against-uptake) direction but **not significant** after adjustment, describe as inconclusive, not "no effect".
- Residence: comparing crude vs adjusted OR illustrates **mild confounding**.

*Accept reasonable variation in candidate-variable lists and reference coding, provided the pre-specified core determinants are present, ORs are exponentiated with CIs, and the diagnosed cohort is used.*

---

## Common errors and mark penalties

| Error | Penalty |
|---|---|
| Leaving sentinels `999` / `-99` / blanks as real numbers | **−4** (Component 1) |
| Duplicates not removed (1,503 rows analysed) | **−3** (Component 1) |
| Impossible values (age 200, SBP 700, etc.) left in | **−3** (Component 1) |
| Analysing all **1,500** instead of diagnosed hypertensives | **−4** (Component 4) and cascade if model is also wrong |
| Reporting **log-odds** instead of exponentiated ORs | **−5** (Component 5) |
| Outcome reversed / wrong event level | **−3** (Component 5) |
| Linear regression on the binary outcome | **−5** (Component 5) |
| ORs reported without 95% CIs | **−2 to −3** (Components 5/6) |
| Interpreting a **non-significant** result as "no effect" | **−3** (Component 6) |
| Causal language for a cross-sectional association | **−2** (Component 6) |
| **Absolute file paths** / `setwd()` to a personal folder | **−1** (Component 7) |
| Script fails to run top-to-bottom | **−2** (Component 7) |
| Table 1 / figures not exported | **−3** (across Components 2 & 3) |

*Penalties are capped at the marks available for the relevant component, a single mistake cannot drive a component below zero.*

---

## Grade bands

| Band | Marks | Descriptor |
|---|---|---|
| **Distinction** | 80–100 | Clean reproducible pipeline from raw data; correct cohort and sample flow; polished Table 1 and 300-dpi figures; correctly specified logistic models with exponentiated aORs and CIs; AUC reported; accurate, appropriately cautious clinical interpretation and a well-structured Results section. |
| **Merit** | 65–79 | Sound end-to-end analysis with mostly correct cleaning, the right population, and a valid adjusted model on the OR scale. Minor gaps (a missed sentinel, a thin Results section, one mis-chosen test) but conclusions are correct. |
| **Pass** | 50–64 | Core analysis attempted and broadly correct, but with notable weaknesses, incomplete cleaning, weak Table 1/figures, partial reporting of CIs, or over-stated interpretation. Demonstrates competence but not polish. |
| **Fail** | <50 | Fundamental errors: wrong population, sentinels/duplicates left in, log-odds reported as ORs, linear model on a binary outcome, or a non-reproducible/non-running submission. |
