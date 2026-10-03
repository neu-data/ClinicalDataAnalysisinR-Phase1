# Knit one book source file (R Markdown) to Markdown with real R output and figures.
#
#   Rscript Book/tools/knit_chapter.R <lang> <name>
#   e.g. Rscript Book/tools/knit_chapter.R en 01-r-basics
#
# Run from the repository root. Reads  Book/chapters/<lang>/<name>.Rmd
# Writes Book/_knit/<lang>/<name>.md  and figures in Book/_knit/<lang>/figures/
# R code runs with the working directory set to Course/, so paths such as
# "Data/analysis_data.rds" work exactly as in the course scripts.
# Any error in a chunk stops the knit (error = FALSE), so a successful run
# means every chunk ran.

args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 2) stop("usage: knit_chapter.R <lang> <name>")
lang <- args[[1]]; name <- args[[2]]

book   <- normalizePath("Book", winslash = "/", mustWork = TRUE)
course <- normalizePath("Course", winslash = "/", mustWork = TRUE)
src    <- file.path(book, "chapters", lang, paste0(name, ".Rmd"))
outdir <- file.path(book, "_knit", lang)
dir.create(file.path(outdir, "figures"), recursive = TRUE, showWarnings = FALSE)
out    <- file.path(outdir, paste0(name, ".md"))

set.seed(2026)
options(width = 77, knitr.table.format = "pipe", digits = 4,
        pillar.width = 77, tibble.width = 77, cli.unicode = TRUE,
        dplyr.summarise.inform = FALSE, readr.show_col_types = FALSE)

knitr::opts_knit$set(root.dir = course, base.dir = outdir)
knitr::opts_chunk$set(
  fig.path   = paste0("figures/", name, "-"),
  dev        = c("png", "cairo_pdf"),   # cairo: Unicode (Vietnamese) text in PDF figures
  dpi        = 150,
  fig.width  = 7,
  fig.height = 4.3,
  comment    = "#>",
  message    = FALSE,
  warning    = FALSE,
  error      = FALSE
)
# ggplot2 theme for every figure in the book (Neudata colours, clean background)
if (requireNamespace("ggplot2", quietly = TRUE)) {
  ggplot2::theme_set(ggplot2::theme_minimal(base_size = 11) +
    ggplot2::theme(plot.title = ggplot2::element_text(face = "bold", colour = "#04242F"),
                   plot.title.position = "plot",
                   panel.grid.minor = ggplot2::element_blank()))
}

knitr::knit(src, out, quiet = TRUE, envir = new.env(), encoding = "UTF-8")
cat("Knitted", src, "->", out, "\n")
