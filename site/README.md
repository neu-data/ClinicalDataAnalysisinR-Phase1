# Course website · Trang web khóa học

**Live site:** <https://neu-data.github.io/ClinicalDataAnalysisinR-Phase1/>
(English: `/en/` · Tiếng Việt: `/vi/`)

The website is generated from the course materials in this repository and uses the Neudata
templates ([Quarto slides](https://github.com/neu-data/quarto-slides-template),
[course website](https://github.com/neu-data/quarto-course-template)).

## What is on the site (both languages)

| Section | Built from |
|---|---|
| Slide decks — course introduction, Days 1–5, final assignment (123 slides, speaker notes on every slide) | `Deck_and_Build/deckbuild/content_*.py` |
| Session pages — agenda, slides, PowerPoint, demo script, exercise, solution | `Course/Scripts`, `Practicals`, `Solutions` |
| Pre-course module — study guide, checklist, install guide, RStudio manual, 5 runnable lessons, exercises, data, cheat sheets, guides | `Course_Preparation/` |
| Materials — participant handbook, R command reference, package guide, data dictionary, final assignment, downloads | `Course/References`, `Course/Data`, `Course/Assignment` |

**Not published** (instructor-only): the instructor manual, the marking guide, trainer notes and the participant email templates.

## Updating the site

1. Edit the course content as usual (e.g. `Deck_and_Build/deckbuild/content_day3.py`, `Course/References/participant_handbook.md`).
2. Regenerate the site sources:

   ```bash
   python site/build.py
   ```

3. Render both languages (needs Quarto and, for the pre-course lessons, R with tidyverse, gtsummary, broom, readxl, pROC, car):

   ```bash
   quarto render site/en
   quarto render site/vi
   ```

4. Commit everything in `site/` **including the `_freeze/` folders**, and push. GitHub Actions publishes the site automatically.

Preview locally with `quarto preview site/en` (or `site/vi`).

## How it fits together

```
site/
├── build.py          generator: course files → two Quarto websites
├── _shared/          Neudata slide extension, site theme, logo, language switch, landing page
├── en/               English website (generated; commit it)
└── vi/               Vietnamese website (generated; commit it)
```

The language button in the navbar opens the same page in the other language. The site root asks visitors to choose a language and remembers their choice.
