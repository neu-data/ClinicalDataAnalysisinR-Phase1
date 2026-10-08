# =====================================================================
#  EXERCISE 4, Visualisation
#  Clinical Data Analysis in R (Phase I), Pre-course
#  ------------------------------------------------------------------
#  Goal: create the four core plots and interpret each one.
#  Answers: Solutions/Solution_4_Visualization.R
# =====================================================================

library(tidyverse)
clinical_data <- read_csv("Data/clinical_data_clean.csv")

# 1. Histogram, distribution of systolic BP ------------------------
ggplot(clinical_data, aes(x = systolic_bp)) +
  geom_histogram(binwidth = 5, fill = "#0D7377", colour = "white") +
  labs(title = "Distribution of systolic BP",
       x = "Systolic BP (mmHg)", y = "Number of patients")

# 2. Boxplot, BMI by sex -------------------------------------------
ggplot(clinical_data, aes(x = sex, y = BMI, fill = sex)) +
  geom_boxplot() +
  labs(title = "BMI by sex", x = "Sex", y = "BMI (kg/m2)") +
  theme(legend.position = "none")

# 3. Bar plot, number of patients per hospital ---------------------
ggplot(clinical_data, aes(x = hospital, fill = hospital)) +
  geom_bar() +
  labs(title = "Patients per hospital", x = NULL, y = "Number of patients") +
  theme(legend.position = "none") +
  coord_flip()          # horizontal bars so labels are readable

# 4. Scatterplot, age against systolic BP --------------------------
ggplot(clinical_data, aes(x = age, y = systolic_bp)) +
  geom_point(alpha = 0.5, colour = "#0D7377") +
  geom_smooth(method = "lm", se = TRUE, colour = "#C1440E") +
  labs(title = "Systolic BP against age",
       x = "Age (years)", y = "Systolic BP (mmHg)")

# ------------------------------------------------------------------
#  QUESTIONS  (interpret each plot)
# ------------------------------------------------------------------
# Q1. Is the distribution of systolic BP roughly symmetric or skewed?
#     ANSWER:
# Q2. Do men and women differ much in BMI?
#     ANSWER:
# Q3. Which hospital recruited the most patients?
#     ANSWER:
# Q4. Does systolic BP tend to rise, fall, or stay flat with age?
#     ANSWER:
