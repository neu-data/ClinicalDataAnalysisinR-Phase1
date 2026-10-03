# =============================================================================
# R Training Course | Day 5 - Regression Modelling & Reproducibility (CAPSTONE)
# Instructor Live Demo
#
# Study: "Determinants of Hypertension Treatment Uptake among Adults attending
#         Primary Healthcare Facilities" (multicentre cross-sectional, n = 1500)
# Primary outcome: treatment_uptake (Yes/No), reference = "No"
# Analytic population: patients with diagnosed hypertension (htn_diagnosed == "Yes")
#
# Author: Vương Mỹ Lượng & Bernard Isekah Osang'ir | Neudata | #ClearDataClearImpact
# =============================================================================

# -----------------------------------------------------------------------------
# 0. PACKAGES
# -----------------------------------------------------------------------------
# TEACHING POINT: load every package up front so the reader knows the toolkit.
# If a package is missing, install it once with install.packages("pkgname").
library(dplyr)        # data wrangling (filter, mutate, ...)
library(ggplot2)      # plotting (forest plot)
library(broom)        # tidy() / augment() - turns model objects into data frames
library(gtsummary)    # publication-ready tables (tbl_regression)
library(car)          # vif() for multicollinearity
library(pROC)         # ROC curve / AUC for model discrimination
# library(here)       # OPTIONAL: here() builds paths from the project root

# REPRODUCIBILITY NOTE: set a seed whenever ANY randomness is involved
# (bootstraps, train/test splits, simulations). Logistic regression itself is
# deterministic, but we set a seed so the whole script is reproducible end-to-end.
set.seed(2025)

# -----------------------------------------------------------------------------
# 1. LOAD DATA AND BUILD THE ANALYTIC SUBSET
# -----------------------------------------------------------------------------
# TEACHING POINT: always load the CLEANED, analysis-ready dataset - never re-clean
# inside an analysis script. Cleaning lives in its own script (separation of concerns).
analysis_data <- readRDS("Data/analysis_data.rds")

# Our research question only concerns people ALREADY DIAGNOSED with hypertension,
# because only they can "take up" treatment. This is the analytic population.
dx <- filter(analysis_data, htn_diagnosed == "Yes")

# COMMON MISTAKE: analysing all 1500 patients. People without a diagnosis cannot
# logically have a treatment-uptake decision - including them biases everything.
nrow(dx)                              # ~1089 - report this n in your paper
table(dx$treatment_uptake)           # check the outcome distribution / events

# CLINICAL CHECK: the reference level of the outcome must be "No" so the model
# estimates the odds of UPTAKE (the event of interest). Confirm it:
levels(dx$treatment_uptake)          # should be c("No", "Yes") -> "No" is reference

# -----------------------------------------------------------------------------
# 2. MODEL-BUILDING PHILOSOPHY
# -----------------------------------------------------------------------------
# TEACHING POINT: build the model from CLINICAL KNOWLEDGE, not from p-values.
# Decide your predictors BEFORE looking at the data, based on:
#   - biological/clinical plausibility (e.g. diabetes drives clinic attendance)
#   - known confounders from the literature (age, sex, education, residence)
#   - the study's stated determinants (access: distance; awareness: knowledge)
# Then fit ONE pre-specified multivariable model. This avoids "data dredging".
#
# COMMON MISTAKE: running stepwise selection on everything and reporting only the
# "significant" variables. That inflates false positives and is hard to replicate.

# Crude (unadjusted) model for ONE predictor - we will use it to show confounding.
crude_residence <- glm(treatment_uptake ~ residence,
                       data = dx, family = binomial(link = "logit"))

# FULL pre-specified multivariable model (our main analysis).
model_full <- glm(
  treatment_uptake ~ age + sex + education + residence + diabetes +
    family_history_htn + health_insurance + knowledge_score +
    distance_to_facility_km,
  data   = dx,
  family = binomial(link = "logit")
)

summary(model_full)   # coefficients are on the LOG-ODDS scale (not yet interpretable)

# -----------------------------------------------------------------------------
# 3. CONFOUNDING: crude vs adjusted OR for residence
# -----------------------------------------------------------------------------
# TEACHING POINT: a confounder distorts the crude association. We see this by
# comparing the CRUDE OR for residence with its ADJUSTED OR (from the full model).
# exp(coefficient) converts log-odds to an ODDS RATIO.

crude_or_residence <- exp(coef(crude_residence))["residenceUrban"]
adj_or_residence   <- exp(coef(model_full))["residenceUrban"]

cat("Crude OR (Urban vs Rural):   ", round(crude_or_residence, 2), "\n")
cat("Adjusted OR (Urban vs Rural):", round(adj_or_residence, 2), "\n")

# CLINICAL INTERPRETATION: if the OR moves noticeably (a rule of thumb is a >10%
# change) when other variables are added, those variables were CONFOUNDING the
# crude residence effect. The adjusted OR is the one you report and interpret,
# e.g. "after adjustment, urban residents had X times the odds of uptake".

