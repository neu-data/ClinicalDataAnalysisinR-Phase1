# ============================================================================
# DAY 3 GUIDED EXERCISE  -  Produce Table 1 for a manuscript
# Clinical Data Analysis in R - Phase I | Neudata
# ----------------------------------------------------------------------------
# Time: 15-30 minutes. Start from your cleaned data.
# Solution: Solutions/day3_solution.R
# ============================================================================

library(tidyverse)
library(gtsummary)

# TASK 1. Reload the cleaned dataset saved on Day 2.
analysis_data <- readRDS("Data/analysis_data.rds")

# TASK 2. Report the mean and SD of age, and the median and IQR of
#         distance_to_facility_km. Remember na.rm = TRUE.


# TASK 3. Make a frequency table (counts and %) of education and of
#         bp_category.


# TASK 4. Cross-tabulate treatment_uptake by diabetes. Add row percentages.
#         What proportion of diabetics are on treatment?


# TASK 5. Build a publication-ready Table 1 of baseline characteristics
#         stratified by treatment_uptake, with p-values:
#           tbl_summary(by = treatment_uptake) |> add_p()
#         Include: age, sex, residence, education, diabetes, bmi, sbp_mmhg,
#         health_insurance, knowledge_score.


# TASK 6. Create and SAVE two figures to Resources/ at 300 dpi with ggsave():
#           (a) a boxplot of sbp_mmhg by treatment_uptake
#           (b) a bar chart of education


# TASK 7. Export your Table 1 (as HTML or CSV) to Resources/.

# QUESTION: name TWO characteristics that differ between treated and
# untreated patients. Are the differences clinically plausible?
# ============================================================================
