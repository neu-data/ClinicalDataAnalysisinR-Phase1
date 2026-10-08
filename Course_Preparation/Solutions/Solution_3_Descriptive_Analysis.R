# =====================================================================
#  SOLUTION 3, Descriptive Analysis
# =====================================================================
library(tidyverse)
clinical_data <- read_csv("Data/clinical_data_clean.csv")

mean(clinical_data$age)                          # 54.2
median(clinical_data$BMI)                        # 26.6
mean(clinical_data$sex == "Female") * 100        # 54.7 %
mean(clinical_data$hypertension == "Yes") * 100  # 36.0 %

clinical_data %>%
  group_by(sex) %>%
  summarise(mean_systolic = mean(systolic_bp),
            mean_diastolic = mean(diastolic_bp))

# ---- Answers -------------------------------------------------------
# Q1. Mean age = 54.2 years.
# Q2. Median BMI = 26.6 kg/m2.
# Q3. 54.7 % of patients are female.
# Q4. Hypertension prevalence = 36.0 %.
# Q5. No, mean systolic BP is almost identical in men (~124.5) and women
#     (~124.3). (Lesson 4 confirms this with a t-test: p ~ 0.85.)