# -----------------------------------------------------------------------------
# 4. INTERACTION (EFFECT MODIFICATION)
# -----------------------------------------------------------------------------
# TEACHING POINT: interaction asks "does the effect of A DIFFER across levels of B?"
# Example: does the effect of diabetes on uptake change with age?
# We add the product term and compare the two NESTED models with a likelihood
# ratio test (LRT). The smaller model must be a special case of the larger.

model_interax <- glm(
  treatment_uptake ~ age + sex + education + residence + diabetes +
    family_history_htn + health_insurance + knowledge_score +
    distance_to_facility_km + diabetes:age,   # <- the interaction term
  data   = dx,
  family = binomial(link = "logit")
)

# anova() with test = "LRT" gives the p-value for the ADDED interaction term.
anova(model_full, model_interax, test = "LRT")

# CLINICAL INTERPRETATION: in this dataset the interaction is expected to be
# NON-significant (p > 0.05). When that happens, KEEP THE SIMPLER model_full -
# it is easier to interpret and report. Only retain an interaction if it is both
# statistically supported AND clinically meaningful. Do not chase interactions.
#
# COMMON MISTAKE: interpreting a main effect (e.g. diabetes) in isolation AFTER
# leaving an interaction in the model - once diabetes:age is present, the diabetes
# coefficient is the effect of diabetes only at age = 0, which is meaningless.

# -----------------------------------------------------------------------------
# 5. VARIABLE SELECTION WITH step() - ONE OPTION, USE WITH CAUTION
# -----------------------------------------------------------------------------
# TEACHING POINT: step() searches for the model with the lowest AIC (a measure
# that rewards fit but penalises complexity). It is automated, NOT clinical.
model_step <- step(model_full, direction = "both", trace = 0)

# Compare AIC: lower is "better" by this criterion, but a 1-2 point difference
# is trivial. Prefer the pre-specified clinical model unless step() strongly disagrees.
AIC(model_full, model_step)

# CAUTION (say this out loud to the class):
#   - Stepwise selection produces optimistic p-values and CIs (not corrected for
#     the search), and different datasets give different "selected" models.
#   - It can drop a known confounder just because p > 0.05 - that REINTRODUCES bias.
#   - For an EXPLANATORY study (determinants), keep clinically chosen variables
#     even if non-significant. Reserve step()/AIC mostly for PREDICTION tasks.
# DECISION: we proceed with model_full as our FINAL model.

model_final <- model_full

# -----------------------------------------------------------------------------
# 6. DIAGNOSTICS & ASSUMPTION CHECKS FOR LOGISTIC REGRESSION
# -----------------------------------------------------------------------------

# 6a. MULTICOLLINEARITY - are predictors too correlated with each other?
# TEACHING POINT: VIF (Variance Inflation Factor). Rule of thumb:
#   VIF < 5 fine; 5-10 worth a look; > 10 serious collinearity.
car::vif(model_final)
# For factors, car reports GVIF^(1/(2*Df)); compare its SQUARE to the VIF thresholds.

# 6b. LINEARITY OF CONTINUOUS PREDICTORS ON THE LOGIT
# TEACHING POINT: logistic regression assumes each CONTINUOUS predictor is
# linear on the LOG-ODDS scale (not on the probability scale). A quick visual
# check: plot the predictor against the empirical logit, or add a smoother.
# A formal check is the Box-Tidwell test (add term x*log(x)).
ggplot(dx, aes(x = knowledge_score,
               y = as.numeric(treatment_uptake) - 1)) +    # 0/1 outcome
  geom_jitter(height = 0.03, alpha = 0.2) +
  geom_smooth(method = "loess", se = FALSE) +              # should be ~monotonic
  labs(title = "Linearity check: knowledge_score vs P(uptake)",
       x = "Knowledge score", y = "Treatment uptake (0/1)")
# COMMON MISTAKE: assuming linearity on the probability scale - logistic curves
# are S-shaped in probability but should be straight in the logit.

# 6c. INFLUENTIAL OBSERVATIONS - Cook's distance via broom::augment()
# TEACHING POINT: a few extreme records can pull the whole model. augment()
# returns one row per observation with diagnostics (.cooksd, .hat, .resid).
aug <- broom::augment(model_final)
infl_cut <- 4 / nrow(aug)                                  # common Cook's D cutoff
sum(aug$.cooksd > infl_cut, na.rm = TRUE)                  # how many flagged?

ggplot(aug, aes(x = seq_along(.cooksd), y = .cooksd)) +
  geom_point(alpha = 0.4) +
  geom_hline(yintercept = infl_cut, colour = "red", linetype = "dashed") +
  labs(title = "Cook's distance (influential points)",
       x = "Observation index", y = "Cook's distance")
# CLINICAL INTERPRETATION: don't just delete flagged points. Inspect them - are
# they data-entry errors or genuine extreme patients? Report a sensitivity
# analysis if results change when they are excluded.

