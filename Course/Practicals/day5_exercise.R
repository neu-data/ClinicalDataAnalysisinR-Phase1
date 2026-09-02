# ============================================================================
# DAY 5 GUIDED EXERCISE  -  Complete the analysis & write a Results section
# Clinical Data Analysis in R - Phase I | Neudata
# ----------------------------------------------------------------------------
# Time: 15-30 minutes. Solution: Solutions/day5_solution.R
# This is the in-class version of the final assignment.
# ============================================================================

library(tidyverse)
library(broom)
library(gtsummary)

# TASK 1. Reload data; restrict to diagnosed hypertensives.
analysis_data <- readRDS("Data/analysis_data.rds")
dx <- filter(analysis_data, htn_diagnosed == "Yes")

# TASK 2. Fit the final multivariable logistic regression of treatment_uptake on:
#         age + sex + education + residence + diabetes + family_history_htn +
#         health_insurance + knowledge_score + distance_to_facility_km


# TASK 3. Check multicollinearity with car::vif(model). Any value > 5?


# TASK 4. Produce a publication-ready table of adjusted ORs:
#         gtsummary::tbl_regression(model, exponentiate = TRUE)
#         (or broom::tidy(model, exponentiate = TRUE, conf.int = TRUE)).
#         Save it to Resources/.


# TASK 5. Create and save a forest plot of the adjusted odds ratios.


# TASK 6. Compute the model's AUC with pROC to summarise discrimination.


# TASK 7. Write a 150-250 word Results section in plain clinical English that
#         reports the significant determinants with their adjusted ORs and 95%
#         CIs, and one sentence on model discrimination. Save it as a .txt file.


# QUESTION: which determinant has the largest adjusted effect, and which has
# the widest confidence interval? What does the width tell you?
# ============================================================================
