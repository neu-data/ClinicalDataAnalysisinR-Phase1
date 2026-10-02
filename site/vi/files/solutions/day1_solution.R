# ============================================================================
# DAY 1 EXERCISE - SOLUTION  |  Import the simulated clinical dataset
# Clinical Data Analysis in R - Phase I | Neudata | #ClearDataClearImpact
# ============================================================================

# TASK 1. Packages
library(tidyverse)
library(readxl)

# TASK 2. Import the CSV
htn <- read_csv("Data/hypertension_phc_raw.csv")
dim(htn)        # 1503 rows x 36 columns  (note: 1503, not 1500!)

# TASK 3. Import the Excel version
htn_xl <- read_excel("Data/hypertension_phc_raw.xlsx", sheet = "data")
dim(htn_xl)     # same 1503 x 36

# TASK 4. Structure
glimpse(htn)
# Numeric-looking:    age, sbp_mmhg, bmi, knowledge_score, creatinine_umol_l
# Categorical-looking: sex, residence, education, occupation, facility

# TASK 5. Age summary
summary(htn$age)
# Maximum age = 200  -> NOT plausible. A data-entry error to fix on Day 2.

# TASK 6. Sex frequency table
table(htn$sex)
# Eight spellings appear: Female, F, female, f, Male, M, male, m.
# Problem: R treats "Male" and "male" as DIFFERENT categories, so any
# analysis by sex would be wrong until we standardise them.

# TASK 7. Facility counts (note stray spaces in some labels)
table(htn$facility)
sum(str_detect(htn$facility, "^\\s|\\s$"), na.rm = TRUE)  # values with spaces

# SUMMARY ANSWER: Two problems already visible on Day 1 ->
#   (1) impossible values (age = 200), and
#   (2) inconsistent category spellings (sex), plus stray whitespace and
#       a row count (1503) that implies duplicate records.
# ============================================================================