# 6d. OVERALL MODEL FIT & DISCRIMINATION
# Hosmer-Lemeshow goodness-of-fit test (calibration). It has no base-R function;
# install ResourceSelection for it. A NON-significant p (> 0.05) means the model
# fits acceptably (we WANT a high p here - opposite of usual tests).
# if (requireNamespace("ResourceSelection", quietly = TRUE)) {
#   ResourceSelection::hoslem.test(model_final$y, fitted(model_final), g = 10)
# }

# Discrimination: AUC (area under the ROC curve). 0.5 = chance, 0.7-0.8 = acceptable,
# > 0.8 = good. response = observed outcome; predictor = model's predicted prob.
roc_obj <- pROC::roc(response  = model_final$y,                 # 0/1 outcome
                     predictor = fitted(model_final),
                     quiet     = TRUE)
auc_val <- as.numeric(pROC::auc(roc_obj))
cat("Model AUC:", round(auc_val, 3), "\n")

# -----------------------------------------------------------------------------
# 7. PRESENT THE FINAL MODEL AS ADJUSTED ORs WITH 95% CI
# -----------------------------------------------------------------------------
# TEACHING POINT: exponentiate = TRUE turns log-odds coefficients into ORs;
# conf.int = TRUE adds 95% confidence intervals. This is the table your reader needs.
or_table <- broom::tidy(model_final, exponentiate = TRUE, conf.int = TRUE)
print(or_table, n = Inf)

# CLINICAL INTERPRETATION of an OR:
#   OR > 1  -> higher odds of treatment uptake (e.g. diabetes increases uptake)
#   OR < 1  -> lower odds  (e.g. greater distance decreases uptake)
#   OR = 1  -> no association
# A 95% CI that EXCLUDES 1 indicates statistical significance at the 5% level.
# For continuous predictors the OR is "per 1-unit increase" (e.g. per extra km,
# per 1 point of knowledge_score, per 1 year of age).

# -----------------------------------------------------------------------------
# 8. PUBLICATION-READY REGRESSION TABLE (gtsummary)
# -----------------------------------------------------------------------------
# TEACHING POINT: tbl_regression() reads the model directly and formats ORs, CIs
# and p-values to journal style - no manual copying of numbers (which is error-prone).
tbl <- gtsummary::tbl_regression(model_final, exponentiate = TRUE) |>
  gtsummary::bold_p() |>
  gtsummary::modify_caption("**Adjusted odds ratios for hypertension treatment uptake**")
tbl

# Save the table. as_gt() -> gtsave() writes HTML (and PNG/Word if available).
gtsummary::as_gt(tbl) |>
  gt::gtsave(filename = "Resources/regression_table.html")

# FALLBACK (if gtsummary/gt are unavailable): just write the broom OR table to CSV.
# readr::write_csv(or_table, "Resources/regression_table.csv")

# -----------------------------------------------------------------------------
# 9. FOREST PLOT OF ADJUSTED ORs
# -----------------------------------------------------------------------------
# TEACHING POINT: a forest plot shows each OR (point) and its 95% CI (whiskers)
# on a LOG scale, with a reference line at OR = 1 (no effect). Points right of 1
# increase uptake; points left of 1 decrease it.
plot_df <- or_table |>
  filter(term != "(Intercept)")            # the intercept is not a clinical OR

forest <- ggplot(plot_df,
                 aes(x = estimate, y = reorder(term, estimate))) +
  geom_vline(xintercept = 1, linetype = "dashed", colour = "grey50") +   # null line
  geom_errorbarh(aes(xmin = conf.low, xmax = conf.high), height = 0.2,
                 colour = "#0D7377") +
  geom_point(size = 2.6, colour = "#0D7377") +
  scale_x_log10() +                        # log scale so CIs are symmetric
  labs(title = "Adjusted odds ratios for treatment uptake",
       subtitle = "Multivariable logistic regression (95% CI); reference line at OR = 1",
       x = "Adjusted odds ratio (log scale)", y = NULL) +
  theme_minimal(base_size = 12)

forest

ggsave("Resources/forest_plot_or.png", plot = forest,
       width = 8, height = 5, dpi = 300)

# -----------------------------------------------------------------------------
# 10. REPRODUCIBILITY - the capstone message
# -----------------------------------------------------------------------------
# TEACHING POINTS:
#  - set.seed() at the top makes any randomness repeatable.
#  - Use RELATIVE paths (or here::here("Data", "analysis_data.rds")) so the project
#    runs on any machine, not just yours. NEVER hard-code "C:/Users/yourname/...".
#  - Keep a clear folder structure: Data/, Scripts/, Solutions/, Resources/, References/.
#  - Save every output (tables, plots) to disk so the report can be rebuilt from code.
#  - Record your exact software environment so others can reproduce it:
sessionInfo()
# Optionally write it to a file for your appendix / supplementary material:
# writeLines(capture.output(sessionInfo()), "References/session_info.txt")

#  - ONE-CLICK REPORTS: move this analysis into an R Markdown (.Rmd) or Quarto
#    (.qmd) document. Knitting it re-runs the code and produces a Word/PDF/HTML
#    report with text, tables and figures together - the gold standard for
#    reproducible clinical reporting. #ClearDataClearImpact
# =============================================================================
