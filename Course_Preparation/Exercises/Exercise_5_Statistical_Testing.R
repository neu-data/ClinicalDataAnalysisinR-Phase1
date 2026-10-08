# =====================================================================
#  EXERCISE 5, Statistical Testing (thinking + doing)
#  Clinical Data Analysis in R (Phase I), Pre-course
#  ------------------------------------------------------------------
#  Goal: practise CHOOSING the right test before running it.
#  For each research question, first decide (in the comments):
#     - Outcome                 - Variable type(s)
#     - Exposure / comparison   - Appropriate test
#     - Null hypothesis (H0)    - Interpretation of the result
#  Then run the test and check your thinking.
#  Use the Statistical_Test_Decision_Guide in Cheat_Sheets/ to help.
#  Answers: Solutions/Solution_5_Statistical_Testing.R
# =====================================================================

library(tidyverse)
clinical_data <- read_csv("Data/clinical_data_clean.csv")

# -------------------------------------------------------------------
# QUESTION A: Is fasting glucose higher in patients with diabetes?
#   Outcome:            ______
#   Exposure/groups:    ______
#   Variable types:     ______
#   Appropriate test:   ______
#   Null hypothesis:    ______
# Run it:
t.test(glucose ~ diabetes, data = clinical_data)
#   Interpretation:     ______

# -------------------------------------------------------------------
# QUESTION B: Is hypertension associated with diabetes?
#   Outcome:            ______
#   Exposure/groups:    ______
#   Variable types:     ______
#   Appropriate test:   ______
#   Null hypothesis:    ______
# Run it:
chisq.test(table(clinical_data$hypertension, clinical_data$diabetes))
#   Interpretation:     ______

# -------------------------------------------------------------------
# QUESTION C: Are age and systolic blood pressure related?
#   Outcome:            ______
#   Exposure:           ______
#   Variable types:     ______
#   Appropriate test:   ______
#   Null hypothesis:    ______
# Run it:
cor.test(clinical_data$age, clinical_data$systolic_bp)
#   Interpretation:     ______

# -------------------------------------------------------------------
# QUESTION D (you choose the test):
#   "Does systolic blood pressure differ between men and women?"
#   Decide the test, then write and run the code yourself below.
#   YOUR CODE:
#
#   Interpretation:     ______
