# ============================================================================
# Clinical Data Analysis in R - Phase I
# DAY 2 LIVE DEMONSTRATION: Understanding & Cleaning Clinical Data
#
# Goal: turn the messy raw file into a tidy, analysis-ready dataset and
#       SAVE it so every later day starts from the same clean data.
#
# THIS SCRIPT DEFINES THE CLEANING CONTRACT for Days 3-5.
# Output: Data/analysis_data.rds  and  Data/analysis_data.csv
#
# Author: Vương Mỹ Lượng & Bernard Isekah Osang'ir | Neudata | #ClearDataClearImpact
# ============================================================================
#install.packages("tidyverse")
library(tidyverse)                   # Load tidyverse for data import, cleaning, transformation and export


# ----------------------------------------------------------------------------
# 1. IMPORT - tell read_csv which strings mean "missing"
# ----------------------------------------------------------------------------

raw <- read_csv(                     # Import the raw hypertension dataset from a CSV file
  "Data/hypertension_phc_raw.csv",   # Path to the raw data file
  na = c("", "NA", "999", "-99")     # Treat blank, NA, 999 and -99 as missing values (NA)
)
glimpse(raw)                         # Show variable names, data types and example values
head(raw)
tail(raw)
nrow(raw)                            # Count records: 1503 rows, including duplicates
ncol(raw)

# ----------------------------------------------------------------------------
# 2. REMOVE DUPLICATE RECORDS
# ----------------------------------------------------------------------------

sum(duplicated(raw))                 # Count rows that are exact duplicates of previous rows" 3
raw <- distinct(raw)                 # Remove exact duplicate records and retain unique rows
n_distinct(raw$patient_id)           # Count unique patient IDs; should now equal the number of rows
nrow(raw)                            # Confirm 1500 records remain after duplicate removal


# ----------------------------------------------------------------------------
# 3. CLEAN CATEGORICAL TEXT  -- whitespace + inconsistent spellings
# ----------------------------------------------------------------------------

# 3a. Trim stray spaces from all character columns

raw <- raw  %>% mutate(across(where(is.character), str_trim))  # Remove leading/trailing spaces from all text variables


# 3b. Recode the messy sex variable to two clean levels

raw <- raw  %>%
  mutate(sex = case_when(                                      # Standardise different representations of sex
    str_to_lower(sex) %in% c("female", "f") ~ "Female",        # Convert Female/female/F/f to "Female"
    str_to_lower(sex) %in% c("male", "m")   ~ "Male",          # Convert Male/male/M/m to "Male"
    TRUE ~ NA_character_                                       # Convert unrecognised values to missing
  ))
table(raw$sex, useNA = "ifany")                                # Check frequencies, including missing values if present


# 3c. A reusable helper to standardise Yes/No/Y/N/1/0 binaries

to_yesno <- function(x) {                                      # Define a reusable function for cleaning binary variables
  x <- str_to_lower(str_trim(as.character(x)))                 # Convert to text, remove spaces and change to lowercase
  case_when(
    x %in% c("yes", "y", "1", "true") ~ "Yes",                 # Standardise Yes/Y/1/TRUE as "Yes"
    x %in% c("no",  "n", "0", "false") ~ "No",                 # Standardise No/N/0/FALSE as "No"
    TRUE ~ NA_character_                                       # Convert all other values to missing
  )
}

raw <- raw  %>%
  mutate(across(c(diabetes, family_history_htn, health_insurance,
                  htn_diagnosed, treatment_uptake), to_yesno)) # Apply the Yes/No cleaning function to all listed variables

table(raw$treatment_uptake, useNA = "ifany")                   # Check cleaned treatment-uptake categories and missing values


# ----------------------------------------------------------------------------
# 4. DATA VALIDATION  -- find & fix impossible clinical values
# ----------------------------------------------------------------------------
# Define plausible physiological ranges; anything outside becomes NA.

raw <- raw  %>%
  mutate(
    age        = if_else(age >= 18 & age <= 110, age, NA_real_),                    # Keep ages 18-110; otherwise set to NA
    sbp_mmhg   = if_else(sbp_mmhg >= 70 & sbp_mmhg <= 260, sbp_mmhg, NA_real_),     # Keep plausible systolic BP 70-260 mmHg
    dbp_mmhg   = if_else(dbp_mmhg >= 40 & dbp_mmhg <= 150, dbp_mmhg, NA_real_),     # Keep plausible diastolic BP 40-150 mmHg
    height_cm  = if_else(height_cm >= 120 & height_cm <= 210, height_cm, NA_real_), # Keep plausible height 120-210 cm
    weight_kg  = if_else(weight_kg >= 30 & weight_kg <= 200, weight_kg, NA_real_)   # Keep plausible weight 30-200 kg
  )

summary(select(raw, age, sbp_mmhg, dbp_mmhg, height_cm, weight_kg))                 # Summarise validated continuous variables


# ----------------------------------------------------------------------------
# 5. RECODE / DERIVE  -- recompute BMI and create clinical categories
# ----------------------------------------------------------------------------

