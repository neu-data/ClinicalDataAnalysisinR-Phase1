# -*- coding: utf-8 -*-
"""Front matter: title, overview, audience, objectives, schedule, case study, data."""

SLIDES_FRONT = [
    {"type": "title",
     "title": ["Clinical Data Analysis in R"],
     "title_sz": 4000,
     "subtitle": ["Phase I  -  Introduction to R for Clinical Research",
                  "A five-session evening short course  -  Tuesdays, 8:00 PM",
                  "Trainers: Vương Mỹ Lượng & Bernard Osang'ir"],
     "date": "8 September - 6 October 2026",
     "notes": ("TITLE SLIDE.\n"
               "Welcome participants to Phase I of Clinical Data Analysis in R.\n"
               "Key teaching point: by the final session every participant will import, clean, "
               "analyse and report a real clinical dataset, with no prior coding.\n"
               "Demo tip: ask the room who has opened R before - calibrate pace.\n"
               "Audience question: what do you hope to analyse in your own work? "
               "Expected answer: trial/survey/audit data - reassure all fit this workflow.")},

    {"type": "content", "title": "Welcome & Course Aim",
     "blocks": [
        {"header": "Why this course", "lines": [
            "Clinicians increasingly need to analyse their own data and read statistics critically.",
            "R is free, reproducible and the standard tool in modern clinical research."]},
        {"header": "Our promise", "lines": [
            "Start from zero - no programming background assumed.",
            "Learn by doing, using ONE real clinical dataset all week.",
            "Finish able to produce publication-ready tables, figures and regression results."]},
        {"callout": "tip", "header": "Learning by analogy",
         "lines": ["Think of R as a very precise research assistant: you write the instructions once, it repeats them perfectly forever."]},
     ],
     "notes": ("Set the tone: supportive, practical, clinically relevant.\n"
               "Common misconception: 'I am not a maths/computer person so R is not for me.' "
               "Reframe: R is a skill like using a new clinical device - learnable with practice.\n"
               "Clinical interpretation: reproducibility protects you in audits, revisions and re-analysis.\n"
               "Audience question: how many currently use Excel/SPSS/Stata? Expected: most - bridge from there.\n"
               "Demo tip: keep the first day light on jargon.")},

    {"type": "bullets", "title": "Who This Course Is For",
     "intro": "Designed for busy clinical professionals - no programming experience needed.",
     "items": ["Medical doctors and residents",
               "Nurses and hospital research staff",
               "Clinical and hospital pharmacists",
               "Clinical researchers and trial coordinators",
               "Public health professionals",
               "Masters students and PhD candidates",
               "Anyone who collects or interprets clinical data"],
     "notes": ("Establish the shared starting point.\n"
               "Key teaching point: the mix of backgrounds is a strength - pair confident with less confident learners.\n"
               "Common misconception: that statisticians and clinicians need different tools - they do not.\n"
               "Audience question: what is your single biggest data frustration today? Expected: cleaning, or 'I cannot reproduce last year's analysis'.\n"
               "Demo tip: note names/roles to tailor examples.")},

    {"type": "content", "title": "Learning Objectives (1 of 2)",
     "blocks": [
        {"header": "By the end of the week you will be able to", "lines": [
            "Navigate R and RStudio with confidence.",
            "Understand the structure of clinical datasets.",
            "Import data from Excel and CSV files.",
            "Clean, validate and recode clinical data.",
            "Perform and interpret descriptive statistics.",
            "Generate publication-quality tables (a manuscript Table 1).",
            "Generate publication-quality figures."], "bullets": True},
     ],
     "notes": ("Walk through objectives 1-7 (the data-handling and description skills).\n"
               "Key teaching point: these map one-to-one onto the five days.\n"
               "Clinical interpretation: each objective is a step in a real manuscript workflow.\n"
               "Audience question: which objective matters most to you? Expected: varies - reassure all are covered.\n"
               "Demo tip: return to this list at each day's recap to show progress.")},

    {"type": "content", "title": "Learning Objectives (2 of 2)",
     "blocks": [
        {"header": "You will also be able to", "lines": [
            "Choose and perform common statistical tests.",
            "Interpret statistical output correctly.",
            "Perform simple and multiple logistic regression.",
            "Report odds ratios with confidence intervals.",
            "Write reproducible analysis scripts.",
            "Export publication-ready outputs.",
            "Interpret findings for medical publications."], "bullets": True},
     ],
     "notes": ("Objectives 8-13 (the analysis, inference and reporting skills).\n"
               "Key teaching point: interpretation is weighted as heavily as computation throughout.\n"
               "Common misconception: that running the test is the hard part - interpreting and reporting it well is harder.\n"
               "Audience question: who has had a paper criticised for statistics? Expected: a few - this course prevents that.\n"
               "Demo tip: emphasise we always ask 'what does this mean clinically?'")},

    {"type": "table", "title": "Course Structure - Five Sessions",
     "headers": ["Session", "Theme", "Core skill", "Exercise output"],
     "rows": [
        ["1", "Introduction to R & RStudio", "Import data", "Dataset imported"],
        ["2", "Understanding & Cleaning Clinical Data", "Clean & recode", "Analysis-ready data"],
        ["3", "Descriptive Statistics, Tables & Figures", "Tables & figures", "Manuscript Table 1"],
        ["4", "Common Medical Statistical Tests", "t-test, Chi-square, Non-parametric", "Correct test chosen"],
        ["5", "Introduction to Regression & Interpreting Output", "Modelling & reporting", "Short Results section"]],
     "caption": "Five evening sessions (Tuesdays, 90 minutes each); each session builds on the last.",
     "notes": ("Give the map of the whole week.\n"
               "Key teaching point: skills are cumulative - Day 2's clean data feeds every later day.\n"
               "Clinical interpretation: this is exactly how a real analysis project flows, start to finish.\n"
               "Audience question: which day looks most daunting? Expected: Days 4-5 - reassure we build up gently.\n"
               "Demo tip: keep this slide handy to re-orient anyone who feels lost.")},

    {"type": "content", "title": "How Each Session Runs (90 Minutes)",
     "blocks": [
        {"header": "A predictable evening rhythm", "lines": [
            "Recap & set-up - about 10 minutes: reconnect to last week.",
            "Lecture & live demo - about 55 minutes: concepts, then the trainer codes as you watch.",
            "Guided exercise - about 20 minutes: you code, we help.",
            "Wrap-up & questions - throughout and in the last 5 minutes."]},
        {"callout": "note", "header": "Bring",
         "lines": ["A laptop with R and RStudio installed (see the pre-course pack), and the course data folder."]},
     ],
     "notes": ("Explain the format so participants know what to expect each session.\n"
               "Key teaching point: watching then doing (the demo-then-exercise pattern) is how coding is learned.\n"
               "Common mistake: trying to type along during the demo and falling behind - watch first, code in the exercise.\n"
               "Audience question: prefer to type along or watch then do? Expected: mixed - explain why watch-first works.\n"
               "Demo tip: share your screen with a large font (e.g. 16-18pt).")},

    {"type": "content", "title": "Our Case Study - One Dataset All Week",
     "blocks": [
        {"header": "Study", "lines": [
            "Determinants of Hypertension Treatment Uptake among Adults attending Primary Healthcare Facilities."]},
        {"header": "Design", "lines": [
            "Multicentre cross-sectional study - 6 primary healthcare facilities.",
            "1,500 adult attendees screened for hypertension.",
            "Facilities: Bugando PHC, Kisesa HC, Nyamagana PHC, Ilemela HC, Buzuruga PHC, Igoma HC."]},
        {"header": "Primary outcome", "lines": [
            "Treatment uptake - whether a diagnosed patient is currently on antihypertensive therapy."]},
     ],
     "notes": ("Introduce the single dataset that anchors every exercise.\n"
               "Key teaching point: using one realistic dataset all week lets skills compound.\n"
               "Clinical interpretation: treatment uptake is a real implementation-science question - many diagnosed patients never start therapy.\n"
               "Audience question: why might a diagnosed patient not be on treatment? Expected: cost, distance, beliefs, no insurance - these are our predictors.\n"
               "Demo tip: this is simulated data built to behave realistically - safe to share and reproduce.")},

    {"type": "content", "title": "The Variables We Will Use",
     "blocks": [
        {"header": "Demographics & social", "lines": [
            "Age, sex, residence, education, occupation, marital status, health insurance."]},
        {"header": "Behavioural & clinical", "lines": [
            "Smoking, alcohol, physical activity, BMI, diabetes, family history, blood pressure."]},
        {"header": "Laboratory & outcomes", "lines": [
            "Cholesterol panel, glucose, creatinine, electrolytes; treatment uptake, adherence, BP control."]},
        {"callout": "tip", "header": "Data dictionary",
         "lines": ["A full data dictionary (36 variables) is provided - keep it open during every exercise."]},
     ],
     "notes": ("Preview the data dictionary so variables are familiar before Day 1's import.\n"
               "Key teaching point: knowing your variables and their types is half of good analysis.\n"
               "Common misconception: more variables is always better - we will discuss parsimony on Day 5.\n"
               "Clinical interpretation: these span the determinants framework (predisposing, enabling, need factors).\n"
               "Audience question: which variable would you expect to predict uptake? Expected: insurance, diabetes, education - we will test this.\n"
               "Demo tip: hand out the printed data dictionary now.")},

    {"type": "content", "title": "How the Week Builds to a Published Result",
     "blocks": [
        {"header": "The analysis pipeline", "lines": [
            "Import (Day 1)  ->  Clean & validate (Day 2)  ->  Describe (Day 3)",
            "Test & model (Day 4)  ->  Final model, interpret & report (Day 5)."]},
        {"header": "Your final deliverable", "lines": [
            "A short, reproducible Results section identifying the determinants of treatment uptake -",
            "exactly what a journal would expect."]},
        {"callout": "interpretation", "header": "The big idea",
         "lines": ["Every day produces one piece of a real manuscript; by Friday the pieces form a whole analysis."]},
     ],
     "notes": ("Show the throughline so participants see the destination from Day 1.\n"
               "Key teaching point: analysis is a pipeline, not a single magic command.\n"
               "Clinical interpretation: reproducibility means a reviewer could rerun your script and get your numbers.\n"
               "Audience question: where do most analyses go wrong? Expected: cleaning and interpretation - hence two full sessions on them.\n"
               "Demo tip: revisit this pipeline diagram at each session's start.")},

    {"type": "content", "title": "Sessions, Trainers & How to Register",
     "blocks": [
        {"header": "When we meet", "lines": [
            "Five evening sessions - every Tuesday, 8:00 PM, 90 minutes each.",
            "8 September to 6 October 2026.",
            "Online delivery - join from anywhere with a laptop."]},
        {"header": "Your trainers", "lines": [
            "Vương Mỹ Lượng - Senior Biostatistician (lead trainer).",
            "Bernard Osang'ir - Senior Biostatistician."]},
        {"callout": "tip", "header": "Register / enquire",
         "lines": ["Vương Mỹ Lượng  -  myluong.1710@gmail.com  -  www.neu-data.com  -  scan the poster QR code to register."]},
     ],
     "notes": ("Use this slide to confirm logistics and introduce the teaching team.\n"
               "Key teaching point: three trainers means plenty of help during the guided exercises.\n"
               "Housekeeping: share the registration link/QR and the enquiries email for colleagues who want to join a future cohort.\n"
               "Demo tip: invite each trainer to say one line about themselves.\n"
               "Audience question: any scheduling or access questions before we begin? Expected: confirm the Tuesday evening slot works.")},
]
