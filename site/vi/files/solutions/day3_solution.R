# ============================================================================
# Clinical Data Analysis in R - Phase I
# DAY 3 EXERCISE - WORKED SOLUTION:  "Produce Table 1 for a manuscript"
#
# Task (as set in the practical):
#   Using the clean analysis data, restrict to a sensible analytic sample and
#   produce a polished, publication-ready Table 1 of baseline characteristics
#   compared BY treatment uptake, with p-values and a caption. Save the table
#   to Resources/. Then produce two publication figures and save them too.
#
# Study: Determinants of Hypertension Treatment Uptake among Adults attending
#        Primary Healthcare Facilities (multicentre cross-sectional, n = 1500).
#
# Author:  Bernard Isekah Osang'ir & My Luong Vuong | Neudata | #ClearDataClearImpact
# ============================================================================

# ----------------------------------------------------------------------------
# 0. PACKAGES & SETUP
# ----------------------------------------------------------------------------
library(tidyverse)
library(gtsummary)
# These help save the gtsummary table as HTML / PNG. Install once if needed:
# install.packages(c("gt", "gtsummary"))

course_teal <- "#0D7377"                       # course branding colour
if (!dir.exists("Resources")) dir.create("Resources")

# ----------------------------------------------------------------------------
# 1. RELOAD THE ANALYSIS-READY DATA
# ----------------------------------------------------------------------------
analysis_data <- readRDS("Data/analysis_data.rds")
glimpse(analysis_data)

# ----------------------------------------------------------------------------
# 2. DEFINE A SENSIBLE ANALYTIC SAMPLE
# ----------------------------------------------------------------------------
# For a Table 1 comparing patients BY treatment uptake, every patient must have
# a known treatment-uptake status (the grouping variable). We therefore drop
# the few rows where treatment_uptake is missing. We also confirm the study
# eligibility (adults, age >= 18) which the cleaning step already enforced.
#
# TEACHING POINT: always state and count your analytic sample explicitly so
# the manuscript's "we analysed N patients" sentence is reproducible.
analytic <- analysis_data |>
  filter(!is.na(treatment_uptake), age >= 18)

nrow(analysis_data)   # full clean dataset
nrow(analytic)        # analytic sample actually used in Table 1

# ----------------------------------------------------------------------------
# 3. BUILD THE POLISHED TABLE 1
# ----------------------------------------------------------------------------
# We group the variables into the usual manuscript blocks:
#   - Demographics      : age, sex, residence, education, occupation, insurance
#   - Behavioural       : smoking, alcohol, physical activity
#   - Clinical          : BMI (+ category), family history, diabetes, BP + cat
#   - Laboratory        : cholesterol, HDL, LDL, glucose
table1 <- analytic |>
  select(
    # demographics
    age, sex, residence, education, occupation, health_insurance,
    # behavioural
    smoking, alcohol, physical_activity,
    # clinical
    bmi, bmi_cat, family_history_htn, diabetes,
    sbp_mmhg, dbp_mmhg, bp_category,
    # laboratory
    total_chol_mmol_l, hdl_mmol_l, ldl_mmol_l, fasting_glucose_mmol_l,
    # grouping variable (primary outcome)
    treatment_uptake
  ) |>
  tbl_summary(
    by = treatment_uptake,
    missing_text = "(Missing)",
    # report continuous variables as mean (SD) where symmetric;
    # gtsummary defaults to median (IQR) - we override age & BP to mean (SD).
    statistic = list(
      all_continuous()  ~ "{mean} ({sd})",
      all_categorical() ~ "{n} ({p}%)"
    ),
    digits = all_continuous() ~ 1,
    label = list(
      age ~ "Age (years)",
      sex ~ "Sex",
      residence ~ "Residence",
      education ~ "Education level",
      occupation ~ "Occupation",
      health_insurance ~ "Health insurance",
      smoking ~ "Smoking status",
      alcohol ~ "Alcohol use",
      physical_activity ~ "Physical activity",
      bmi ~ "BMI (kg/m^2)",
      bmi_cat ~ "BMI category",
      family_history_htn ~ "Family history of hypertension",
      diabetes ~ "Diabetes",
      sbp_mmhg ~ "Systolic BP (mmHg)",
      dbp_mmhg ~ "Diastolic BP (mmHg)",
      bp_category ~ "Blood-pressure category",
      total_chol_mmol_l ~ "Total cholesterol (mmol/L)",
      hdl_mmol_l ~ "HDL cholesterol (mmol/L)",
      ldl_mmol_l ~ "LDL cholesterol (mmol/L)",
      fasting_glucose_mmol_l ~ "Fasting glucose (mmol/L)"
    )
  ) |>
  add_p() |>                                   # statistical test per variable
  add_overall() |>                             # an overall (total) column
  bold_labels() |>                             # bold variable names
  modify_header(label ~ "**Characteristic**") |>
  modify_spanning_header(
    all_stat_cols() ~ "**Hypertension treatment uptake**"
  ) |>
  modify_caption(
    "**Table 1. Baseline characteristics of participants, by hypertension treatment uptake (N = {nrow(analytic)})**"
  )

