# Preface {.unnumbered}

Every clinical research project ends in numbers: a proportion of patients who were treated, a difference in mean blood pressure, an odds ratio with its confidence interval. Those numbers shape guidelines, funding decisions and, ultimately, the care that patients receive. Yet the path from a spreadsheet of raw measurements to a sentence in a manuscript is often hidden from view. It may live in a sequence of mouse clicks that nobody recorded, in a spreadsheet that was edited by hand, or in the memory of a single analyst who has since moved on. This book is about making that path visible, careful and repeatable.

*Introduction to R for Clinical Research* teaches you to analyse clinical data with R, a free programming language for statistical computing [@rcore2026]. It is written for health professionals who want to understand and carry out their own analyses, not for programmers who happen to work in health. We start from the very beginning, assuming no previous experience of programming, and finish with a complete, reproducible analysis of a realistic clinical study, from importing a messy raw data file to writing the Results section of a manuscript.

## Why R for clinical research?

There are many statistical packages on the market, and most of them can produce a t-test or a logistic regression. The case for R does not rest on any single statistical procedure. It rests on a way of working.

### The analysis as code

When you analyse data in R, you write instructions in a script: import this file, recode that variable, exclude these impossible values, fit this model. The script *is* the analysis. Anyone who has the script and the raw data can run it and obtain exactly the same tables and figures. If a reviewer asks how a variable was derived, the answer is written down. If you discover an error in the raw data six months later, you correct it and re-run the script, and every downstream number updates consistently.

This is the essence of **reproducible research**: the idea that a published result should be accompanied by the data and code needed to regenerate it [@peng2011]. Peng argued that in computational science, where results depend on long chains of data processing, reproducibility is the minimum standard against which findings can be checked, even before anyone attempts to replicate a study independently. Clinical research is now thoroughly computational. Even a modest cross-sectional survey involves dozens of decisions about missing values, outliers, categories and model specification, and each decision can change the answer.

Point-and-click software encourages us to make those decisions silently. A script makes them explicit. That is why we will insist throughout this book that you write your work in scripts rather than typing commands into the console and forgetting them.

### Transparency and trust

Clinical research is increasingly expected to be open. Journals ask for data-sharing statements, funders ask for data-management plans, and reporting guidelines ask authors to describe their statistical methods in enough detail for others to judge them. An R script is the most complete methods section you can write. It records not only *which* test was used but *how* the data were prepared for it, which is where most real errors occur.

Transparency also protects you. Writing analysis code forces you to think about each step, and reading it back later lets you, a colleague or a supervisor find mistakes before they reach print. @wilson2017 describe a set of "good enough" practices for scientific computing: keep raw data untouched, write code in scripts, give files and variables meaningful names, organise each project in its own folder, and record the steps that turn raw data into results. None of these practices requires advanced skills, and all of them are easy to follow in R. We adopt them from the first chapter.

### Free, open and widely used

R is free and open source. You can install it on your own laptop, on a hospital computer or on a university server without a licence fee, and you can keep using it when you change institutions or countries. For researchers in low- and middle-income settings, and for anyone working on a limited budget, this matters a great deal. It also means that your collaborators can run your code without buying anything.

Because R is open, thousands of statisticians and researchers have contributed *packages*: bundles of functions that extend what R can do. Many of the methods used in medical statistics were first implemented in R, and new methods often appear there before anywhere else. In this book we rely heavily on the **tidyverse**, a coherent collection of packages for importing, tidying, transforming and visualising data that share a common design and grammar [@wickham2019tidyverse]. The tidyverse makes R code read almost like a description of what you want to do, which is a great help to beginners and to anyone who must read your code later.

### An honest word about the learning curve

R asks more of you at the start than a menu-driven package. You will make typing mistakes, meet error messages and occasionally wonder why a comma matters so much. This is normal, and it passes faster than most people expect. The investment pays back quickly: once you have written a script that cleans and describes one dataset, adapting it to the next study takes minutes rather than days, and you never have to remember which menu options you chose.

::: {.callout-tip title="Good practice"}
Treat your R script as part of the study record, in the same way as the protocol and the data-management plan. Save it with the project, give it a clear name such as `02_clean_data.R`, and add short comments that explain *why* each step is done, not only *what* it does.
:::

## Who this book is for

This book is written for people who work in or around health care and who want to analyse data themselves:

