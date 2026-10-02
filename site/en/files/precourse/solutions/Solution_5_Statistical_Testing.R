# =====================================================================
#  SOLUTION 5 — Statistical Testing
# =====================================================================
library(tidyverse)
clinical_data <- read_csv("Data/clinical_data_clean.csv")

# QUESTION A: glucose by diabetes
t.test(glucose ~ diabetes, data = clinical_data)
#   Outcome:          glucose (continuous)
#   Exposure/groups:  diabetes (Yes / No), 2 groups
#   Variable types:   continuous outcome, binary group
#   Test:             two-sample t-test (Wilcoxon if skewed)
#   H0:               mean glucose is the SAME in both groups
#   Interpretation:   glucose is much higher with diabetes; p < 0.001, so we
#                     reject H0. Diabetic patients have higher fasting glucose.

# QUESTION B: hypertension vs diabetes
chisq.test(table(clinical_data$hypertension, clinical_data$diabetes))
#   Outcome/vars:     hypertension and diabetes (both categorical)
#   Test:             chi-square test of association (Fisher if counts small)
#   H0:               the two conditions are INDEPENDENT (not associated)
#   Interpretation:   chi-square = 26.0, p < 0.001 -> reject H0. Hypertension and
#                     diabetes are associated (they co-occur more than by chance).

# QUESTION C: age vs systolic BP
cor.test(clinical_data$age, clinical_data$systolic_bp)
#   Outcome:          systolic_bp (continuous)
#   Exposure:         age (continuous)
#   Test:             Pearson correlation (Spearman if non-linear/skewed)
#   H0:               there is NO correlation (r = 0)
#   Interpretation:   r ~ 0.55, p < 0.001 -> positive, moderate correlation.
#                     Older patients tend to have higher systolic BP.

# QUESTION D: systolic BP by sex  (you choose the test)
t.test(systolic_bp ~ sex, data = clinical_data)
#   Test:             two-sample t-test (continuous outcome, two groups)
#   H0:               mean systolic BP is the same in men and women
#   Interpretation:   means ~124 in both; p ~ 0.85 -> do NOT reject H0. There is
#                     no evidence of a sex difference in systolic BP.
