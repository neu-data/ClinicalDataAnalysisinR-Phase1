# ============================================================================
# Clinical Data Analysis in R - Phase I
# DAY 4 LIVE DEMONSTRATION:  Statistical Analysis
#                            (Hypothesis Tests + Intro to Logistic Regression)
#
# Goal: move from DESCRIBING the data (Day 3) to ASKING QUESTIONS of it.
#       - Are two groups different? (t-test / Wilcoxon)
#       - Are several groups different? (ANOVA)
#       - Are two categorical variables associated? (chi-square / Fisher)
#       - Do two numbers move together? (correlation)
#       - What are the ODDS of treatment uptake, and what drives them?
#         (logistic regression -> odds ratios)
#
# Study: Determinants of Hypertension Treatment Uptake among Adults attending
#        Primary Healthcare Facilities (multicentre cross-sectional, n = 1500).
#
# PRIMARY OUTCOME: treatment_uptake (Yes/No), reference level = "No".
# ANALYTIC POPULATION for uptake: patients already DIAGNOSED with hypertension
#        (htn_diagnosed == "Yes", about 1089 people). You cannot "take up"
#        treatment for a disease you have not been diagnosed with.
#
# This script READS the clean data produced on Day 2 (Data/analysis_data.rds).
#
# Author:  Bernard Isekah Osang'ir & My Luong Vuong | Neudata | #ClearDataClearImpact
# ============================================================================

# ----------------------------------------------------------------------------
# 0. PACKAGES & SETUP
# ----------------------------------------------------------------------------
library(tidyverse)     # dplyr for data wrangling, ggplot2 for plots
library(broom)         # turns ugly model output into a tidy data frame
# install.packages(c("tidyverse", "broom"))   # <- run once if not installed

# Course branding colour - the teal accent used across all our figures.
course_teal <- "#0D7377"

# ----------------------------------------------------------------------------
# 1. RELOAD THE ANALYSIS-READY DATA & BUILD THE ANALYTIC SUBSET
# ----------------------------------------------------------------------------
# We ALWAYS start from the saved clean file - never re-clean by hand.
analysis_data <- readRDS("Data/analysis_data.rds")

# KEY TEACHING POINT: define the analytic population EXPLICITLY and once.
# Our question is about treatment uptake, which only makes sense for people
# who have been diagnosed. So we filter to htn_diagnosed == "Yes".
dx <- filter(analysis_data, htn_diagnosed == "Yes")

nrow(dx)                          # how many patients are in the analysis?
table(dx$treatment_uptake)        # how many took up treatment vs not?

# COMMON MISTAKE: running the analysis on all 1500 patients. That mixes in
# undiagnosed people for whom the outcome is undefined, and biases every result.

# ----------------------------------------------------------------------------
# 2. CHECKING NORMALITY (does a continuous variable follow a bell curve?)
# ----------------------------------------------------------------------------
# WHY WE CARE: many classic ("parametric") tests - the t-test, ANOVA, Pearson
# correlation - assume the data are roughly normally distributed. If that
# assumption is badly violated we switch to "non-parametric" alternatives.

# --- Look first. Always plot before you test. ---
# A histogram shows the SHAPE of the distribution.
hist(dx$age,
     breaks = 30,
     col    = course_teal,
     border = "white",
     main   = "Distribution of Age",
     xlab   = "Age (years)")

# A Q-Q (quantile-quantile) plot compares our data to a perfect normal line.
# Points hugging the straight line  ->  approximately normal.
# Points curving away at the ends   ->  skew / heavy tails.
qqnorm(dx$age, main = "Q-Q Plot: Age")
qqline(dx$age, col = course_teal, lwd = 2)

qqnorm(dx$sbp_mmhg, main = "Q-Q Plot: Systolic BP")
qqline(dx$sbp_mmhg, col = course_teal, lwd = 2)

# --- Then test formally with the Shapiro-Wilk test. ---
# H0 (null hypothesis): the data ARE normally distributed.
# A SMALL p-value (< 0.05) means we REJECT normality.
shapiro.test(dx$age)
shapiro.test(dx$sbp_mmhg)

# COMMON MISTAKE: trusting Shapiro-Wilk alone in LARGE samples. With ~1089
# rows the test is so powerful it flags trivial, clinically meaningless
# departures from normality as "significant". A near-straight Q-Q plot and a
# symmetric histogram matter MORE than the Shapiro p-value here.
#
# RULE OF THUMB for this course:
#   - Symmetric, bell-shaped, big sample  -> parametric test is fine.
#   - Clearly skewed or small sample      -> use the non-parametric test.

