# =====================================================================
#  EXERCISE 1, Meet Your Dataset
#  Clinical Data Analysis in R (Phase I), Pre-course
#  ------------------------------------------------------------------
#  Goal: get comfortable opening a dataset and looking around it.
#  This is practice, NOT a test. Run each line and read the output.
#  Answers are in  Solutions/Solution_1_Meet_Your_Dataset.R
# =====================================================================

# 1. Load the tidyverse and read the clean dataset -------------------
library(tidyverse)

clinical_data <- read_csv("Data/clinical_data_clean.csv")
# NOTE: this path assumes you opened the project via
# Clinical_Data_Analysis_PreCourse.Rproj (so R is in the main folder).

# 2. Look at the dataset with the five essential commands -----------
dim(clinical_data)       # rows and columns
names(clinical_data)     # variable names
head(clinical_data)      # first 6 rows
str(clinical_data)       # structure: each variable and its type
summary(clinical_data)   # quick summary of every variable

# 3. A few targeted looks -------------------------------------------
table(clinical_data$sex)            # how many of each sex?
colSums(is.na(clinical_data))       # missing values per column

# ------------------------------------------------------------------
#  QUESTIONS  (write your answers as comments below each one)
# ------------------------------------------------------------------
# Q1. How many patients (rows) are in the dataset?
#     ANSWER:
#
# Q2. How many variables (columns) are there?
#     ANSWER:
#
# Q3. Name three variables that are CATEGORICAL (text/groups).
#     ANSWER:
#
# Q4. Name three variables that are CONTINUOUS (numbers).
#     ANSWER:
#
# Q5. Which variables contain missing data in this clean file?
#     (Hint: look at the colSums(is.na(...)) output.)
#     ANSWER:
