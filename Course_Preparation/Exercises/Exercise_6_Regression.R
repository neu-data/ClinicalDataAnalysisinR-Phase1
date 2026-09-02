# =====================================================================
#  EXERCISE 6 — Regression
#  Clinical Data Analysis in R (Phase I) — Pre-course
#  ------------------------------------------------------------------
#  Goal: fit a simple logistic regression and read the odds ratios.
#  Answers: Solutions/Solution_6_Regression.R
# =====================================================================

library(tidyverse)
library(broom)
clinical_data <- read_csv("Data/clinical_data_clean.csv")

# Make hypertension a factor with "No" as the reference group
clinical_data <- clinical_data %>%
  mutate(hypertension = factor(hypertension, levels = c("No", "Yes")))

# 1. Fit a logistic regression --------------------------------------
#    Outcome: hypertension (Yes/No).  Predictors: age, sex, BMI.
model <- glm(hypertension ~ age + sex + BMI,
             data = clinical_data,
             family = binomial)

# 2. Look at the raw output (log-odds scale) ------------------------
summary(model)

# 3. Convert to odds ratios with 95% confidence intervals -----------
tidy(model, exponentiate = TRUE, conf.int = TRUE)

# ------------------------------------------------------------------
#  QUESTIONS
# ------------------------------------------------------------------
# Q1. What is the OUTCOME in this model?
#     ANSWER:
# Q2. What are the PREDICTORS?
#     ANSWER:
# Q3. What is the odds ratio (OR) for age? For BMI?
#     ANSWER:
# Q4. Give the 95% confidence interval for the BMI odds ratio.
#     ANSWER:
# Q5. Which predictors are statistically significant?
#     (Hint: is the p-value < 0.05, and does the CI exclude 1?)
#     ANSWER:
# Q6. Write ONE clinical sentence interpreting the effect of BMI.
#     ANSWER:
