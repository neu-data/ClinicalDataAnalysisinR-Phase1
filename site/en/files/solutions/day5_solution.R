# =============================================================================
# R Training Course | Day 5 - Regression Modelling & Reproducibility (CAPSTONE)
# Worked Solution to the Final In-Class Exercise
#
# EXERCISE: "Complete the analysis and produce a short Results section suitable
#            for publication."
#
# Study: "Determinants of Hypertension Treatment Uptake among Adults attending
#         Primary Healthcare Facilities" (multicentre cross-sectional, n = 1500)
# Primary outcome: treatment_uptake (Yes/No), reference = "No"
# Analytic population: htn_diagnosed == "Yes" (~1089)
#
# Author: Vương Mỹ Lượng & Bernard Isekah Osang'ir | Neudata | #ClearDataClearImpact
# =============================================================================

# -----------------------------------------------------------------------------
# 0. PACKAGES & REPRODUCIBILITY
# -----------------------------------------------------------------------------
library(dplyr)
library(readr)        # write_csv() fallback
library(ggplot2)
library(broom)
library(gtsummary)
library(pROC)

set.seed(2025)        # reproducibility: makes any randomness repeatable

# -----------------------------------------------------------------------------
# 1. LOAD DATA AND DEFINE THE ANALYTIC POPULATION
# -----------------------------------------------------------------------------
analysis_data <- readRDS("Data/analysis_data.rds")

# Only diagnosed hypertensives can take up treatment -> restrict to them.
dx <- filter(analysis_data, htn_diagnosed == "Yes")

n_analysed <- nrow(dx)               # number analysed - REPORT THIS in the paper
cat("N analysed (diagnosed hypertensives):", n_analysed, "\n")
cat("Outcome distribution:\n"); print(table(dx$treatment_uptake))

# -----------------------------------------------------------------------------
# 2. FIT THE FINAL MULTIVARIABLE LOGISTIC REGRESSION MODEL
# -----------------------------------------------------------------------------
# Pre-specified, clinically motivated predictors (NOT chosen by p-values).
model_final <- glm(
  treatment_uptake ~ age + sex + education + residence + diabetes +
    family_history_htn + health_insurance + knowledge_score +
    distance_to_facility_km,
  data   = dx,
  family = binomial(link = "logit")
)

summary(model_final)

# -----------------------------------------------------------------------------
# 3. ADJUSTED OR TABLE (broom) - the numbers to quote in the Results
# -----------------------------------------------------------------------------
or_table <- broom::tidy(model_final, exponentiate = TRUE, conf.int = TRUE)
print(or_table, n = Inf)
# INTERPRETATION: OR > 1 = higher odds of uptake; OR < 1 = lower odds;
# CI excluding 1 = statistically significant at 5%.

# -----------------------------------------------------------------------------
# 4. PUBLICATION-READY TABLE (gtsummary) WITH FALLBACK, SAVED TO Resources/
# -----------------------------------------------------------------------------
# We wrap saving in tryCatch so the script never crashes if an optional
# back-end (gt, webshot2) is not installed - it falls back to a CSV.
saved_table <- tryCatch({
  tbl <- gtsummary::tbl_regression(model_final, exponentiate = TRUE) |>
    gtsummary::bold_p() |>
    gtsummary::modify_caption(
      "**Adjusted odds ratios for hypertension treatment uptake**")

  gt_obj <- gtsummary::as_gt(tbl)
  gt::gtsave(gt_obj, filename = "Resources/regression_table.html")  # HTML
  try(gt::gtsave(gt_obj, filename = "Resources/regression_table.png"),
      silent = TRUE)                                                 # PNG (needs webshot2)
  "gtsummary table saved to Resources/regression_table.html (+ .png if available)"
}, error = function(e) {
  # FALLBACK: write the broom OR table to CSV - always works.
  readr::write_csv(or_table, "Resources/regression_table.csv")
  paste("gtsummary unavailable; wrote CSV fallback to",
        "Resources/regression_table.csv. Reason:", conditionMessage(e))
})
cat(saved_table, "\n")

# -----------------------------------------------------------------------------
# 5. FOREST PLOT OF ADJUSTED ORs, SAVED TO Resources/
# -----------------------------------------------------------------------------
plot_df <- filter(or_table, term != "(Intercept)")

forest <- ggplot(plot_df,
                 aes(x = estimate, y = reorder(term, estimate))) +
  geom_vline(xintercept = 1, linetype = "dashed", colour = "grey50") +
  geom_errorbarh(aes(xmin = conf.low, xmax = conf.high), height = 0.2,
                 colour = "#0D7377") +
  geom_point(size = 2.6, colour = "#0D7377") +
  scale_x_log10() +
  labs(title = "Adjusted odds ratios for treatment uptake",
       subtitle = "Multivariable logistic regression (95% CI); reference at OR = 1",
       x = "Adjusted odds ratio (log scale)", y = NULL) +
  theme_minimal(base_size = 12)

ggsave("Resources/forest_plot_or.png", plot = forest,
       width = 8, height = 5, dpi = 300)

# -----------------------------------------------------------------------------
# 6. MODEL DISCRIMINATION (AUC)
# -----------------------------------------------------------------------------
roc_obj <- pROC::roc(response  = model_final$y,
                     predictor = fitted(model_final),
                     quiet     = TRUE)
auc_val <- as.numeric(pROC::auc(roc_obj))
cat("Model AUC:", round(auc_val, 3), "  (0.7-0.8 acceptable; >0.8 good)\n")

# -----------------------------------------------------------------------------
# 7. WRITE THE PUBLICATION-STYLE RESULTS PARAGRAPH
# -----------------------------------------------------------------------------
# TEACHING POINT: a Results section reports (1) the n analysed, (2) the modelling
# approach, (3) the key adjusted ORs with 95% CIs and direction of effect, and
# (4) model performance (AUC). Below is a ~200-word template.
#
# >>> ACTION REQUIRED <<<: after running the model, read the printed `or_table`
# and the AUC, then REPLACE every placeholder X.XX with the computed values.
# The EXPECTED DIRECTIONS (from the study design) are stated so you can sanity-check.

results_paragraph <- paste0(
"RESULTS (DRAFT - replace X.XX placeholders with computed values)\n\n",
"Of the ", n_analysed, " adults with diagnosed hypertension, [N (XX.X%)] reported ",
"uptake of antihypertensive treatment. In the multivariable logistic regression ",
"model, several factors were independently associated with treatment uptake. ",
"Diabetes was associated with higher odds of uptake (aOR = X.XX, 95% CI X.XX-X.XX; ",
"expected direction: increased, ~2.x). A positive family history of hypertension ",
"(aOR = X.XX, 95% CI X.XX-X.XX) and having health insurance (aOR = X.XX, ",
"95% CI X.XX-X.XX) were likewise associated with greater odds of uptake. ",
"Urban (vs rural) residence was associated with higher odds (aOR = X.XX, ",
"95% CI X.XX-X.XX), as were higher educational attainment (aOR per level = X.XX, ",
"95% CI X.XX-X.XX), older age (aOR per year = X.XX, 95% CI X.XX-X.XX) and a higher ",
"knowledge score (aOR per point = X.XX, 95% CI X.XX-X.XX). Conversely, greater ",
"distance to the facility was associated with lower odds of uptake (aOR per km = ",
"X.XX, 95% CI X.XX-X.XX). Sex was not significantly associated with uptake ",
"(aOR = X.XX, 95% CI X.XX-X.XX). The model showed acceptable discrimination ",
"(area under the ROC curve = ", round(auc_val, 2), "). Associations with a 95% ",
"confidence interval excluding 1.00 were considered statistically significant.\n"
)

# Echo to the console as comments for the learner...
cat(results_paragraph)

# ...and write it to References/ for inclusion in the manuscript draft.
writeLines(results_paragraph, "References/results_section_draft.txt")
cat("\nResults draft written to References/results_section_draft.txt\n")

# CLINICAL INTERPRETATION SUMMARY (for the learner):
#  - Diabetes / family history / insurance / urban / education / age / knowledge
#    all PUSH UPTAKE UP (OR > 1) - more contact with care, awareness, and means.
#  - DISTANCE pushes uptake DOWN (OR < 1) - an access barrier; a target for policy.
#  - Report ADJUSTED ORs (they account for the other variables) and always pair
#    each OR with its 95% CI; never report a point estimate alone.

# -----------------------------------------------------------------------------
# 8. REPRODUCIBILITY APPENDIX
# -----------------------------------------------------------------------------
# Record the software environment so the analysis can be reproduced exactly.
writeLines(capture.output(sessionInfo()), "References/session_info.txt")
cat("Session info written to References/session_info.txt\n")
# TIP: convert this script into an R Markdown / Quarto report for a one-click,
# fully reproducible manuscript. #ClearDataClearImpact
# =============================================================================
