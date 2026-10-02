# =====================================================================
#  EXERCISE 2 — Data Management
#  Clinical Data Analysis in R (Phase I) — Pre-course
#  ------------------------------------------------------------------
#  Goal: practise the everyday data-cleaning verbs on the messy file.
#  Answers: Solutions/Solution_2_Data_Management.R
# =====================================================================

library(tidyverse)

# Read the RAW (messy) dataset
raw <- read_csv("Data/clinical_data_raw.csv")

# 1. Identify problems ----------------------------------------------
colSums(is.na(raw))      # (a) which columns have missing values?
sum(duplicated(raw))     # (b) how many duplicate rows?
table(raw$sex)           # (c) how many different ways is sex written?

# 2. Remove duplicates ----------------------------------------------
clean <- raw %>% distinct()
nrow(clean)              # how many unique patients remain?

# 3. Recode sex into two clean labels -------------------------------
clean <- clean %>%
  mutate(sex = case_when(
    sex %in% c("Female", "female", "F", "f") ~ "Female",
    sex %in% c("Male",   "male",   "M", "m") ~ "Male"
  ))
table(clean$sex)

# 4. filter() and select() ------------------------------------------
# Keep only women, and only a few columns
women <- clean %>%
  filter(sex == "Female") %>%
  select(patient_id, age, BMI, systolic_bp)
head(women)

# 5. Create new variables with mutate() + case_when() ---------------
clean <- clean %>%
  mutate(
    bmi_group = case_when(
      BMI < 18.5 ~ "Underweight",
      BMI < 25   ~ "Normal",
      BMI < 30   ~ "Overweight",
      BMI >= 30  ~ "Obese"
    ),
    age_group = case_when(
      age < 40  ~ "<40",
      age < 55  ~ "40-54",
      age < 70  ~ "55-69",
      age >= 70 ~ "70+"
    ),
    pulse_pressure = systolic_bp - diastolic_bp   # a derived variable
  )

table(clean$bmi_group)
table(clean$age_group)

# ------------------------------------------------------------------
#  QUESTIONS
# ------------------------------------------------------------------
# Q1. Which columns contained missing values, and which had the most?
#     ANSWER:
# Q2. How many duplicate rows were there, and how many unique patients remained?
#     ANSWER:
# Q3. How many patients are in the "Obese" BMI group?
#     ANSWER:
# Q4. What does 'pulse_pressure' represent clinically?
#     ANSWER:
# Q5. Use filter() to count how many patients are aged 60 or over.
#     (Write the code and the answer.)
#     ANSWER:
