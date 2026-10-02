# ============================================================================
# DAY 2 EXERCISE - SOLUTION  |  Clean the simulated dataset
# Clinical Data Analysis in R - Phase I | Neudata | #ClearDataClearImpact
#
# NOTE: Scripts/day2_demo.R is the full, authoritative cleaning pipeline that
#       produces Data/analysis_data.rds. This solution mirrors the exercise
#       tasks step by step.
# ============================================================================

library(tidyverse)

# TASK 1. Import with missing-value codes
raw <- read_csv("Data/hypertension_phc_raw.csv",
                na = c("", "NA", "999", "-99"))

# TASK 2. Remove duplicate records
raw <- distinct(raw)
nrow(raw)                       # 1500

# TASK 3. Clean sex
raw <- raw |>
  mutate(sex = case_when(
    str_to_lower(str_trim(sex)) %in% c("female", "f") ~ "Female",
    str_to_lower(str_trim(sex)) %in% c("male", "m")   ~ "Male",
    TRUE ~ NA_character_
  ))
table(raw$sex, useNA = "ifany")

# TASK 4. Standardise binaries
to_yesno <- function(x) {
  x <- str_to_lower(str_trim(as.character(x)))
  case_when(x %in% c("yes","y","1") ~ "Yes",
            x %in% c("no","n","0")  ~ "No",
            TRUE ~ NA_character_)
}
raw <- raw |> mutate(diabetes = to_yesno(diabetes),
                     treatment_uptake = to_yesno(treatment_uptake))
table(raw$diabetes); table(raw$treatment_uptake)

# TASK 5. Validation: impossible values -> NA
raw <- raw |>
  mutate(age      = if_else(age >= 18 & age <= 110, age, NA_real_),
         sbp_mmhg = if_else(sbp_mmhg >= 70 & sbp_mmhg <= 260, sbp_mmhg, NA_real_))
summary(raw$age); summary(raw$sbp_mmhg)

# TASK 6. Recompute BMI and categorise
raw <- raw |>
  mutate(bmi = round(weight_kg / (height_cm/100)^2, 1),
         bmi_cat = cut(bmi, breaks = c(-Inf, 18.5, 25, 30, Inf),
                       labels = c("Underweight","Normal","Overweight","Obese")))
table(raw$bmi_cat, useNA = "ifany")

# TASK 7. Factors (reference level "No" first for the outcome)
raw <- raw |>
  mutate(sex = factor(sex, levels = c("Female","Male")),
         residence = factor(residence, levels = c("Rural","Urban")),
         diabetes = factor(diabetes, levels = c("No","Yes")),
         treatment_uptake = factor(treatment_uptake, levels = c("No","Yes")))
levels(raw$treatment_uptake)    # "No" "Yes"  -> No is the reference

# TASK 8. Save (this exercise version; the demo saves the full contract)
saveRDS(raw, "Data/analysis_data_exercise.rds")

# QUESTION: missing total cholesterol after import
sum(is.na(raw$total_chol_mmol_l))   # ~90 values were NA / sentinel-coded
# ============================================================================