# ----------------------------------------------------------------------------
# 3. COMPARING A CONTINUOUS VARIABLE BETWEEN TWO GROUPS
# ----------------------------------------------------------------------------
# QUESTION: Is age different between those who took up treatment and those who
#           did not? (We expect older patients to be MORE likely to take up.)

# --- Parametric: Welch two-sample t-test ---
# The formula reads "age explained BY treatment_uptake".
# t.test() defaults to the Welch version, which does NOT assume equal variances
# in the two groups - a safer default than the classic Student t-test.
t.test(age ~ treatment_uptake, data = dx)

# INTERPRETATION: read three things from the output -
#   1. the two group means (e.g. mean age in No vs Yes),
#   2. the 95% confidence interval for their DIFFERENCE,
#   3. the p-value (p < 0.05  ->  the difference is statistically significant).

# --- Non-parametric equivalent: Wilcoxon rank-sum (Mann-Whitney U) ---
# Use this if age were skewed. It compares ranks, not means, so it is not
# thrown off by outliers or non-normal shapes.
wilcox.test(age ~ treatment_uptake, data = dx)

# CLINICAL INTERPRETATION: if both tests agree (and they usually do for large,
# roughly symmetric data), report the t-test with means; if they disagree,
# trust the non-parametric one and report medians instead.

# ----------------------------------------------------------------------------
# 4. COMPARING A CONTINUOUS VARIABLE ACROSS MORE THAN TWO GROUPS (ANOVA)
# ----------------------------------------------------------------------------
# QUESTION: Does systolic BP differ across blood-pressure categories?
#           (We'd expect it to, by definition - a nice sanity check.)
# COMMON MISTAKE: running many t-tests for many group pairs. Each test has its
# own 5% false-positive risk, so doing several inflates the overall error.
# ANOVA tests ALL groups at once with a single, honest p-value.

aov_sbp <- aov(sbp_mmhg ~ bp_category, data = dx)
summary(aov_sbp)        # the F-statistic and its p-value

# A second, more interesting example: does AGE differ across EDUCATION levels?
aov_age <- aov(age ~ education, data = dx)
summary(aov_age)

# INTERPRETATION: a small ANOVA p-value tells you SOME groups differ, but NOT
# which ones. To find out which specific pairs differ, run a post-hoc test that
# corrects for multiple comparisons - Tukey's Honest Significant Differences:
TukeyHSD(aov_age)

# ASSUMPTIONS (same family as the t-test): roughly normal residuals and similar
# spread across groups. If badly violated, the non-parametric analogue is
# kruskal.test(sbp_mmhg ~ bp_category, data = dx).

# ----------------------------------------------------------------------------
# 5. ASSOCIATION BETWEEN TWO CATEGORICAL VARIABLES (CHI-SQUARE / FISHER)
# ----------------------------------------------------------------------------
# QUESTION: Is treatment uptake associated with having diabetes?

# Step 1 - build the contingency table (cross-tabulation) of counts.
uptake_diabetes <- table(dx$treatment_uptake, dx$diabetes)
uptake_diabetes
addmargins(uptake_diabetes)     # the same table with row/column totals

# Step 2 - the chi-square test of independence.
# H0: the two variables are INDEPENDENT (no association).
chisq.test(uptake_diabetes)

# KEY TEACHING POINT: the chi-square test is only valid when EXPECTED counts
# are large enough (a common rule: all expected cells >= 5). Check them:
chisq.test(uptake_diabetes)$expected

# WHEN EXPECTED COUNTS ARE SMALL (e.g. a rare category): use Fisher's exact
# test instead, which is valid for any cell size.
fisher.test(uptake_diabetes)

# INTERPRETATION: a small p-value means uptake and diabetes are associated.
# The TABLE tells you the DIRECTION (e.g. a higher proportion of diabetics
# took up treatment). The test alone does not give effect size - the odds
# ratio from logistic regression (below) does.

# ----------------------------------------------------------------------------
# 6. CORRELATION BETWEEN TWO CONTINUOUS VARIABLES
# ----------------------------------------------------------------------------
# QUESTION: Do systolic BP and BMI move together?

# --- Pearson correlation: measures LINEAR association; assumes normality. ---
cor.test(dx$sbp_mmhg, dx$bmi, method = "pearson")

# --- Spearman correlation: based on RANKS; robust to outliers & non-linearity.
cor.test(dx$sbp_mmhg, dx$bmi, method = "spearman")

# INTERPRETATION of the correlation coefficient r (ranges -1 to +1):
#   ~ 0.0-0.3  weak      ~ 0.3-0.7  moderate      ~ 0.7-1.0  strong
#   the SIGN gives direction (+ together, - opposite).
# COMMON MISTAKE: confusing a significant p-value with a strong relationship.
# In big samples even a tiny r (say 0.08) is "significant" yet clinically
# trivial. ALWAYS report and judge r, not just the p-value.
# Reminder: correlation is NOT causation.

