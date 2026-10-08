# =====================================================================
#  SOLUTION 1, Meet Your Dataset
# =====================================================================
library(tidyverse)
clinical_data <- read_csv("Data/clinical_data_clean.csv")

dim(clinical_data)
colSums(is.na(clinical_data))

# ---- Answers -------------------------------------------------------
# Q1. Patients (rows): 430
# Q2. Variables (columns): 20
# Q3. Categorical variables (any three of):
#     sex, smoking, alcohol_use, hypertension, diabetes, treatment, hospital
#     (patient_id is an identifier; outcome is a 0/1 indicator;
#      admission_date and followup_date are dates.)
# Q4. Continuous variables (any three of):
#     age, weight_kg, height_cm, BMI, systolic_bp, diastolic_bp,
#     glucose, cholesterol, time_to_event
# Q5. Missing data: NONE, the CLEAN file has no missing values (that is the
#     point of cleaning). Missingness lives in clinical_data_raw.csv, which you
#     clean in Lesson 2 / Exercise 2.
