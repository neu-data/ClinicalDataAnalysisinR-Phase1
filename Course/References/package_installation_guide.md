# Recommended Package Installation Guide
### Clinical Data Analysis in R - Phase I | Neudata · #ClearDataClearImpact

Run these steps **before Day 1** (or during the Day 1 setup session). You need an internet connection the first time only.

---

## Step 1: Install R and RStudio
1. **R** (the engine): https://cran.r-project.org → download for Windows / macOS → install with default options.
2. **RStudio Desktop** (the workbench): https://posit.co/download/rstudio-desktop/ → install.
3. Open **RStudio** (not plain R). You should see four panes: Source, Console, Environment, Files/Plots.

> This course was prepared with **R 4.6.0**. Any recent 4.x version works.

## Step 2: Install the course packages
Copy the block below into the RStudio **Console** and press Enter. It installs everything used across the five days in one go.

```r
install.packages(c(
  # --- core: import, wrangle, visualise ---
  "tidyverse",      # dplyr, ggplot2, readr, stringr, tibble, lubridate ...
  "readxl",         # read Excel (.xlsx) files
  "lubridate",      # working with dates
  "janitor",        # quick cleaning helpers (clean_names, tabyl)

  # --- tables & reporting ---
  "gtsummary",      # publication-ready Table 1 and regression tables
  "gt",             # rendering / exporting tables
  "broom",          # tidy model output (odds ratios, CIs)
  "broom.helpers",  # required by gtsummary for tbl_regression()

  # --- statistics & diagnostics ---
  "car",            # VIF and regression diagnostics
  "pROC",           # ROC curve / AUC
  "scales"          # nice axis formatting
))
```

Installation can take several minutes. Windows and macOS receive pre-compiled binaries, so no extra build tools are needed.

## Step 3: Confirm everything loaded
Run this check. Every line should print `TRUE`.

```r
pkgs <- c("tidyverse","readxl","lubridate","janitor","gtsummary",
          "gt","broom","broom.helpers","car","pROC","scales")
for (p in pkgs) cat(sprintf("%-15s %s\n", p, requireNamespace(p, quietly = TRUE)))
```

## Step 4: Set up the project
1. Download/unzip the **Course** folder supplied by the instructor.
2. In RStudio: **File → New Project → Existing Directory →** choose the `Course` folder.
3. Working from this project means all paths like `Data/hypertension_phc_raw.csv` "just work" on any computer.

---

## Optional extras
| Package | Why you might want it |
|---------|-----------------------|
| `rmarkdown` / `quarto` | one-click reproducible reports (PDF/Word/HTML) |
| `webshot2` + `chromote` | export `gt` tables to PNG/PDF (needs Chrome installed) |
| `here` | robust relative paths in larger projects |
| `flextable` / `officer` | send tables straight to Word/PowerPoint |

## Troubleshooting
- **"there is no package called X"** → you skipped Step 2, or `library(X)` is spelled differently from `install.packages("X")`.
- **Table export to PNG fails / "Chrome not found"** → install Google Chrome, or export tables as `.html`/`.csv` instead (the course scripts fall back automatically).
- **Corporate network blocks CRAN** → set a mirror: `options(repos = c(CRAN = "https://cloud.r-project.org"))` then retry, or ask IT for an approved mirror.
- **Slow install** → install in smaller groups (core first, then reporting, then stats).
