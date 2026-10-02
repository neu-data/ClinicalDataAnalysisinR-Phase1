# =====================================================================
#  INSTALLATION TEST  -  Clinical Data Analysis in R (Phase I)
#  ------------------------------------------------------------------
#  Purpose: confirm that R, RStudio and the course packages all work.
#
#  HOW TO USE (no experience needed):
#    1. Open this file in RStudio (it should already be open).
#    2. Click "Source" (top-right of this editor pane), OR press
#       Ctrl+Shift+S (Windows) / Cmd+Shift+S (Mac).
#    3. Watch the Console (bottom-left). If everything is installed,
#       the last line it prints will be:
#           My R and RStudio installation is working.
#
#  If you see a red error instead, read the message, then check the
#  Troubleshooting section of Install_R_and_RStudio.md.
# =====================================================================

cat("\n--- Step 1: Is R running? ---\n")

# Basic arithmetic - R is a calculator
2 + 2

# Make a small vector of numbers and take its average
x <- c(10, 12, 14, 16)
mean(x)          # should be 13

cat("2 + 2 =", 2 + 2, "\n")
cat("mean(x) =", mean(x), "  (this should be 13)\n")


cat("\n--- Step 2: Are the course packages installed? ---\n")

# These are the add-on packages the course uses.
needed <- c("tidyverse", "readxl", "gtsummary",
            "broom", "survival", "survminer")

installed_ok <- needed %in% rownames(installed.packages())

for (i in seq_along(needed)) {
  status <- if (installed_ok[i]) "OK" else "MISSING"
  cat(sprintf("  %-12s %s\n", needed[i], status))
}


cat("\n--- Step 3: Can we load a package and use it? ---\n")

# dplyr (part of the tidyverse) is what we use to handle data.
library(dplyr)

# A tiny data-handling test: average of a small table
demo <- data.frame(patient = 1:4, age = c(45, 60, 52, 71))
demo_summary <- demo %>% summarise(mean_age = mean(age))
print(demo_summary)          # mean_age should be 57


cat("\n=====================================================================\n")
if (all(installed_ok)) {
  cat("My R and RStudio installation is working.\n")
  cat("You are ready for the course. See you on 8 September!\n")
} else {
  missing <- needed[!installed_ok]
  cat("Almost there! R works, but these packages are still missing:\n   ",
      paste(missing, collapse = ", "), "\n")
  cat("Install them by running (copy the line below into the Console):\n")
  cat('   install.packages(c("',
      paste(missing, collapse = '", "'), '"))\n', sep = "")
  cat("Then Source this file again.\n")
}
cat("=====================================================================\n")
