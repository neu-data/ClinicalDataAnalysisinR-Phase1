## Chapter 2: Understanding and Cleaning Clinical Data



The solutions below start either from the raw file or from the clean analysis file,
as each exercise requires. We load the packages and both datasets once.


``` r
library(tidyverse)
library(lubridate)

na_codes <- c("", "NA", "999", "-99")
raw_default  <- read_csv("Data/hypertension_phc_raw.csv")
raw          <- read_csv("Data/hypertension_phc_raw.csv", na = na_codes)
analysis_data <- readRDS("Data/analysis_data.rds")

# The Yes/No helper from Section 2.6
to_yesno <- function(x) {
  x <- str_to_lower(str_trim(as.character(x)))
  case_when(
    x %in% c("yes", "y", "1", "true")  ~ "Yes",
    x %in% c("no",  "n", "0", "false") ~ "No",
    TRUE ~ NA_character_
  )
}
```

### Exercise 2.1

We write a small summary function and apply it to both imports, so that the two rows
of the result are directly comparable.


``` r
# 1-2. Fasting glucose under the two imports
glucose_summary <- function(d) {
  summarise(d,
            mean = mean(fasting_glucose_mmol_l, na.rm = TRUE),
            median = median(fasting_glucose_mmol_l, na.rm = TRUE),
            max = max(fasting_glucose_mmol_l, na.rm = TRUE),
            n_missing = sum(is.na(fasting_glucose_mmol_l)))
}
bind_rows(default = glucose_summary(raw_default),
          declared = glucose_summary(raw), .id = "import")
```

```
#> # A tibble: 2 × 5
#>   import      mean median   max n_missing
#>   <chr>      <dbl>  <dbl> <dbl>     <int>
#> 1 default  32.521     5.4 999          35
#> 2 declared  5.4489    5.4  10.1        75
```

With the default import, the 40 values coded `999` are treated as real glucose
concentrations. The **mean** is the most affected summary: it rises from 5.4 to 32.5
mmol/L, because the mean uses the size of every value and a few enormous values
dominate it. The **maximum** is also wrong (999 instead of 10.1). The **median** is
unchanged at 5.4, because the 40 sentinels, although extreme, are only 2.7 per cent
of the values and do not move the middle of the distribution; this robustness is one
reason medians are preferred for skewed data. The default import reports 35 missing
values and the declared import 75, the difference being the 40 sentinels.

For question 3, we import with only the standard missing codes and convert `999` to
`NA` in the glucose column alone, using `na_if()`.



``` r
# 3. Treat 999 as missing only in the column where it is a sentinel
raw_selective <- read_csv("Data/hypertension_phc_raw.csv",
                          na = c("", "NA")) |>
  mutate(fasting_glucose_mmol_l = na_if(fasting_glucose_mmol_l, 999))

sum(is.na(raw_selective$fasting_glucose_mmol_l))
```

```
#> [1] 75
```

``` r
max(raw_selective$creatinine_umol_l)   # creatinine untouched
```

```
#> [1] 141
```

Glucose now has the same 75 missing values as before, while creatinine is untouched
(its maximum, 141 µmol/L, shows no column was altered by mistake; in a dataset where
creatinine genuinely reached 999 it would be kept). This selective approach is the
safe default whenever a code could be real in some columns.


### Exercise 2.2

We list the repeated IDs, show their records with `janitor::get_dupes()`, and compare
the number of exact duplicate rows with the number of surplus IDs.


``` r
# 1. IDs that occur more than once, and their records
raw |> count(patient_id) |> filter(n > 1)
```

```
#> # A tibble: 3 × 2
#>   patient_id     n
#>   <chr>      <int>
#> 1 PHC-0011       2
#> 2 PHC-0251       2
#> 3 PHC-0881       2
```

``` r
janitor::get_dupes(raw, patient_id) |>
  select(patient_id, dupe_count, facility, age, sex, sbp_mmhg)
```

