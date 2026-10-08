# =====================================================================
#  EXERCISE 3, Descriptive Analysis
#  Clinical Data Analysis in R (Phase I), Pre-course
#  ------------------------------------------------------------------
#  Goal: summarise the data with simple descriptive statistics.
#  Answers: Solutions/Solution_3_Descriptive_Analysis.R
# =====================================================================

library(tidyverse)
clinical_data <- read_csv("Data/clinical_data_clean.csv")

# 1. Mean age -------------------------------------------------------
mean(clinical_data$age, na.rm = TRUE)

# 2. Median BMI -----------------------------------------------------
median(clinical_data$BMI, na.rm = TRUE)

# 3. Proportion female (as a percentage) ----------------------------
mean(clinical_data$sex == "Female") * 100

# 4. Prevalence of hypertension (as a percentage) -------------------
mean(clinical_data$hypertension == "Yes") * 100

# 5. Mean blood pressure by sex -------------------------------------
clinical_data %>%
  group_by(sex) %>%
  summarise(
    n            = n(),
    mean_systolic  = mean(systolic_bp, na.rm = TRUE),
    mean_diastolic = mean(diastolic_bp, na.rm = TRUE)
  )

# ------------------------------------------------------------------
#  QUESTIONS
# ------------------------------------------------------------------
# Q1. What is the mean age (to 1 decimal place)?
#     ANSWER:
# Q2. What is the median BMI?
#     ANSWER:
# Q3. What percentage of patients are female?
#     ANSWER:
# Q4. What is the prevalence of hypertension?
#     ANSWER:
# Q5. Is mean systolic BP noticeably different between men and women?
#     ANSWER:
