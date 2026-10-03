# -*- coding: utf-8 -*-
"""Final assignment, marking rubric, resources, and closing."""

SLIDES_ASSIGN = [
    {"type": "divider", "title": "Final Assignment",
     "plan_title": "Overview",
     "agenda": ["An independent, take-home analysis",
                "One week to complete",
                "Uses the same study dataset",
                "Marked out of 100%"],
     "notes": ("Introduce the capstone assessment.\n"
               "Key teaching point: this consolidates all five days into one independent analysis.\n"
               "Clinical interpretation: it mirrors writing the analysis for a real paper.\n"
               "Audience question: how long should you budget? Expected: a few focused sessions across the week.\n"
               "Demo tip: encourage starting from their saved Day 2 cleaning script.")},

    {"type": "content", "title": "Final Assignment - What to Do",
     "blocks": [
        {"header": "Task", "lines": [
            "Working independently, analyse the study dataset and identify the determinants of treatment uptake."]},
        {"header": "Your submission must", "lines": [
            "Import the raw data and clean/validate it.",
            "Produce descriptive statistics and a publication-ready Table 1.",
            "Create at least two publication-quality figures.",
            "Perform appropriate statistical tests.",
            "Fit simple and multiple logistic regression models.",
            "Interpret the results and write a short Results section.",
            "Be fully reproducible (a single script that runs start to finish)."], "bullets": True},
     ],
     "notes": ("Spell out exactly what to deliver.\n"
               "Key teaching point: reproducibility is graded - the script must run on a clean machine.\n"
               "Common mistake: submitting only output with no script, or a script with hard-coded absolute paths.\n"
               "Clinical interpretation: the Results section should read like a journal submission.\n"
               "Audience question: what makes a script reproducible? Expected: relative paths, library() calls, set.seed, no manual steps.\n"
               "Demo tip: point them to the Day 5 results draft as a template.")},

    {"type": "content", "title": "Final Assignment - Deliverables & Submission",
     "blocks": [
        {"header": "Submit", "lines": [
            "1. A single commented R script (.R) or R Markdown/Quarto file.",
            "2. The exported Table 1 and figures.",
            "3. A one-page Results section (about 250-400 words)."]},
        {"header": "Format", "lines": [
            "Use an RStudio Project with relative paths.",
            "Name files clearly: Surname_Phase1_Assignment.R",
            "Email the .zip to the lead trainer, Vương Mỹ Lượng: myluong.1710@gmail.com"]},
        {"callout": "warning", "header": "Academic integrity",
         "lines": ["Work independently. You may use the course scripts and notes, but the analysis and writing must be your own."]},
     ],
     "notes": ("Clarify the mechanics of submission.\n"
               "Key teaching point: clear, commented code is part of the grade, not an afterthought.\n"
               "Common mistake: figures saved at screen resolution - require 300 dpi via ggsave.\n"
               "Clinical interpretation: a tidy submission reflects a tidy analyst.\n"
               "Audience question: R script or Quarto? Expected: either - Quarto earns the reproducibility marks easily.\n"
               "Demo tip: show the folder structure you expect.")},

    {"type": "table", "title": "Marking Rubric (out of 100%)",
     "headers": ["Component", "What is assessed", "Marks"],
     "rows": [
        ["Data import & cleaning", "Correct import, missing codes, validation, recoding", "20"],
        ["Descriptive statistics", "Appropriate summaries and a correct Table 1", "15"],
        ["Figures", "Two clear, correctly labelled, publication-quality figures", "10"],
        ["Statistical tests", "Right test chosen and correctly applied", "15"],
        ["Regression modelling", "Sound univariable & multivariable logistic models", "20"],
        ["Interpretation & Results", "Accurate ORs/CIs and clear clinical writing", "15"],
        ["Reproducibility & code quality", "Runs end-to-end; clean, commented, relative paths", "5"]],
     "caption": "Total = 100%. A detailed marking guide is provided to instructors.",
     "notes": ("Make grading transparent.\n"
               "Key teaching point: cleaning and regression carry the most weight (20 each) - spend time there.\n"
               "Clinical interpretation: interpretation is explicitly rewarded, not just computation.\n"
               "Common mistake: perfect code, wrong interpretation - you lose the 15 interpretation marks.\n"
               "Audience question: where will you focus your effort? Expected: cleaning + modelling - correct.\n"
               "Demo tip: the full marking guide with point-by-point criteria is in the instructor pack.")},

    {"type": "two_column", "title": "Marking Guide - What Earns Full Marks",
     "left": {"header": "Strong submission", "lines": [
        "Handles all messiness (dups, sentinels, impossible values).",
        "Table 1 stratified by uptake with sensible tests.",
        "Adjusted ORs with 95% CIs and correct reference levels.",
        "Results paragraph matches the numbers and is clinically framed.",
        "One script runs cleanly from raw data to outputs."], "bullets": True},
     "right": {"header": "Common mark losses", "lines": [
        "Leaving 999 / -99 as real numbers.",
        "Analysing all 1,500 instead of diagnosed patients.",
        "Reporting log-odds instead of odds ratios.",
        "Interpreting a non-significant result as 'no effect'.",
        "Absolute paths that break on another computer."], "bullets": True},
     "notes": ("Give participants a concrete picture of excellent vs weak work.\n"
               "Key teaching point: most marks are lost on avoidable cleaning and interpretation errors.\n"
               "Clinical interpretation: 'not significant' means 'insufficient evidence', not 'no effect'.\n"
               "Common mistake: forgetting to restrict to htn_diagnosed == Yes for the uptake analysis.\n"
               "Audience question: why analyse only diagnosed patients? Expected: uptake is only defined once diagnosed.\n"
               "Demo tip: hand out this slide as a self-check before submission.")},

    {"type": "content", "title": "Resources & Further Reading",
     "blocks": [
        {"header": "In your course pack", "lines": [
            "R command reference sheet and package installation guide.",
            "All demonstration scripts and worked solutions.",
            "The dataset, data dictionary and this slide deck."]},
        {"header": "To go further", "lines": [
            "R for Data Science (Wickham & Grolemund) - free online.",
            "Regression Modeling Strategies (Harrell).",
            "The gtsummary and ggplot2 documentation websites."]},
        {"callout": "tip", "header": "Keep practising",
         "lines": ["Re-run the week's scripts on your own data - that is where the skills become permanent."]},
     ],
     "notes": ("Point to everything they can take away and where to grow next.\n"
               "Key teaching point: the reference sheet answers 80% of day-to-day questions.\n"
               "Clinical interpretation: applying R to their OWN data is the real test of learning.\n"
               "Audience question: what will you analyse first after the course? Expected: an audit or a stalled project.\n"
               "Demo tip: mention Phase II as the next step - its topics (potentially survival analysis, mixed models or prediction) will follow the participant survey.")},

    {"type": "divider", "title": "Thank You & Questions",
     "plan_title": "Stay in touch",
     "agenda": ["You can now import, clean, analyse and report clinical data in R",
                "Practise on your own datasets",
                "Phase II: potentially survival analysis, mixed models or prediction - shaped by your survey answers",
                "Contact: Neudata  -  #ClearDataClearImpact"],
     "notes": ("Close warmly and open the floor.\n"
               "Key teaching point: celebrate that everyone went from zero to a full analysis in five days.\n"
               "Clinical interpretation: encourage them to embed reproducible analysis in their teams.\n"
               "Audience question: what is your single biggest takeaway? Expected: varies - affirm each.\n"
               "Demo tip: collect feedback and share contact details for follow-up.")},

    {"type": "closing", "notes": ("COPYRIGHT / CLOSING SLIDE.\n"
               "Standard Neudata copyright. Thank participants and the host institution.")},
]
