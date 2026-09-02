# -*- coding: utf-8 -*-
"""Day 5 (capstone) slides: Introduction to regression (linear + logistic),
model building, publication-ready reporting, and reproducibility."""

SLIDES_DAY5 = [

    {"type": "divider", "title": "Day 5: Introduction to Regression & Interpreting Output",
     "agenda": ["Linear regression: modelling a continuous outcome",
                "Logistic regression: odds ratios for a Yes/No outcome",
                "Adjusting for several factors, and confounding",
                "Publication-ready tables, figures and a Results section",
                "Reproducibility: scripts, seeds and projects"],
     "notes": "Welcome to the capstone day.\nKey point: today we turn a fitted model into a publishable, reproducible result.\nThis ties together everything from Days 1-4: importing, cleaning, summarising, and now modelling and reporting.\nTell the class the goal is not more statistics but better judgement and cleaner reporting.\nDemonstration tip: keep day5_demo.R open in RStudio throughout."},

    {"type": "bullets", "title": "Today's Objectives",
     "intro": "By the end of Day 5 you will be able to:",
     "items": [
        "Fit and read a linear regression for a continuous outcome.",
        "Fit a logistic regression and read odds ratios with 95% CIs.",
        "Understand why we adjust for several factors, and recognise confounding.",
        "Present adjusted results as a clear table and a forest plot.",
        "Write a short, honest Results section from your own numbers.",
        "Make the whole analysis reproducible end to end."],
     "notes": "Set concrete, checkable goals for the day.\nKey teaching point: these objectives map one-to-one onto the exercise deliverable.\nClinical interpretation: each skill is something they will use on their own studies, not abstract theory.\nAudience question: which of these feels least familiar? Use the show of hands to pace the day.\nDemonstration tip: return to this list at the wrap-up and tick items off."},

    {"type": "content", "title": "Where We Are in the Journey",
     "blocks": [
        {"header": "Across the week", "lines": [
            "Sessions 1-2: import and clean the hypertension dataset.",
            "Session 3: summarise and visualise (Table 1, figures).",
            "Session 4: common statistical tests (t-test, chi-square, correlation).",
            "Session 5: regression - model, interpret, report and reproduce."]},
        {"header": "Today's running example", "lines": [
            "Outcome: treatment_uptake among diagnosed hypertensives.",
            "Analytic sample: 1,089 diagnosed; 992 complete cases modelled."]},
        {"callout": "note", "header": "One dataset, end to end",
         "lines": ["Every result today comes from the same study you cleaned earlier."]},
     ],
     "notes": "Orient the audience: this is a coherent pipeline, not isolated tricks.\nCommon misconception: that modelling is the hard part. The judgement (which variables, how to report) is harder.\nClinical interpretation: only diagnosed patients can take up treatment, so we restrict to them.\nAudience question: why model only the 1,089 diagnosed and not all 1,500? Expected answer: people without a diagnosis cannot have a treatment-uptake decision; including them biases the estimates."},

    {"type": "content", "title": "Linear Regression: Modelling a Number",
     "blocks": [
        {"header": "When the outcome is a number", "lines": [
            "Linear regression models a CONTINUOUS outcome, such as blood pressure.",
            "Outcome = a systematic part (the predictors) + unexplained variation.",
            "It estimates how much the outcome changes per one unit of a predictor."]},
        {"header": "Reading the output", "lines": [
            "The coefficient (slope) is the change in the outcome per one-unit rise.",
            "Each coefficient comes with a 95% CI and a p-value.",
            "Adding predictors gives each one's ADJUSTED effect, holding the others constant."]},
        {"callout": "interpretation", "header": "Clinical question",
         "lines": ["Is systolic blood pressure associated with age - and does it hold after adjusting for sex and BMI?"]},
     ],
     "notes": "Key teaching point: linear regression is for a continuous outcome; the slope is a change per unit.\nClinical interpretation: the intercept is rarely meaningful; the slopes are what we report.\nCommon mistake: using linear regression for a Yes/No outcome - that needs logistic regression (next).\nAudience question: outcome is systolic BP (a number) and predictor is age - which model? Answer: linear regression."},

    {"type": "code", "title": "Demo: Linear Regression of SBP on Age",
     "intro": "Does systolic blood pressure rise with age, adjusting for sex and BMI?",
     "code": "m1 <- lm(sbp_mmhg ~ age, data = analysis_data)\nsummary(m1)\n\n# adjust for sex and BMI\nm2 <- lm(sbp_mmhg ~ age + sex + bmi,\n         data = analysis_data)\ntidy(m2, conf.int = TRUE)",
     "output": "term        estimate conf.low conf.high p.value\n(Intercept)   87.31    81.01    93.61   <0.001\nage            0.26     0.19     0.33   <0.001\nsexMale        0.33    -1.57     2.22    0.74\nbmi            1.45     1.26     1.64   <0.001",
     "note": "Each extra year adds ~0.26 mmHg to SBP and each BMI unit ~1.45 mmHg; sex is not significant.",
     "notes": "Key teaching point: read each slope as an adjusted change per unit, with its 95% CI.\nClinical interpretation: age and BMI are independently associated with SBP; sex is not (CI crosses 0, p = 0.74).\nCommon mistake: reporting the intercept as if it were clinically meaningful.\nDemo tip: run summary(m1) first (crude), then the adjusted m2, and note the age slope barely changes."},

    {"type": "content", "title": "Why Logistic Regression?",
     "blocks": [
        {"header": "The outcome is binary", "lines": [
            "Treatment uptake is Yes/No - not a number, so not linear regression.",
            "Logistic regression models the ODDS of the 'Yes' outcome.",
            "It handles one predictor or many at once."]},
        {"header": "Odds and odds ratios", "lines": [
            "Odds = probability of Yes divided by probability of No.",
            "An odds ratio (OR) compares the odds between two groups.",
            "The OR is the single number clinicians read from the model."]},
        {"callout": "tip", "header": "Why odds, not probability",
         "lines": ["Odds let us multiply effects cleanly and give a constant OR per group."]},
     ],
     "notes": "Key teaching point: a binary outcome calls for logistic regression, which models odds rather than a mean.\nClinical interpretation: the odds ratio is the deliverable - it travels straight into the manuscript and the forest plot.\nCommon mistake: trying to fit a linear model to a Yes/No outcome.\nAudience question: what are the odds if 3 of 4 patients take up treatment? Answer: 3 to 1, i.e. odds = 3."},

    {"type": "content", "title": "Reading an Odds Ratio",
     "blocks": [
        {"header": "Direction of the effect", "lines": [
            "OR = 1: the predictor has no effect on the odds of uptake.",
            "OR > 1: higher odds of uptake (a positive driver).",
            "OR < 1: lower odds of uptake (a protective / negative driver)."]},
        {"header": "Precision and significance", "lines": [
            "The 95% CI shows the plausible range for the true OR.",
            "If the CI excludes 1, the effect is statistically significant.",
            "A wide CI means an imprecise, uncertain estimate."]},
        {"callout": "interpretation", "header": "Example phrasing",
         "lines": ["Diabetics had 3.6 times the odds of uptake (aOR 3.56, 95% CI 1.46 to 9.61)."]},
     ],
     "notes": "Key teaching point: read an OR as direction (vs 1) plus significance (does the CI cross 1?).\nCommon mistake: reading the raw coefficient (log-odds) as if it were the OR - always exponentiate first.\nClinical interpretation: 'OR excludes 1' is the regression equivalent of p < 0.05, but with magnitude attached.\nAudience question: OR 0.7 with CI 0.5 to 0.9 - what does it mean? Answer: a real protective effect, 30% lower odds."},

    {"type": "code", "title": "Demo: Univariable Logistic Regression (Diabetes)",
     "intro": "Does diabetes raise the odds of treatment uptake?",
     "code": "m_diab <- glm(treatment_uptake ~ diabetes,\n              data = dx, family = binomial)\nexp(coef(m_diab))      # odds ratio\nexp(confint(m_diab))   # 95% CI",
     "output": "(Intercept)   diabetesYes\n      0.74          2.85\n            2.5 %   97.5 %\ndiabetesYes  2.01     4.07",
     "note": "Unadjusted OR ~2.85: diabetics have roughly triple the odds of uptake; CI excludes 1.",
     "notes": "Key teaching point: family = binomial tells glm the outcome is 0/1; exp() turns log-odds into an interpretable OR.\nCommon mistake: reporting exp(coef) but forgetting the reference level - here diabetesYes is compared with No.\nClinical interpretation: the unadjusted OR will shrink once we adjust for confounders such as age.\nDemo tip: show summary(m_diab) first so they see the log-odds, then exp() to make it a clinician-friendly OR."},

    {"type": "content", "title": "A Continuous Predictor: Age",
     "blocks": [
        {"header": "OR per one unit", "lines": [
            "glm(treatment_uptake ~ age) gives the OR per ONE extra year.",
            "That OR is close to 1 because one year is a tiny step.",
            "Here about 1.03 per year - easy to overlook."]},
        {"header": "Rescale to a meaningful unit", "lines": [
            "OR per 10 years = the 1-year OR raised to the power 10.",
            "exp(coef(m_age)[\"age\"] * 10) gives the per-decade OR.",
            "1.03 per year becomes roughly 1.34 per decade."]},
        {"callout": "tip", "header": "Communicate in clinical units",
         "lines": ["Per decade is far easier for a clinical audience than per year."]},
     ],
     "notes": "Key teaching point: for a continuous predictor the OR is per one-unit change - choose a unit people care about.\nCommon mistake: dismissing age as unimportant because OR ~1.03 looks trivial per single year.\nClinical interpretation: per-decade framing (about 1.34) shows age is a meaningful driver of uptake.\nDemo tip: run exp(coef(m_age)['age'] * 10) live to convert per-year into per-decade."},

    {"type": "content", "title": "Model Building: Clinical Knowledge First",
     "blocks": [
        {"header": "Choose predictors before you look at p-values", "lines": [
            "Biological or clinical plausibility (diabetes drives clinic visits).",
            "Known confounders from the literature (age, sex, education).",
            "The study's stated determinants (distance, knowledge)."]},
        {"header": "Then fit ONE pre-specified model", "lines": [
            "Decide the variable list first, fit once, report it.",
            "This is the honest, replicable approach for a determinants study."]},
        {"callout": "mistake", "header": "Data dredging",
         "lines": ["Trying many models and reporting only significant ones inflates false positives."]},
     ],
     "notes": "Core philosophy slide: clinically-motivated selection beats blind automation.\nKey teaching point: a pre-specified model is defensible to reviewers and reproducible.\nCommon mistake: letting the computer pick variables, then telling a clinical story around whatever survived.\nClinical interpretation: in an explanatory study we keep known confounders even if non-significant.\nAudience question: should we drop a variable just because p > 0.05? Expected answer: no, not if it is a known confounder; dropping it can reintroduce bias."},

    {"type": "two_column", "title": "Confounding: A Clinical Example",
     "left": {"header": "What confounding is", "lines": [
        "A third variable distorts the crude link between exposure and outcome.",
        "Example: urban residents are younger and better insured.",
        "Those factors also raise uptake - so crude residence looks too strong.",
        "Adjusting for them isolates the true residence effect."], "bullets": True},
     "right": {"header": "How we detect it", "lines": [
        "Compare the crude OR with the adjusted OR for residence.",
        "If the estimate shifts noticeably (rule of thumb >10%), confounding is present.",
        "Always report and interpret the ADJUSTED odds ratio.",
        "The adjusted urban OR in our model is 1.87 (1.41-2.49)."], "bullets": True},
     "notes": "Confounding is the single most important modelling concept for clinicians.\nKey teaching point: adjustment is how observational studies approximate a fair comparison.\nCommon mistake: reporting and interpreting the crude OR.\nClinical interpretation: the crude urban effect is partly explained by age and insurance; after adjustment a genuine residual urban advantage of about 1.87 remains.\nDemonstration tip: in the next slide we show the crude vs adjusted numbers from R."},

    {"type": "code", "title": "Demo: Crude vs Adjusted OR for Residence",
     "intro": "Fit a crude model, then compare with the full model.",
     "code": "crude <- glm(treatment_uptake ~ residence,\n             data = dx, family = binomial)\nfull <- glm(treatment_uptake ~ age + sex + education +\n             residence + diabetes + family_history_htn +\n             health_insurance + knowledge_score +\n             distance_to_facility_km,\n             data = dx, family = binomial)\nexp(coef(crude))[\"residenceUrban\"]\nexp(coef(full))[\"residenceUrban\"]",
     "output": "residenceUrban\n     2.34\nresidenceUrban\n     1.87",
     "note": "The OR shrinks from 2.34 (crude) to 1.87 (adjusted): age and insurance were confounding it.",
     "notes": "Live demo from day5_demo.R, sections 2-3.\nKey teaching point: exp() converts log-odds to an odds ratio.\nCommon mistake: forgetting that glm needs family = binomial for a logistic model.\nClinical interpretation: a >10% drop confirms confounding; the adjusted 1.87 is what we report.\nAudience question: why does the urban effect shrink? Expected answer: because urban residents differ on age and insurance, which independently raise uptake."},

    {"type": "code", "title": "Demo: The Final Model and Tidy ORs",
     "intro": "Fit once, then turn coefficients into odds ratios with CIs.",
     "code": "model_final <- full\nlibrary(broom)\nor_table <- tidy(model_final,\n                 exponentiate = TRUE,\n                 conf.int = TRUE)\nprint(or_table, n = Inf)",
     "output": "term            estimate conf.low conf.high\ndiabetesYes        3.56     1.46      9.61\nhealth_insuranceYes 2.05    1.54      2.74\nresidenceUrban     1.87     1.41      2.49\nage                1.03     1.02      1.04",
     "note": "exponentiate = TRUE gives ORs; conf.int = TRUE adds 95% CIs - the exact table your reader needs.",
     "notes": "Live demo from day5_demo.R, section 7.\nKey teaching point: broom::tidy() converts a model object into a clean data frame, ready to plot or export.\nCommon mistake: hand-copying numbers from summary() into a Word table - error-prone and unreproducible.\nClinical interpretation: every CI shown excludes 1, so all are significant; diabetes has the largest OR but the widest CI.\nAudience question: why is the diabetes CI so wide? Expected answer: diabetics are a smaller subgroup, so the estimate is less precise."},

    {"type": "table", "title": "Final Multivariable Model: Adjusted ORs",
     "headers": ["Predictor", "aOR", "95% CI", "p"],
     "rows": [["Age (per year)", "1.03", "1.02-1.04", "<0.001"],
              ["Sex: Male (vs Female)", "0.74", "0.56-0.97", "0.031"],
              ["Education (linear trend)", "1.96", "1.39-2.77", "<0.001"],
              ["Residence: Urban (vs Rural)", "1.87", "1.41-2.49", "<0.001"],
              ["Diabetes: Yes", "3.56", "1.46-9.61", "0.007"],
              ["Health insurance: Yes", "2.05", "1.54-2.74", "<0.001"],
              ["Distance to facility (per km)", "0.98", "0.96-1.01", "0.128"]],
     "caption": "Logistic regression; n = 992 complete cases; AUC = 0.71. Family history aOR 1.91 (1.44-2.54); knowledge 1.10 (1.06-1.14) per point.",
     "notes": "These are the canonical numbers from key_findings.md - cite them accurately.\nKey teaching point: this is the manuscript's main results table.\nCommon mistake: omitting the CI or the n; reviewers always ask.\nClinical interpretation: distance is in the expected protective-against-uptake direction (OR 0.98) but not significant - report it as such, do not call it null.\nAudience question: which predictor matters most? Expected answer: diabetes has the largest OR (3.56), but caution - its CI is widest, so precision is lower.\nDemonstration tip: family history and knowledge are in the caption to keep the table within the row limit."},

    {"type": "image", "title": "Visualising the Adjusted ORs",
     "image": "forest_plot_or.png", "aspect": 0.78,
     "side_header": "How to read it",
     "side_notes": ["Each point is an adjusted odds ratio.",
                    "Whiskers are the 95% confidence intervals.",
                    "Dashed line at 1 = no effect.",
                    "Right of 1 increases uptake; left decreases it.",
                    "Diabetes sits farthest right - largest effect.",
                    "Distance crosses 1 - not significant."],
     "notes": "Key teaching point: a forest plot communicates the whole model at a glance.\nThe x-axis is on a log scale so the CIs appear symmetric around each point.\nCommon mistake: putting the OR axis on a linear scale, which squashes the small ORs.\nClinical interpretation: any CI whisker that crosses the dashed line at 1 is non-significant - here only distance does.\nAudience question: why does distance look different from the others? Expected answer: its interval straddles 1, so we cannot rule out no effect."},

    {"type": "code", "title": "Demo: Publication-Ready Table and Forest Plot",
     "intro": "Build a journal-style table, then save the figure.",
     "code": "library(gtsummary)\ntbl <- tbl_regression(model_final,\n                      exponentiate = TRUE) |>\n  bold_p()\ntbl\n# save the forest plot built from or_table\nggsave(\"Resources/forest_plot_or.png\",\n       plot = forest, width = 8, height = 5, dpi = 300)",
     "note": "tbl_regression reads the model directly - no manual copying - and ggsave exports the figure for the manuscript.",
     "notes": "Live demo from day5_demo.R, sections 8-9.\nKey teaching point: tables and figures should be generated from code, never retyped.\nCommon mistake: editing numbers by hand in Word, which breaks reproducibility and invites transcription errors.\nClinical interpretation: the saved PNG is the exact figure on the previous slide.\nDemonstration tip: show as_gt(tbl) |> gtsave(\"Resources/regression_table.html\") to export the table too; mention a write_csv fallback if gtsummary is unavailable."},

    {"type": "content", "title": "Exporting Outputs for the Manuscript",
     "blocks": [
        {"header": "Save tables", "lines": [
            "gtsummary: as_gt(tbl) then gtsave() writes HTML, PNG or Word.",
            "Fallback: write_csv(or_table, \"Resources/regression_table.csv\")."]},
        {"header": "Save figures", "lines": [
            "ggsave() writes the forest plot at a fixed size and resolution.",
            "Use dpi = 300 for print-quality figures in journals."]},
        {"header": "Why export from code", "lines": [
            "The report can be rebuilt from raw data with no manual steps.",
            "No copy-paste means no transcription errors."]},
        {"callout": "tip", "header": "Keep a Resources/ folder",
         "lines": ["Send every table and figure there so outputs live in one place."]},
     ],
     "notes": "Key teaching point: outputs are artefacts of code, not hand-built files.\nCommon mistake: screenshotting a plot from the RStudio viewer instead of using ggsave - low resolution and not reproducible.\nClinical interpretation: a reviewer who asks for a tweak gets it by editing one line and re-running.\nAudience question: what dpi for a print figure? Expected answer: 300.\nDemonstration tip: run ggsave and gtsave live, then open the Resources/ folder to show the files appear."},

    {"type": "two_column", "title": "From Odds Ratios to Prose",
     "left": {"header": "The numbers", "lines": [
        "Diabetes: aOR 3.56 (1.46-9.61).",
        "Insurance: aOR 2.05 (1.54-2.74).",
        "Urban: aOR 1.87 (1.41-2.49).",
        "Education trend: aOR 1.96 (1.39-2.77).",
        "Male sex: aOR 0.74 (0.56-0.97).",
        "Distance: aOR 0.98 (0.96-1.01), NS."], "bullets": True},
     "right": {"header": "Turning each OR into a sentence", "lines": [
        "State direction, size, comparison group and CI.",
        "OR>1: 'X times the odds of uptake'.",
        "OR<1: 'lower odds' - here men vs women.",
        "Continuous: 'per 1-unit increase'.",
        "Name the reference group explicitly.",
        "Report NS findings honestly, with the CI."], "bullets": True},
     "notes": "Key teaching point: a Results section is structured translation, not invention.\nEach OR becomes one clear clause: direction, magnitude, comparator, precision.\nCommon mistake: writing 'X caused Y' from an observational OR - use 'was associated with'.\nClinical interpretation: an OR of 0.74 for male sex means men had about 26% lower odds than women.\nAudience question: how do you phrase a non-significant finding? Expected answer: report the estimate and CI and state it was not statistically significant - do not claim 'no effect'."},

    {"type": "content", "title": "Worked Example: A Results Paragraph",
     "blocks": [
        {"header": "Model results paragraph", "lines": [
            "Among 992 diagnosed hypertensives, treatment uptake was independently",
            "associated with diabetes (aOR 3.56, 95% CI 1.46-9.61), health insurance",
            "(2.05, 1.54-2.74), urban residence (1.87, 1.41-2.49) and higher education",
            "(1.96, 1.39-2.77). Older age (1.03 per year) and greater knowledge (1.10",
            "per point) also raised the odds, while men had lower odds than women",
            "(0.74, 0.56-0.97). Distance to facility was not significant (0.98,",
            "0.96-1.01). The model discriminated acceptably (AUC 0.71)."]},
        {"callout": "tip", "header": "Always close with discrimination",
         "lines": ["Reporting the AUC tells the reader how well the model separates uptake from non-uptake."]},
     ],
     "notes": "This is a model answer the class can adapt for the exercise.\nKey teaching point: lead with the analytic n, list significant determinants with ORs and CIs, then report the non-significant one and overall fit.\nCommon mistake: causal language ('diabetes increases uptake') from a cross-sectional study.\nClinical interpretation: the paragraph mirrors exactly the directions in key_findings.md.\nAudience question: what belongs in the very first sentence? Expected answer: the sample size and outcome, so the reader knows the basis of every number that follows."},

    {"type": "content", "title": "Reproducibility: The Capstone Message",
     "blocks": [
        {"header": "Make your work re-runnable by anyone", "lines": [
            "Scripts over click-menus: the code is the permanent record.",
            "set.seed() makes any randomness (bootstraps, splits) repeatable.",
            "Use RStudio Projects and relative paths - never C:/Users/yourname/...",
            "Save every table and figure to disk so the report rebuilds from code."]},
        {"header": "Record and share your environment", "lines": [
            "sessionInfo() captures your exact R and package versions.",
            "R Markdown / Quarto knit code, text and figures into one report."]},
        {"callout": "tip", "header": "Best practice",
         "lines": ["One click should rebuild the whole report from raw data to PDF."]},
     ],
     "notes": "Key teaching point: a result you cannot reproduce is a result you cannot defend.\nClick-menu analyses leave no trace; scripts do.\nCommon mistake: hard-coding an absolute path that only works on your laptop - it breaks for every collaborator.\nClinical interpretation: reproducibility is part of research integrity, not an optional extra.\nAudience question: why set a seed if logistic regression is deterministic? Expected answer: so the whole script - including any resampling or simulation - reproduces identically end to end.\nDemonstration tip: show the folder structure Data/ Scripts/ Solutions/ Resources/ References/."},

    {"type": "code", "title": "Demo: A Reproducibility Snippet",
     "intro": "Seed, relative path, and a recorded environment.",
     "code": "set.seed(2025)\nanalysis_data <- readRDS(\"Data/analysis_data.rds\")\ndx <- filter(analysis_data, htn_diagnosed == \"Yes\")\n# record the exact software environment\nwriteLines(capture.output(sessionInfo()),\n           \"References/session_info.txt\")",
     "output": "R version 4.4.1 (2024-06-14)\nattached: dplyr_1.1.4 broom_1.0.6 gtsummary_2.0\n... (full environment written to References/session_info.txt)",
     "note": "Relative paths plus a saved sessionInfo() let any colleague rerun this on any machine.",
     "notes": "Live demo from day5_demo.R, sections 0-1 and 10.\nKey teaching point: these three habits - seed, relative path, recorded environment - cover most reproducibility failures.\nCommon mistake: re-cleaning data inside the analysis script; cleaning belongs in its own script (separation of concerns).\nClinical interpretation: readRDS loads the already-cleaned, analysis-ready data.\nDemonstration tip: open References/session_info.txt after running to show what was captured."},

    {"type": "content", "title": "Day 5 Exercise: Complete the Analysis & Write a Results Section",
     "blocks": [
        {"header": "Your tasks", "lines": [
            "Fit the pre-specified multivariable model on the diagnosed subset.",
            "Produce a tidy OR table (exponentiate = TRUE, conf.int = TRUE).",
            "Run the diagnostics: VIF, a linearity check, Cook's distance, AUC.",
            "Build a gtsummary table and a forest plot, and save both to Resources/.",
            "Write a 4-6 sentence Results section from your own ORs."]},
        {"callout": "note", "header": "Deliverable",
         "lines": ["A reproducible script plus a short Results paragraph citing aORs, 95% CIs and the AUC."]},
     ],
     "notes": "Key teaching point: this exercise integrates the whole week into one deliverable.\nCommon mistake: forgetting to restrict to htn_diagnosed == 'Yes', or reporting crude instead of adjusted ORs.\nClinical interpretation: the marking rubric (key_findings.md) rewards correct method and interpretation, not 2nd-decimal matches.\nAudience question: how long should the Results paragraph be? Expected answer: a tight 4-6 sentences - n and outcome, significant determinants with ORs and CIs, the non-significant one, then AUC.\nDemonstration tip: point them to day5_demo.R as a scaffold and circulate while they work."},

    {"type": "bullets", "title": "Course Wrap-Up: What You Can Now Do",
     "intro": "Five days, one real dataset, a full analysis pipeline.",
     "items": [
        "Import messy clinical data into R and understand its structure.",
        "Clean it: fix impossible values, standardise categories, handle missingness.",
        "Summarise and visualise: Table 1, histograms, boxplots, bar charts.",
        "Fit and interpret logistic regression with adjusted odds ratios.",
        "Build models from clinical reasoning and check their assumptions.",
        "Produce publication-ready tables and figures, and a Results section.",
        "Work reproducibly with scripts, projects, seeds and Quarto reports."],
     "notes": "Key teaching point: celebrate the distance travelled - they started with no programming background.\nReassure them that fluency comes with practice on their own data.\nClinical interpretation: they now own a defensible, reproducible workflow they can take to their own studies.\nAudience question: what is the single most valuable habit to keep? Expected answer: do everything in a script so it is reproducible.\nDemonstration tip: invite one or two participants to share what surprised them most."},

    {"type": "content", "title": "What Phase II Might Cover",
     "blocks": [
        {"header": "Deeper modelling", "lines": [
            "Confounding, interaction and effect modification in depth.",
            "Model diagnostics: multicollinearity, fit and discrimination (AUC).",
            "Variable selection and how to build a model responsibly."]},
        {"header": "New methods and skills", "lines": [
            "Survival analysis: Kaplan-Meier and Cox models for time-to-event data.",
            "Mixed-effects models: patients clustered within facilities.",
            "Missing data (multiple imputation) and automated Quarto reporting."]},
        {"callout": "tip", "header": "Keep practising",
         "lines": ["Bring your own dataset to Phase II and analyse it end to end."]},
     ],
     "notes": "Key teaching point: today's logistic model is the foundation; Phase II generalises it.\nClinical interpretation: their 6-facility study is naturally clustered, which motivates mixed models in Phase II.\nCommon misconception: that survival and logistic regression are unrelated - both are regression, just for different outcome types.\nAudience question: which Phase II topic fits a study following patients over time? Expected answer: survival analysis, because the outcome is time-to-event.\nDemonstration tip: thank the class, point to References/ for further reading, and close with #ClearDataClearImpact."},
]