```
#> # A tibble: 6 × 6
#>   patient_id dupe_count facility      age sex    sbp_mmhg
#>   <chr>           <int> <chr>       <dbl> <chr>     <dbl>
#> 1 PHC-0011            2 Ilemela HC     51 Male        128
#> 2 PHC-0011            2 Ilemela HC     51 Male        128
#> 3 PHC-0251            2 Bugando PHC    51 Female      131
#> 4 PHC-0251            2 Bugando PHC    51 Female      131
#> 5 PHC-0881            2 Kisesa HC      45 Female      140
#> 6 PHC-0881            2 Kisesa HC      45 Female      140
```

``` r
# 2. Exact duplicates versus surplus IDs
sum(duplicated(raw))
```

```
#> [1] 3
```

``` r
nrow(raw) - n_distinct(raw$patient_id)
```

```
#> [1] 3
```

Three IDs (`PHC-0011`, `PHC-0251` and `PHC-0881`) occur twice, and `get_dupes()` shows
the two records of each side by side, with a `dupe_count` column. There are 3 exact
duplicate rows and 3 surplus IDs (1,503 rows minus 1,500 distinct IDs). Because the two
numbers agree, every repeated ID is an exact copy, and there are no conflicting records
that would need checking against source documents.

A suitable sentence for a methods section: *"The raw dataset contained 1,503 records;
three were exact duplicates of other records (identical in all variables) and were
removed, leaving 1,500 participants with unique identifiers."*


### Exercise 2.3

We tabulate the raw codes, then apply the helper after removing duplicates and check
the mapping with a cross-tabulation of old against new values.


``` r
# 1. Codes used before cleaning
table(raw$health_insurance, useNA = "ifany")
```

```
#> 
#>   0   1   N  No   Y Yes 
#> 150  70  97 743  49 394
```

``` r
table(raw$htn_diagnosed, useNA = "ifany")
```

```
#> 
#>   0   1   N  No   Y Yes 
#>  73 158  44 296 110 822
```

``` r
# 2. Apply the helper and check the mapping
clean_bin <- distinct(raw) |>
  mutate(health_insurance_new = to_yesno(health_insurance),
         htn_diagnosed_new = to_yesno(htn_diagnosed))

table(before = clean_bin$health_insurance,
      after = clean_bin$health_insurance_new)
```

```
#>       after
#> before  No Yes
#>    0   150   0
#>    1     0  70
#>    N    96   0
#>    No  742   0
#>    Y     0  49
#>    Yes   0 393
```

``` r
table(before = clean_bin$htn_diagnosed,
      after = clean_bin$htn_diagnosed_new)
```

```
#>       after
#> before  No Yes
#>    0    73   0
#>    1     0 158
#>    N    43   0
#>    No  295   0
#>    Y     0 110
#>    Yes   0 821
```

Both variables use six codes: `0`/`1`, `N`/`Y` and `No`/`Yes`. The cross-tabulations
show that every code maps to exactly one clean value (all the `0`, `N` and `No` codes to
"No" and all the `1`, `Y` and `Yes` codes to "Yes") and that no value became missing.
The counts are slightly smaller than in the first two tables because the three duplicate
records have been removed.



``` r
# 3. Proportions in the clean data
analysis_data |>
  summarise(insured_pct = round(100 * mean(health_insurance == "Yes"), 1),
            diagnosed_pct = round(100 * mean(htn_diagnosed == "Yes"), 1))
```

```
#> # A tibble: 1 × 2
#>   insured_pct diagnosed_pct
#>         <dbl>         <dbl>
#> 1        34.1          72.6
```

In the clean data, 34.1 per cent of patients have health insurance and 72.6 per cent
(1,089 of 1,500) have been diagnosed with hypertension. Because `health_insurance` and
`htn_diagnosed` have no missing values, `mean(x == "Yes")` gives the proportion directly;
with missing values you would need `na.rm = TRUE` and should report the denominator.