- **clinicians and medical doctors** who conduct audits, quality-improvement projects or research alongside clinical work;
- **pharmacists** interested in medicines use, adherence and pharmacoepidemiology;
- **nurses and midwives** who collect and use patient data in practice and research;
- **public-health practitioners, epidemiologists and programme staff** who monitor services and evaluate interventions;
- **postgraduate and undergraduate students** in medicine, nursing, pharmacy, public health and allied disciplines who need to analyse data for a dissertation or thesis;
- **research coordinators and data managers** who prepare datasets and want to understand what happens to them next.

You do **not** need any programming background. We explain every piece of code the first time it appears, and we build up slowly from typing a calculation to fitting a multivariable model. Nor do you need advanced mathematics. Where a formula helps understanding, we show it and explain each term in words, but the emphasis is always on knowing *when* a method is appropriate, *how* to run it correctly and *what* the result means for patients.

What you do need is curiosity, your clinical reasoning and a willingness to learn from mistakes. Clinical knowledge is a genuine advantage here: you already know that a systolic blood pressure of 700 mmHg is impossible and that a 200-year-old patient is a data-entry error. Much of good data analysis is applying exactly that kind of judgement systematically.

Readers who already use another statistical package, such as SPSS or Stata, will find that the statistical content is familiar and can concentrate on the R implementation and on reproducible workflow. Readers new to statistics will find the key concepts explained from first principles, with references to standard medical statistics texts for those who want to go deeper [@altman1991; @kirkwood2003; @bland2015].

### What you will be able to do

By the end of the book you will be able to:

1. navigate R and RStudio confidently, working in scripts within an RStudio Project;
2. create and use objects, vectors and data frames, and install and load packages;
3. import clinical data from CSV and Excel files and inspect them systematically;
4. recognise common data-quality problems and identify variable types (numeric, character, factor, date);
5. clean data reproducibly: handle missing-value codes, remove duplicates, harmonise inconsistent categories and validate impossible values;
6. derive new clinical variables, such as body mass index and blood-pressure categories, and set sensible reference levels for factors;
7. compute descriptive statistics correctly, including the proper handling of missing data;
8. build a manuscript-ready "Table 1" and publication-quality figures, and export them;
9. choose an appropriate hypothesis test for a given clinical question, run it, check its assumptions and interpret p-values and confidence intervals honestly;
10. fit univariable and multivariable logistic regression models, interpret odds ratios with 95% confidence intervals and check the model;
11. report your results in the style expected by clinical journals, with a complete script that regenerates every number.

These skills are cumulative. Each chapter takes the output of the previous one as its starting point, so that by the final chapter you have performed a complete analysis of a single study.

## How this book is organised

The book has five chapters, an appendix of solutions and a bibliography. All chapters use the same case study, described later in this preface, so that the skills you learn build directly on one another.

**Chapter 1: Getting started with R and RStudio.** We install R and RStudio, tour the RStudio interface and learn why scripts and Projects are the foundation of reproducible work. We use R as a calculator, create objects and vectors, meet the main data types, and learn to install and load packages. The chapter ends by importing the raw case-study data from both a CSV file and an Excel workbook and taking a first, structured look at what they contain. By the end of Chapter 1 you will have the raw data in R and a sense that something is not quite right with it.

**Chapter 2: Understanding and cleaning clinical data.** Real clinical data are rarely clean, and analysis of dirty data produces confident but wrong answers. This chapter works through the problems deliberately planted in the raw file: missing-value codes such as `999` and `-99`, duplicate patient records, inconsistent spellings of categories, stray spaces, physiologically impossible measurements and dates recorded in several formats. We derive new variables, convert categorical variables to factors with clinically sensible reference levels, audit the remaining missing data and save a clean, analysis-ready file. Every later chapter starts from this file.

**Chapter 3: Descriptive statistics, tables and figures.** Before testing anything, we must describe the study population well. This chapter covers measures of central tendency and spread, frequency tables and cross-tabulations, and the common trap of missing values in summary functions. We build a manuscript-quality "Table 1" with the **gtsummary** package [@sjoberg2021] and produce histograms, bar charts, box plots and scatter plots with **ggplot2** [@wickham2016ggplot2], paying attention to the principles of clear graphical presentation.

