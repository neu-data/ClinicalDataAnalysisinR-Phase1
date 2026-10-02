# ============================================================================
# Clinical Data Analysis in R - Phase I
# DAY 3 LIVE DEMONSTRATION:  Descriptive Statistics & Publication-Quality
#                            Tables and Figures
#
# Goal: describe the study sample numerically and visually, then build a
#       manuscript-ready "Table 1" and a set of journal-quality figures.
#
# Study: Determinants of Hypertension Treatment Uptake among Adults attending
#        Primary Healthcare Facilities (multicentre cross-sectional, n = 1500).
#
# This script READS the clean data produced on Day 2 (Data/analysis_data.rds).
# Every figure is SAVED to the Resources/ folder at 300 dpi.
#
# Author:  Bernard Isekah Osang'ir & My Luong Vuong | Neudata | #ClearDataClearImpact
# ============================================================================

# ----------------------------------------------------------------------------
# 0. PACKAGES & SETUP
# ----------------------------------------------------------------------------
library(tidyverse)     # dplyr, ggplot2, readr, etc. - our everyday toolkit
library(gtsummary)     # the gold standard for "Table 1" in R
# install.packages("gtsummary")   # <- run once if not installed

# Course branding colour - a teal accent used across all our figures.
# KEY TEACHING POINT: define styling ONCE as a variable, reuse everywhere.
# If the brand colour ever changes, you edit a single line.
course_teal <- "#0D7377"

# Make sure the output folder exists (does nothing if it already does).
if (!dir.exists("Resources")) dir.create("Resources")

# ----------------------------------------------------------------------------
# 1. RELOAD THE ANALYSIS-READY DATA
# ----------------------------------------------------------------------------
# We ALWAYS start from the saved clean file - never re-clean by hand.
# This guarantees Day 3 uses exactly the same data as Days 4 and 5.
analysis_data <- readRDS("Data/analysis_data.rds")

glimpse(analysis_data)          # quick look at columns and types
nrow(analysis_data)             # 1500 patients


# ============================================================================
# 2. MEASURES OF CENTRAL TENDENCY & SPREAD
# ============================================================================
# Central tendency = "where is the middle?"  (mean, median)
# Spread           = "how scattered are the values?"  (sd, IQR, range)
#
# COMMON MISTAKE (the #1 reason a summary returns NA):
#   If a column has ANY missing value, mean()/sd() return NA by default.
#   You MUST pass na.rm = TRUE to tell R "ignore the missing values".
# ----------------------------------------------------------------------------

# Demonstrate the trap first, then the fix, on systolic blood pressure.
mean(analysis_data$sbp_mmhg)                 # may be NA if any value missing
mean(analysis_data$sbp_mmhg, na.rm = TRUE)   # the CORRECT way

# --- Age (years) ---
mean(analysis_data$age, na.rm = TRUE)        # average age
median(analysis_data$age, na.rm = TRUE)      # middle age (robust to outliers)
sd(analysis_data$age, na.rm = TRUE)          # standard deviation
IQR(analysis_data$age, na.rm = TRUE)         # interquartile range (Q3 - Q1)
quantile(analysis_data$age,                  # the five-number summary + custom cuts
         probs = c(0, 0.25, 0.5, 0.75, 1),
         na.rm = TRUE)

# --- Systolic blood pressure (mmHg) ---
mean(analysis_data$sbp_mmhg, na.rm = TRUE)
median(analysis_data$sbp_mmhg, na.rm = TRUE)
sd(analysis_data$sbp_mmhg, na.rm = TRUE)
IQR(analysis_data$sbp_mmhg, na.rm = TRUE)

# --- Body Mass Index (kg/m^2) ---
mean(analysis_data$bmi, na.rm = TRUE)
median(analysis_data$bmi, na.rm = TRUE)
sd(analysis_data$bmi, na.rm = TRUE)

# CLINICAL INTERPRETATION:
#   When mean and median are close, the distribution is roughly symmetric and
#   the mean is a fair summary. When the mean is pulled ABOVE the median
#   (common for BP and BMI), the data are right-skewed - a few high values
#   drag the mean up, so the MEDIAN (IQR) is often the better summary to report.


# ============================================================================
# 3. summary() AND A GROUPED NUMERIC-SUMMARY TABLE
# ============================================================================

# 3a. Base-R one-liner: summary() of selected numeric columns at once.
#     Great for a fast eyeball check; not for publication.
analysis_data |>
  select(age, bmi, sbp_mmhg, dbp_mmhg, total_chol_mmol_l) |>
  summary()

# 3b. A tidy, reusable summary table grouped by the PRIMARY OUTCOME.
#     across() applies the SAME set of functions to MANY columns at once -
#     no copy-paste, no typos.
# KEY TEACHING POINT: list = list(...) names each statistic so the output
# columns are self-documenting (e.g. age_mean, age_sd).
numeric_summary <- analysis_data |>
  group_by(treatment_uptake) |>
  summarise(
    n = n(),
    across(
      c(age, bmi, sbp_mmhg, dbp_mmhg),
      list(
        mean   = ~ mean(.x, na.rm = TRUE),
        sd     = ~ sd(.x,   na.rm = TRUE),
        median = ~ median(.x, na.rm = TRUE)
      ),
      .names = "{.col}_{.fn}"
    ),
    .groups = "drop"
  )
