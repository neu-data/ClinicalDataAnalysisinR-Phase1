SLIDES_DAY2 = [

    # 1. Divider
    {"type": "divider", "title": "Day 2: Understanding & Cleaning Clinical Data",
     "plan_title": "Plan",
     "agenda": [
         "Why cleaning matters: garbage in, garbage out",
         "Variable types and clinical coding",
         "Missing data, duplicates, inconsistent categories",
         "Validation, recoding, dates and factors",
         "Save the clean dataset: the contract for Days 3-5"],
     "notes": "Key point: today we turn a messy raw file into a tidy, analysis-ready dataset and save it once for the whole week.\nMisconception: cleaning is not a quick step before the 'real' work; it IS most of the work.\nClinical interpretation: every later result depends on decisions made today.\nAsk: who has ever found an error in their data after running the analysis? Expected: most hands go up, often after submission.\nDemo tip: keep the raw file open beside the script so people see the mess we are taming."},

    # 2. Why cleaning matters
    {"type": "content", "title": "Why Data Cleaning Matters",
     "blocks": [
         {"header": "Garbage in, garbage out",
          "lines": [
              "A p-value cannot rescue a mistyped blood pressure.",
              "Errors do not announce themselves; they hide in plausible numbers.",
              "Clean data is the foundation of a credible result."]},
         {"header": "How much of a project is cleaning?",
          "lines": [
              "Typically 60-80% of total analysis time.",
              "Skipping it does not save time; it moves the cost to peer review."]},
         {"callout": "interpretation", "header": "Why clinicians should care",
          "lines": ["A wrong cut-off or unit can flip a clinical conclusion."]},
     ],
     "notes": "Key point: cleaning is the majority of real-world analysis time and the part reviewers scrutinise most.\nMisconception: 'the data manager already cleaned it' - someone must still check it against clinical sense.\nClinical interpretation: an SBP of 7 or an age of 200 will quietly distort means and models.\nAsk: what is a realistic resting SBP range for an adult? Expected: roughly 90-180; this intuition is exactly what we encode as validation rules.\nDemo tip: show one impossible value and ask what it would do to a mean."},

    # 3. Variable types overview (table)
    {"type": "table", "title": "Variable Types in Clinical Data",
     "headers": ["Type", "What it is", "Example in our data"],
     "rows": [
         ["Continuous", "Numbers on a scale", "age, sbp_mmhg, weight_kg"],
         ["Binary", "Two categories", "diabetes (Yes/No)"],
         ["Categorical", "Unordered groups", "facility, occupation"],
         ["Ordinal", "Ordered groups", "education (None to Tertiary)"],
         ["Date", "Calendar time", "enroll_date"]],
     "caption": "The type decides how R stores, summarises and models a variable.",
     "notes": "Key point: choosing the right type up front controls every later summary, plot and model.\nMisconception: 'a number is always continuous' - coded categories (1=Yes) are numbers but are categorical.\nClinical interpretation: ordinal education should keep its order; facility should not be treated as a ranked scale.\nAsk: is a Likert pain score 0-10 continuous or ordinal? Expected: defensible either way; the point is to decide deliberately.\nDemo tip: map each row to a column in the open raw file."},

    # 4. Clinical coding
    {"type": "content", "title": "Clinical Coding: Consistent Codes",
     "blocks": [
         {"header": "What coding means",
          "lines": [
              "Agreeing one written value per real-world category.",
              "Sex stored as Female / Male, not F / f / female.",
              "Binaries stored as Yes / No, not a mix of Y, 1, true."]},
         {"header": "Why it matters",
          "lines": [
              "R treats 'Yes' and 'yes' as two different groups.",
              "Inconsistent codes split one category into several.",
              "Consistent codes make tables and models trustworthy."]},
         {"callout": "warning", "header": "Common trap",
          "lines": ["Eight spellings of sex become eight phantom categories."]},
     ],
     "notes": "Key point: a category exists only if its label is written identically every time.\nMisconception: R is smart enough to know 'Y' means 'Yes' - it is not.\nClinical interpretation: a split sex variable would bias any sex-adjusted estimate.\nAsk: how many distinct values of sex might a free-text field produce? Expected: surprisingly many; we will see eight.\nDemo tip: run table() before cleaning to reveal the chaos."},

    # 5. Missing data
    {"type": "content", "title": "Missing Data: How It Hides",
     "blocks": [
         {"header": "It rarely looks like one thing",
          "lines": [
              "Blank cells, the word NA, and sentinel codes 999 or -99.",
              "If R does not recognise them, 999 is treated as a real value.",
              "A single 999 can wreck a mean or a regression."]},
         {"header": "Read it correctly at import",
          "lines": [
              "Tell read_csv which strings mean missing.",
              "na = c(\"\", \"NA\", \"999\", \"-99\")"]},
         {"callout": "note", "header": "Types of missingness (brief)",
          "lines": ["MCAR, MAR, MNAR - the pattern affects how we handle it later."]},
     ],
     "notes": "Key point: define missingness at import so sentinels never enter the analysis as numbers.\nMisconception: blanks are the only kind of missing - numeric sentinels are the dangerous ones.\nClinical interpretation: 999 systolic would inflate the mean and falsely raise hypertension prevalence.\nAsk: what happens to mean(sbp) if one 999 is read as a real value? Expected: it jumps; the example sells the na= argument.\nDemo tip: import once without na= and once with it; compare summary()."},

    # 6. Duplicates
    {"type": "content", "title": "Duplicates: 1503 vs 1500",
     "blocks": [
         {"header": "The story",
          "lines": [
              "The raw file has 1503 rows but only 1500 patients.",
              "Three records were entered twice - exact duplicates.",
              "Duplicates inflate the sample and distort estimates."]},
         {"header": "Detect and remove",
          "lines": [
              "sum(duplicated(raw)) shows how many full duplicates.",
              "distinct(raw) keeps one copy of each unique row.",
              "n_distinct(raw$patient_id) should then equal nrow(raw)."]},
         {"callout": "tip", "header": "Always re-check",
          "lines": ["Confirm row count is 1500 after distinct()."]},
     ],
     "notes": "Key point: duplicates are a false sample-size increase and must go before any counting.\nMisconception: distinct() drops rows you wanted - it only removes exact full-row copies here.\nClinical interpretation: a duplicated patient double-counts their outcome, biasing prevalence.\nAsk: why check n_distinct(patient_id) as well as nrow? Expected: to catch same-ID-different-row data-entry errors distinct() would keep.\nDemo tip: print nrow before and after so the 1503 to 1500 drop is visible."},

    # 7. Inconsistent categories - sex
    {"type": "content", "title": "Inconsistent Categories: the 8 Spellings of Sex",
     "blocks": [
         {"header": "The mess",
          "lines": [
              "Female, F, female, f and Male, M, male, m.",
              "Stray spaces make even more variants.",
              "Eight labels for two real groups."]},
         {"header": "The fix",
          "lines": [
              "str_trim() removes leading and trailing spaces.",
              "str_to_lower() makes case irrelevant.",
              "case_when() maps every variant to Female or Male."]},
         {"callout": "interpretation", "header": "Clinical sense",
          "lines": ["Anything unexpected becomes NA, not a guess."]},
     ],
     "notes": "Key point: normalise case and spacing first, then map a small set of known values.\nMisconception: you must list every variant by hand - lowercasing collapses half of them instantly.\nClinical interpretation: never invent a sex for an unreadable entry; NA is honest.\nAsk: why send unknowns to NA rather than to the larger group? Expected: guessing introduces bias; NA is transparent.\nDemo tip: show table(sex) before and after the case_when."},

    # 8. Standardising binaries (code slide)
    {"type": "code", "title": "Standardising Binaries with a Helper",
     "intro": "One reusable function fixes every Yes/No variable.",
     "code": "to_yesno <- function(x) {\n  x <- str_to_lower(str_trim(as.character(x)))\n  case_when(\n    x %in% c(\"yes\",\"y\",\"1\",\"true\") ~ \"Yes\",\n    x %in% c(\"no\",\"n\",\"0\",\"false\") ~ \"No\",\n    TRUE ~ NA_character_)\n}\nraw <- raw |> mutate(across(\n  c(diabetes, family_history_htn, health_insurance,\n    htn_diagnosed, treatment_uptake), to_yesno))",
     "note": "Write the rule once, apply it to many columns with across().",
     "notes": "Key point: a helper function makes the same cleaning rule consistent and auditable across columns.\nMisconception: you should repeat case_when for each variable - across() avoids copy-paste errors.\nClinical interpretation: treatment_uptake must be a clean Yes/No before it can be an outcome.\nAsk: why coerce as.character first? Expected: a column read as numeric 0/1 would not match the text patterns otherwise.\nDemo tip: call to_yesno(c(\"Y\",\" no \",1)) on its own to show it working."},

    # 9. Data validation - impossible values
    {"type": "content", "title": "Validation: Impossible Physiological Values",
     "blocks": [
         {"header": "Spot the impossible",
          "lines": [
              "age 200 and age 0; sbp 0 and sbp 700.",
              "weight 7 kg; height 17 cm.",
              "These are data-entry errors, not real patients."]},
         {"header": "Fix with plausible ranges",
          "lines": [
              "if_else(age >= 18 & age <= 110, age, NA_real_)",
              "Outside the range becomes NA, not a deletion of the row."]},
         {"callout": "interpretation", "header": "Choosing ranges",
          "lines": ["Set limits from clinical knowledge and your study's population, not from the data alone."]},
     ],
     "notes": "Key point: encode clinical plausibility as explicit ranges and convert violations to NA.\nMisconception: outliers and impossible values are the same - a true SBP of 185 is plausible and must stay.\nClinical interpretation: ranges should reflect the population; an adult study justifies age >= 18.\nAsk: should we delete the whole row for one bad height? Expected: no - blank only that cell so the other valid fields survive.\nDemo tip: show summary() before and after; the min and max snap into a sensible range."},

    # 10. Recode / derive (two_column)
    {"type": "two_column", "title": "Recoding and Deriving Variables",
     "left": {"header": "Recompute BMI from source",
              "lines": [
                  "bmi = weight_kg / (height_cm/100)^2",
                  "Derive after cleaning height and weight.",
                  "Never trust a pre-computed BMI blindly."],
              "bullets": True},
     "right": {"header": "Create clinical categories",
               "lines": [
                   "bmi_cat with cut(): Underweight to Obese.",
                   "bp_category with case_when().",
                   "Normal, Elevated, Hypertension."],
               "bullets": True},
     "notes": "Key point: derive variables from cleaned inputs so the derived value inherits the cleaning.\nMisconception: recomputing BMI is redundant - the supplied column may be stale or wrong.\nClinical interpretation: bp_category uses guideline cut-offs (>=140/90 hypertension, >=130/80 elevated).\nAsk: why recompute BMI instead of keeping the file's column? Expected: it guarantees consistency with the validated height and weight.\nDemo tip: show one row where the supplied BMI disagrees with the recomputed value."},

    # 11. Recode / derive (code slide)
    {"type": "code", "title": "Demo: Recompute BMI and Categorise",
     "code": "raw <- raw |> mutate(\n  bmi = round(weight_kg / (height_cm/100)^2, 1),\n  bmi_cat = cut(bmi,\n    breaks = c(-Inf, 18.5, 25, 30, Inf),\n    labels = c(\"Underweight\",\"Normal\",\n               \"Overweight\",\"Obese\")),\n  bp_category = case_when(\n    is.na(sbp_mmhg) | is.na(dbp_mmhg) ~ NA_character_,\n    sbp_mmhg >= 140 | dbp_mmhg >= 90 ~ \"Hypertension\",\n    sbp_mmhg >= 130 | dbp_mmhg >= 80 ~ \"Elevated\",\n    TRUE ~ \"Normal\"))",
     "note": "Handle NA explicitly first so missing BP never reads as Normal.",
     "notes": "Key point: order case_when from most specific to most general, and trap NA before the TRUE branch.\nMisconception: NA falls through to the last TRUE branch - so a missing BP would be wrongly labelled Normal.\nClinical interpretation: misclassifying missing BP as Normal would understate hypertension burden.\nAsk: what would happen if the is.na line were removed? Expected: patients with missing BP get labelled Normal - a silent error.\nDemo tip: deliberately drop the is.na line, run table(bp_category), then restore it."},

    # 12. Dates (code slide)
    {"type": "code", "title": "Demo: Parsing Mixed Date Formats",
     "intro": "enroll_date arrives in several different formats.",
     "code": "library(lubridate)\nraw <- raw |> mutate(\n  enroll_date = parse_date_time(\n    enroll_date,\n    orders = c(\"ymd\",\"dmy\",\"d-b-Y\")) |>\n  as_date())\nsum(is.na(raw$enroll_date))",
     "output": "[1] 0",
     "note": "orders lists the formats to try, in priority order.",
     "notes": "Key point: lubridate's parse_date_time tries each format in turn, taming mixed entry styles.\nMisconception: dates are just text - stored as text they cannot be sorted or differenced.\nClinical interpretation: a real Date lets you compute follow-up time and check enrolment windows.\nAsk: why check sum(is.na(enroll_date)) afterwards? Expected: a spike means a format we did not list and must add.\nDemo tip: feed parse_date_time a few sample strings to show each order matching."},

    # 13. Factors and labels
    {"type": "content", "title": "Factors and Reference Levels",
     "blocks": [
         {"header": "Factors give categories structure",
          "lines": [
              "factor() stores categories with defined levels.",
              "Ordered factors keep ordinal meaning (education, activity).",
              "Levels control the order in tables and plots."]},
         {"header": "Set the reference level deliberately",
          "lines": [
              "For binary outcomes, list 'No' first.",
              "factor(treatment_uptake, levels = c(\"No\",\"Yes\"))",
              "The first level is the comparison baseline in models."]},
         {"callout": "interpretation", "header": "Why 'No' first",
          "lines": ["Odds ratios then read as the odds of Yes versus No - the natural clinical direction."]},
     ],
     "notes": "Key point: the first factor level is the reference, and it sets how every odds ratio is interpreted.\nMisconception: level order is cosmetic - it silently flips the direction of model estimates.\nClinical interpretation: with 'No' as reference, OR > 1 means higher odds of the outcome, as clinicians expect.\nAsk: what does an OR of 3.56 for diabetes mean with 'No' as reference? Expected: diabetics have 3.56 times the odds of treatment uptake versus non-diabetics.\nDemo tip: refit with levels reversed to show the OR invert to 1/3.56."},

    # 14. Missing-data audit (code slide)
    {"type": "code", "title": "Demo: Final Missing-Data Audit",
     "code": "colSums(is.na(analysis_data)) |>\n  sort(decreasing = TRUE) |>\n  head(12)",
     "output": "adherence        411\nbp_controlled    411\nbmi               18\nsbp_mmhg          12\nage                9",
     "note": "adherence and bp_controlled are NA by design for untreated patients.",
     "notes": "Key point: audit missingness per column and distinguish structural NA from data problems.\nMisconception: all NA is bad - adherence is undefined for someone not on treatment, so its NA is expected.\nClinical interpretation: only patients on treatment can have an adherence or BP-control status.\nAsk: should we impute adherence for untreated patients? Expected: no - it is structurally missing, not unknown.\nDemo tip: cross-tabulate adherence missingness against treatment_uptake to show the by-design pattern."},

    # 15. Saving the clean data
    {"type": "content", "title": "Saving the Clean Data: the Contract",
     "blocks": [
         {"header": "Save once, reuse all week",
          "lines": [
              "saveRDS keeps factor types and levels intact.",
              "write_csv gives a human-readable backup.",
              "Days 3, 4 and 5 all start from this one file."]},
         {"header": "The commands",
          "lines": [
              "saveRDS(analysis_data, \"Data/analysis_data.rds\")",
              "write_csv(analysis_data, \"Data/analysis_data.csv\")"]},
         {"callout": "tip", "header": "Reload later",
          "lines": ["analysis_data <- readRDS(\"Data/analysis_data.rds\")"]},
     ],
     "notes": "Key point: the saved .rds is the single source of truth for the rest of the course.\nMisconception: CSV preserves everything - it loses factor levels and ordering, so .rds is the analysis file.\nClinical interpretation: a fixed clean dataset makes every later result reproducible and auditable.\nAsk: why prefer .rds over .csv for the analysis? Expected: it restores factors and ordered levels exactly, no re-cleaning needed.\nDemo tip: save, clear the workspace, then readRDS to prove the factors survive."},

    # 16. Common mistakes / debugging
    {"type": "content", "title": "Common Mistakes and Debugging",
     "blocks": [
         {"header": "Watch for these",
          "lines": [
              "Forgetting na= so 999 enters as a real number.",
              "Wrong factor level order flipping every odds ratio.",
              "Letting NA fall through case_when to the wrong group."]},
         {"callout": "mistake", "header": "NA propagation",
          "lines": ["Any arithmetic with NA returns NA; check is.na before computing."]},
         {"callout": "tip", "header": "Debug habit",
          "lines": ["After each step run summary() or table(..., useNA = \"ifany\")."]},
     ],
     "notes": "Key point: most cleaning bugs are silent; build the habit of inspecting after every step.\nMisconception: no error message means the step worked - wrong results often run without complaint.\nClinical interpretation: a silently mis-coded outcome can change the entire study conclusion.\nAsk: how would you catch a forgotten na= argument? Expected: an implausible max in summary(), e.g. an SBP of 999.\nDemo tip: trigger each mistake live, then show the diagnostic that catches it."},

    # 17. Exercise
    {"type": "bullets", "title": "Day 2 Exercise: Clean the Simulated Dataset",
     "intro": "Work in Practicals/day2_exercise.R and mirror today's pipeline.",
     "items": [
         "Import the raw CSV with the correct na= sentinels.",
         "Remove duplicate records with distinct(); confirm 1500 rows.",
         "Recode sex to Female/Male; standardise the Yes/No binaries.",
         "Apply plausible ranges; set impossible values to NA.",
         "Recompute BMI; derive bmi_cat and bp_category.",
         "Parse enroll_date; set factors and reference levels.",
         "Run the final missing-data audit and explain each NA.",
         "Save the result to Data/analysis_data.rds."],
     "notes": "Key point: the exercise reproduces the full contract so each participant ends with an identical clean file.\nMisconception: skipping a step is fine if numbers 'look ok' - later days will fail to load a wrong-typed file.\nClinical interpretation: the expected end state is the validated dataset used for all later analyses.\nAsk: how will you know your file is correct? Expected: 1500 rows, clean factors, and the audit matching the demo counts.\nDemo tip: have them readRDS their own file and glimpse() it to self-check against yours."},

    # 18. Recap / bridge
    {"type": "content", "title": "Recap and Bridge to Day 3",
     "blocks": [
         {"header": "What we achieved today",
          "lines": [
              "Imported, de-duplicated and standardised the raw data.",
              "Validated values, derived variables, parsed dates.",
              "Set factors and saved analysis_data.rds."]},
         {"header": "Tomorrow: Day 3",
          "lines": [
              "Explore and describe the clean data.",
              "Summary tables, distributions and first plots.",
              "We start from analysis_data.rds - no re-cleaning."]},
         {"callout": "note", "header": "Remember",
          "lines": ["Clean data clear impact - everything downstream rests on today."]},
     ],
     "notes": "Key point: the clean, saved dataset is the bridge into descriptive analysis on Day 3.\nMisconception: cleaning is finished forever - revisit it if Day 3 plots reveal new anomalies.\nClinical interpretation: trustworthy description requires the validated data we built today.\nAsk: what is the first thing you do on Day 3? Expected: readRDS the analysis file and glimpse it, not re-import the raw CSV.\nDemo tip: open tomorrow's script header to show it begins with readRDS."},

]