**Chapter 4: Common statistical tests in medical research.** Here we turn from description to inference. We explain what a p-value is and is not [@wasserstein2016; @greenland2016], how to check distributional assumptions, and how to choose between parametric and non-parametric tests. We compare groups with t-tests, Wilcoxon tests and analysis of variance, examine associations between categorical variables with chi-square and Fisher's exact tests, and measure correlation. Each test is applied to a genuine question from the case study, with careful attention to effect sizes and confidence intervals rather than p-values alone.

**Chapter 5: Regression modelling and reporting results.** The final chapter brings everything together. We introduce logistic regression for a binary outcome, interpret odds ratios, and move from crude to adjusted models while discussing confounding and the principles of model building [@hosmer2013; @heinze2018]. We check the model for multicollinearity and assess its discrimination with the area under the ROC curve, then present the results in a publication-ready regression table and write a short Results section in clinical-manuscript style.

**Appendix: Solutions to the exercises.** Each chapter ends with a set of exercises, graded from straightforward to challenging. The appendix gives a worked solution for every exercise, with the R code, its output and a short interpretation. Use it to check your work after you have made a genuine attempt.

**Bibliography.** All the sources cited in the text are listed at the end of the book. They include standard textbooks of medical statistics, the original papers that introduced the methods we use and the references for the software packages. Each chapter also closes with a short "Further reading" section that points to the most useful of these sources and explains why.

## How to read and use this book

The chapters are designed to be read in order, because each one builds on the data and skills produced by the last. If you already know some R, you may skim Chapter 1, but please do read Chapter 2: the clean data file produced there is used everywhere else, and the decisions taken in cleaning it affect every later result.

### R code and output

R code appears in shaded blocks. The output that R prints when the code is run appears immediately below, with each line beginning with `#>`. For example:


``` r
# Mean of four systolic blood pressure readings (mmHg)
sbp <- c(120, 130, 140, 150)
mean(sbp)
```

```
#> [1] 135
```

The first line of the block, beginning with `#`, is a *comment*: R ignores everything after a `#` on a line, so comments are notes for human readers. The second line creates an object called `sbp` holding four values, and the third line calculates their mean. The line `#> [1] 135` is R's answer. The `#>` prefix is there so that you can tell code and output apart at a glance; when you run the code yourself, the output appears in the RStudio console without it. (The `[1]` simply tells you that the answer is the first element of the result; it will be explained in Chapter 1.)

All the output in this book was produced by actually running the code on the case-study data while the book was being prepared. If you run the same code on the same data, you should see the same results, apart from minor differences in formatting between versions of R and its packages.

Within the text, names of functions, variables, packages and files are written in a fixed-width font, for example `mean()`, `treatment_uptake` and `analysis_data.rds`. Function names are followed by brackets to distinguish them from other objects.

### Callout boxes

Four kinds of highlighted box appear throughout the book. Each has a particular purpose, and recognising them will help you navigate the text.

A **Clinical interpretation** box explains what a statistical result means for patients or for clinical practice:

::: {.callout-note title="Clinical interpretation"}
An odds ratio of 2.0 for diabetes would mean that, among patients diagnosed with hypertension, the odds of being on treatment are twice as high in those who also have diabetes as in those who do not, after accounting for the other variables in the model. It does not mean that diabetes doubles the *probability* of treatment, and in a cross-sectional study it does not, on its own, show cause and effect.
:::

A **Good practice** box offers a habit or technique that will make your work more reliable, efficient or readable:

::: {.callout-tip title="Good practice"}
Never edit the raw data file by hand. Keep it exactly as you received it, and make every correction in your R script, so that each change is documented and can be reviewed or reversed.
:::

A **Common mistake** box warns about an error that beginners, and sometimes experienced analysts, often make:

::: {.callout-warning title="Common mistake"}
Running `mean(x)` on a variable that contains missing values returns `NA` rather than a number. Adding `na.rm = TRUE` removes the missing values before the calculation, but you should always report how many values were missing, rather than silently dropping them.
:::

Finally, every chapter closes with a **Key points** box that summarises the essential messages:

::: {.callout-important title="Key points"}
- R scripts make an analysis transparent and reproducible.
- Every chapter uses the same case study, so skills build on one another.
- Type the code yourself, run it, and read the output carefully.
:::

### Exercises and solutions

