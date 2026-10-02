# ============================================================================
# DAY 2 GUIDED EXERCISE  -  Clean the simulated dataset
# Clinical Data Analysis in R - Phase I | Neudata
# ----------------------------------------------------------------------------
# Time: 15-30 minutes. Build the analysis-ready dataset step by step.
# Solution: Solutions/day2_solution.R
# ============================================================================

library(tidyverse)

# TASK 1. Import Data/hypertension_phc_raw.csv, telling read_csv that
#         "", "NA", "999" and "-99" all mean missing.


# TASK 2. The file has more rows than patients. Remove duplicate records with
#         distinct(). How many rows remain? (Should be 1500.)


# TASK 3. Clean the `sex` variable so it has only two values: Female and Male.
#         (Hint: str_to_lower() then case_when().)


# TASK 4. Standardise `diabetes` and `treatment_uptake` to "Yes"/"No"
#         (they currently mix Yes/No/Y/N/1/0).


# TASK 5. Validation: set impossible values to NA -
#         age outside 18-110, and sbp_mmhg outside 70-260.


# TASK 6. Recompute bmi from height_cm and weight_kg. Create bmi_cat with
#         cut(): Underweight (<18.5), Normal (18.5-25), Overweight (25-30),
#         Obese (>=30).


# TASK 7. Convert sex, residence, diabetes, treatment_uptake to factors.
#         For treatment_uptake make "No" the reference (first) level.


# TASK 8. Save your cleaned data as Data/analysis_data.rds with saveRDS().
#         You will reuse it every remaining day.


# QUESTION: how many values of total_chol_mmol_l were missing after import?
# (Hint: sum(is.na(...)).)
# ============================================================================