print(numeric_summary)

# CLINICAL INTERPRETATION: compare the rows. If treated patients have a higher
# mean age and SBP, that is an early signal that older / sicker patients are
# the ones being started on treatment - we will test this formally in Table 1.


# ============================================================================
# 4. FREQUENCY TABLES (categorical variables)
# ============================================================================
# Three ways to count categories - know all three, they appear everywhere.

# 4a. Base R: table() = counts,  prop.table() = proportions.
table(analysis_data$sex)                       # raw counts
prop.table(table(analysis_data$sex))           # proportions (sum to 1)
round(100 * prop.table(table(analysis_data$sex)), 1)   # as percentages

table(analysis_data$bp_category)
round(100 * prop.table(table(analysis_data$bp_category)), 1)

# COMMON MISTAKE: table() SILENTLY DROPS NAs by default, so percentages can be
# misleading. Use useNA = "ifany" to make missing values visible.
table(analysis_data$education, useNA = "ifany")

# 4b. tidyverse: count() returns a tidy data frame you can pipe onward.
analysis_data |> count(sex)
analysis_data |>
  count(education) |>
  mutate(percent = round(100 * n / sum(n), 1))

analysis_data |>
  count(bp_category) |>
  mutate(percent = round(100 * n / sum(n), 1))


# ============================================================================
# 5. CROSS-TABULATIONS (two categorical variables together)
# ============================================================================
# A 2x2 (or larger) table of outcome vs a predictor.
xtab <- table(analysis_data$treatment_uptake, analysis_data$diabetes)
xtab        # rows = treatment_uptake, columns = diabetes

# Proportions can be taken three ways - the MARGIN argument decides which.
# KEY TEACHING POINT: margin = 1 -> ROW percentages (each row sums to 100%)
#                     margin = 2 -> COLUMN percentages (each column sums to 100%)
#                     no margin  -> percentage of the GRAND total.
round(100 * prop.table(xtab, margin = 1), 1)   # row %: among the treated, what % are diabetic?
round(100 * prop.table(xtab, margin = 2), 1)   # col %: among diabetics, what % got treated?

# CLINICAL INTERPRETATION: choose the percentage that answers your question.
#   "What proportion of diabetics are on treatment?"  -> COLUMN % (margin = 2).
#   "What proportion of treated patients are diabetic?" -> ROW % (margin = 1).
# Reporting the wrong margin is one of the most common errors in manuscripts.

# tidyverse equivalent - a tidy cross-tab is just a two-variable count():
analysis_data |> count(treatment_uptake, diabetes)


# ============================================================================
# 6. "TABLE 1" - BASELINE CHARACTERISTICS WITH gtsummary
# ============================================================================
# This is the table every clinical manuscript opens with. gtsummary picks
# sensible summaries automatically: mean (SD) or median (IQR) for numerics,
# n (%) for categoricals, and handles missing data labelling for you.

table1 <- analysis_data |>
  # pick the baseline variables a reviewer expects to see
  select(
    age, sex, residence, education, bmi, bmi_cat,
    smoking, alcohol, physical_activity,
    family_history_htn, diabetes,
    sbp_mmhg, dbp_mmhg, bp_category,
    total_chol_mmol_l, fasting_glucose_mmol_l,
    treatment_uptake
  ) |>
  tbl_summary(
    by = treatment_uptake,                       # one column per outcome group
    missing_text = "(Missing)",                  # label NAs explicitly
    label = list(                                # human-readable row labels
      age ~ "Age (years)",
      sex ~ "Sex",
      bmi ~ "BMI (kg/m^2)",
      sbp_mmhg ~ "Systolic BP (mmHg)",
      dbp_mmhg ~ "Diastolic BP (mmHg)"
    )
  ) |>
  add_p() |>                                     # add a p-value column
  add_overall() |>                               # add a total column
  bold_labels() |>                               # bold the variable names
  modify_caption("**Table 1. Baseline characteristics by treatment uptake**")

table1   # prints in the Viewer / RStudio

# --- Exporting the gtsummary table ---
# To a Word document (ideal for manuscripts):
#   table1 |> as_flex_table() |>
#     flextable::save_as_docx(path = "Resources/table1_demo.docx")
# To an HTML file:
#   table1 |> as_gt() |> gt::gtsave("Resources/table1_demo.html")

# BASE-R FALLBACK (if gtsummary is NOT installed):
#   Build the table by hand with table()/prop.table() per variable, or use
#   aggregate(age ~ treatment_uptake, data = analysis_data, FUN = mean).
#   gtsummary simply automates this so you do not assemble it cell by cell.


# ============================================================================
# 7. PUBLICATION-QUALITY FIGURES (ggplot2) - each SAVED to Resources/
# ============================================================================
# Every plot: clear title, axis labels WITH UNITS, theme_minimal(), teal accent.
# ggsave() writes the LAST printed plot (or the object you pass) to a file.

