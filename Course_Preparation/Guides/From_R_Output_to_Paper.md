# From R Output to a Scientific Paper

*A complete worked example — Clinical Data Analysis in R — Phase I (Neudata)*

R gives you numbers. A paper needs **clear sentences with estimates, confidence intervals and interpretation**. This guide walks the whole journey for one research question, using our dataset `clinical_data` (430 patients).

---

## 1. Research question

> **Is hypertension associated with age and BMI?**

Hypertension (`hypertension`, Yes/No) is a **binary** outcome, so the natural tool is **logistic regression**, which reports **odds ratios (OR)**. We adjust for `sex` so each effect is estimated holding the others constant.

---

## 2. Data

The outcome must be numeric 0/1 (or a factor) for `glm()`. `hypertension` is stored as "Yes"/"No"; the simplest fix is to create a 0/1 version, then model it. (If you leave it as a factor, R uses the first level as the reference — creating the 0/1 variable just makes the direction explicit.)

```r
# Make an explicit 0/1 outcome: 1 = hypertension present
clinical_data$htn <- as.integer(clinical_data$hypertension == "Yes")
```

---

## 3. Code — fit the model

```r
# Use the 0/1 outcome created in step 2 (1 = hypertension present)
model <- glm(htn ~ age + sex + BMI,
             data = clinical_data,
             family = binomial)
summary(model)
```

`summary(model)` prints coefficients on the **log-odds** scale — useful for the machinery, but not what we report. To get **odds ratios with confidence intervals**, exponentiate with **broom**:

```r
library(broom)
tidy(model, exponentiate = TRUE, conf.int = TRUE)
```

---

## 4. Output — the numbers to report

`tidy(..., exponentiate = TRUE, conf.int = TRUE)` gives a tidy table. The key results are:

| Predictor | Odds ratio | 95% CI | p-value |
|---|---|---|---|
| age (per year) | **1.09** | 1.07 – 1.12 | < 0.001 |
| sex (Male vs Female) | 1.20 | 0.76 – 1.90 | 0.43 |
| BMI (per kg/m²) | **1.16** | 1.10 – 1.22 | < 0.001 |

---

## 5. Interpretation — what the numbers mean clinically

- **Age, OR 1.09 per year:** each additional year of age is associated with about **9% higher odds** of hypertension, holding sex and BMI constant. Over a decade that compounds substantially (1.09 to the power 10 ≈ 2.4-fold higher odds). The confidence interval (1.07–1.12) lies entirely above 1, so the association is clear.
- **BMI, OR 1.16 per unit:** each extra unit of BMI (1 kg/m²) is associated with about **16% higher odds** of hypertension, again adjusting for the other variables. CI 1.10–1.22 is well above 1.
- **Sex, OR 1.20 (Male vs Female):** men appear to have somewhat higher odds, but the **95% CI (0.76–1.90) crosses 1** and p = 0.43. We therefore say there is **no statistically significant** difference by sex in this model — the data are compatible with anything from a modest protective effect to a near two-fold increase.

**"Per-unit odds ratio" vs "risk".** An OR of 1.09 does *not* mean 9% more patients get hypertension. It is a multiplier on the **odds** for each one-unit rise in the predictor. Odds ratios approximate relative risk only when the outcome is rare; when an outcome is common, an OR overstates the change in absolute risk. So describe an OR as a change in *odds per unit of the predictor*, not as an absolute number of extra cases.

---

## 6. Reporting — ready-to-use sentences

**Methods (one sentence):**
> We used multivariable logistic regression to assess the association of age, sex and body mass index with the presence of hypertension, reporting odds ratios with 95% confidence intervals.

**Results (one sentence):**
> In a multivariable logistic regression, older age (OR 1.09 per year, 95% CI 1.07–1.12) and higher BMI (OR 1.16 per kg/m², 95% CI 1.10–1.22) were independently associated with hypertension; sex was not (OR 1.20, 95% CI 0.76–1.90, p = 0.43).

Notice what these sentences contain: the **method**, the **estimate**, its **confidence interval**, and a plain statement of significance — and nothing copied from the console.

---

## 7. Results vs Interpretation vs Discussion

These three are different jobs, and mixing them is the most common beginner mistake.

- **Results — what you found.** The numbers only: estimates, confidence intervals, p-values, counts. Neutral and factual. *"BMI was associated with hypertension (OR 1.16 per kg/m², 95% CI 1.10–1.22)."* No speculation.
- **Interpretation — what the numbers mean.** Translate the statistics into clinical meaning, in context. *"A higher BMI corresponds to meaningfully greater odds of hypertension, consistent with BMI being a modifiable risk factor in this population."* Still tied to *your* data.
- **Discussion — how it fits the wider picture.** Compare with previous literature, acknowledge **limitations** (observational data cannot prove causation; residual confounding; single time-point BMI; five hospitals only), and state **implications** for practice or future research. *"These findings echo established cohort evidence linking adiposity to hypertension; as a cross-sectional analysis it cannot establish causality, and unmeasured confounders such as diet and physical activity may remain."*

---

> **Golden rule.** Never paste raw R console output into a manuscript. Report **estimates, confidence intervals and clear sentences** that a clinical reader can understand at a glance.