### Exercise 2.4

Cross-variable checks compare variables that must stand in a fixed relationship to
each other.


``` r
# 1. Diastolic at least as high as systolic
analysis_data |>
  summarise(dbp_ge_sbp = sum(dbp_mmhg >= sbp_mmhg, na.rm = TRUE))
```

```
#> # A tibble: 1 × 1
#>   dbp_ge_sbp
#>        <int>
#> 1         11
```

``` r
# 2. Pulse pressure
analysis_data <- analysis_data |>
  mutate(pulse_pressure = sbp_mmhg - dbp_mmhg)
summary(analysis_data$pulse_pressure)
```

```
#>    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.     NAs 
#>   -18.0    39.0    53.0    53.3    68.0   129.0       3
```

``` r
sum(analysis_data$pulse_pressure < 20, na.rm = TRUE)
```

```
#> [1] 92
```

Eleven patients have a diastolic pressure equal to or higher than their systolic
pressure. That is not physiologically possible for a correctly measured brachial blood
pressure: systolic pressure is, by definition, the peak pressure of the cardiac cycle.
These records have each passed the single-variable range checks, which is exactly why
cross-variable checks are needed. The pulse pressure summary confirms the problem from a
different angle: the minimum is -18 mmHg. A further 92 patients have a pulse pressure
below 20 mmHg, which is unusual (normal pulse pressure is around 40 mmHg) and might
reflect transposed or mistyped readings. In a real study these records would be queried
with the facilities. The data in this book are simulated and the readings are left
unchanged in `analysis_data`, but if you were cleaning these data for publication you
would add a rule (for example, setting both pressures to `NA` when diastolic is at least
systolic) to the cleaning script and report it.



``` r
# 3. Consistency rules from the data dictionary
analysis_data |>
  group_by(htn_diagnosed) |>
  summarise(n = n(),
            min_months = min(months_since_diagnosis),
            max_months = max(months_since_diagnosis))
```

```
#> # A tibble: 2 × 4
#>   htn_diagnosed     n min_months max_months
#>   <fct>         <int>      <dbl>      <dbl>
#> 1 No              411          0          0
#> 2 Yes            1089          1        119
```

``` r
analysis_data |>
  count(treatment_uptake, adherence_recorded = !is.na(adherence))
```

```
#> # A tibble: 2 × 3
#>   treatment_uptake adherence_recorded     n
#>   <fct>            <lgl>              <int>
#> 1 No               FALSE                992
#> 2 Yes              TRUE                 508
```

Both rules hold. All 411 patients who are not diagnosed have
`months_since_diagnosis` equal to 0, and the 1,089 diagnosed patients have values from
1 to 119 months. Adherence is recorded for all 508 treated patients and for none of the
992 untreated patients.


### Exercise 2.5

Adding `right = FALSE` makes each interval include its lower limit, for example
`[18.5, 25)`, which matches the WHO definition.


``` r
# 1. WHO-consistent categories: intervals closed on the left
analysis_data <- analysis_data |>
  mutate(bmi_cat_who = cut(bmi,
                           breaks = c(-Inf, 18.5, 25, 30, Inf),
                           labels = c("Underweight", "Normal",
                                      "Overweight", "Obese"),
                           right = FALSE))

# 2. Compare the two versions
table(default = analysis_data$bmi_cat, who = analysis_data$bmi_cat_who)
```

```
#>              who
#> default       Underweight Normal Overweight Obese
#>   Underweight          82      2          0     0
#>   Normal                0    466         10     0
#>   Overweight            0      0        568     9
#>   Obese                 0      0          0   316
```

``` r
analysis_data |>
  filter(bmi_cat != bmi_cat_who) |>
  count(bmi, bmi_cat, bmi_cat_who)
```

