# =====================================================================
#  SOLUTION 6, Regression
# =====================================================================
library(tidyverse)
library(broom)
clinical_data <- read_csv("Data/clinical_data_clean.csv")

clinical_data <- clinical_data %>%
  mutate(hypertension = factor(hypertension, levels = c("No", "Yes")))

model <- glm(hypertension ~ age + sex + BMI,
             data = clinical_data, family = binomial)

tidy(model, exponentiate = TRUE, conf.int = TRUE)

# ---- Answers -------------------------------------------------------
# Q1. Outcome: hypertension (Yes / No).
# Q2. Predictors: age, sex, BMI.
# Q3. OR for age  ~ 1.09  (each extra year raises the odds ~9%).
#     OR for BMI  ~ 1.16  (each extra BMI unit raises the odds ~16%).
# Q4. 95% CI for the BMI odds ratio: about 1.10 to 1.22.
# Q5. Statistically significant: age and BMI (p < 0.001, CIs exclude 1).
#     Sex is NOT significant (OR ~1.20, 95% CI 0.76-1.90, p ~ 0.43).
# Q6. Example sentence:
#     "Higher BMI was independently associated with hypertension: each additional
#      kg/m2 increased the odds of hypertension by about 16% (OR 1.16,
#      95% CI 1.10-1.22), after adjusting for age and sex."