# ----------------------------------------------------------------------------
# 7. SIMPLE (UNIVARIABLE) LOGISTIC REGRESSION
# ----------------------------------------------------------------------------
# Now the centrepiece of Day 4. Our outcome (treatment uptake) is BINARY
# (Yes/No), so we use LOGISTIC regression, not ordinary linear regression.
#
# family = binomial tells glm() the outcome is 0/1.
# Because treatment_uptake is a factor with reference "No", R models the
# probability (odds) of the OTHER level, "Yes" - exactly what we want.

# --- Model 7a: a single categorical predictor (diabetes) ---
m_diab <- glm(treatment_uptake ~ diabetes, data = dx, family = binomial)
summary(m_diab)

# The raw coefficients are on the LOG-ODDS scale - hard to interpret directly.
# We exponentiate to get ODDS RATIOS (OR), which clinicians understand.
exp(coef(m_diab))                 # odds ratios
exp(confint(m_diab))              # their 95% confidence intervals

# INTERPRETATION of the OR for diabetes (Yes vs No, the reference):
#   OR = 1   ->  no effect on the odds of uptake.
#   OR > 1   ->  diabetics have HIGHER odds of taking up treatment.
#   OR < 1   ->  diabetics have LOWER odds.
# We expect OR > 1 here. A 95% CI that EXCLUDES 1 means statistically
# significant. Example phrasing: "Patients with diabetes had about X times the
# odds of treatment uptake compared with those without (OR X.X, 95% CI a-b)."

# --- Model 7b: a single CONTINUOUS predictor (age) ---
m_age <- glm(treatment_uptake ~ age, data = dx, family = binomial)
summary(m_age)
exp(coef(m_age))
exp(confint(m_age))

# INTERPRETATION for a continuous predictor: the OR is the change in odds for
# EACH ONE-UNIT increase - here, per ONE extra YEAR of age. That number is
# close to 1 because one year is a small step.
# CLINICAL TIP: rescale to a meaningful unit. The OR per 10 YEARS is the
# 1-year OR raised to the power 10:
exp(coef(m_age)["age"] * 10)      # odds ratio per 10-year increase in age
# This is far easier to communicate: "each decade of age multiplied the odds
# of uptake by about this much."

# ----------------------------------------------------------------------------
# 8. BRIEF INTRO TO MULTIPLE (MULTIVARIABLE) LOGISTIC REGRESSION
# ----------------------------------------------------------------------------
# Real patients differ in many ways at once. A multivariable model estimates
# the effect of EACH predictor while holding the others constant ("adjusting"
# for them). This separates, e.g., the effect of diabetes from the fact that
# diabetics also tend to be older.

m_multi <- glm(treatment_uptake ~ age + sex + diabetes + residence,
               data = dx, family = binomial)
summary(m_multi)

# ADJUSTED odds ratios with confidence intervals:
exp(cbind(OR = coef(m_multi), confint(m_multi)))

# KEY TEACHING POINT: these are ADJUSTED ORs. "Adjusted for age, sex and
# residence" means we are comparing patients who are otherwise similar on
# those variables. An OR can shrink, grow, or even flip direction after
# adjustment - that change is itself informative (confounding).
#
# IMPORTANT: glm() uses COMPLETE CASES by default - any row with a missing
# value in ANY model variable is silently dropped. Check how many remain:
nobs(m_multi)                     # rows actually used in the model

# ----------------------------------------------------------------------------
# 9. TIDY, REPORT-READY OUTPUT WITH broom
# ----------------------------------------------------------------------------
# Typing exp(coef(...)) and exp(confint(...)) separately is tedious and
# error-prone. broom::tidy() does it all in one tidy data frame:
#   exponentiate = TRUE  -> report odds ratios instead of log-odds
#   conf.int = TRUE      -> add the 95% confidence interval columns
tidy(m_multi, exponentiate = TRUE, conf.int = TRUE)

# This tidy table (estimate = OR, conf.low/conf.high = 95% CI, p.value) is
# exactly the format we use on Day 4's EXERCISE and on Day 5 to build the
# final results table and forest plot.

# ============================================================================
# RECAP - matching the QUESTION to the RIGHT TEST
#   two groups, continuous    -> t.test()  (or wilcox.test() if skewed)
#   >2 groups, continuous     -> aov()     (or kruskal.test() if skewed)
#   two categorical variables -> chisq.test() (or fisher.test() if sparse)
#   two continuous variables  -> cor.test() (Pearson or Spearman)
#   binary outcome + drivers  -> glm(..., family = binomial) -> odds ratios
# Day 5 goes deeper into model building, diagnostics and reporting.
# ============================================================================