Each chapter ends with five to eight exercises, all of which can be answered using the case-study data. They begin with short tasks that consolidate the main techniques and progress to more open questions that ask you to choose an approach and interpret the result clinically. Worked solutions are collected in the appendix. You will learn far more by attempting each exercise before looking at the solution, and by comparing your code with ours afterwards: there is usually more than one correct way to write it.

### Type, do not copy

It is tempting to copy and paste code from the book into R. We encourage you instead to **type it yourself**. Typing slows you down just enough to notice each function name, each argument and each bracket. You will make small mistakes, see the resulting error messages and learn to fix them, and that is exactly the skill you will need when analysing your own data. After a few chapters, much of the syntax will have become second nature.

When you do meet an error, read the message carefully. It usually tells you which function failed and often why. Check for unmatched brackets or quotation marks, misspelt object names (R is case-sensitive, so `Age` and `age` are different), and missing commas between arguments. Then experiment: change one thing at a time and run the code again.

## Software and set-up

### Installing R and RStudio

You need two pieces of free software. **R** is the language and the engine that performs the calculations. **RStudio** is an integrated development environment: a comfortable workspace that sits on top of R, with a script editor, a console, a view of the objects in memory, and panes for files, plots, packages and help. You install R first, then RStudio.

1. Download and install R from the Comprehensive R Archive Network (CRAN) at [https://cran.r-project.org](https://cran.r-project.org). Choose the version for your operating system (Windows, macOS or Linux) and accept the default installation options.
2. Download and install RStudio Desktop (the free edition) from [https://posit.co/download/rstudio-desktop/](https://posit.co/download/rstudio-desktop/).
3. Open RStudio. It finds R automatically, and you will rarely need to open R on its own.

Both programs are updated regularly. Any recent version of R will work with this book; if you already have an older version installed, it is worth updating before you start, because some packages require a reasonably current version of R.

### Packages used in this book

R's core installation provides a great deal of statistical functionality, but we also use a number of contributed packages:

- **tidyverse**: a collection of packages for data import, manipulation and visualisation, including **dplyr**, **tidyr**, **readr**, **forcats** and **stringr** [@wickham2019tidyverse];
- **readxl**: imports data from Excel workbooks;
- **janitor**: tidies column names and helps to find duplicates and tabulate data;
- **lubridate**: parses and manipulates dates;
- **gtsummary**: produces publication-ready summary and regression tables [@sjoberg2021];
- **broom**: converts model output into tidy data frames;
- **ggplot2**: creates graphics based on the grammar of graphics (it is installed with the tidyverse) [@wickham2016ggplot2];
- **car**: provides regression diagnostics, including variance inflation factors;
- **pROC**: computes and plots ROC curves and the area under the curve.

A package needs to be *installed* only once on each computer, which downloads it from CRAN. The following code installs everything used in the book. It requires an internet connection and may take several minutes the first time:


``` r
# Run ONCE per computer: download and install the packages used in this book
install.packages(c(
  "tidyverse", "readxl", "janitor", "lubridate",
  "gtsummary", "broom", "ggplot2", "car", "pROC"
))
```

Once installed, a package must be *loaded* with `library()` in every new R session before its functions can be used, for example `library(tidyverse)`. Confusing these two steps is one of the most common sources of early frustration: you install once, but you load every time.

::: {.callout-warning title="Common mistake"}
Do not leave `install.packages()` at the top of your analysis scripts. Reinstalling packages every time a script runs is slow, needs an internet connection and may silently change package versions in the middle of a project. Install once from the console; load with `library()` in the script.
:::

### Working in RStudio Projects

R always works relative to a folder called the *working directory*. If your code reads `"Data/analysis_data.rds"`, R looks for a `Data` folder inside the working directory. The most reliable way to manage this is an **RStudio Project**: a folder containing a small `.Rproj` file that tells RStudio "this is the root of the analysis".

To create one, choose *File > New Project*, then either *New Directory* or *Existing Directory*, and select the folder that holds (or will hold) your data and scripts. Whenever you open the project, RStudio sets the working directory to that folder automatically, so every path in your code can be *relative* to it. Your analysis will then run unchanged on a colleague's computer, on a server or on your own laptop a year later.

A simple, effective folder structure for a clinical analysis project is:

- `Data/` for raw and cleaned data files (with the raw files never edited);
- `Scripts/` for R scripts, numbered in the order they should be run;
- `Outputs/` for tables and figures produced by the scripts;
- a short `README` describing the project and how to run it.

::: {.callout-tip title="Good practice"}
Avoid `setwd("C:/Users/yourname/Documents/...")` in scripts. A hard-coded absolute path works only on one computer. Inside an RStudio Project, use relative paths such as `"Data/hypertension_phc_raw.csv"`.
:::

### The software versions used in this book

R and its packages evolve over time, and occasionally a new version changes how a function behaves or how its output is printed. The code in this book was run with the versions shown below. If your output looks slightly different from ours, compare your versions with these.


``` r
# Version of R used to produce this book
R.version.string
```

```
#> [1] "R version 4.6.1 (2026-06-24 ucrt)"
```

``` r
# Versions of the main packages used in this book
pkgs <- c("tidyverse", "readxl", "janitor", "lubridate",
          "gtsummary", "broom", "ggplot2", "car", "pROC")
data.frame(
  package = pkgs,
  version = vapply(pkgs, function(p) as.character(packageVersion(p)),
                   character(1)),
  row.names = NULL
)
```

```
#>     package  version
#> 1 tidyverse    2.0.0
#> 2    readxl    1.5.0
#> 3   janitor    2.2.1
#> 4 lubridate    1.9.5
#> 5 gtsummary    2.5.1
#> 6     broom   1.0.13
#> 7   ggplot2    4.0.3
#> 8       car    3.1.5
#> 9      pROC 1.19.0.1
```

You can run the same code on your own computer. Small differences in the final digit of a version number rarely matter; a different major version (the first number) occasionally does.

## The case study

Throughout the book we analyse one study. Working with a single, coherent dataset from start to finish has a great advantage: you see how decisions made while cleaning the data affect the descriptive tables, how the descriptive tables guide the choice of tests, and how all of these feed into the final regression model and the written report. This mirrors how real clinical research is done.

### Clinical background: hypertension and its treatment gap

Raised blood pressure is the leading modifiable risk factor for cardiovascular disease and premature death worldwide. It is a major cause of stroke, ischaemic heart disease, heart failure and chronic kidney disease. Its global burden has grown steadily, and the increase has been especially steep in low- and middle-income countries, where health systems are often organised around acute rather than chronic care [@mills2020].

A pooled analysis of population-based studies from around the world found that the number of adults aged 30 to 79 years living with hypertension roughly doubled between 1990 and 2019, to well over a billion people [@ncdrisc2021]. The same analysis documented a large and persistent *treatment gap*: a substantial proportion of people with hypertension were unaware of their condition, fewer than half were receiving treatment, and only a minority had their blood pressure controlled. The gaps were widest in parts of sub-Saharan Africa, South Asia and Oceania.

Effective, inexpensive medicines exist. The World Health Organization guideline on the pharmacological treatment of hypertension recommends starting drug treatment in adults with a confirmed diagnosis and a systolic blood pressure of 140 mmHg or more or a diastolic blood pressure of 90 mmHg or more, with treatment of people at high cardiovascular risk starting at lower thresholds [@who2021htn]. The problem in many settings is therefore not a lack of effective therapy but the failure of diagnosed patients to start and continue it. The reasons are many: cost and lack of health insurance, distance to the health facility, limited knowledge about hypertension, competing priorities and the absence of symptoms, as well as characteristics of the health services themselves.

Primary healthcare facilities are where most adults with hypertension are diagnosed and managed. Understanding which patients attending these facilities are, and are not, on treatment can help health services target education, outreach and financial protection to those who need it most. That is the question our case study addresses.

### The study

**Title.** *Determinants of hypertension treatment uptake among adults attending primary healthcare facilities.*

**Design.** A multicentre cross-sectional study of 1,500 adults attending six primary healthcare facilities. For each participant, the study recorded socio-demographic characteristics, health behaviours, anthropometric measurements, blood pressure, laboratory biomarkers, knowledge of hypertension, access to care, hypertension diagnosis and treatment.

**Research question.** Among adults who have been diagnosed with hypertension, which factors are associated with being on antihypertensive treatment?

**Primary outcome.** `treatment_uptake`: whether the participant is currently taking antihypertensive medication (Yes/No, with "No" as the reference category). It is analysed only among participants who have been diagnosed with hypertension, that is, those with `htn_diagnosed == "Yes"`. This restriction is a matter of clinical logic as much as statistics: a person cannot take up treatment for a condition that has not been diagnosed.

**Secondary outcomes.** Two further outcomes are defined only among participants who are on treatment:

- `adherence`: treatment adherence, recorded as Good or Poor;
- `bp_controlled`: whether blood pressure is controlled, defined as a systolic pressure below 140 mmHg *and* a diastolic pressure below 90 mmHg.

**Candidate determinants.** The study recorded a range of factors that might plausibly influence whether a diagnosed patient is on treatment:

- *socio-demographic*: age, sex, place of residence (urban or rural), education, occupation, marital status and health insurance;
- *behavioural*: smoking, alcohol intake and physical activity;
- *clinical*: body mass index, family history of hypertension, diabetes, number of comorbidities, systolic and diastolic blood pressure and time since diagnosis;
- *knowledge and access*: a hypertension knowledge score (0 to 20) and distance to the health facility.

In addition, eight laboratory biomarkers (lipids, fasting glucose, creatinine, sodium and potassium) are available for descriptive analysis and exercises.

::: {.callout-warning title="Common mistake"}
Because the design is cross-sectional, exposure and outcome are measured at the same time. An association between, say, health insurance and treatment uptake does not establish that insurance *causes* uptake. Throughout the book we speak of *associations* and *determinants* in this cautious sense, and we discuss confounding explicitly in Chapter 5.
:::

### The data are simulated

The dataset used in this book was **simulated for teaching**. It was generated by computer to resemble the kind of data collected in a real primary-care survey of hypertension, with realistic distributions, plausible relationships between variables and the sort of data-quality problems found in practice. It does not describe real patients, and the facility names are used purely for illustration.

This has two consequences. First, there are no confidentiality concerns, and you are free to explore, modify and share the data as you learn. Second, and more importantly, **the results in this book illustrate methods, not real clinical findings**. When we report that a particular factor is associated with treatment uptake, that statement is about the simulated data and should not be quoted as evidence about hypertension care anywhere. We shall remind you of this whenever results are interpreted.

### The variables

The data dictionary describes each of the 36 variables recorded in the study. It is provided as a CSV file so that R can read it like any other dataset. The code below reads it and prints the main columns:


``` r
# Read the data dictionary that accompanies the case-study data
dictionary <- read.csv("Data/data_dictionary.csv")

# Keep the columns that describe each variable and show them as a table
knitr::kable(
  dictionary[, c("variable", "label", "type", "units_coding", "role")],
  col.names = c("Variable", "Label", "Type", "Units / coding", "Role"),
  caption = "Variables recorded in the hypertension treatment-uptake study."
)
```



Table: Variables recorded in the hypertension treatment-uptake study.

|Variable                |Label                          |Type        |Units / coding                              |Role              |
|:-----------------------|:------------------------------|:-----------|:-------------------------------------------|:-----------------|
|patient_id              |Patient identifier             |Character   |PHC-0001 ... PHC-1500                       |ID                |
|facility                |Healthcare facility            |Categorical |6 PHC facilities                            |Cluster/covariate |
|enroll_date             |Date of enrolment              |Date        |Mixed: YYYY-MM-DD, DD/MM/YYYY, DD-Mon-YYYY  |Metadata          |
|age                     |Age                            |Numeric     |Years                                       |Predictor         |
|sex                     |Sex                            |Categorical |Female / Male                               |Predictor         |
|residence               |Place of residence             |Categorical |Urban / Rural                               |Predictor         |
|education               |Highest education              |Ordinal     |None < Primary < Secondary < Tertiary       |Predictor         |
|occupation              |Occupation                     |Categorical |Unemployed/Farmer/Trader/Professional/Other |Predictor         |
|marital_status          |Marital status                 |Categorical |Single/Married/Divorced/Widowed             |Predictor         |
|health_insurance        |Has health insurance           |Binary      |Yes / No                                    |Predictor         |
|height_cm               |Height                         |Numeric     |centimetres                                 |Derived input     |
|weight_kg               |Weight                         |Numeric     |kilograms                                   |Derived input     |
|bmi                     |Body mass index                |Numeric     |kg/m^2                                      |Predictor         |
|smoking                 |Smoking status                 |Categorical |Never / Former / Current                    |Predictor         |
|alcohol                 |Alcohol intake                 |Categorical |None / Moderate / Heavy                     |Predictor         |
|physical_activity       |Physical activity level        |Ordinal     |Low / Moderate / High                       |Predictor         |
|family_history_htn      |Family history of hypertension |Binary      |Yes / No                                    |Predictor         |
|diabetes                |Diabetes mellitus              |Binary      |Yes / No                                    |Predictor         |
|sbp_mmhg                |Systolic blood pressure        |Numeric     |mmHg                                        |Clinical          |
|dbp_mmhg                |Diastolic blood pressure       |Numeric     |mmHg                                        |Clinical          |
|total_chol_mmol_l       |Total cholesterol              |Numeric     |mmol/L                                      |Lab biomarker     |
|hdl_mmol_l              |HDL cholesterol                |Numeric     |mmol/L                                      |Lab biomarker     |
|ldl_mmol_l              |LDL cholesterol                |Numeric     |mmol/L                                      |Lab biomarker     |
|triglycerides_mmol_l    |Triglycerides                  |Numeric     |mmol/L                                      |Lab biomarker     |
|fasting_glucose_mmol_l  |Fasting glucose                |Numeric     |mmol/L                                      |Lab biomarker     |
|creatinine_umol_l       |Serum creatinine               |Numeric     |umol/L                                      |Lab biomarker     |
|sodium_mmol_l           |Serum sodium                   |Numeric     |mmol/L                                      |Lab biomarker     |
|potassium_mmol_l        |Serum potassium                |Numeric     |mmol/L                                      |Lab biomarker     |
|knowledge_score         |Hypertension knowledge score   |Numeric     |0-20                                        |Predictor         |
|distance_to_facility_km |Distance to facility           |Numeric     |kilometres                                  |Predictor         |
|comorbidity_count       |Number of comorbidities        |Count       |0+                                          |Predictor         |
|htn_diagnosed           |Diagnosed hypertensive         |Binary      |Yes / No                                    |Filter            |
|months_since_diagnosis  |Months since HTN diagnosis     |Numeric     |Months                                      |Predictor         |
|treatment_uptake        |On antihypertensive treatment  |Binary      |Yes / No                                    |PRIMARY OUTCOME   |
|adherence               |Treatment adherence            |Categorical |Good / Poor (blank if untreated)            |Secondary outcome |
|bp_controlled           |Blood pressure controlled      |Binary      |Yes / No (blank if untreated)               |Secondary outcome |

The **Role** column shows how each variable is used. `patient_id` identifies participants and `facility` records the cluster (the health facility) each participant attended. Most variables are candidate predictors. `htn_diagnosed` acts as a *filter* that defines the analysis population, `treatment_uptake` is the primary outcome, and `adherence` and `bp_controlled` are the secondary outcomes. The data dictionary file also contains a column of notes describing the known problems in the raw data, which we use in Chapter 2. Keep the dictionary close at hand: knowing exactly what each variable means and how it was coded is half of good analysis.

In the clean analysis file, two derived variables are added to these 36: `bmi_cat`, the World Health Organization body mass index category, and `bp_category`, a categorisation of measured blood pressure. Both are created in Chapter 2.

### The study population at a glance

The clean analysis file, created in Chapter 2, contains one row per participant. The following code loads it and counts the participants, the facilities and the participants diagnosed with hypertension, who form the population for the primary analysis:


``` r
# Load the clean, analysis-ready data created in Chapter 2
analysis_data <- readRDS("Data/analysis_data.rds")

# Number of rows (participants) and columns (variables)
dim(analysis_data)
```

```
#> [1] 1500   38
```

``` r
# Key numbers describing the study population
diagnosed <- analysis_data[analysis_data$htn_diagnosed == "Yes", ]
study_size <- data.frame(
  quantity = c("Participants", "Facilities",
               "Diagnosed with hypertension",
               "Diagnosed and on treatment"),
  n = c(nrow(analysis_data),
        length(unique(analysis_data$facility)),
        nrow(diagnosed),
        sum(diagnosed$treatment_uptake == "Yes", na.rm = TRUE))
)
knitr::kable(study_size, col.names = c("Quantity", "n"),
             caption = "The case-study population.")
```



Table: The case-study population.

|Quantity                    |    n|
|:---------------------------|----:|
|Participants                | 1500|
|Facilities                  |    6|
|Diagnosed with hypertension | 1089|
|Diagnosed and on treatment  |  508|

The data contain 1,500 participants and 38 variables (the 36 recorded variables plus the two derived categories) from six facilities. Of the participants, 1089 had been diagnosed with hypertension, and these form the denominator for the primary outcome. Among them, 508 (47%) were on antihypertensive treatment. In the chapters that follow we ask who these patients are, how they differ from those who are not on treatment, and which factors remain associated with treatment once others are taken into account.

::: {.callout-note title="Clinical interpretation"}
In these simulated data, fewer than half of the patients known to have hypertension were on treatment. In a real study, a finding like this would point to a substantial gap between diagnosis and care at the primary-care level, and would motivate the search for determinants that the rest of the book carries out.
:::

## The data files and the analysis workflow

### The data files

The case-study data come in several files, each with a specific purpose. All are stored in a folder called `Data/`, and all the code in this book reads them with relative paths such as `"Data/analysis_data.rds"`.

- `hypertension_phc_raw.csv` and `hypertension_phc_raw.xlsx`: the **raw data**, as they might arrive from a data-collection team, in two common formats. The two files contain the same records. They have deliberately been given the problems that real clinical data so often have: 1,503 rows for 1,500 patients because of three duplicate records; categories spelled in several ways (for example `F`, `f`, `female` and `Female`); yes/no variables coded variously as `Yes`/`No`, `Y`/`N` and `1`/`0`; missing values recorded as blanks, `NA`, `999` or `-99`; impossible values such as an age of 200 years or a systolic blood pressure of 700 mmHg; stray spaces before and after text; and dates entered in three different formats. These files are used in Chapters 1 and 2.
- `analysis_data.rds`: the **clean, analysis-ready data**, saved in R's own file format. Problems have been corrected, variables have their proper types, categorical variables are factors with clinically sensible reference levels, and the derived variables have been added. The `.rds` format preserves all of this exactly, which a CSV file cannot. Chapters 3 to 5 start from this file.
- `data_dictionary.csv` and `data_dictionary.md`: the **data dictionary**, describing every variable, its coding, its role in the analysis and its known problems.

Chapter 2 shows you how to produce `analysis_data.rds` from the raw file yourself. A ready-made copy is provided so that you can work on any chapter independently, and so that you can compare your own cleaned data with ours.

::: {.callout-tip title="Good practice"}
Keep raw data and analysis-ready data in separate files, and generate the second from the first with a script. If a problem is later found in the raw data, you fix the script and regenerate the clean file, rather than patching the clean file by hand.
:::

### The analysis workflow

The chapters follow the stages of a typical clinical data analysis. It is worth keeping this sequence in mind, because it applies to almost any study you will analyse:

1. **Import** the raw data into R and inspect them: how many rows and columns, what types of variable, what looks wrong (Chapter 1).
2. **Clean** the data: handle missing-value codes, remove duplicates, harmonise categories, validate impossible values, parse dates, derive new variables and set factor levels, then save a clean analysis file (Chapter 2).
3. **Describe** the study population with summary statistics, a "Table 1" and well-designed figures, overall and by outcome group (Chapter 3).
4. **Test** specific hypotheses about differences and associations, choosing each test to suit the type of data and checking its assumptions (Chapter 4).
5. **Model** the outcome with regression, moving from crude to adjusted estimates and checking the model's adequacy (Chapter 5).
6. **Report** the findings clearly and honestly, in tables, figures and text that meet the expectations of clinical journals and reporting guidelines such as STROBE for observational studies [@vonelm2007] (Chapters 3 and 5).

Each stage is written as code, so the whole pathway from raw file to final report can be re-run at any time. This, in a sentence, is what the book aims to teach.

## About the authors

**Bernard Isekah Osang'ir** is a Senior Biostatistician at Neudata Consulting Ltd.

**Vương Mỹ Lượng** is a Senior Biostatistician at Neudata Consulting Ltd.

Both authors work on the design and analysis of clinical and public-health studies and on training health professionals to analyse their own data reproducibly in R.

## Acknowledgements

This book grew out of teaching material developed for health professionals learning to analyse clinical data in R. We are grateful to the participants who worked through earlier versions of the material: their questions, their errors and their insights revealed where explanations needed to be clearer, where examples needed to be more clinical and where the pace needed to be slower. We also thank the colleagues and reviewers who read drafts of the chapters and whose careful comments improved both the statistics and the prose.

Finally, we thank the R community: the R Core Team, who develop and maintain R itself, and the many authors of the packages used in this book, who share their work freely so that others may build upon it. Any errors that remain are our own.
