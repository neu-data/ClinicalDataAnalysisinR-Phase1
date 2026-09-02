SLIDES_DAY1 = [

    {"type": "divider", "title": "Day 1: Introduction to R & RStudio",
     "plan_title": "Today's Plan",
     "agenda": [
        "Why R for clinical research",
        "R vs RStudio: install and the interface",
        "Projects, scripts, objects and vectors",
        "Data frames and packages (tidyverse)",
        "Importing and a first look at the study data",
        "Hands-on exercise"],
     "notes": "Key point: this whole day is about getting comfortable, not memorising. By tonight every participant will have imported a real clinical dataset and looked at it.\nCommon misconception: that you must be a programmer. You do not; R is a tool like a calculator or a stethoscope.\nClinical interpretation: reproducible analysis means a colleague or a regulator can re-run your work and get the same numbers.\nAsk the audience: who has used Excel for research? Expected answer: almost everyone. Bridge: R does what Excel does, but it records every step.\nDemo tip: keep RStudio open on screen behind you so people see the real thing, not just slides."},

    {"type": "content", "title": "Why R for Clinical Research",
     "blocks": [
        {"header": "What R gives you", "lines": [
            "A free, open-source language for statistics and data",
            "Used in clinical trials, epidemiology and journals",
            "Handles import, cleaning, analysis and plots in one place"]},
        {"header": "Why it matters", "lines": [
            "Every step is written down, so the analysis is repeatable",
            "No cost and no licence: install on any computer",
            "A huge community and packages for medical research"]},
        {"callout": "interpretation", "header": "Reproducibility",
         "lines": ["If you can re-run the script, you can defend the result."]}],
     "notes": "Key point: the headline advantage is reproducibility plus zero cost. Click-by-click in Excel is hard to reproduce; a script is the recipe.\nCommon misconception: that free means low quality. R is used by FDA, EMA reviewers, and most major epidemiology groups.\nClinical interpretation: when a reviewer asks how you derived a number, you point to a line of code, not your memory.\nAsk the audience: what happens if you redo last year's analysis in Excel by hand? Expected answer: you may get slightly different numbers. A script removes that risk.\nDemo tip: mention that the figures in many NEJM and Lancet papers are made in R."},

    {"type": "two_column", "title": "R vs RStudio: Two Different Things",
     "left": {"header": "R (the engine)",
        "lines": [
            "The actual statistical language",
            "Does the computation",
            "You install it first",
            "Rarely opened on its own"],
        "bullets": True},
     "right": {"header": "RStudio (the dashboard)",
        "lines": [
            "A friendly workspace around R",
            "Editor, console, plots, help",
            "Install it second",
            "This is what you open daily"],
        "bullets": True},
     "notes": "Key point: R is the engine, RStudio is the dashboard. You need both, and you install R first.\nCommon mistake: people try to open R directly and find a bare console. Always open RStudio instead.\nClinical interpretation: think of R as the lab analyser and RStudio as the technician's interface to it.\nAsk the audience: which one do you double-click each morning? Expected answer: RStudio.\nDemo tip: show both icons on the desktop so the distinction is concrete."},

    {"type": "content", "title": "The RStudio Interface: Four Panes",
     "blocks": [
        {"header": "Top-left: Source (Script editor)", "lines": [
            "Where you write and save your code"]},
        {"header": "Bottom-left: Console", "lines": [
            "Where code runs and results appear"]},
        {"header": "Top-right: Environment", "lines": [
            "The objects and data you have created"]},
        {"header": "Bottom-right: Files / Plots / Help", "lines": [
            "Folders, your graphs, and documentation"]},
        {"callout": "tip", "header": "Orientation",
         "lines": ["Spend two minutes finding each pane before you type."]}],
     "notes": "Key point: just four panes. Source and Console on the left, Environment and the Files/Plots/Help tabs on the right.\nCommon misconception: that the layout is fixed; it is configurable, but the defaults are fine for beginners.\nClinical interpretation: the Environment pane is your worktop, it shows what data is currently loaded.\nAsk the audience: where will a graph appear? Expected answer: bottom-right, the Plots tab.\nDemo tip: type a line in the Console and the same line in the Source, and show that only the saved Source persists."},

    {"type": "content", "title": "RStudio Projects and the Working Directory",
     "blocks": [
        {"header": "The working directory", "lines": [
            "The folder R looks in when you open a file",
            "Check it with getwd()"]},
        {"header": "Use a Project, not setwd()", "lines": [
            "File > New Project keeps everything in one folder",
            "Paths become relative, like Data/file.csv",
            "The work runs on any computer, unchanged"]},
        {"callout": "warning", "header": "Avoid setwd()",
         "lines": ["A hard-coded path breaks on every other machine."]}],
     "notes": "Key point: an RStudio Project sets the working directory for you and makes paths portable.\nCommon mistake: setwd(\"C:/Users/me/Desktop/...\") at the top of a script. It works only on that one computer.\nClinical interpretation: portability matters when you share an analysis with a statistician or a collaborator at another site.\nAsk the audience: what is wrong with writing the full C: path? Expected answer: nobody else has that exact folder.\nDemo tip: run getwd() once so people see what the current folder actually is, then open the course Project."},

    {"type": "two_column", "title": "Script vs Console",
     "intro": "Both run R code, but only one is your record.",
     "left": {"header": "Console",
        "lines": [
            "Type, press Enter, get an answer",
            "Good for quick tries",
            "Not saved when you close"],
        "bullets": True},
     "right": {"header": "Script (Source)",
        "lines": [
            "You write, then save as a .R file",
            "Re-run any time, line by line",
            "This is your reproducible record"],
        "bullets": True},
     "notes": "Key point: the script is the reproducible record; the console is a scratchpad.\nCommon misconception: that typing in the console is enough. It vanishes on close.\nClinical interpretation: the saved script is your analysis audit trail, like a signed lab notebook.\nAsk the audience: where should the real analysis live? Expected answer: in a saved script.\nDemo tip: run a line with Ctrl+Enter from the script and show the result appearing in the console below."},

    {"type": "code", "title": "First Steps: R as a Calculator",
     "intro": "The simplest way to start - just type sums into the Console.",
     "code": '2 + 2\n140 / 90        # a blood-pressure ratio\nsqrt(16)\n(120 + 130 + 145 + 150) / 4   # mean of four readings',
     "output": "[1] 4\n[1] 1.555556\n[1] 4\n[1] 136.25",
     "note": "Everything in R is built from small steps like these - start simple, then build up.",
     "notes": ("Key teaching point: R is first and foremost a calculator - functions like sqrt() "
               "and arithmetic (+, -, *, /) work exactly as you expect.\n"
               "Common misconception: that you must memorise commands before you can do anything. "
               "You can explore by just typing sums.\n"
               "Clinical interpretation: a blood-pressure ratio or a quick mean of a few readings is "
               "real, useful work on day one.\n"
               "Audience question: what does 140 / 90 give, and what might it represent? "
               "Expected answer: about 1.56 - a crude systolic-to-diastolic ratio.\n"
               "Demo tip: let participants call out sums and type them live; build confidence before "
               "introducing objects.")},

    {"type": "content", "title": "Objects and the Assignment Arrow",
     "blocks": [
        {"header": "Store a value in an object", "lines": [
            "sbp <- 152 means store 152 in an object named sbp",
            "Type the name sbp to print it back",
            "The arrow <- is the assignment operator"]},
        {"header": "R is case-sensitive", "lines": [
            "SBP and sbp are two different objects"]},
        {"callout": "mistake", "header": "Common slips",
         "lines": ["Using = instead of <-; mixing up upper and lower case."]}],
     "notes": "Key point: <- stores a value in a named object; the name then behaves like the value.\nCommon mistake: writing sbp = 152 (works but is discouraged) or calling it Sbp later and getting an error.\nClinical interpretation: an object is just a labelled container, like a labelled specimen tube.\nAsk the audience: is Age the same as age in R? Expected answer: no, R is case-sensitive.\nDemo tip: type the shortcut Alt+- (Alt and minus) to insert <- automatically, and show the case-sensitivity error live."},

    {"type": "code", "title": "Objects and Vectors in Action",
     "intro": "A vector holds many values of the same type.",
     "code": "sbp <- 152\nsbp\nsbp_readings <- c(152, 138, 145, 160, 129, 142)\nlength(sbp_readings)\nmean(sbp_readings)\nsd(sbp_readings)",
     "output": "[1] 152\n[1] 6\n[1] 144.3333\n[1] 11.23239",
     "note": "c() means combine; mean() and sd() summarise the whole vector.",
     "notes": "Key point: c() combines values into a vector; functions like length(), mean() and sd() act on the whole vector at once.\nCommon mistake: forgetting the commas inside c(), or mixing text and numbers in one vector.\nClinical interpretation: a vector is one column of readings, six systolic measurements here.\nAsk the audience: what does length() tell us? Expected answer: how many values are in the vector, here six.\nDemo tip: also run summary(sbp_readings) and max(sbp_readings) so they see more functions on the same object."},

    {"type": "content", "title": "Data Types You Will Meet",
     "blocks": [
        {"header": "Three everyday types", "lines": [
            "numeric: numbers, like age or sbp (60, 152)",
            "character: text in quotes, like \"Female\"",
            "logical: TRUE or FALSE, like sbp >= 140"]},
        {"header": "Why type matters", "lines": [
            "You can average numbers, not text",
            "R picks the type when it reads your data"]},
        {"callout": "note", "header": "Tip",
         "lines": ["glimpse() shows the type of every column at a glance."]}],
     "notes": "Key point: numeric, character and logical are the three types beginners need. Each column of data is one type.\nCommon misconception: that a number stored as text behaves like a number; it does not, you cannot average it.\nClinical interpretation: if age was imported as text (because of a stray value like 200 or a letter), means will fail until it is fixed.\nAsk the audience: what type is \"Yes\"/\"No\"? Expected answer: character text; we will recode it later.\nDemo tip: create high_bp <- sbp_readings >= 140 and show the TRUE/FALSE logical vector, then sum() it to count."},

    {"type": "content", "title": "Data Frames and Tibbles",
     "blocks": [
        {"header": "The shape of a dataset", "lines": [
            "A data frame is a table: rows and columns",
            "Each row is one patient (one observation)",
            "Each column is one variable (age, sex, sbp)"]},
        {"header": "Tibble", "lines": [
            "The tidyverse version of a data frame",
            "Prints neatly and shows column types"]},
        {"callout": "interpretation", "header": "Read it as a clinic",
         "lines": ["Rows are people; columns are what you measured."]}],
     "notes": "Key point: a data frame (or tibble) is the rectangular table that holds your study, rows = patients, columns = variables.\nCommon misconception: that R data looks like a spreadsheet with merged cells and colours; it is plain tidy columns.\nClinical interpretation: this rows-are-patients, columns-are-variables layout is exactly the tidy structure analyses expect.\nAsk the audience: in our data, what does one row represent? Expected answer: one adult attending a PHC facility.\nDemo tip: contrast a tibble print (clean, shows types) with a base data.frame print so they appreciate tibbles."},

    {"type": "content", "title": "Packages: Install Once, Load Each Session",
     "blocks": [
        {"header": "Two different commands", "lines": [
            "install.packages(\"tidyverse\") downloads it once",
            "library(tidyverse) loads it every new session"]},
        {"header": "Packages we use today", "lines": [
            "tidyverse: import, wrangle, plot",
            "readxl: read Excel .xlsx files"]},
        {"callout": "mistake", "header": "Common mistake",
         "lines": ["Running install.packages() every time (slow, needs internet)."]}],
     "notes": "Key point: install once (downloads from the internet), library() every time you start R. Two separate jobs.\nCommon mistake: putting install.packages() at the top of a script that runs daily; it re-downloads needlessly and fails offline.\nClinical interpretation: a package is a toolbox of extra functions; tidyverse and readxl are the ones we need for import.\nAsk the audience: do you install a package every session? Expected answer: no, you only library() it.\nDemo tip: show library(tidyverse) printing its attaching message, and note that is normal, not an error."},

    {"type": "code", "title": "Importing the Study Data",
     "intro": "Load packages first, then read the file.",
     "code": "library(tidyverse)\nlibrary(readxl)\nhtn <- read_csv(\"Data/hypertension_phc_raw.csv\")\nhtn_xl <- read_excel(\n  \"Data/hypertension_phc_raw.xlsx\", sheet = \"data\")\ndim(htn)",
     "output": "Rows: 1503  Columns: 36\n[1] 1503   36",
     "note": "read_csv for CSV, read_excel for Excel. Note 1503, not 1500.",
     "notes": "Key point: read_csv() reads the CSV, read_excel() reads the Excel; both land in a tibble. The paths are relative because we are in a Project.\nCommon mistake: forgetting library(readxl) before read_excel, or a wrong path/file name (case and spelling must match exactly).\nClinical interpretation: 1503 rows but the study enrolled 1,500, so three duplicate records are hiding in here.\nAsk the audience: why 1503 and not 1500? Expected answer: there are 3 duplicate records, which we fix on Day 2.\nDemo tip: point out the column specification message read_csv prints; it is informational, not an error."},

    {"type": "bullets", "title": "First Look: Knowing Your Data",
     "intro": "Run these the moment any dataset is imported.",
     "items": [
        "dim(htn): how many rows and columns",
        "names(htn): the variable names",
        "glimpse(htn): every column with its type",
        "head(htn): the first few rows",
        "View(htn): open the spreadsheet viewer",
        "htn$age: pull one column out with the dollar sign",
        "summary(htn$age): min, mean, max of a variable",
        "table(htn$sex): counts of each category"],
     "notes": "Key point: a fixed first-look routine, dim, names, glimpse, head, View, then $ to inspect single variables with summary and table.\nCommon mistake: jumping straight to analysis without looking; many data problems are visible in the first thirty seconds.\nClinical interpretation: summary() and table() are your screening tests for the data; they flag impossible values and messy categories.\nAsk the audience: what does htn$age return? Expected answer: the age column as a single vector.\nDemo tip: run View(htn) so people see the familiar spreadsheet grid, then close it and rely on glimpse()."},

    {"type": "code", "title": "Inspecting Single Variables",
     "intro": "The $ extracts one column to summarise.",
     "code": "summary(htn$age)\ntable(htn$sex)",
     "output": "   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.\n   0.0    38.0    52.0    53.4    66.0   200.0\n\n     f      F female Female      m ...\n    11     63    402    498     14 ...",
     "note": "Max age 200 and eight spellings of sex: this data needs cleaning.",
     "notes": "Key point: summary() on age and table() on sex immediately expose problems, an impossible max of 200 and many spellings of the same category.\nCommon misconception: that imported data is clean; raw clinical data almost never is.\nClinical interpretation: an age of 200 (and a 0) cannot be real; Female/female/F/f are all the same group recorded inconsistently.\nAsk the audience: how many true sex categories should there be? Expected answer: two, but the table shows eight labels.\nDemo tip: also run table(htn$facility) to reveal stray spaces, and tell them Day 2 fixes all of this."},

    {"type": "content", "title": "Common Mistakes and Quick Debugging",
     "blocks": [
        {"header": "When it does not work, check", "lines": [
            "Did you run library() for the package?",
            "Did you use <- and not = for assignment?",
            "Is the spelling and CASE exactly right?",
            "Is the file path and name correct?"]},
        {"callout": "warning", "header": "could not find function",
         "lines": ["Usually means the package is not loaded: run library()."]},
        {"callout": "mistake", "header": "cannot open file",
         "lines": ["Wrong path or file name; check the Files pane."]}],
     "notes": "Key point: most beginner errors are one of four things, missing library(), wrong operator, a case/spelling slip, or a bad path.\nCommon mistake: panicking at red text. Read the message; it usually names the problem.\nClinical interpretation: debugging is like differential diagnosis, read the sign (the error), form a hypothesis, test the fix.\nAsk the audience: you get could not find function read_csv, what is wrong? Expected answer: tidyverse is not loaded; run library(tidyverse).\nDemo tip: deliberately trigger one error live (mistype the file name) and walk through reading the message calmly."},

    {"type": "content", "title": "What the Data Is Already Telling Us",
     "blocks": [
        {"header": "Problems visible on the first look", "lines": [
            "Age = 200 and age = 0: impossible values",
            "Sex recorded eight different ways",
            "1503 rows for 1,500 people: duplicates"]},
        {"header": "Why this is good news", "lines": [
            "We found it in seconds, before any analysis",
            "Cleaning is the topic of Day 2"]},
        {"callout": "interpretation", "header": "Garbage in, garbage out",
         "lines": ["No statistic is trustworthy on uncleaned data."]}],
     "notes": "Key point: the first look has already surfaced the three big issues, impossible values, inconsistent categories, and duplicate rows.\nCommon misconception: that finding problems means you did something wrong; finding them early is exactly the goal.\nClinical interpretation: analysing before cleaning would bias every result, the mean age would be pulled up by the 200.\nAsk the audience: should we calculate mean age right now? Expected answer: no, fix the impossible values first.\nDemo tip: foreshadow Day 2 by showing how a single 200 distorts mean(htn$age); it motivates the cleaning day."},

    {"type": "content", "title": "Day 1 Exercise: Import the Clinical Dataset",
     "blocks": [
        {"header": "Your tasks", "lines": [
            "Open the course RStudio Project",
            "library(tidyverse) and library(readxl)",
            "Import the CSV with read_csv()",
            "Import the Excel file with read_excel()",
            "Run glimpse() on the data",
            "summary() the age column, table() the sex column"]},
        {"callout": "tip", "header": "What to notice",
         "lines": ["Spot the impossible age, the many sex spellings, 1503 rows."]}],
     "notes": "Key point: the exercise is the whole Day 1 workflow end to end, project, packages, import both formats, then inspect.\nCommon mistake: forgetting a library() call, or a path typo; circulate and check these first.\nClinical interpretation: by importing and inspecting, participants experience the same data-quality red flags we just discussed.\nAsk the audience: after table(sex), how many distinct labels do you see? Expected answer: eight, for two real categories.\nDemo tip: give a fixed time (about 15 minutes), then debrief by asking who found the age of 200 first."},

    {"type": "content", "title": "Recap and Bridge to Day 2",
     "blocks": [
        {"header": "Today you learned to", "lines": [
            "Tell R from RStudio and find the four panes",
            "Work in a Project with a saved script",
            "Make objects (<-) and vectors (c())",
            "Load packages and import CSV and Excel data",
            "Inspect data with glimpse, summary and table"]},
        {"header": "Tomorrow: Day 2", "lines": [
            "Cleaning the mess: fix ages, unify categories",
            "Remove duplicates and handle missing values"]},
        {"callout": "note", "header": "Well done",
         "lines": ["You imported real clinical data on day one."]}],
     "notes": "Key point: consolidate the arc, from never having opened R to importing and inspecting a real dataset, then preview cleaning.\nCommon misconception: that we will start analysing tomorrow; first we clean, because trustworthy analysis needs clean data.\nClinical interpretation: today was data IN and a first look; Day 2 turns the raw, messy file into an analysis-ready dataset.\nAsk the audience: what are the three data problems we must fix tomorrow? Expected answer: impossible values, inconsistent categories, duplicate rows.\nDemo tip: end by re-opening their script and re-running it top to bottom, proving reproducibility in one keystroke."},

]
