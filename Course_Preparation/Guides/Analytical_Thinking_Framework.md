# Start With the Question, Not the Code

*The analytical thinking framework, Clinical Data Analysis in R - Phase I (Neudata)*

Beginners often ask, *"What is the R command for this?"* Experienced analysts ask, *"What is my question, and what kind of data do I have?"* The command is the **last** step, not the first. If you understand **why** a method is used, the R code becomes a small, safe detail. If you only copy commands, you will eventually apply the right code to the wrong question, and get a confident, wrong answer.

This is the pipeline every good analysis follows, from question to published sentence.

---

## The framework (read top to bottom)

```
        Research question
               │
            Outcome
               │
      Exposure / predictors
               │
         Variable types
               │
          Study design
               │
       Descriptive analysis
               │
          Visualisation
               │
       Statistical method
               │
     Assumptions / diagnostics
               │
  Effect estimate + uncertainty
               │
         Interpretation
               │
      Scientific reporting
```

Each step below says **what to do** and gives a **clinical example** from `clinical_data`.

---

### 1. Research question
State a specific, answerable question before touching R. Vague questions ("look at the data") produce vague analyses.
- *Example:* "Is BMI associated with blood pressure?"

### 2. Outcome
Identify the single thing you are trying to explain or predict, the dependent variable.
- *Example:* `systolic_bp` (systolic blood pressure).

### 3. Exposure / predictors
Name the main exposure of interest and any other predictors you will consider.
- *Example:* main predictor `BMI`; you might later adjust for `age` and `sex`.

### 4. Variable types
Classify each variable: continuous, binary, categorical, or time-to-event. This single step usually decides the method.
- *Example:* `systolic_bp` continuous, `BMI` continuous → a relationship between two continuous variables.

### 5. Study design
Note how the data arose (cross-sectional, cohort, comparison of groups) and whether observations are independent. Design shapes what you can claim.
- *Example:* cross-sectional clinical dataset; patients are independent; we can describe **association**, not causation.

### 6. Descriptive analysis
Summarise before you model. Means, medians, ranges, counts and missingness tell you whether the data are plausible and whether assumptions are realistic.
- *Example:* `summary(clinical_data$systolic_bp)` and `summary(clinical_data$BMI)`; a `gtsummary` table of key variables.

### 7. Visualisation
Plot the relationship. A picture reveals shape, outliers and skew that numbers hide, and guides the choice between parametric and non-parametric methods.
- *Example:* a scatterplot of `BMI` (x) against `systolic_bp` (y) with a smooth line.

### 8. Statistical method
Choose the method that matches the variable types and design, not the one you happen to remember. (See the *Statistical Test Decision Guide*.)
- *Example:* continuous outcome with a continuous predictor → **linear regression**, `lm(systolic_bp ~ BMI, data = clinical_data)`.

### 9. Assumptions / diagnostics
Check that the method's assumptions hold, normality, linearity, constant variance, expected cell counts, proportional hazards, as relevant. Report honestly if they don't and adapt.
- *Example:* residual plots for the linear model (`plot(model)`); consider a transformation or a robust/non-parametric alternative if assumptions fail.

### 10. Effect estimate + uncertainty
Report the size of the effect **with a confidence interval**, not just a p-value. The estimate is the clinical message; the CI is your honesty about precision.
- *Example:* the slope from `lm()`, e.g. mmHg increase in systolic BP per unit of BMI, with its 95% CI (`confint(model)`).

### 11. Interpretation
Translate the estimate into clinical language, in context. What would this mean for a patient or a population?
- *Example:* "Each unit of BMI is associated with an X mmHg higher systolic pressure, consistent with adiposity contributing to raised blood pressure."

### 12. Scientific reporting
Write the Methods and Results sentences a reader can understand, estimate, CI, method, never raw console output.
- *Example:* "In linear regression, BMI was associated with systolic blood pressure (β = X mmHg per kg/m², 95% CI …)."

> **Throughout: understand WHY, don't just copy.** The same three lines of R mean different things for different questions. Knowing why the method fits is what turns output into evidence.

---

## Fully worked walk-through

**Question:** *What factors are associated with hypertension?*

1. **Research question**: Which patient factors are associated with having hypertension?
2. **Outcome**: `hypertension` (Yes/No).
3. **Predictors**: `age`, `sex`, `BMI` (candidates suggested by clinical knowledge).
4. **Variable types**: outcome **binary**; `age` and `BMI` continuous; `sex` categorical.
5. **Study design**: cross-sectional; independent patients; association only, not causation.
6. **Descriptive analysis**, proportion with hypertension (`table(clinical_data$hypertension)`); compare age and BMI in those with vs without, e.g. a `gtsummary` table.
7. **Visualisation**: boxplots of `age` and of `BMI` by `hypertension` status to see whether the groups separate.
8. **Statistical method**: binary outcome with several predictors → **logistic regression**:
   ```r
   # make the Yes/No outcome a factor first (No = reference)
   clinical_data$hypertension <- factor(clinical_data$hypertension, levels = c("No", "Yes"))
   model <- glm(hypertension ~ age + sex + BMI,
                data = clinical_data, family = binomial)
   ```
9. **Assumptions / diagnostics**, independent observations; enough events per predictor; roughly linear relationship on the log-odds scale; check influential points.
10. **Effect estimate + uncertainty**, odds ratios with 95% CIs:
    ```r
    library(broom)
    tidy(model, exponentiate = TRUE, conf.int = TRUE)
    ```
11. **Interpretation**: e.g. older age and higher BMI are associated with greater odds of hypertension; a predictor whose CI crosses 1 is not clearly associated.
12. **Scientific reporting**, "In multivariable logistic regression, age and BMI were independently associated with hypertension (odds ratios with 95% CIs reported), whereas sex was not."

---

Twelve steps, one habit: **decide what you are asking and what your data are, and the method, and then the R, follows.** That is what separates an analysis you can defend from a command you merely ran.