table1   # preview in the Viewer

# ----------------------------------------------------------------------------
# 4. SAVE THE TABLE
# ----------------------------------------------------------------------------
# Preferred: convert to a gt object and save as HTML (and PNG) to Resources/.
# Wrapped in tryCatch so the script still finishes if the optional packages
# (gt / webshot2 for PNG) are missing - it then falls back to a CSV export.
saved_ok <- tryCatch({
  gt_table1 <- as_gt(table1)
  gt::gtsave(gt_table1, filename = "Resources/table1_baseline.html")
  # PNG export needs the 'webshot2' package; ignore quietly if unavailable.
  try(gt::gtsave(gt_table1, filename = "Resources/table1_baseline.png"),
      silent = TRUE)
  TRUE
}, error = function(e) {
  message("gt/gtsave unavailable - falling back to CSV: ", conditionMessage(e))
  FALSE
})

# CSV fallback: a flat data frame of the table body, always written so there
# is ALWAYS a shareable artefact regardless of which packages are installed.
table1_df <- as_tibble(table1)
write_csv(table1_df, "Resources/table1_baseline.csv")

# ----------------------------------------------------------------------------
# 5. INTERPRETATION OF TABLE 1  (what to write in the manuscript)
# ----------------------------------------------------------------------------
# Read DOWN the p-value column to spot what differs between treated and
# untreated patients. In this dataset we typically observe:
#   * Treated patients are OLDER on average (higher mean age, small p-value) -
#     clinicians more readily start older patients on antihypertensives.
#   * DIABETES and FAMILY HISTORY are more common among treated patients -
#     comorbid / higher-risk patients are prioritised for treatment.
#   * Systolic and diastolic BP and the "Hypertension" BP category are more
#     frequent in the treated group, as expected (treatment follows diagnosis).
#   * Demographics such as sex or residence usually differ little (large p),
#     suggesting treatment is driven by clinical need rather than demography.
# CAUTION: these are UNADJUSTED comparisons; confounding is addressed later
# with regression models (Day 4/5). A small p-value flags an association,
# not a causal effect.

# ----------------------------------------------------------------------------
# 6. PUBLICATION FIGURE 1 - Treatment uptake across facilities
# ----------------------------------------------------------------------------
# A grouped/proportional bar chart answers: does uptake vary by facility?
fig1 <- analytic |>
  count(facility, treatment_uptake) |>
  group_by(facility) |>
  mutate(percent = 100 * n / sum(n)) |>
  ungroup() |>
  ggplot(aes(x = facility, y = percent, fill = treatment_uptake)) +
  geom_col(position = "fill") +                      # 100% stacked bars
  scale_y_continuous(labels = scales::label_percent(scale = 1)) +
  scale_fill_manual(values = c(No = "grey70", Yes = course_teal)) +
  labs(
    title = "Hypertension treatment uptake by facility",
    x = "Facility", y = "Percent of patients", fill = "On treatment?"
  ) +
  theme_minimal(base_size = 13) +
  theme(axis.text.x = element_text(angle = 30, hjust = 1))
print(fig1)
ggsave("Resources/day3_fig1_uptake_by_facility.png", plot = fig1,
       width = 8, height = 5, dpi = 300)

# ----------------------------------------------------------------------------
# 7. PUBLICATION FIGURE 2 - Age distribution by treatment uptake
# ----------------------------------------------------------------------------
# Overlaid density curves make the "treated patients are older" finding visual.
fig2 <- ggplot(analytic, aes(x = age, fill = treatment_uptake)) +
  geom_density(alpha = 0.5, na.rm = TRUE) +
  scale_fill_manual(values = c(No = "grey70", Yes = course_teal)) +
  labs(
    title = "Age distribution by treatment uptake",
    subtitle = "Treated patients tend to be older",
    x = "Age (years)", y = "Density", fill = "On treatment?"
  ) +
  theme_minimal(base_size = 13)
print(fig2)
ggsave("Resources/day3_fig2_age_by_treatment.png", plot = fig2,
       width = 7, height = 5, dpi = 300)

message("Day 3 solution complete - Table 1 and 2 figures written to Resources/.")

# ----------------------------------------------------------------------------
# CHECKLIST a reviewer expects from a good Table 1:
#  [x] Clear analytic sample with a stated N.
#  [x] Variables grouped logically (demographic / behavioural / clinical / lab).
#  [x] Appropriate summaries (mean (SD) vs n (%)), missing data shown.
#  [x] A comparison column, p-values, an overall column, and a caption.
#  [x] Saved in a shareable format (HTML/PNG, with CSV fallback).
# ----------------------------------------------------------------------------