```
#> # A tibble: 3 × 4
#>     bmi bmi_cat     bmi_cat_who     n
#>   <dbl> <fct>       <fct>       <int>
#> 1  18.5 Underweight Normal          2
#> 2  25   Normal      Overweight     10
#> 3  30   Overweight  Obese           9
```

The cross-tabulation is almost diagonal: 21 patients change category, all of them
moving one category up. The second table shows why: they are exactly the patients
whose BMI, rounded to one decimal place, sits on a cut-point. Two patients with a BMI
of 18.5 move from "Underweight" to "Normal", ten with a BMI of 25.0 from "Normal" to
"Overweight" and nine with a BMI of 30.0 from "Overweight" to "Obese". The difference
is small here, but in a study reporting the prevalence of obesity it would change the
estimate, and it would make the results disagree with studies that applied the WHO
definition correctly.



``` r
# 3. Age groups, checked against age
analysis_data <- analysis_data |>
  mutate(age_group = cut(age, breaks = c(18, 40, 60, Inf),
                         labels = c("18-39", "40-59", "60+"),
                         right = FALSE))

analysis_data |>
  group_by(age_group) |>
  summarise(n = n(), min_age = min(age), max_age = max(age))
```

```
#> # A tibble: 4 × 4
#>   age_group     n min_age max_age
#>   <fct>     <int>   <dbl>   <dbl>
#> 1 18-39       274      18      39
#> 2 40-59       772      40      59
#> 3 60+         452      60      95
#> 4 <NA>          2      NA      NA
```

The same `right = FALSE` idea defines age groups whose labels mean what they say:
`[18, 40)` is 18 to 39 years. The minimum and maximum ages within each group confirm the
definition (18–39, 40–59 and 60–95), and the two patients whose age was set to missing
during validation correctly have a missing age group.


### Exercise 2.6

Regular expressions describe each format: `\\d{4}` (with the backslash doubled inside an R
string) is four digits and `[A-Za-z]{3}` three letters; `^` and `$` anchor the pattern to the start and end of the value.


``` r
# 1. Count each date format
dates <- distinct(raw)$enroll_date
c(iso = sum(str_detect(dates, "^\\d{4}-\\d{2}-\\d{2}$")),
  slash = sum(str_detect(dates, "^\\d{2}/\\d{2}/\\d{4}$")),
  month_name = sum(str_detect(dates, "^\\d{2}-[A-Za-z]{3}-\\d{4}$")))
```

```
#>        iso      slash month_name 
#>       1050        347        103
```

``` r
# 2. Month-first interpretation of the slash format
wrong <- parse_date_time(dates, orders = c("ymd", "mdy", "d-b-Y")) |>
  as_date()
sum(is.na(wrong))                                  # failures
```

```
#> [1] 221
```

``` r
sum(wrong != analysis_data$enroll_date, na.rm = TRUE) # silently different
```

```
#> [1] 137
```

The three formats account for all 1,500 dates (1,050 + 347 + 103). With month-first
parsing of the slash format, 221 dates fail to parse: they have a first number greater
than 12 (such as `18/02/2024`), which cannot be a month. That failure is at least
visible. More dangerous are the 137 dates that parse successfully but differ from the
correct dates. Most of them (115) are slash dates in which both numbers are 12 or less,
so that `01/02/2024` becomes 2 January instead of 1 February; the remaining 22 are
month-name dates that `parse_date_time()` matched to a different order once the
order list changed. Without a comparison against the correctly parsed dates, none of
these 137 errors would have been noticed. This is why the order must be chosen from
knowledge of the data, and why the result must be checked.



``` r
# 3. Enrolments per quarter
analysis_data |>
  mutate(enroll_quarter = quarter(enroll_date)) |>
  count(enroll_quarter)
```

```
#> # A tibble: 4 × 2
#>   enroll_quarter     n
#>            <int> <int>
#> 1              1   392
#> 2              2   412
#> 3              3   421
#> 4              4   275
```

Enrolment was evenly spread over the first three quarters (392 to 421 patients) and
lower in the fourth quarter (275), because recruitment ended on 2 December.


### Exercise 2.7

We create a missingness indicator and compare it across groups of observed variables.


``` r
analysis_data <- analysis_data |>
  mutate(chol_missing = is.na(total_chol_mmol_l))

# 1. Percentage missing by diagnosis and by residence
analysis_data |>
  group_by(htn_diagnosed) |>
  summarise(n = n(), pct_missing = round(100 * mean(chol_missing), 1))
```

```
#> # A tibble: 2 × 3
#>   htn_diagnosed     n pct_missing
#>   <fct>         <int>       <dbl>
#> 1 No              411         3.9
#> 2 Yes            1089         6.8
```

``` r
analysis_data |>
  group_by(residence) |>
  summarise(n = n(), pct_missing = round(100 * mean(chol_missing), 1))
```

```
#> # A tibble: 2 × 3
#>   residence     n pct_missing
#>   <fct>     <int>       <dbl>
#> 1 Rural       703         5.4
#> 2 Urban       797         6.5
```

``` r
# 2. Mean age by missingness
analysis_data |>
  group_by(chol_missing) |>
  summarise(n = n(), mean_age = round(mean(age, na.rm = TRUE), 1))
```

```
#> # A tibble: 2 × 3
#>   chol_missing     n mean_age
#>   <lgl>        <int>    <dbl>
#> 1 FALSE         1410     52  
#> 2 TRUE            90     55.9
```

Cholesterol is missing for 6.8 per cent of diagnosed patients and 3.9 per cent of
undiagnosed patients, and for 6.5 per cent of urban and 5.4 per cent of rural residents.
Patients with missing cholesterol are on average about four years older (55.9 versus
52.0 years). The differences are modest, and Chapter 4 shows how to test whether
differences of this size could be due to chance, but they point in a consistent
direction: missingness appears to be related to observed characteristics (diagnosis,
age). If so, the data are not MCAR, and an analysis restricted to patients with a
cholesterol result would slightly over-represent younger, undiagnosed patients. MAR,
with missingness depending on age and diagnosis, is a more plausible working
assumption, and any analysis using cholesterol should at least include these variables
in the model or in an imputation model.

The data cannot tell us whether cholesterol is MNAR. That would require knowing whether
patients with missing values tend to have higher or lower cholesterol than observed
patients of the same age and diagnosis, and their cholesterol is precisely what we do
not observe. Judgements about MNAR rest on knowledge of how the data were collected
(for example, whether blood was drawn only from patients who looked unwell) and are
explored with sensitivity analyses. Because these data are simulated, the pattern
illustrates the reasoning rather than a real clinical finding.


### Exercise 2.8

The function collects the steps of the chapter in the same order. It relies on the
`to_yesno()` helper defined at the top of this appendix; in a real project you would
keep both functions in the same script file.


