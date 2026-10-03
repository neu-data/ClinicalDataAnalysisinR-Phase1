# Clinical Data Analysis in R — Phase I
### Introduction to R for Clinical Research · A five-session evening short course

**Trainers:** Vương Mỹ Lượng (Senior Biostatistician, lead trainer) · Bernard Osang'ir (Senior Biostatistician)
**Schedule:** Five evening sessions · every Tuesday, 8:00 PM, 90 minutes · 8 September – 6 October 2026
**Brand:** Neudata · *#ClearDataClearImpact*

A complete, ready-to-teach course package. Every exercise across the five sessions
uses **one** simulated clinical study so skills build cumulatively into a full,
reproducible analysis.

**Case study:** *Determinants of Hypertension Treatment Uptake among Adults
attending Primary Healthcare Facilities* — a multicentre cross-sectional study
of 1,500 adults across 6 primary healthcare facilities. Primary outcome:
treatment uptake among diagnosed hypertensives.

---

## What's in this folder

| Folder | Contents |
|--------|----------|
| **Slides/** | `Clinical_Data_Analysis_in_R_Phase1.pptx` — 123 slides on the Neudata template, with speaker notes on every slide |
| **Data/** | Raw dataset (`hypertension_phc_raw.csv` / `.xlsx`), tidy reference (`hypertension_phc_clean.csv`), data dictionary (`.md` / `.csv` / `.pdf`), and the generator script |
| **Scripts/** | `day1_demo.R` … `day5_demo.R` — the instructor live-coding demonstrations |
| **Practicals/** | `day1_exercise.R` … `day5_exercise.R` — the guided in-class exercises |
| **Solutions/** | `day1_solution.R` … `day5_solution.R` — worked solutions |
| **Assignment/** | Final take-home assignment + marking guide (`.md` and `.pdf`) |
| **Instructor_Notes/** | Instructor manual / facilitation guide (`.md` and `.pdf`) |
| **References/** | Participant Handbook (PDF), R command reference sheet, package installation guide, key findings |
| **Resources/** | Generated publication-quality figures and tables (PNG/CSV/HTML) used in the deck and exercises |
| **Images/** | Neudata logo and image assets |

## How the sessions flow

| Session | Theme | You produce |
|---------|-------|-------------|
| 1 | Introduction to R & RStudio | Imported dataset |
| 2 | Understanding & Cleaning Clinical Data | `Data/analysis_data.rds` (clean) |
| 3 | Descriptive Statistics, Tables & Figures | A manuscript Table 1 |
| 4 | Common Medical Statistical Tests | Correct test chosen & interpreted |
| 5 | Introduction to Regression & Interpreting Output | A short Results section |

## Getting started (participants)

1. Install **R** and **RStudio**, then the course packages — see
   `References/package_installation_guide.md`.
2. Open this `Course` folder as an **RStudio Project**
   (File → New Project → Existing Directory).
3. Work session by session: read the slide deck, follow `Scripts/dayN_demo.R`,
   then do `Practicals/dayN_exercise.R`. Check yourself against `Solutions/`.

> All scripts use **relative paths** from this `Course/` root, so they run on any
> machine once the project is open.

## Reproducing the data and outputs

```bash
# regenerate the dataset (Python)
python Data/generate_dataset.py
python Data/make_data_dictionary.py

# regenerate all figures/tables (R, from the Course/ directory)
Rscript Scripts/day3_demo.R
Rscript Scripts/day4_demo.R
Rscript Scripts/day5_demo.R
```

---
*Prepared for postgraduate clinical audiences — universities, clinical research
centres, hospitals, NGOs and clinical trial units.*
Neudata · *#ClearDataClearImpact*
