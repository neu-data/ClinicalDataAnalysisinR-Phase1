# ============================================================================
# Clinical Data Analysis in R - Phase I
# DAY 2 LIVE DEMONSTRATION:  Understanding & Cleaning Clinical Data
#
# Goal: turn the messy raw file into a tidy, analysis-ready dataset and
#       SAVE it so every later day starts from the same clean data.
#
# THIS SCRIPT DEFINES THE CLEANING CONTRACT for Days 3-5.
# Output: Data/analysis_data.rds  and  Data/analysis_data.csv
#
# Author:  Bernard Isekah Osang'ir & My Luong Vuong | Neudata | #ClearDataClearImpact
# ============================================================================

library(tidyverse)

# ----------------------------------------------------------------------------
# 1. IMPORT - tell read_csv which strings mean "missing"
# ----------------------------------------------------------------------------
raw <- read_csv(
  "Data/hypertension_phc_raw.csv",
  na = c("", "NA", "999", "-99")     # treat all these sentinels as NA
)
glimpse(raw)
nrow(raw)                            # 1503 - duplicates present


# ----------------------------------------------------------------------------
# 2. REMOVE DUPLICATE RECORDS
# ----------------------------------------------------------------------------
sum(duplicated(raw))                 # how many full-duplicate rows?
raw <- distinct(raw)                 # drop exact duplicates
n_distinct(raw$patient_id)           # should now equal nrow(raw)
nrow(raw)                            # 1500


# ----------------------------------------------------------------------------
# 3. CLEAN CATEGORICAL TEXT  -- whitespace + inconsistent spellings
# ----------------------------------------------------------------------------
# 3a. Trim stray spaces from all character columns
raw <- raw |> mutate(across(where(is.character), str_trim))

# 3b. Recode the messy sex variable to two clean levels
raw <- raw |>
  mutate(sex = case_when(
    str_to_lower(sex) %in% c("female", "f") ~ "Female",
    str_to_lower(sex) %in% c("male", "m")   ~ "Male",
    TRUE ~ NA_character_
  ))
table(raw$sex, useNA = "ifany")      # now just Female / Male

# 3c. A reusable helper to standardise Yes/No/Y/N/1/0 binaries
to_yesno <- function(x) {
  x <- str_to_lower(str_trim(as.character(x)))
  case_when(
    x %in% c("yes", "y", "1", "true") ~ "Yes",
    x %in% c("no",  "n", "0", "false") ~ "No",
    TRUE ~ NA_character_
  )
}
raw <- raw |>
  mutate(across(c(diabetes, family_history_htn, health_insurance,
                  htn_diagnosed, treatment_uptake), to_yesno))
table(raw$treatment_uptake, useNA = "ifany")


# ----------------------------------------------------------------------------
# 4. DATA VALIDATION  -- find & fix impossible clinical values
# ----------------------------------------------------------------------------
# Define plausible physiological ranges; anything outside becomes NA.
raw <- raw |>
  mutate(
    age        = if_else(age >= 18 & age <= 110, age, NA_real_),
    sbp_mmhg   = if_else(sbp_mmhg >= 70 & sbp_mmhg <= 260, sbp_mmhg, NA_real_),
    dbp_mmhg   = if_else(dbp_mmhg >= 40 & dbp_mmhg <= 150, dbp_mmhg, NA_real_),
    height_cm  = if_else(height_cm >= 120 & height_cm <= 210, height_cm, NA_real_),
    weight_kg  = if_else(weight_kg >= 30 & weight_kg <= 200, weight_kg, NA_real_)
  )
summary(select(raw, age, sbp_mmhg, dbp_mmhg, height_cm, weight_kg))


# ----------------------------------------------------------------------------
# 5. RECODE / DERIVE  -- recompute BMI and create clinical categories
# ----------------------------------------------------------------------------
raw <- raw |>
  mutate(
    bmi = round(weight_kg / (height_cm / 100)^2, 1),     # recompute from source
    bmi_cat = cut(bmi,
                  breaks = c(-Inf, 18.5, 25, 30, Inf),
                  labels = c("Underweight", "Normal", "Overweight", "Obese")),
    bp_category = case_when(
      is.na(sbp_mmhg) | is.na(dbp_mmhg) ~ NA_character_,
      sbp_mmhg >= 140 | dbp_mmhg >= 90  ~ "Hypertension",
      sbp_mmhg >= 130 | dbp_mmhg >= 80  ~ "Elevated",
      TRUE                              ~ "Normal"
    )
  )


# ----------------------------------------------------------------------------
# 6. DATES  -- parse the mixed formats in enroll_date
# ----------------------------------------------------------------------------
# lubridate handles many formats; here we coerce the common ones.
library(lubridate)
raw <- raw |>
  mutate(enroll_date = parse_date_time(
    enroll_date,
    orders = c("ymd", "dmy", "d-b-Y")) |> as_date())
sum(is.na(raw$enroll_date))          # how many failed to parse?


# ----------------------------------------------------------------------------
# 7. FACTORS & LABELS  -- set the right type and reference levels
# ----------------------------------------------------------------------------
analysis_data <- raw |>
  mutate(
    facility           = factor(facility),
    sex                = factor(sex, levels = c("Female", "Male")),
    residence          = factor(residence, levels = c("Rural", "Urban")),
    education          = factor(education,
                                levels = c("None","Primary","Secondary","Tertiary"),
                                ordered = TRUE),
    occupation         = factor(occupation),
    marital_status     = factor(marital_status),
    physical_activity  = factor(physical_activity,
                                levels = c("Low","Moderate","High"), ordered = TRUE),
    smoking            = factor(smoking, levels = c("Never","Former","Current")),
    alcohol            = factor(alcohol, levels = c("None","Moderate","Heavy")),
    bp_category        = factor(bp_category,
                                levels = c("Normal","Elevated","Hypertension")),
    # Binary outcomes/predictors: reference level "No" listed FIRST
    health_insurance   = factor(health_insurance, levels = c("No","Yes")),
    family_history_htn = factor(family_history_htn, levels = c("No","Yes")),
    diabetes           = factor(diabetes, levels = c("No","Yes")),
    htn_diagnosed      = factor(htn_diagnosed, levels = c("No","Yes")),
    treatment_uptake   = factor(treatment_uptake, levels = c("No","Yes")),
    adherence          = factor(na_if(adherence, ""), levels = c("Poor","Good")),
    bp_controlled      = factor(na_if(bp_controlled, ""), levels = c("No","Yes"))
  )

glimpse(analysis_data)


# ----------------------------------------------------------------------------
# 8. FINAL MISSING-DATA AUDIT
# ----------------------------------------------------------------------------
colSums(is.na(analysis_data)) |> sort(decreasing = TRUE) |> head(12)
# NOTE: adherence / bp_controlled are NA by design for untreated patients.


# ----------------------------------------------------------------------------
# 9. SAVE THE CLEAN DATA  -- this is the contract for Days 3, 4, 5
# ----------------------------------------------------------------------------
saveRDS(analysis_data, "Data/analysis_data.rds")     # preserves factor types
write_csv(analysis_data, "Data/analysis_data.csv")   # human-readable backup

# To reload on later days:  analysis_data <- readRDS("Data/analysis_data.rds")
#
# DAY 2 EXERCISE: see Practicals/day2_exercise.R
# ============================================================================