``` r
clean_htn <- function(path) {
  # Import with missing-value codes; remove exact duplicates; trim text
  dat <- read_csv(path, na = c("", "NA", "999", "-99"),
                  show_col_types = FALSE) |>
    distinct() |>
    mutate(across(where(is.character), str_trim))

  # Categories: sex and the Yes/No variables
  dat <- dat |>
    mutate(
      sex = case_when(
        str_to_lower(sex) %in% c("female", "f") ~ "Female",
        str_to_lower(sex) %in% c("male", "m")   ~ "Male",
        TRUE ~ NA_character_),
      across(c(diabetes, family_history_htn, health_insurance,
               htn_diagnosed, treatment_uptake), to_yesno)
    )

  # Validation: impossible values become NA
  dat <- dat |>
    mutate(
      age       = if_else(between(age, 18, 110), age, NA_real_),
      sbp_mmhg  = if_else(between(sbp_mmhg, 70, 260), sbp_mmhg, NA_real_),
      dbp_mmhg  = if_else(between(dbp_mmhg, 40, 150), dbp_mmhg, NA_real_),
      height_cm = if_else(between(height_cm, 120, 210), height_cm, NA_real_),
      weight_kg = if_else(between(weight_kg, 30, 200), weight_kg, NA_real_)
    )

  # Derived variables and dates
  dat <- dat |>
    mutate(
      bmi = round(weight_kg / (height_cm / 100)^2, 1),
      bmi_cat = cut(bmi, breaks = c(-Inf, 18.5, 25, 30, Inf),
                    labels = c("Underweight", "Normal",
                               "Overweight", "Obese")),
      bp_category = case_when(
        is.na(sbp_mmhg) | is.na(dbp_mmhg) ~ NA_character_,
        sbp_mmhg >= 140 | dbp_mmhg >= 90  ~ "Hypertension",
        sbp_mmhg >= 130 | dbp_mmhg >= 80  ~ "Elevated",
        TRUE                              ~ "Normal"),
      enroll_date = as_date(parse_date_time(
        enroll_date, orders = c("ymd", "dmy", "d-b-Y")))
    )

  # Factors with deliberate levels
  yn <- c("No", "Yes")
  dat <- dat |>
    mutate(
      facility = factor(facility),
      sex = factor(sex, levels = c("Female", "Male")),
      residence = factor(residence, levels = c("Rural", "Urban")),
      education = factor(education, ordered = TRUE,
                         levels = c("None", "Primary", "Secondary",
                                    "Tertiary")),
      occupation = factor(occupation),
      marital_status = factor(marital_status),
      physical_activity = factor(physical_activity, ordered = TRUE,
                                 levels = c("Low", "Moderate", "High")),
      smoking = factor(smoking, levels = c("Never", "Former", "Current")),
      alcohol = factor(alcohol, levels = c("None", "Moderate", "Heavy")),
      bp_category = factor(bp_category,
                           levels = c("Normal", "Elevated", "Hypertension")),
      health_insurance = factor(health_insurance, levels = yn),
      family_history_htn = factor(family_history_htn, levels = yn),
      diabetes = factor(diabetes, levels = yn),
      htn_diagnosed = factor(htn_diagnosed, levels = yn),
      treatment_uptake = factor(treatment_uptake, levels = yn),
      adherence = factor(na_if(adherence, ""), levels = c("Poor", "Good")),
      bp_controlled = factor(na_if(bp_controlled, ""), levels = yn)
    )

  # Assertions: fail loudly if a new problem appears
  stopifnot(
    n_distinct(dat$patient_id) == nrow(dat),
    !anyNA(dat$sex),
    !anyNA(dat$enroll_date),
    !anyNA(dat$treatment_uptake),
    all(between(dat$sbp_mmhg, 70, 260), na.rm = TRUE)
  )
  dat
}

my_clean <- clean_htn("Data/hypertension_phc_raw.csv")
all.equal(my_clean, readRDS("Data/analysis_data.rds"))
```

```
#> [1] TRUE
```

`all.equal()` returns `TRUE`: the function reproduces the analysis dataset exactly.
The assertions at the end check that the patient ID is unique, that sex, enrolment date
and the outcome have no missing values, and that systolic pressures are in range; if a
future version of the raw file contained, say, a new spelling of sex or a new date
format, the function would stop with an error naming the failed condition instead of
returning quietly flawed data.

A function is more useful than a long script when a corrected raw file arrives for three
reasons. It can be rerun on the new file with one line, without editing anything.
It can be applied to several files (for example, an interim and a final data export) and
the results compared. And because everything happens inside the function, no
intermediate objects are left in the workspace to be confused with the clean data.
Packaging a cleaning pipeline as a function is a small step towards the reproducible
workflows recommended by @wilson2017.

