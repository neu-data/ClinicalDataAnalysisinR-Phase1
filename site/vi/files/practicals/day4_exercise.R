# ============================================================================
# DAY 4 GUIDED EXERCISE  -  Identify determinants of treatment uptake
# Clinical Data Analysis in R - Phase I | Neudata
# ----------------------------------------------------------------------------
# Time: 15-30 minutes. Solution: Solutions/day4_solution.R
# ============================================================================

library(tidyverse)
library(broom)

# TASK 1. Reload the cleaned data and restrict to diagnosed hypertensives.
analysis_data <- readRDS("Data/analysis_data.rds")
dx <- filter(analysis_data, htn_diagnosed == "Yes")
nrow(dx)

# TASK 2. Is age normally distributed in dx? Draw a histogram and a Q-Q plot
#         (qqnorm/qqline). Decide: t-test or Wilcoxon for comparing age by
#         treatment_uptake? Run the test you chose and interpret the p-value.


# TASK 3. Test whether treatment_uptake is associated with diabetes using a
#         chi-square test on table(dx$treatment_uptake, dx$diabetes).
#         Interpret the result.


# TASK 4. Fit a SIMPLE logistic regression of treatment_uptake on diabetes.
#         Report the odds ratio and 95% CI (exp(coef), exp(confint)).
#         Interpret the OR in one clinical sentence.


# TASK 5. Fit a simple logistic regression with age as the predictor.
#         What is the OR per 1 year? per 10 years (OR^10)?


# TASK 6. Fit a MULTIPLE logistic regression of treatment_uptake on
#         age + sex + diabetes + residence + health_insurance.
#         Produce a tidy table of adjusted ORs with broom::tidy(...,
#         exponentiate = TRUE, conf.int = TRUE).


# QUESTION: list the variables that are statistically significant determinants
# of treatment uptake, and state the direction of each effect.
# ============================================================================
