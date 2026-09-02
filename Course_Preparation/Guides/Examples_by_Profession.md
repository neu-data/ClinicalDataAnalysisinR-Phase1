# The Same Skills, Your Own Questions

*Clinical Data Analysis in R — Phase I (Neudata)*

This course brings together many backgrounds — doctors, nurses, pharmacists, public-health researchers, and Master's and PhD students. That is a strength, not a problem. The **skills are the same for everyone**: ask a clear question, know your variable types, choose a matching method, and report an estimate with its uncertainty. What differs is the *question you care about*.

The course is built so that **beginners can follow the main thread** — one clear analysis, explained step by step — while **more advanced participants go deeper** using the same dataset. Everyone works from the same `clinical_data` (430 patients), so you can always try a neighbour's question with skills you already have.

Below is a starting question for each background. Every one is answerable with our variables.

---

### Doctors — does treatment change outcomes?
> **Does treatment reduce mortality / cardiovascular events?**
- **Outcome:** `outcome` (0/1 event) together with `time_to_event` (months) — a time-to-event outcome.
- **Predictor:** `treatment` (Treated / Untreated).
- **Method:** Kaplan–Meier curves to describe survival, Cox regression for an adjusted hazard ratio.
```r
library(survival); library(survminer)
survfit(Surv(time_to_event, outcome) ~ treatment, data = clinical_data)   # KM
coxph(Surv(time_to_event, outcome) ~ treatment, data = clinical_data)      # Cox HR
```

### Nurses — do two patient groups differ on a continuous measure?
> **Is follow-up time (or blood pressure) different between two patient groups?**
- **Outcome:** `time_to_event` (or `systolic_bp`) — continuous.
- **Predictor:** a two-level group, e.g. `sex` or `treatment`.
- **Method:** t-test if roughly normal, Wilcoxon rank-sum if skewed.
```r
t.test(systolic_bp ~ sex, data = clinical_data)
wilcox.test(time_to_event ~ treatment, data = clinical_data)   # non-parametric
```

### Public-health researchers — what drives a condition in the population?
> **What factors are associated with hypertension?**
- **Outcome:** `hypertension` (Yes/No) — binary.
- **Predictors:** `age`, `sex`, `BMI`, `smoking`, `diabetes`, …
- **Method:** logistic regression, reporting odds ratios with 95% CIs.
```r
# Make the Yes/No outcome a factor first (No = reference)
clinical_data$hypertension <- factor(clinical_data$hypertension, levels = c("No", "Yes"))
glm(hypertension ~ age + sex + BMI + smoking, data = clinical_data, family = binomial)
```

### Master's students — an adjusted association
> **Is BMI associated with systolic blood pressure after adjustment for age and sex?**
- **Outcome:** `systolic_bp` — continuous.
- **Predictors:** `BMI` (main), plus `age` and `sex` (adjustment).
- **Method:** multivariable linear regression; interpret the BMI coefficient holding age and sex constant.
```r
lm(systolic_bp ~ BMI + age + sex, data = clinical_data)
```

### PhD students — building and interpreting a multivariable model
> **Which covariates should enter a multivariable model, and how are adjusted estimates interpreted?**
- **Focus:** not one command but the reasoning — **confounding**, variable selection driven by clinical knowledge (not just p-values), and the meaning of **adjusted vs crude** estimates.
- **Method:** compare a crude model with an adjusted one and discuss why the estimate changes.
```r
clinical_data$hypertension <- factor(clinical_data$hypertension, levels = c("No", "Yes"))
crude    <- glm(hypertension ~ BMI, data = clinical_data, family = binomial)
adjusted <- glm(hypertension ~ BMI + age + sex, data = clinical_data, family = binomial)
# Compare the BMI odds ratio before and after adjustment — how much does it shift, and why?
```
An adjusted estimate answers "the effect of BMI *for patients of the same age and sex*", which is usually the clinically meaningful question. A large gap between crude and adjusted estimates points to **confounding**.

---

## Going further

Throughout the lessons you'll see optional **"Going further"** boxes. Beginners can safely skip them and still complete every analysis end to end — the main thread is self-contained. Advanced participants can use them to push each example further: adding covariates, checking assumptions more formally, trying a non-parametric alternative, or producing a publication-ready `gtsummary` table. Same dataset, same core skills — just as far as you want to take them.
