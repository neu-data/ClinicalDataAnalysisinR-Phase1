# =====================================================================
#  SOLUTION 4, Visualisation
# =====================================================================
library(tidyverse)
clinical_data <- read_csv("Data/clinical_data_clean.csv")

# (The four plots are identical to the exercise; see Exercise_4 for the code.)

# ---- Answers (interpretation) --------------------------------------
# Q1. Systolic BP is roughly symmetric and bell-shaped, centred around
#     120-125 mmHg, with a modest right tail, a fairly normal distribution.
# Q2. Men and women have broadly similar BMI; the boxes overlap heavily, so any
#     difference is small.
# Q3. Riverside Clinic recruited the most patients (104), closely followed by
#     Central Hospital (103). Lakeside Health recruited the fewest (51).
# Q4. Systolic BP tends to RISE with age, the fitted line slopes upward
#     (this matches the correlation r ~ 0.55 found in Lesson 4).
