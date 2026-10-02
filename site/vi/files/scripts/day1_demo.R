# ============================================================================
# Clinical Data Analysis in R - Phase I
# DAY 1 LIVE DEMONSTRATION:  Introduction to R & RStudio
#
# Study: Determinants of Hypertension Treatment Uptake among Adults
#        attending Primary Healthcare Facilities (multicentre, n = 1,500)
#
# Author:  Bernard Isekah Osang'ir & My Luong Vuong | Neudata | #ClearDataClearImpact
# ----------------------------------------------------------------------------
# HOW TO USE: Run this script line by line (Ctrl+Enter / Cmd+Enter).
#             Read each comment, type the code, watch the Console output.
# ============================================================================


# ----------------------------------------------------------------------------
# 1. R AS A CALCULATOR  -- everything happens in the Console
# ----------------------------------------------------------------------------
# basic calculation
2 + 2
140 / 90              # a blood-pressure ratio, just to show division
sqrt(16)
mean(c(120, 130, 145, 150))   # mean of four systolic readings

# INSTRUCTOR TIP: point out the Console vs the Script editor.
#   - Script  = what you save and re-run (reproducibility).
#   - Console = where results appear.


# ----------------------------------------------------------------------------
# 2. OBJECTS  -- store a value with the assignment arrow  <-
# ----------------------------------------------------------------------------
sbp <- 152            # systolic blood pressure of one patient
sbp
print(sbp)# type the name to print it
SBP
age <- 60
age
sbp + 10 # objects behave like the values they hold
sbp = 152
sbp <- 152

# COMMON MISTAKE: using = instead of <-, or forgetting the object exists.
#   R is case-sensitive:  SBP is NOT the same object as sbp.


# ----------------------------------------------------------------------------
# 3. VECTORS  -- many values of the SAME type
# ----------------------------------------------------------------------------
sbp_readings <- c(152, 138, 145, 160, 129, 142)   # c() = "combine"
sbp_readings
length(sbp_readings)
mean(sbp_readings)
sd(sbp_readings) # standard deviation
max(sbp_readings)
summary(sbp_readings)

# A character vector and a logical vector
sex <- c("Female", "Male", "Female", "Female", "Male", "Female", "Male")
sex

# logical
high_bp <- sbp_readings >= 140      # TRUE / FALSE for each reading
high_bp
sum(high_bp)                        # how many readings were >= 140?


# ----------------------------------------------------------------------------
# 4. PACKAGES  -- install once, load every session
# ----------------------------------------------------------------------------
# install.packages("tidyverse")   # <- run ONCE (already installed in class)
# install.packages("readxl")

library(tidyverse)    # data import, wrangling, ggplot2
library(readxl)       # read Excel files

# COMMON MISTAKE: install.packages() every time (slow / needs internet).
#   You only library() each session.


# ----------------------------------------------------------------------------
# 5. WORKING DIRECTORY & PROJECTS
# ----------------------------------------------------------------------------
getwd()               # where is R looking right now?
# BEST PRACTICE: use an RStudio Project (File > New Project) so paths are
# relative to the project root and the analysis is portable.
# Avoid setwd("C:/Users/.../somewhere") - it breaks on every other computer.


# ----------------------------------------------------------------------------
# 6. IMPORTING THE CLINICAL DATA  -- CSV and Excel
# ----------------------------------------------------------------------------
# Adjust the path if your Data folder is elsewhere. With an RStudio Project
# rooted at "Course/", this relative path works on any machine.

# 6a. CSV
htn <- read_csv("Data/hypertension_phc_raw.csv")

# 6b. Excel (same data, .xlsx) - just to show readxl
htn_xl <- read_excel("Data/hypertension_phc_raw.xlsx", sheet = "data")

# EXPECTED CONSOLE OUTPUT: read_csv prints a column specification and
# "Rows: 1503 Columns: 36". Note 1503 (not 1500) - duplicates lurk here!

# you can also read spss files with the haven package
# E.g.: Import the SPSS file
library(haven)
data <- read_sav("path/to/your/file.sav")

# ----------------------------------------------------------------------------
# 7. FIRST LOOK AT A DATA FRAME
# ----------------------------------------------------------------------------
htn                   # tibble prints first 10 rows neatly
dim(htn)              # rows, columns
nrow(htn); ncol(htn)
names(htn)            # variable names
head(htn, 5)          # first 5 rows
glimpse(htn)          # compact structure: type of every column
# View(htn)           # opens the spreadsheet viewer (run in RStudio)


# ----------------------------------------------------------------------------
# 8. LOOKING AT SINGLE VARIABLES
# ----------------------------------------------------------------------------
# $
htn$age               # the $ extracts one column as a vector
summary(htn$age)      # NOTE the max = 200  -> an impossible age (Day 2!)
table(htn$sex)        # NOTE: Female, F, female, f ... messy (Day 2!)
table(htn$facility)   # the six facilities (some with stray spaces)

# INTERPRETATION: even before any statistics, R is already telling us the
# data need cleaning: impossible ages and inconsistent category spellings.
# That is exactly what Day 2 is about.


# ----------------------------------------------------------------------------
# 9. SAVE NOTHING YET - Day 1 is about getting data IN and looking at it.
# ----------------------------------------------------------------------------
# Recap of what we learned:
#   objects (<-), vectors (c()), functions (mean, summary, table),
#   packages (library), import (read_csv / read_excel), inspect (glimpse).
#
# DAY 1 EXERCISE: see Practicals/day1_exercise.R
# ============================================================================
