# ============================================================================
# DAY 1 GUIDED EXERCISE  -  Import the simulated clinical dataset
# Clinical Data Analysis in R - Phase I | Neudata
# ----------------------------------------------------------------------------
# Time: 15-30 minutes. Work in your RStudio Project (root = Course/).
# Type the code yourself; do not copy-paste. Ask when stuck.
# Solution: Solutions/day1_solution.R
# ============================================================================

# TASK 1. Load the packages you need (tidyverse and readxl).


# TASK 2. Import the CSV file Data/hypertension_phc_raw.csv into an object
#         called `htn`. How many rows and columns does it have?


# TASK 3. Import the Excel version Data/hypertension_phc_raw.xlsx (sheet "data")
#         into an object called `htn_xl`. Confirm it has the same dimensions.


# TASK 4. Use glimpse() to view the structure. List THREE variables that look
#         numeric and THREE that look categorical.


# TASK 5. Print summary() of the age variable. What is the maximum age?
#         Is it plausible? Write your answer as a comment.


# TASK 6. Make a frequency table of the `sex` variable with table().
#         How many different spellings of sex do you see? Why is that a problem?


# TASK 7. (Stretch) How many patients attend "Nyamagana PHC"? Try
#         table(htn$facility). Do any facility names have extra spaces?

# Write one sentence: what TWO data problems did you already find on Day 1?
# ============================================================================
