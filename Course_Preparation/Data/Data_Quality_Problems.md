# Deliberate Data-Quality Problems in `clinical_data_raw.csv`

Real clinical data is **never** clean. To make the cleaning lessons realistic, we
deliberately introduced the problems below into `clinical_data_raw.csv`. Every
one of them is a *teaching example*: you will learn to **find** it and **fix** it
in lesson **04: Data Management**.

`clinical_data_clean.csv` is the tidy reference file with all of these resolved.

---

### 1. Duplicate records
- **3 rows are exact duplicates** of other patients (same `patient_id` and values).
- The raw file therefore has **433 rows** but only **430 unique patients**.
- **Detect:** `sum(duplicated(clinical_data_raw))` or `janitor::get_dupes()`.
- **Fix:** `dplyr::distinct()`.

### 2. Missing values
- Values were removed at random from several columns:
  `glucose` (22), `cholesterol` (18), `alcohol_use` (12), `BMI` (9),
  `followup_date` (7), `diastolic_bp` (5).
- **Detect:** `colSums(is.na(clinical_data_raw))`.
- **Fix:** decide per variable: leave as `NA`, use complete-case analysis, or impute. In this course we simply keep them as `NA` and let R ignore them with `na.rm = TRUE`.

### 3. Inconsistent categorical coding
- `sex` appears as **Female, female, F, f, Male, male, M, m**.
- `hypertension` and `diabetes` mix **Yes / No / yes / no / 1 / 0**.
- `smoking` contains a stray lower-case **"current"** alongside "Current".
- **Detect:** `table(clinical_data_raw$sex)`.
- **Fix:** `dplyr::case_when()` / `forcats` to collapse to consistent labels.

### 4. Impossible values
| Variable | Bad value | Why impossible |
|----------|-----------|----------------|
| `age` | 219 | No one is 219 years old |
| `age` | 2 | A 2-year-old is not an adult patient |
| `height_cm` | 17 | 17 cm is not a human height |
| `weight_kg` | 400 | Implausible body weight |
| `BMI` | 4.2 | BMI below ~12 is not survivable |
| `systolic_bp` | 350 | Far outside any real blood pressure |

- **Detect:** `summary()`, `range()`, boxplots, or logical checks like `age > 110`.
- **Fix:** set impossible values to `NA` (we cannot know the true value).

### 5. Extreme laboratory values
- `glucose` value of **41 mmol/L** (a real fasting glucose is rarely above ~30).
- `cholesterol` value of **−3.0 mmol/L** (a laboratory value cannot be negative).
- **Detect:** `summary()` / sort the column / boxplot.
- **Fix:** set to `NA` (data-entry error).

### 6. Date inconsistency
- For **2 patients**, `followup_date` is **before** `admission_date`.
- **Detect:** `clinical_data_raw$followup_date < clinical_data_raw$admission_date`.
- **Fix:** set the impossible follow-up date to `NA` (or query the source).

---

## The cleaning "contract" (what a clean version looks like)

After lesson 04 you should be able to turn the raw file into a dataset that:

1. has **430 unique** patients (duplicates removed);
2. uses **consistent labels** (`Female`/`Male`, `Yes`/`No`, `Never`/`Former`/`Current`);
3. has **no impossible values** (impossible ages, heights, weights, BMI, BP, labs → `NA`);
4. has **no follow-up date before admission**;
5. has a **recomputed, internally consistent `BMI`**.

The provided `clinical_data_clean.csv` is the reference answer.