raw <- raw %>%
  mutate(
    bmi = round(weight_kg / (height_cm / 100)^2, 1),           # Recalculate BMI = kg/m² and round to one decimal place

    bmi_cat = cut(bmi,                                         # Convert continuous BMI into clinical categories
                  breaks = c(-Inf, 18.5, 25, 30, Inf),         # Define BMI cut-points
                  labels = c("Underweight", "Normal",
                             "Overweight", "Obese")),          # Assign labels to the four BMI groups

    bp_category = case_when(                                   # Derive BP category using systolic and diastolic BP
      is.na(sbp_mmhg) | is.na(dbp_mmhg) ~ NA_character_,       # BP category is missing if either BP measurement is missing
      sbp_mmhg >= 140 | dbp_mmhg >= 90  ~ "Hypertension",      # SBP >=140 or DBP >=90 -> Hypertension
      sbp_mmhg >= 130 | dbp_mmhg >= 80  ~ "Elevated",          # SBP >=130 or DBP >=80 -> Elevated
      TRUE                              ~ "Normal"             # All remaining valid measurements -> Normal
    )
  )


# ----------------------------------------------------------------------------
# 6. DATES  -- parse the mixed formats in enroll_date
# ----------------------------------------------------------------------------
# lubridate handles many formats; here we coerce the common ones.

library(lubridate)                                             # Load functions for parsing and manipulating dates

raw <- raw  %>%
  mutate(enroll_date = parse_date_time(                        # Convert mixed-format enrollment dates into proper dates
    enroll_date,                                               # Original enrollment-date variable
    orders = c("ymd", "dmy", "d-b-Y"))  %>% as_date())         # Accept year-month-day, day-month-year and day-Mon-year formats

sum(is.na(raw$enroll_date))                                    # Count missing dates and dates that failed to parse


# ----------------------------------------------------------------------------
# 7. FACTORS & LABELS  -- set the right type and reference levels
# ----------------------------------------------------------------------------

analysis_data <- raw  %>%
  mutate(
    facility           = factor(facility),                                # Convert facility to a categorical factor
    sex                = factor(sex, levels = c("Female", "Male")),       # Set Female as the reference/first category
    residence          = factor(residence, levels = c("Rural", "Urban")), # Set Rural as the reference/first category
    education          = factor(education,levels = c("None","Primary","Secondary","Tertiary"),
                                ordered = TRUE),                          # Ordered education levels from lowest to highest
    occupation         = factor(occupation),                              # Convert occupation to a categorical factor
    marital_status     = factor(marital_status),                          # Convert marital status to a categorical factor
    physical_activity  = factor(physical_activity, levels = c("Low","Moderate","High"),
                                ordered = TRUE),                          # Ordered activity levels: Low < Moderate < High
    smoking            = factor(smoking, levels = c("Never","Former","Current")), # Use Never as the first/reference category
    alcohol            = factor(alcohol,levels = c("None","Moderate","Heavy")),   # Order alcohol-use categories
    bp_category        = factor(bp_category, levels = c("Normal","Elevated","Hypertension")), # Use Normal as reference BP category

    # Binary outcomes/predictors: reference level "No" listed FIRST
    health_insurance   = factor(health_insurance, levels = c("No","Yes")), # Convert to binary factor with No as reference
    family_history_htn = factor(family_history_htn,levels = c("No","Yes")),# Convert family history to binary factor
    diabetes           = factor(diabetes, levels = c("No","Yes")),         # Convert diabetes status to binary factor
    htn_diagnosed      = factor(htn_diagnosed, levels = c("No","Yes")),    # Convert hypertension diagnosis to binary factor
    treatment_uptake   = factor(treatment_uptake,levels = c("No","Yes")),  # Convert treatment uptake to binary factor
    adherence          = factor(na_if(adherence, ""),levels = c("Poor","Good")),  # Convert blanks to NA; Poor is the first category
    bp_controlled      = factor(na_if(bp_controlled, ""), levels = c("No","Yes")) # Convert blanks to NA; No is the reference category
  )

glimpse(analysis_data)                                         # Inspect final variable names, types and example values
str(analysis_data)                                             # Inspect detailed structure and factor levels


# ----------------------------------------------------------------------------
# 8. FINAL MISSING-DATA AUDIT
# ----------------------------------------------------------------------------

colSums(is.na(analysis_data))  %>% sort(decreasing = TRUE)  %>% head(12)  # Show 12 variables with the most missing observations

# NOTE: adherence / bp_controlled are NA by design for untreated patients.
# These are structurally missing values and are not necessarily data-quality errors.


# ----------------------------------------------------------------------------
# 9. SAVE THE CLEAN DATA  -- this is the contract for Days 3, 4, 5
# ----------------------------------------------------------------------------

saveRDS(analysis_data, "Data/analysis_data.rds")                # Save R version; preserves factors, dates and variable classes
write_csv(analysis_data, "Data/analysis_data.csv")              # Save CSV version for viewing/sharing outside R

# To reload on later days:  analysis_data <- readRDS("Data/analysis_data.rds")
# readRDS() restores the dataset with its R variable types and factor levels preserved.
#
# DAY 2 EXERCISE: see Practicals/day2_exercise.R
# ============================================================================