# --- 7a. Histogram of age ---
p_age <- ggplot(analysis_data, aes(x = age)) +
  geom_histogram(binwidth = 5, fill = course_teal, colour = "white") +
  labs(
    title = "Age distribution of study participants",
    x = "Age (years)", y = "Number of patients"
  ) +
  theme_minimal(base_size = 13)
print(p_age)
ggsave("Resources/day3_hist_age.png", plot = p_age,
       width = 7, height = 5, dpi = 300)

# --- 7b. Histogram + density of systolic BP ---
# aes(y = after_stat(density)) rescales the histogram so a density curve overlays it.
p_sbp <- ggplot(analysis_data, aes(x = sbp_mmhg)) +
  geom_histogram(aes(y = after_stat(density)),
                 binwidth = 5, fill = course_teal, colour = "white", alpha = 0.7) +
  geom_density(linewidth = 1, colour = "grey20") +
  labs(
    title = "Distribution of systolic blood pressure",
    x = "Systolic BP (mmHg)", y = "Density"
  ) +
  theme_minimal(base_size = 13)
print(p_sbp)
ggsave("Resources/day3_hist_sbp.png", plot = p_sbp,
       width = 7, height = 5, dpi = 300)

# --- 7c. Bar chart of education level ---
# geom_bar() counts the categories for you (do NOT pre-summarise).
p_edu <- ggplot(analysis_data, aes(x = education)) +
  geom_bar(fill = course_teal) +
  labs(
    title = "Educational attainment of participants",
    x = "Education level", y = "Number of patients"
  ) +
  theme_minimal(base_size = 13)
print(p_edu)
ggsave("Resources/day3_bar_education.png", plot = p_edu,
       width = 7, height = 5, dpi = 300)

# --- 7d. Boxplot of SBP by treatment uptake ---
# COMMON MISTAKE: forgetting na.rm = TRUE makes ggplot print a warning and
# silently drop rows; we keep it explicit so the message is expected.
p_box_sbp <- ggplot(analysis_data,
                    aes(x = treatment_uptake, y = sbp_mmhg)) +
  geom_boxplot(fill = course_teal, alpha = 0.6, na.rm = TRUE) +
  labs(
    title = "Systolic BP by treatment uptake",
    x = "On hypertension treatment?", y = "Systolic BP (mmHg)"
  ) +
  theme_minimal(base_size = 13)
print(p_box_sbp)
ggsave("Resources/day3_box_sbp_by_treatment.png", plot = p_box_sbp,
       width = 7, height = 5, dpi = 300)

# --- 7e. Boxplot of BMI by blood-pressure category ---
p_box_bmi <- ggplot(analysis_data,
                    aes(x = bp_category, y = bmi)) +
  geom_boxplot(fill = course_teal, alpha = 0.6, na.rm = TRUE) +
  labs(
    title = "BMI across blood-pressure categories",
    x = "Blood-pressure category", y = "BMI (kg/m^2)"
  ) +
  theme_minimal(base_size = 13)
print(p_box_bmi)
ggsave("Resources/day3_box_bmi_by_bpcat.png", plot = p_box_bmi,
       width = 7, height = 5, dpi = 300)

# --- 7f. Scatterplot of SBP vs BMI with a smoother ---
# geom_smooth() adds a fitted trend; method = "lm" draws a straight regression line.
p_scatter <- ggplot(analysis_data, aes(x = bmi, y = sbp_mmhg)) +
  geom_point(alpha = 0.3, colour = course_teal) +
  geom_smooth(method = "lm", se = TRUE, colour = "grey20") +
  labs(
    title = "Systolic BP vs BMI",
    subtitle = "Each point is one patient; line shows the linear trend",
    x = "BMI (kg/m^2)", y = "Systolic BP (mmHg)"
  ) +
  theme_minimal(base_size = 13)
print(p_scatter)
ggsave("Resources/day3_scatter_sbp_bmi.png", plot = p_scatter,
       width = 7, height = 5, dpi = 300)

# CLINICAL INTERPRETATION: an upward-sloping line suggests higher BMI tends to
# accompany higher systolic BP - consistent with obesity as a hypertension
# risk factor. NOTE: this is association, not proof of causation.


# ============================================================================
# 8. EXPORTING A SUMMARY TABLE TO CSV
# ============================================================================
# Share numbers with co-authors who do not use R: write a plain CSV.
write_csv(numeric_summary, "Resources/day3_numeric_summary.csv")

message("Day 3 demo complete - figures and tables written to Resources/.")

# ----------------------------------------------------------------------------
# RECAP:
#  * Always use na.rm = TRUE in summaries (the #1 beginner trap).
#  * Choose median (IQR) over mean (SD) for skewed clinical variables.
#  * Pick the correct prop.table() margin for the question you are asking.
#  * gtsummary turns raw data into a manuscript Table 1 in a few lines.
#  * Save every figure with ggsave() at 300 dpi for publication.
# ----------------------------------------------------------------------------
