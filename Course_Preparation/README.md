# Course Preparation — Clinical Data Analysis in R (Phase I)

**A one-week, self-study preparation pack for a complete R beginner.**

Send this folder to participants **about one week before** the course. By working
through it (roughly 2–3 hours, spread over a few evenings), someone who has never
used R can install the software, learn the RStudio interface, practise on a real
clinical dataset, and arrive ready for Session 1.

> **New here? Start with the Study Guide** — `00_READ_ME_FIRST/Study_Guide_EN.pdf`
> (or `Study_Guide_VN.pdf`). It walks you, step by step, through installing R, setting
> up, and how to study — then open [`00_READ_ME_FIRST/README.md`](00_READ_ME_FIRST/README.md).

---

## Course at a glance

- **Course:** Clinical Data Analysis in R — Phase I — Introduction to R for Clinical Research (Neudata)
- **Format:** 5 evening sessions · every Tuesday · 8:00 pm · 90 minutes · 8 September – 6 October 2026
- **Trainers:** Bernard Isekah Osang'ir (Senior Biostatistician) and My Luong Vuong (Biostatistician and Epidemiologist)
- **Enquiries / registration:** My Luong Vuong — myluong1710@gmail.com — www.neu-data.com
- **Audience:** doctors, nurses, pharmacists, public-health workers, and MSc/PhD students — **no programming experience needed**

## Quick start (3 steps)

1. **Install** — open `01_Install_R_and_RStudio/`, follow the manual, then open and
   Source `installation_test.R`. You should see *"My R and RStudio installation is working."*
2. **Open the project** — double-click **`Clinical_Data_Analysis_PreCourse.Rproj`**.
   This opens RStudio in the right folder so all file paths work.
3. **Learn & practise** — read `02_Getting_Started_with_RStudio/`, work through the
   lessons `03_…` → `07_…` in order, then try the `Exercises/`.

## What's in this folder

| Folder / file | What it is |
|---|---|
| `00_READ_ME_FIRST/` | Start here — welcome, how to use the pack, checklist |
| `01_Install_R_and_RStudio/` | Installation manual (Windows + macOS) + `installation_test.R` |
| `02_Getting_Started_with_RStudio/` | Beginner tour of the RStudio interface |
| `03_R_Basics/` | Lesson 1 — objects, vectors, data frames (`01_R_Basics.Rmd`) |
| `04_Data_Management/` | Lesson 2 — cleaning clinical data (`02_Data_Management.Rmd`) |
| `05_Exploratory_Data_Analysis/` | Lesson 3 — descriptives, tables, plots (`03_Exploratory_Analysis.Rmd`) |
| `06_Statistical_Tests/` | Lesson 4 — t-test, chi-square, correlation (`04_Statistical_Tests.Rmd`) |
| `07_Regression/` | Lesson 5 — linear & logistic regression (`05_Regression.Rmd`) || `Data/` | The dataset (`clinical_data_clean.csv`, `clinical_data_raw.csv`, `.xlsx`), data dictionary, data-quality notes, generator script |
| `Exercises/` | Six short pre-course exercises (`.R`) — practice, not assessment |
| `Solutions/` | Worked solutions + `expected_results.md` reference answers |
| `Cheat_Sheets/` | Course R cheat sheet + statistical test decision guide |
| `Guides/` | Analytical thinking framework, examples by profession, R-output-to-paper || `Clinical_Data_Analysis_PreCourse.Rproj` | RStudio project file — double-click to open |

## The dataset

A fully **synthetic** dataset of **430 patients** (no real patient data), built so
that the analyses produce realistic, interpretable results. See
[`Data/data_dictionary.md`](Data/data_dictionary.md) for all 20 variables and
[`Data/Data_Quality_Problems.md`](Data/Data_Quality_Problems.md) for the deliberate
"messy data" problems you will learn to fix.

## Software required

- **R** (4.x) and **RStudio Desktop** — both free
- R packages: `tidyverse`, `readxl`, `gtsummary`, `broom`, `survival`, `survminer`
  (installed in one step during setup)

## What this pack is for

**This pack is everything you need before the course.** Work through it this week
to arrive installed and comfortable with R — it gets everyone to the same starting
line. That is all you need to do right now.

The live teaching materials (slides and worked examples) are used *during* the
sessions and will be shared as the course runs — you do **not** need them yet.

---

*It's fine to arrive with things half-working — there will be help on the first
evening. But trying beforehand makes Session 1 far smoother. See you on 8 September.*
