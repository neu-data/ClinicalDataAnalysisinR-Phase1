# =====================================================================
#  SOLUTION 2 — Data Management
# =====================================================================
library(tidyverse)
raw <- read_csv("Data/clinical_data_raw.csv")

colSums(is.na(raw))
sum(duplicated(raw))

clean <- raw %>%
  distinct() %>%
  mutate(sex = case_when(
    sex %in% c("Female", "female", "F", "f") ~ "Female",
    sex %in% c("Male",   "male",   "M", "m") ~ "Male"
  )) %>%
  mutate(
    bmi_group = case_when(
      BMI < 18.5 ~ "Underweight",
      BMI < 25   ~ "Normal",
      BMI < 30   ~ "Overweight",
      BMI >= 30  ~ "Obese"
    ),
    pulse_pressure = systolic_bp - diastolic_bp
  )

# Q5 code: patients aged 60 or over
clean %>% filter(age >= 60) %>% nrow()

# ---- Answers -------------------------------------------------------
# Q1. Missing values were in: glucose (22 - the most), cholesterol (18),
#     alcohol_use (12), BMI (9), followup_date (7), diastolic_bp (5).
# Q2. There were 3 duplicate rows; 430 unique patients remained.
# Q3. About 92 patients fall in the "Obese" group here. (This is computed on the
#     partially-cleaned raw data, which still contains a few impossible/missing
#     BMI values; after full cleaning — Lesson 2 — the count is 93.)
# Q4. pulse_pressure = systolic - diastolic BP. It reflects arterial stiffness;
#     a wide pulse pressure is common in older patients.
# Q5. 148 patients are aged 60 or over.
