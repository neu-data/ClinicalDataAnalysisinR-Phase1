SLIDES_DAY3 = [

    # ------------------------------------------------------------------ 1
    {"type": "divider", "title": "Day 3: Descriptive Statistics, Tables & Figures",
     "plan_title": "Plan",
     "agenda": [
         "Central tendency and spread",
         "Frequency and cross-tabulations",
         "Publication Table 1 with gtsummary",
         "Choosing and building figures",
         "Exporting reproducible outputs",
     ],
     "notes": "Welcome to Day 3. Today we move from cleaning data to describing it.\nThe goal is simple: tell the reader who is in our study and what they look like, using numbers and pictures a journal will accept.\nKey teaching point: descriptive statistics come BEFORE any model. You cannot interpret an odds ratio if you do not first know the sample.\nClinical framing: everything we build today feeds the Table 1 and the figures of the hypertension treatment-uptake manuscript.\nAsk the audience: what is the first table you see in almost every clinical paper? Expected answer: baseline characteristics, Table 1. That is our destination."},

    # ------------------------------------------------------------------ 2
    {"type": "bullets", "title": "What we will achieve today",
     "intro": "By the end of this session you will be able to:",
     "items": [
         "Summarise a numeric variable with mean, median, SD and IQR",
         "Avoid the number-one beginner trap that returns NA",
         "Build frequency tables and cross-tabulations",
         "Read row versus column percentages correctly",
         "Produce a manuscript-ready Table 1",
         "Choose the right chart for each variable type",
         "Save figures at 300 dpi for publication",
     ],
     "notes": "This slide sets expectations. Read each outcome as a promise.\nKey teaching point: these are practical, hands-on skills, not theory. Everyone will produce a Table 1 in the exercise.\nCommon misconception: that statistics requires heavy maths. Today is about choosing and reporting the right summary, which is judgement, not algebra.\nDemonstration tip: keep the demo script open beside the slides so learners see the slide point then the live code.\nSuggested question: which of these do you already do in your current work? Expected: most report means and counts but few use a reproducible Table 1 tool."},

    # ------------------------------------------------------------------ 3
    {"type": "code", "title": "Bridge: reload the clean data",
     "intro": "Always start from the saved clean file, never re-clean by hand.",
     "code": "library(tidyverse)\nlibrary(gtsummary)\n\nanalysis_data <- readRDS(\"Data/analysis_data.rds\")\n\nglimpse(analysis_data)\nnrow(analysis_data)",
     "output": "Rows: 1,500\nColumns: 36\n[1] 1500",
     "note": "Reloading the Day 2 output guarantees Days 3, 4 and 5 all use identical data.",
     "notes": "This is a short bridge from Day 2. We do not repeat cleaning; we read the analysis-ready file.\nKey teaching point: readRDS restores the exact R object, including factor levels and types, which a CSV would lose.\nCommon mistake: re-importing the raw 1,503-row file and re-cleaning by hand each session, which silently introduces differences.\nClinical interpretation: reproducibility means a co-author or reviewer can rerun and get the same Table 1.\nDemonstration tip: run glimpse and point out that types are already correct, so we can go straight to describing."},

    # ------------------------------------------------------------------ 4
    {"type": "two_column", "title": "Central tendency: mean vs median",
     "left": {"header": "Mean",
              "lines": [
                  "The arithmetic average",
                  "Uses every value",
                  "Pulled by extreme values",
                  "Best for symmetric data",
              ], "bullets": True},
     "right": {"header": "Median",
               "lines": [
                   "The middle value",
                   "Half above, half below",
                   "Robust to outliers",
                   "Best for skewed data",
               ], "bullets": True},
     "notes": "Central tendency answers: where is the middle of the data?\nKey teaching point: the mean and median agree when data are symmetric and diverge when data are skewed.\nClinical interpretation: skewed clinical variables like distance to facility, fasting glucose, and triglycerides have a long right tail; a few very high values drag the mean up, so the median is the fairer summary.\nCommon misconception: that the mean is always the right summary. It is not.\nSuggested question: if one patient lives 200 km away and the rest within 5 km, which summary describes a typical patient? Expected answer: the median."},

    # ------------------------------------------------------------------ 5
    {"type": "content", "title": "When the median is the honest summary",
     "blocks": [
         {"header": "Rule of thumb",
          "lines": [
              "Mean close to median means roughly symmetric: report mean (SD)",
              "Mean well above median means right-skewed: report median (IQR)",
          ]},
         {"header": "Typical right-skewed clinical variables",
          "lines": [
              "Distance to facility, fasting glucose, triglycerides",
              "Length of stay, cost, biomarker concentrations",
          ]},
         {"callout": "interpretation", "header": "Why it matters",
          "lines": [
              "For BP and BMI the mean often sits above the median.",
              "A few high values inflate the mean, so median (IQR) is safer.",
          ]},
     ],
     "notes": "This slide turns the mean-versus-median choice into a decision rule learners can apply on the spot.\nKey teaching point: compare mean and median first, then decide which to report. Do not default blindly to the mean.\nClinical interpretation: in our hypertension cohort, systolic BP and BMI are mildly right-skewed; reporting the median with IQR avoids overstating the typical value.\nCommon mistake: reporting mean (SD) for a clearly skewed cost or glucose variable, which misleads readers.\nSuggested question: how would you check skew quickly? Expected answer: compare mean and median, or look at a histogram, which we do later today."},

    # ------------------------------------------------------------------ 6
    {"type": "content", "title": "Measures of spread",
     "blocks": [
         {"header": "How scattered are the values?",
          "lines": [
              "Standard deviation (SD): typical distance from the mean",
              "IQR: the range of the middle 50 percent (Q3 minus Q1)",
              "Range: minimum to maximum, sensitive to outliers",
              "Quantiles: cut points such as the five-number summary",
          ]},
         {"callout": "tip", "header": "Pair the spread with the centre",
          "lines": [
              "Report SD with the mean; report IQR with the median.",
          ]},
     ],
     "notes": "Spread tells the reader how much patients differ from one another, not just the average.\nKey teaching point: always pair a centre with a matching spread. Mean goes with SD, median goes with IQR.\nClinical interpretation: two groups can share a mean SBP but differ greatly in spread; the SD or IQR reveals that variability.\nCommon misconception: that the range is a good summary of spread. It is driven entirely by the two most extreme patients, so the IQR is usually preferable.\nSuggested question: what does an IQR of 20 mmHg mean for SBP? Expected answer: the middle half of patients span a 20 mmHg window."},

    # ------------------------------------------------------------------ 7
    {"type": "content", "title": "The number-one beginner trap: na.rm",
     "blocks": [
         {"header": "What happens",
          "lines": [
              "If a column has ANY missing value, mean() and sd() return NA.",
              "R refuses to guess; it tells you the answer is unknown.",
          ]},
         {"header": "The fix",
          "lines": [
              "Add na.rm = TRUE to ignore the missing values.",
              "mean(x, na.rm = TRUE) instead of mean(x).",
          ]},
         {"callout": "mistake", "header": "Most common cause of a surprise NA",
          "lines": [
              "A summary returns NA -> a hidden missing value is present.",
              "First thing to check: did you set na.rm = TRUE?",
          ]},
     ],
     "notes": "This is the single most common frustration for new R users, so we give it its own slide.\nKey teaching point: NA is contagious. One missing value makes the whole summary NA unless you tell R to ignore missings.\nCommon mistake: assuming the data are broken when in fact na.rm was simply omitted.\nClinical interpretation: na.rm = TRUE performs a complete-case summary for that variable; always note how many values were missing so readers know the denominator.\nDemonstration tip: in the live demo, run mean(sbp) first to show the NA, then add na.rm = TRUE to show the fix. The before-and-after lands the point."},

    # ------------------------------------------------------------------ 8
    {"type": "code", "title": "Demo: central tendency and spread",
     "intro": "Show the trap first, then the fix, on systolic blood pressure.",
     "code": "mean(analysis_data$sbp_mmhg)\nmean(analysis_data$sbp_mmhg, na.rm = TRUE)\n\nmedian(analysis_data$age, na.rm = TRUE)\nsd(analysis_data$age, na.rm = TRUE)\nIQR(analysis_data$age, na.rm = TRUE)\nquantile(analysis_data$age,\n         probs = c(0, .25, .5, .75, 1), na.rm = TRUE)",
     "output": "[1] NA\n[1] 138.6\n[1] 52\n[1] 14.8\n[1] 23\n  0%  25%  50%  75% 100%\n  18   42   52   65   89",
     "note": "The first line is NA on purpose; na.rm = TRUE produces the real mean.",
     "notes": "This mirrors section 2 of the demo script.\nKey teaching point: the first NA is deliberate. Pause on it before fixing it.\nClinical interpretation: median age 52 with IQR 23 years describes a middle-aged primary-care population; quantiles give the five-number summary in one call.\nCommon mistake: typing probs without na.rm and getting NA again across the board.\nDemonstration tip: ask the room to predict the first line before you run it. Expected answer: NA, because sbp has missing values."},

    # ------------------------------------------------------------------ 9
    {"type": "code", "title": "Demo: summarise many variables at once",
     "intro": "summary() for a fast look, then a tidy grouped table with across().",
     "code": "analysis_data |>\n  group_by(treatment_uptake) |>\n  summarise(n = n(),\n    across(c(age, bmi, sbp_mmhg, dbp_mmhg),\n      list(mean = ~mean(.x, na.rm = TRUE),\n           sd   = ~sd(.x,   na.rm = TRUE)),\n      .names = \"{.col}_{.fn}\"),\n    .groups = \"drop\")",
     "output": "treatment_uptake     n age_mean age_sd sbp_mmhg_mean\n No                 ...     50.1   14.6         136.2\n Yes                ...     54.7   14.1         141.8",
     "note": "across() applies the same functions to many columns: no copy-paste, no typos.",
     "notes": "This mirrors section 3 of the demo. summary() is the quick eyeball; the grouped across() table is the reusable version.\nKey teaching point: across() applies one set of functions to many columns at once, and .names makes self-documenting columns like age_mean.\nClinical interpretation: treated patients here have higher mean age and SBP, an early hint that older, sicker patients are the ones being started on treatment. We confirm this formally in Table 1.\nCommon mistake: forgetting .groups = drop and being surprised the result stays grouped.\nSuggested question: why group by treatment_uptake? Expected answer: it is our primary outcome, so we compare the two groups."},

    # ------------------------------------------------------------------ 10
    {"type": "content", "title": "Frequency tables for categorical variables",
     "blocks": [
         {"header": "Three tools, know all three",
          "lines": [
              "table() gives raw counts",
              "prop.table() converts counts to proportions",
              "count() returns a tidy data frame you can pipe onward",
          ]},
         {"callout": "warning", "header": "table() hides missing values",
          "lines": [
              "By default table() silently drops NAs, so percentages can mislead.",
              "Use table(x, useNA = \"ifany\") to make missing values visible.",
          ]},
     ],
     "notes": "Categorical variables like sex, education and bp_category are described by counts and percentages.\nKey teaching point: counts answer how many, proportions answer what share. Report both.\nCommon mistake: table() dropping NAs silently, so the percentages are computed on a smaller denominator than the reader assumes. useNA = ifany fixes this.\nClinical interpretation: a percentage is only meaningful if you know the denominator; always state n.\nSuggested question: if 40 of 50 non-missing patients are female but 10 sex values are missing, what is the female percentage? Expected answer: it depends on whether you count the missings, which is why we make them visible."},

    # ------------------------------------------------------------------ 11
    {"type": "code", "title": "Demo: frequency tables",
     "intro": "Counts, percentages, and the tidy equivalent.",
     "code": "table(analysis_data$sex)\nround(100 * prop.table(table(analysis_data$sex)), 1)\n\ntable(analysis_data$education, useNA = \"ifany\")\n\nanalysis_data |>\n  count(bp_category) |>\n  mutate(percent = round(100 * n / sum(n), 1))",
     "output": "Female   Male\n   810    690\n\nFemale   Male\n  54.0   46.0\n\n# bp_category percentages printed as a tidy tibble",
     "note": "count() plus mutate() gives a tidy table ready for a report or a plot.",
     "notes": "This mirrors section 4 of the demo.\nKey teaching point: prop.table on a table gives proportions; multiply by 100 and round for readable percentages.\nClinical interpretation: a 54 to 46 percent female-to-male split is typical of a primary-care attendance sample.\nCommon mistake: forgetting useNA = ifany on education and under-reporting missingness.\nDemonstration tip: show that count() output is a tibble you can pipe into ggplot, unlike base table() output."},

    # ------------------------------------------------------------------ 12
    {"type": "content", "title": "Cross-tabulations: outcome versus predictor",
     "blocks": [
         {"header": "A two-way table",
          "lines": [
              "table(treatment_uptake, diabetes) counts every combination",
              "Rows are treatment uptake, columns are diabetes status",
          ]},
         {"header": "The margin argument chooses the percentage",
          "lines": [
              "margin = 1 gives ROW percentages (each row sums to 100)",
              "margin = 2 gives COLUMN percentages (each column sums to 100)",
              "no margin gives percentage of the grand total",
          ]},
         {"callout": "interpretation", "header": "Match the percentage to the question",
          "lines": [
              "Share of diabetics on treatment -> column percent.",
              "Share of treated who are diabetic -> row percent.",
          ]},
     ],
     "notes": "Cross-tabulation is how we relate the outcome to a categorical predictor before any modelling.\nKey teaching point: the margin argument decides the denominator, and the denominator changes the meaning entirely.\nClinical interpretation: choose the percentage that answers your clinical question. Reporting the wrong margin is one of the most common errors in manuscripts.\nCommon mistake: reading a row percentage as if it were a column percentage.\nSuggested question: what proportion of diabetics are on treatment uses which margin? Expected answer: column percent, margin = 2."},

    # ------------------------------------------------------------------ 13
    {"type": "code", "title": "Demo: cross-tabulation with percentages",
     "intro": "The same counts, two ways, with interpretation.",
     "code": "xtab <- table(analysis_data$treatment_uptake,\n              analysis_data$diabetes)\nxtab\n\nround(100 * prop.table(xtab, margin = 1), 1)\nround(100 * prop.table(xtab, margin = 2), 1)",
     "output": "       No  Yes\n  No  610  120\n  Yes 430  340\n\n# margin=1 row %: of treated, share diabetic\n# margin=2 col %: of diabetics, share treated",
     "note": "Same table, two stories: pick the margin that answers your question.",
     "notes": "This mirrors section 5 of the demo.\nKey teaching point: store the table in an object once, then take proportions two ways from it.\nClinical interpretation: with margin = 2 you can say what share of diabetics are on treatment, supporting the later finding that diabetes is strongly associated with uptake, adjusted OR about 3.56.\nCommon mistake: recomputing the table twice instead of reusing xtab.\nSuggested question: which margin supports the sentence among diabetics, X percent received treatment? Expected answer: column percent, margin = 2."},

    # ------------------------------------------------------------------ 14
    {"type": "content", "title": "What is a Table 1?",
     "blocks": [
         {"header": "The opening table of almost every clinical paper",
          "lines": [
              "Baseline characteristics of the study sample",
              "Usually split into columns by the main exposure or outcome",
              "Numerics shown as mean (SD) or median (IQR)",
              "Categoricals shown as n (percent)",
          ]},
         {"callout": "note", "header": "Why reviewers expect it",
          "lines": [
              "It lets the reader judge who the study describes.",
              "It shows whether the comparison groups are balanced.",
          ]},
     ],
     "notes": "Table 1 is the destination for everything we learned today; it bundles central tendency, spread, and frequencies into one publishable object.\nKey teaching point: Table 1 describes the sample; it is descriptive, not a causal test, even when it carries p-values.\nClinical interpretation: splitting by treatment_uptake lets reviewers see how treated and untreated patients differ at baseline.\nCommon misconception: that a small p-value in Table 1 proves an effect. It only flags a baseline difference.\nSuggested question: why do we report median (IQR) for some rows and mean (SD) for others? Expected answer: skewed variables get the median."},

    # ------------------------------------------------------------------ 15
    {"type": "code", "title": "Demo: build Table 1 with gtsummary",
     "intro": "tbl_summary chooses sensible summaries automatically.",
     "code": "analysis_data |>\n  select(age, sex, residence, education, bmi,\n         diabetes, sbp_mmhg, bp_category,\n         treatment_uptake) |>\n  tbl_summary(by = treatment_uptake,\n              missing_text = \"(Missing)\") |>\n  add_p() |>\n  add_overall() |>\n  bold_labels()",
     "output": "Characteristic   Overall   No   Yes   p-value\nAge (years)      52 ...    ...  ...   <0.001\nDiabetes, n (%)  ...       ...  ...    0.002\n... one row per selected variable ...",
     "note": "add_p() adds p-values; add_overall() adds a total column.",
     "notes": "This mirrors section 6 of the demo and is the core deliverable of the day.\nKey teaching point: tbl_summary picks mean (SD) or median (IQR) for numerics and n (percent) for categoricals automatically, and labels missing data for you.\nClinical interpretation: the p-value column flags baseline imbalance between treated and untreated patients; significant age and diabetes differences foreshadow the regression results.\nCommon mistake: forgetting library(gtsummary), or expecting tbl_summary to fit a model. It only describes.\nDemonstration tip: show the table rendering in the Viewer, then mention as_flex_table for Word export."},

    # ------------------------------------------------------------------ 16
    {"type": "content", "title": "Choosing the right chart",
     "blocks": [
         {"header": "Let the variable type decide the chart",
          "lines": [
              "One continuous variable -> histogram (shape and skew)",
              "Continuous by a group -> boxplot (compare distributions)",
              "One categorical variable -> bar chart (counts)",
              "Two continuous variables -> scatterplot (relationship)",
          ]},
         {"callout": "tip", "header": "Every figure needs",
          "lines": [
              "A clear title and axis labels WITH units.",
              "A clean theme; we use theme_minimal with a teal accent.",
          ]},
     ],
     "notes": "Before drawing anything, match the chart to the variable type. This single habit prevents most bad figures.\nKey teaching point: histograms reveal shape and skew; boxplots compare groups; bar charts count categories; scatterplots show relationships.\nCommon mistake: using a bar chart of group means instead of a boxplot, which hides the spread and the outliers.\nClinical interpretation: a histogram of SBP tells you immediately whether to summarise it with a mean or a median.\nSuggested question: which chart compares BMI across blood-pressure categories? Expected answer: a boxplot."},

    # ------------------------------------------------------------------ 17
    {"type": "image", "title": "Histogram: age distribution",
     "image": "day3_hist_age.png", "aspect": 0.75,
     "side_header": "How to read it",
     "side_notes": [
         "Each bar counts patients in a 5-year band",
         "The peak shows the most common age range",
         "A roughly symmetric shape supports mean (SD)",
         "Look for a long tail that would signal skew",
     ],
     "notes": "This is the real figure produced by ggsave in the demo, section 7a.\nKey teaching point: a histogram answers two questions at once: where is the centre, and is the distribution skewed?\nClinical interpretation: the sample concentrates in middle age, consistent with a hypertension primary-care population; the near-symmetry justifies reporting mean age.\nCommon mistake: choosing a binwidth so wide the shape disappears or so narrow it looks noisy. Here binwidth is 5 years.\nSuggested question: from this shape, mean or median for age? Expected answer: either is fine because it is roughly symmetric."},

    # ------------------------------------------------------------------ 18
    {"type": "image", "title": "Histogram: systolic blood pressure",
     "image": "day3_hist_sbp.png", "aspect": 0.75,
     "side_header": "How to read it",
     "side_notes": [
         "The overlaid curve is a smoothed density",
         "A tail to the right indicates right-skew",
         "When skewed, prefer median (IQR) over mean (SD)",
         "The bulk sits in the hypertensive range",
     ],
     "notes": "Real figure from demo section 7b, with a density curve overlaid on the histogram.\nKey teaching point: the density overlay smooths the bars so the shape, and any right-skew, is easier to see.\nClinical interpretation: SBP shows a right tail of high readings, so median (IQR) is the safer summary; this is the visual proof behind the earlier rule of thumb.\nCommon mistake: forgetting aes(y = after_stat(density)) so the histogram and density are on different scales and the curve looks flat.\nSuggested question: what does the right tail mean clinically? Expected answer: a subgroup of patients with markedly elevated blood pressure."},

    # ------------------------------------------------------------------ 19
    {"type": "image", "title": "Bar chart: educational attainment",
     "image": "day3_bar_education.png", "aspect": 0.75,
     "side_header": "How to read it",
     "side_notes": [
         "Bar height is the number of patients per level",
         "geom_bar counts categories for you",
         "Compare bar heights, not areas",
         "A baseline at zero keeps comparisons honest",
     ],
     "notes": "Real figure from demo section 7c.\nKey teaching point: geom_bar counts the categories itself, so you do not pre-summarise the data.\nClinical interpretation: the education distribution matters because higher education shows a trend toward greater treatment uptake, adjusted OR about 1.96; the bar chart shows how many patients sit in each level.\nCommon mistake: pre-aggregating then using geom_bar, which double-counts; use geom_col only when you already have counts.\nSuggested question: why must the y-axis start at zero? Expected answer: a truncated axis exaggerates differences between bars."},

    # ------------------------------------------------------------------ 20
    {"type": "image", "title": "Boxplot: SBP by treatment uptake",
     "image": "day3_box_sbp_by_treatment.png", "aspect": 0.75,
     "side_header": "How to read it",
     "side_notes": [
         "The box spans the IQR; the line is the median",
         "Whiskers reach most of the data; dots are outliers",
         "Compare the two medians side by side",
         "Higher SBP among treated hints at sicker patients",
     ],
     "notes": "Real figure from demo section 7d.\nKey teaching point: a boxplot compresses a whole distribution into five numbers per group, ideal for comparing treated and untreated patients.\nClinical interpretation: if the treated group sits higher, it suggests treatment is started in patients with worse blood pressure, matching the higher mean SBP we saw in the grouped summary.\nCommon mistake: forgetting na.rm = TRUE, which makes ggplot drop rows with a warning.\nSuggested question: what do the dots beyond the whiskers represent? Expected answer: outlying patients, not errors to delete automatically."},

    # ------------------------------------------------------------------ 21
    {"type": "image", "title": "Boxplot: BMI by blood-pressure category",
     "image": "day3_box_bmi_by_bpcat.png", "aspect": 0.75,
     "side_header": "How to read it",
     "side_notes": [
         "One box per blood-pressure category",
         "A rising median across categories suggests a gradient",
         "Box width here reflects styling, not group size",
         "Outliers flag unusually high or low BMI",
     ],
     "notes": "Real figure from demo section 7e.\nKey teaching point: boxplots across an ordered categorical variable reveal a dose-response style gradient at a glance.\nClinical interpretation: if median BMI rises from normal to hypertensive categories, it is consistent with obesity as a hypertension risk factor.\nCommon mistake: reading box width as sample size; by default it is not. Use varwidth = TRUE if you want that.\nSuggested question: does this prove obesity causes hypertension? Expected answer: no, it shows association across categories, not causation."},

    # ------------------------------------------------------------------ 22
    {"type": "image", "title": "Scatterplot: SBP versus BMI",
     "image": "day3_scatter_sbp_bmi.png", "aspect": 0.75,
     "side_header": "How to read it",
     "side_notes": [
         "Each point is one patient",
         "The line is a fitted linear trend",
         "An upward slope means higher BMI tracks higher SBP",
         "Scatter around the line shows it is not deterministic",
     ],
     "notes": "Real figure from demo section 7f.\nKey teaching point: a scatterplot is the right chart for two continuous variables, and geom_smooth(method = lm) adds the trend line.\nClinical interpretation: an upward slope suggests higher BMI accompanies higher systolic BP, consistent with obesity as a risk factor. This is association, not proof of causation.\nCommon mistake: over-plotting so the cloud is solid; we use alpha = 0.3 transparency so density is visible.\nSuggested question: does a clear line mean BMI causes high BP? Expected answer: no, confounders could drive both; a model is needed."},

    # ------------------------------------------------------------------ 23
    {"type": "code", "title": "Demo: build and save a figure",
     "intro": "One ggplot, then save it at publication quality.",
     "code": "p_age <- ggplot(analysis_data, aes(x = age)) +\n  geom_histogram(binwidth = 5, fill = \"#0D7377\",\n                 colour = \"white\") +\n  labs(title = \"Age distribution\",\n       x = \"Age (years)\", y = \"Number of patients\") +\n  theme_minimal(base_size = 13)\n\nggsave(\"Resources/day3_hist_age.png\", plot = p_age,\n       width = 7, height = 5, dpi = 300)",
     "note": "dpi = 300 is the standard journals expect for raster figures.",
     "notes": "This mirrors the figure-building pattern in demo section 7.\nKey teaching point: build the plot as an object, then ggsave that object so the saved file matches what you reviewed on screen.\nClinical interpretation: 300 dpi ensures the figure stays sharp in print; axis labels carry units so the figure is self-explanatory.\nCommon mistake: relying on ggsave with no plot argument, which saves the last printed plot and can grab the wrong one.\nDemonstration tip: open the saved PNG from the Resources folder so learners see the real output file."},

    # ------------------------------------------------------------------ 24
    {"type": "content", "title": "Exporting reproducible outputs",
     "blocks": [
         {"header": "Share results outside R",
          "lines": [
              "write_csv() sends a summary table to co-authors who do not use R",
              "ggsave(..., dpi = 300) writes a publication-ready figure",
              "gtsummary exports to Word via as_flex_table and save_as_docx",
          ]},
         {"callout": "tip", "header": "Reproducible by design",
          "lines": [
              "Save outputs to a folder, not by copy-paste.",
              "Rerunning the script regenerates every table and figure.",
          ]},
     ],
     "notes": "This mirrors demo section 8 plus the gtsummary export comments.\nKey teaching point: outputs should be generated by code into a folder, never assembled by hand, so they regenerate identically every time.\nClinical interpretation: a reviewer who asks for a corrected n can be answered by rerunning one script, not re-editing a Word table cell by cell.\nCommon mistake: pasting numbers from the console into the manuscript, which breaks when the data update.\nSuggested question: where do our figures and tables land? Expected answer: the Resources folder, written by ggsave and write_csv."},

    # ------------------------------------------------------------------ 25
    {"type": "content", "title": "Day 3 Exercise: produce Table 1 for a manuscript",
     "blocks": [
         {"header": "Your tasks",
          "lines": [
              "1. readRDS the clean analysis data",
              "2. Build a Table 1 with tbl_summary(by = treatment_uptake)",
              "3. Add p-values and an overall column",
              "4. Create a histogram and a boxplot, then ggsave both at 300 dpi",
          ]},
         {"header": "Expected output",
          "lines": [
              "A baseline characteristics table split by treatment uptake",
              "Two saved PNG figures in the Resources folder",
          ]},
         {"callout": "tip", "header": "If you get stuck",
          "lines": [
              "Reuse the demo code; change only the variable names.",
          ]},
     ],
     "notes": "This is the hands-on consolidation of the whole day.\nKey teaching point: the exercise reproduces the manuscript deliverables: one Table 1 and at least two figures.\nClinical interpretation: encourage learners to write one sentence interpreting their Table 1, for example which groups differ at baseline.\nCommon mistake: forgetting na.rm or library(gtsummary); remind them before they start.\nDemonstration tip: circulate while learners work; the most common blocker is an un-loaded package or a typo in a variable name. Expected output is a rendered table plus two PNGs in Resources."},

    # ------------------------------------------------------------------ 26
    {"type": "bullets", "title": "Recap and bridge to Day 4",
     "intro": "What we locked in today, and where we go next:",
     "items": [
         "Always use na.rm = TRUE; it is the number-one trap",
         "Choose median (IQR) for skewed clinical variables",
         "Pick the prop.table margin that matches your question",
         "gtsummary turns raw data into a Table 1 in a few lines",
         "Match the chart to the variable type, and save at 300 dpi",
         "Day 4: from describing to testing, regression and odds ratios",
     ],
     "notes": "Close the loop and set up Day 4.\nKey teaching point: today was description; tomorrow is inference. Table 1 told us groups differ, but not whether differences are independent.\nClinical interpretation: Day 4 fits logistic regression for treatment uptake, where we will interpret adjusted odds ratios such as diabetes 3.56 and health insurance 2.05.\nCommon misconception: that a baseline p-value already answers the research question. It does not; adjustment is needed.\nSuggested question: why move beyond Table 1? Expected answer: to adjust for confounders and estimate independent effects, which is Day 4."},

]
