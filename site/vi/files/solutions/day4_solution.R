# ============================================================================
# Clinical Data Analysis in R - Phase I
# DAY 4 EXERCISE - WORKED SOLUTION:  "Identify the Determinants of
#                                     Hypertension Treatment Uptake"
#
# Task: among DIAGNOSED hypertensive patients, work out which patient
#       characteristics are associated with taking up treatment.
#       Step 1 - screen each candidate one at a time (UNADJUSTED odds ratios).
#       Step 2 - put the candidates together in ONE multivariable model
#                (ADJUSTED odds ratios) to see what survives adjustment.
#       Step 3 - present a tidy OR table (CSV) and a forest plot.
#
# Study: Determinants of Hypertension Treatment Uptake among Adults attending
#        Primary Healthcare Facilities (multicentre cross-sectional, n = 1500).
#
# PRIMARY OUTCOME: treatment_uptake (Yes/No), reference = "No".
# ANALYTIC POPULATION: htn_diagnosed == "Yes" (about 1089 patients).
#
# Author:  Bernard Isekah Osang'ir & My Luong Vuong | Neudata | #ClearDataClearImpact
# ============================================================================

# ----------------------------------------------------------------------------
# 0. PACKAGES & SETUP
# ----------------------------------------------------------------------------
library(dplyr)         # data wrangling
library(broom)         # tidy model output (one row per coefficient)
library(ggplot2)       # the forest plot
library(readr)         # write_csv()
# install.packages(c("dplyr", "broom", "ggplot2", "readr"))  # once if needed

course_teal <- "#0D7377"   # course branding colour for the forest plot

# Make sure the output folder exists (does nothing if it already does).
if (!dir.exists("Resources")) dir.create("Resources")

# ----------------------------------------------------------------------------
# 1. LOAD DATA & BUILD THE ANALYTIC SUBSET
# ----------------------------------------------------------------------------
analysis_data <- readRDS("Data/analysis_data.rds")

# Treatment uptake only makes sense for people already diagnosed.
dx <- filter(analysis_data, htn_diagnosed == "Yes")

cat("Analytic sample size:", nrow(dx), "\n")
print(table(dx$treatment_uptake))   # outcome distribution (reference = "No")

# The candidate determinants we were asked to investigate.
candidates <- c("age", "sex", "education", "residence", "diabetes",
                "family_history_htn", "health_insurance",
                "knowledge_score", "distance_to_facility_km")

# ----------------------------------------------------------------------------
# 2. UNIVARIABLE (UNADJUSTED) LOGISTIC REGRESSIONS - one per candidate
# ----------------------------------------------------------------------------
# A univariable model asks: "ignoring everything else, is THIS variable
# associated with uptake?" We fit one logistic model per candidate and pull
# out the tidy odds ratios. Doing it in a loop avoids copy-paste errors.
#
# NOTE: glm() with family = binomial models the odds of the NON-reference
# level of the outcome - here "Yes" (uptake) - which is what we want.

univariable_results <- lapply(candidates, function(var) {
  # Build the formula "treatment_uptake ~ <var>" programmatically.
  f <- as.formula(paste("treatment_uptake ~", var))
  model <- glm(f, data = dx, family = binomial)

  # exponentiate = TRUE  -> odds ratios; conf.int = TRUE -> 95% CI.
  tidy(model, exponentiate = TRUE, conf.int = TRUE) |>
    filter(term != "(Intercept)") |>          # drop the intercept row
    mutate(predictor = var, model = "Unadjusted")
})

# Stack the per-variable results into one table.
univariable_table <- bind_rows(univariable_results) |>
  select(model, predictor, term, OR = estimate,
         conf.low, conf.high, p.value)

cat("\n--- UNADJUSTED odds ratios ---\n")
print(univariable_table, n = Inf)

# INTERPRETATION (unadjusted):
#   OR > 1 and 95% CI excluding 1  -> a positive determinant (raises odds).
#   OR < 1 and 95% CI excluding 1  -> a negative determinant (lowers odds).
#   For ORDERED factors (education, physical_activity) R fits polynomial
#   contrasts (.L = linear, .Q = quadratic, ...); the LINEAR (.L) term is the
#   one to read - a positive, significant .L means odds rise steadily across
#   None < Primary < Secondary < Tertiary.

# ----------------------------------------------------------------------------
# 3. MULTIVARIABLE (ADJUSTED) LOGISTIC REGRESSION - one combined model
# ----------------------------------------------------------------------------
# Now we estimate each predictor's effect WHILE HOLDING THE OTHERS CONSTANT.
# This disentangles overlapping explanations (e.g. educated patients may also
# be more likely to have insurance).
#
# COMPLETE CASES: glm() automatically drops any row missing a value in ANY
# model variable. We report how many patients actually contributed.

multivariable_model <- glm(
  treatment_uptake ~ age + sex + education + residence + diabetes +
    family_history_htn + health_insurance + knowledge_score +
    distance_to_facility_km,
  data   = dx,
  family = binomial
)

cat("\nRows used in the multivariable model (complete cases):",
    nobs(multivariable_model), "of", nrow(dx), "\n")

