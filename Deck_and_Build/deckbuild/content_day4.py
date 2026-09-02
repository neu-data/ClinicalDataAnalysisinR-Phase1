# -*- coding: utf-8 -*-
"""Day 4 slides - Common Medical Statistical Tests: choosing and running the right test."""

SLIDES_DAY4 = [

    {"type": "divider", "title": "Day 4: Common Medical Statistical Tests",
     "agenda": ["Hypothesis testing basics",
                "Comparing two groups: t-test and Wilcoxon",
                "More than two groups: ANOVA",
                "Categorical association: chi-square and Fisher",
                "Correlation and choosing the right test"],
     "notes": "Welcome to Day 4. Yesterday we DESCRIBED the data; today we ASK QUESTIONS of it with statistical tests.\nKey framing: every test answers a question - are two groups different? are two variables associated?\nReassure clinicians: the maths is automatic in R; your job is to choose the right test and interpret it.\nBridge: today is tests; next week (Day 5) we introduce regression to model several predictors at once.\nDemo tip: keep the day4_demo.R script open and run blocks live as you reach each slide."},

    {"type": "bullets", "title": "What We Will Cover Today",
     "intro": "Choosing and running the common tests used in clinical research.",
     "items": ["Hypothesis testing: null, alternative, p-values and significance",
               "Checking normality before choosing a test",
               "Comparing two groups: t-test and Wilcoxon",
               "Comparing more than two groups: ANOVA and Tukey",
               "Categorical association: chi-square and Fisher's exact",
               "Correlation: Pearson and Spearman",
               "A decision framework: matching the question to the test"],
     "notes": "Roadmap for the day: the common medical statistical tests, and how to choose between them.\nEmphasise the logical thread: outcome type + number of groups + paired vs independent -> the right test.\nBridge: these tests compare groups two at a time; Day 5 introduces regression to study several predictors together.\nAudience question: what decides which test we use? Answer: the type of the outcome and how many groups we compare."},

    {"type": "content", "title": "The Analytic Question",
     "blocks": [
        {"header": "Our research question", "lines": [
            "Do patients on treatment differ from those not on treatment?",
            "Which characteristics (age, sex, comorbidity) differ between the two groups?"]},
        {"header": "Define the analytic population FIRST", "lines": [
            "Uptake only makes sense for those already diagnosed.",
            "We restrict to htn_diagnosed == \"Yes\" (about 1,089 patients).",
            "Roughly 47% of diagnosed patients had taken up treatment."]},
        {"callout": "mistake", "header": "Do not analyse all 1,500",
         "lines": ["Including undiagnosed people, whose outcome is undefined, biases every result."]},
     ],
     "notes": "Key teaching point: define the analytic population explicitly and once, before any test.\nClinical logic: you cannot take up treatment for a disease you have not been diagnosed with.\nCommon mistake: running the analysis on the full 1,500 - it mixes in undefined outcomes and biases estimates.\nDemo tip: show dx <- filter(analysis_data, htn_diagnosed == \"Yes\") then nrow(dx) and table(dx$treatment_uptake)."},

    {"type": "content", "title": "Hypothesis Testing in Plain Language",
     "blocks": [
        {"header": "The two hypotheses", "lines": [
            "Null (H0): there is NO difference / NO association.",
            "Alternative (H1): there IS a difference / association."]},
        {"header": "What a p-value actually is", "lines": [
            "The probability of data this extreme IF the null were true.",
            "Small p (< 0.05) is evidence AGAINST the null.",
            "It is NOT the probability that the null is true."]},
        {"callout": "interpretation", "header": "Significance level",
         "lines": ["We pre-set alpha = 0.05 as the threshold for calling a result significant."]},
     ],
     "notes": "Key teaching point: a p-value answers 'how surprising is my data if nothing is going on?'\nCommon misinterpretation: p is NOT the chance the null is true, and (1 - p) is NOT the chance H1 is true.\nClinical interpretation: significance is about evidence against H0, not about importance or effect size.\nAudience question: does p = 0.04 prove the effect is real? Answer: no - it is one piece of evidence, judged with the effect size and context."},

    {"type": "content", "title": "p < 0.05 Is Not the Whole Story",
     "blocks": [
        {"header": "Statistical vs clinical significance", "lines": [
            "A tiny, meaningless difference can be 'significant' in a large sample.",
            "A large, important difference can be 'non-significant' if the sample is small.",
            "Always report the effect size and its confidence interval, not just p."]},
        {"callout": "warning", "header": "Beware p-value worship",
         "lines": ["Do not chase p < 0.05 or treat 0.049 and 0.051 as opposites.",
                   "A confidence interval tells you the size AND the uncertainty."]},
     ],
     "notes": "Key teaching point: the p-value is necessary but not sufficient - it ignores effect size.\nCommon mistake: dichotomising at 0.05 as if 0.049 and 0.051 are fundamentally different.\nClinical interpretation: a CI shows both the magnitude and the precision; prefer it to a bare p-value.\nAudience question: which is more useful, 'p = 0.03' or 'OR 3.6 (95% CI 1.5 to 9.6)'? Answer: the second - it shows direction, size and uncertainty."},

    {"type": "two_column", "title": "Is the Variable Normal? Look, Then Test",
     "left": {"header": "Look first (always)", "lines": [
        "Histogram shows the shape of the distribution.",
        "Q-Q plot: points on the line means roughly normal.",
        "Points curving away at the ends mean skew or heavy tails."], "bullets": True},
     "right": {"header": "Then test", "lines": [
        "Shapiro-Wilk test: H0 is that data ARE normal.",
        "Small p (< 0.05) means we reject normality.",
        "Symmetric and bell-shaped means a parametric test is fine.",
        "Clearly skewed means use the non-parametric test."], "bullets": True},
     "notes": "Key teaching point: plot before you test - the eye catches what a single p-value hides.\nCommon mistake: trusting Shapiro-Wilk alone in large samples; with ~1,089 rows it flags trivial departures as significant.\nClinical interpretation: a near-straight Q-Q plot and a symmetric histogram matter more than the Shapiro p here.\nDemo tip: run hist(dx$age), qqnorm/qqline, then shapiro.test(dx$age) and contrast the verdicts."},

    {"type": "content", "title": "Shapiro-Wilk: Use With Care in Big Samples",
     "blocks": [
        {"header": "Why the test misleads here", "lines": [
            "Shapiro-Wilk gets more powerful as the sample grows.",
            "In ~1,089 rows it detects tiny, clinically irrelevant departures.",
            "It will almost always return p < 0.05 - even for usable data."]},
        {"callout": "tip", "header": "Rule of thumb for this course",
         "lines": ["Big sample + symmetric histogram + straight Q-Q means parametric is fine.",
                   "Let the plots, not the Shapiro p-value, drive the decision."]},
     ],
     "notes": "Key teaching point: statistical power is a double-edged sword - in large n the normality test over-flags.\nCommon mistake: switching to non-parametric tests purely because Shapiro returned p < 0.05.\nClinical interpretation: judge normality by shape and Q-Q linearity; reserve non-parametric tests for clear skew or small n.\nAudience question: Shapiro says p < 0.001 but the Q-Q is straight - what do you do? Answer: trust the plot and use the parametric test."},

    {"type": "two_column", "title": "Comparing Two Groups: a Continuous Outcome",
     "left": {"header": "t-test (parametric)", "lines": [
        "Compares MEANS of two groups.",
        "Welch t-test is the safe default (unequal variances).",
        "Use when data are roughly symmetric.",
        "Formula: age ~ treatment_uptake."], "bullets": True},
     "right": {"header": "Wilcoxon (non-parametric)", "lines": [
        "Compares RANKS, not means.",
        "Robust to outliers and skew.",
        "Use when data are clearly non-normal.",
        "Report medians instead of means."], "bullets": True},
     "notes": "Key teaching point: the question is the same (do two groups differ?); the test depends on the data shape.\nClinical interpretation example: mean age is higher among those on treatment, consistent with older patients taking up more.\nCommon mistake: defaulting to the classic Student t-test - Welch is safer because it does not assume equal variances.\nDemo tip: run both t.test and wilcox.test on age ~ treatment_uptake; note they usually agree for large, symmetric data."},

    {"type": "code", "title": "Demo: t-test of Age by Treatment Uptake",
     "intro": "Is mean age different between those who took up treatment and those who did not?",
     "code": "t.test(age ~ treatment_uptake, data = dx)",
     "output": "Welch Two Sample t-test\nt = -8.9, df = 1011, p-value < 2.2e-16\n95 percent CI: -6.4 to -4.1\nmean in No  mean in Yes\n   50.1        55.3",
     "note": "Patients on treatment are about 5 years older on average; the CI excludes 0, so p < 0.05.",
     "notes": "Key teaching point: read three things - the two group means, the 95% CI for their difference, and the p-value.\nClinical interpretation: a ~5-year mean age gap, with a CI that excludes zero, supports older patients taking up more.\nCommon mistake: reporting only the p-value and omitting the means and the CI for the difference.\nDemo tip: run wilcox.test(age ~ treatment_uptake, data = dx) alongside and show they agree."},

    {"type": "content", "title": "When Data Are Not Normal: Non-parametric Tests",
     "blocks": [
        {"header": "The rank-based alternatives", "lines": [
            "Wilcoxon rank-sum (Mann-Whitney): compares two groups without assuming normality.",
            "Fisher's exact test: for a 2x2 table when expected counts are small (< 5).",
            "They use ranks and exact counts instead of means and the normal curve."]},
        {"header": "How to run them", "lines": [
            "wilcox.test(sbp_mmhg ~ treatment_uptake, data = dx)",
            "fisher.test(table(dx$treatment_uptake, dx$diabetes))"]},
        {"callout": "tip", "header": "Rule of thumb",
         "lines": ["Skewed or small data -> use the non-parametric test; it is the safe choice when in doubt."]}],
     "notes": ("Key teaching point: when the normality or sample-size assumptions of the t-test or "
               "chi-square fail, the rank-based Wilcoxon test and Fisher's exact test give valid answers.\n"
               "Clinical interpretation: lab values and costs are often skewed - the Wilcoxon test on "
               "medians is frequently the honest choice.\n"
               "Common mistake: forcing a t-test on clearly skewed data, or using chi-square when a cell "
               "has an expected count below 5.\n"
               "Audience question: when would you prefer Fisher's exact over chi-square? Expected answer: "
               "small samples or sparse tables with low expected counts.\n"
               "Demo tip: show that Wilcoxon and the t-test agree here (large, roughly symmetric sample), "
               "then contrive a small table to motivate Fisher's exact.")},

    {"type": "content", "title": "Comparing More Than Two Groups: ANOVA",
     "blocks": [
        {"header": "Why not many t-tests?", "lines": [
            "Each pairwise t-test carries its own 5% false-positive risk.",
            "Doing several inflates the overall error rate.",
            "ANOVA tests all groups at once with one honest p-value."]},
        {"header": "After a significant ANOVA", "lines": [
            "A small p tells you SOME groups differ, not which ones.",
            "TukeyHSD compares every pair and corrects for multiplicity.",
            "Example: does age differ across education levels?"]},
        {"callout": "note", "header": "If assumptions fail",
         "lines": ["Use the non-parametric kruskal.test() instead of aov()."]},
     ],
     "notes": "Key teaching point: ANOVA is the multi-group t-test; it controls the family-wide error a stack of t-tests would not.\nCommon mistake: running every pairwise t-test - inflates false positives. Run ANOVA, then a post-hoc only if it is significant.\nClinical interpretation: a Tukey table shows which specific education pairs differ in mean age.\nAudience question: ANOVA p is significant - are all groups different? Answer: no, at least one pair is; Tukey says which."},

    {"type": "content", "title": "Association Between Two Categories",
     "blocks": [
        {"header": "Chi-square test of independence", "lines": [
            "Question: is treatment uptake associated with diabetes?",
            "Build a contingency table, then test it.",
            "H0: the two variables are independent (no association)."]},
        {"header": "When expected counts are small", "lines": [
            "Chi-square needs all expected cell counts >= 5.",
            "Check with chisq.test(tab)$expected.",
            "If any are too small, use Fisher's exact test instead."]},
        {"callout": "interpretation", "header": "The table gives direction",
         "lines": ["The test gives a p-value; the table shows WHO had higher uptake."]},
     ],
     "notes": "Key teaching point: chi-square asks whether two categorical variables move together; the table shows the direction.\nCommon mistake: applying chi-square when expected counts are below 5 - switch to Fisher's exact in that case.\nClinical interpretation: a higher proportion of diabetics on treatment suggests a positive association, quantified later by the OR.\nDemo tip: show table(dx$treatment_uptake, dx$diabetes), then chisq.test, its $expected, and fisher.test."},

    {"type": "two_column", "title": "Correlation: Do Two Numbers Move Together?",
     "left": {"header": "Pearson", "lines": [
        "Measures LINEAR association.",
        "Assumes roughly normal data.",
        "Sensitive to outliers.",
        "Example: sbp_mmhg vs bmi."], "bullets": True},
     "right": {"header": "Spearman", "lines": [
        "Based on RANKS.",
        "Robust to outliers and non-linearity.",
        "Use when data are skewed.",
        "Reports a rank correlation."], "bullets": True},
     "notes": "Key teaching point: r ranges from -1 to +1; ~0-0.3 weak, 0.3-0.7 moderate, 0.7-1.0 strong; the sign gives direction.\nCommon mistake: confusing a significant p with a strong relationship - in big samples a tiny r (0.08) is significant yet trivial.\nClinical interpretation: always report and judge r, not just the p-value; remember correlation is not causation.\nAudience question: r = 0.1, p < 0.001 - strong link? Answer: no, statistically detectable but clinically negligible."},

    {"type": "code", "title": "Demo: Correlation of SBP and BMI",
     "intro": "Do systolic blood pressure and BMI move together?",
     "code": "cor.test(dx$sbp_mmhg, dx$bmi, method = \"pearson\")",
     "output": "Pearson's product-moment correlation\nt = 6.1, df = 1087, p-value = 1.4e-09\n95 percent CI: 0.12 to 0.24\ncor = 0.18",
     "note": "r = 0.18 is a weak positive link: highly significant, but clinically modest.",
     "notes": "Key teaching point: the p-value confirms the link is real; r tells you it is weak.\nClinical interpretation: SBP and BMI rise together a little, but BMI explains very little of SBP variation.\nCommon mistake: headlining 'significant correlation' while hiding that r is only 0.18.\nDemo tip: rerun with method = \"spearman\" and note the rank correlation is similar, confirming robustness."},

    {"type": "table", "title": "Choosing the Right Test",
     "headers": ["Outcome", "Predictor / 2nd variable", "Test"],
     "rows": [["Continuous", "Two groups", "t-test (Wilcoxon if skewed)"],
              ["Continuous", "More than two groups", "ANOVA (Kruskal-Wallis if skewed)"],
              ["Categorical", "Categorical", "Chi-square (Fisher if sparse)"],
              ["Continuous", "Continuous", "Correlation (Pearson / Spearman)"],
              ["Binary", "One or more predictors", "Logistic regression - Day 5"]],
     "caption": "Match the QUESTION and the data types to the test; a binary outcome with predictors leads to regression (Day 5).",
     "notes": "Key teaching point: the test is determined by the outcome type and the predictor type - not by habit.\nDemo tip: keep this table on screen as a decision aid for the exercise.\nClinical interpretation: when the outcome is binary and we want several predictors at once, we move to logistic regression - that is Day 5.\nAudience question: outcome is Yes/No and we want to adjust for several factors - which method? Answer: logistic regression, next session."},

    {"type": "content", "title": "Day 4 Exercise: Choose and Run the Right Test",
     "blocks": [
        {"header": "Your tasks", "lines": [
            "Compare age between treatment-uptake groups with a t-test.",
            "Test the association between sex and treatment uptake (chi-square).",
            "Test the correlation between SBP and BMI (Pearson or Spearman).",
            "For each, state the question, the test, and a plain-language result."]},
        {"header": "Expected output", "lines": [
            "One test result per question, each with a p-value.",
            "For the t-test and correlation, the estimate and its 95% CI.",
            "One sentence interpreting each result clinically."]},
        {"callout": "tip", "header": "Let the data type choose the test",
         "lines": ["Check the outcome type and the number of groups before you pick a test."]},
     ],
     "notes": "Key teaching point: the deliverable is the reasoning - question -> variable types -> test -> interpretation.\nCommon mistake: reaching for a t-test out of habit without checking the outcome type or distribution.\nClinical interpretation: expect the SBP-BMI correlation to be weak but significant; sex-uptake association may be modest.\nDemo tip: circulate and check that students report the estimate and CI, not just the p-value."},

    {"type": "content", "title": "Recap and Bridge to Day 5",
     "blocks": [
        {"header": "What you can now do", "lines": [
            "Match a question to the correct test using the data types.",
            "Run and interpret t-tests, Wilcoxon, ANOVA, chi-square and correlation.",
            "Read a p-value alongside the effect size and its confidence interval.",
            "Tell statistical significance apart from clinical importance."]},
        {"header": "Day 5 takes it further", "lines": [
            "Introduction to regression: linear (numbers) and logistic (Yes/No).",
            "Odds ratios, adjustment and confounding.",
            "Turning model output into a Results section, reproducibly."]},
        {"callout": "note", "header": "Carry forward",
         "lines": ["Keep your decision-framework table - next session we model several predictors at once."]},
     ],
     "notes": "Key teaching point: today was about choosing and interpreting single tests; Day 5 introduces regression to handle many predictors together.\nClinical interpretation: tests compare two things at a time; regression adjusts for several factors simultaneously.\nCommon mistake: stopping at p-values; next session we focus on effect sizes and clear reporting.\nAudience question: what if we want to study several predictors of a Yes/No outcome at once? Answer: logistic regression - that is Day 5."},
]