summary(multivariable_model)

# Tidy ADJUSTED odds ratios.
adjusted_table <- tidy(multivariable_model,
                       exponentiate = TRUE, conf.int = TRUE) |>
  filter(term != "(Intercept)") |>
  mutate(model = "Adjusted") |>
  select(model, term, OR = estimate, conf.low, conf.high, p.value)

cat("\n--- ADJUSTED odds ratios (multivariable model) ---\n")
print(adjusted_table, n = Inf)

# ----------------------------------------------------------------------------
# 4. SAVE THE ODDS-RATIO TABLE TO Resources/
# ----------------------------------------------------------------------------
# Combine unadjusted and adjusted results into one shareable CSV. We rename
# the unadjusted "term" to match so the columns line up.
or_table_combined <- bind_rows(
  univariable_table |> select(model, term, OR, conf.low, conf.high, p.value),
  adjusted_table
) |>
  mutate(across(c(OR, conf.low, conf.high), \(x) round(x, 3)),
         p.value = signif(p.value, 3))

write_csv(or_table_combined, "Resources/day4_odds_ratios.csv")
cat("\nSaved OR table to Resources/day4_odds_ratios.csv\n")

# ----------------------------------------------------------------------------
# 5. FOREST PLOT OF THE ADJUSTED ODDS RATIOS
# ----------------------------------------------------------------------------
# A forest plot is the standard way to display ORs: a point for each estimate,
# a horizontal line for its 95% CI, and a vertical reference line at OR = 1
# (the "no effect" line). The x-axis is on a LOG scale so that, e.g., OR 0.5
# and OR 2 sit symmetrically about 1.

forest_data <- adjusted_table |>
  # readable labels and order terms by effect size for a clean plot.
  mutate(term = factor(term, levels = rev(term)))

forest_plot <- ggplot(forest_data,
                      aes(x = OR, y = term)) +
  # the "no effect" reference line at OR = 1.
  geom_vline(xintercept = 1, linetype = "dashed", colour = "grey50") +
  # the 95% confidence intervals.
  geom_errorbarh(aes(xmin = conf.low, xmax = conf.high),
                 height = 0.2, colour = course_teal) +
  # the point estimates.
  geom_point(size = 3, colour = course_teal) +
  scale_x_log10() +     # log scale - essential for odds ratios
  labs(
    title    = "Adjusted Determinants of Hypertension Treatment Uptake",
    subtitle = "Multivariable logistic regression; OR with 95% CI (reference OR = 1)",
    x        = "Adjusted Odds Ratio (log scale)",
    y        = NULL,
    caption  = "Points right of the dashed line increase the odds of uptake; left of it decrease the odds."
  ) +
  theme_minimal(base_size = 12)

ggsave("Resources/day4_forest_plot.png", plot = forest_plot,
       width = 8, height = 6, dpi = 300)
cat("Saved forest plot to Resources/day4_forest_plot.png\n")

# ----------------------------------------------------------------------------
# 6. INTERPRETATION - WHICH VARIABLES ARE DETERMINANTS, AND WHAT IT MEANS
# ----------------------------------------------------------------------------
# A predictor is a STATISTICALLY SIGNIFICANT determinant when its 95% CI does
# NOT cross 1 (equivalently p < 0.05). Read the ADJUSTED column for the final
# conclusions, since it accounts for the other factors.
#
# Based on how the data were simulated, we EXPECT the following determinants to
# emerge as significant and to INCREASE the odds of treatment uptake (OR > 1):
#   * diabetes (Yes vs No)            - comorbid patients attend care more,
#                                       so are more likely to start treatment.
#   * family_history_htn (Yes vs No)  - awareness through affected relatives.
#   * health_insurance (Yes vs No)    - removes the cost barrier to treatment.
#   * residence = Urban (vs Rural)    - better access to clinics and pharmacy.
#   * education (linear .L term +)     - higher education -> higher uptake.
#   * age (per year; report per 10 yr) - older patients take up more.
#   * knowledge_score (per point)      - better HTN knowledge -> more uptake.
#
# distance_to_facility_km is expected to be a NEGATIVE / non-significant factor
# (greater distance is a barrier); sex is included as a control and is not
# expected to be a strong determinant.
#
# CLINICAL TAKE-HOME: uptake is driven by a mix of ACCESS factors (insurance,
# urban residence, shorter distance) and AWARENESS factors (education,
# knowledge score, family history, comorbidity). Interventions that improve
# insurance coverage and patient knowledge in rural areas are the levers most
# likely to raise treatment uptake.
#
# REMINDER on continuous predictors: the OR for age is "per 1 extra year" and
# for knowledge_score "per 1 extra point" - small numbers near 1. To make them
# meaningful, rescale, e.g. odds ratio per 10 years of age:
#   exp(coef(multivariable_model)["age"] * 10)
# This is a more clinically intuitive way to state the same effect.

# ============================================================================
# OUTPUTS PRODUCED:
#   Resources/day4_odds_ratios.csv  - unadjusted + adjusted OR table
#   Resources/day4_forest_plot.png  - forest plot of adjusted ORs
# ============================================================================
