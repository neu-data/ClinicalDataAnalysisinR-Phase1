# Slide-spec schema (for content_dayN.py authors)

Each content file defines ONE module-level Python list. Each element is a dict
("slide spec"). Output **valid Python only** — double-quoted strings, escape
internal double quotes, no imports, no f-strings. Use straight ASCII apostrophes
`'` in prose (the engine escapes them). Do NOT use the bullet character `•`.

## Supported slide types and fields

### divider  (start every day with one)
```python
{"type": "divider", "title": "Day N: <Topic>",
 "plan_title": "Plan",                     # optional, default "Plan"
 "agenda": ["item", "item", ...],          # 3-6 short items
 "notes": "<speaker notes>"}
```

### content  (the workhorse: titled sections + optional callout boxes)
```python
{"type": "content", "title": "<Slide title>",
 "blocks": [
    {"header": "<section header>", "lines": ["line", "line"]},
    {"header": "<header>", "lines": ["line"], "bullets": True},   # bulleted lines
    {"callout": "tip", "header": "<short>", "lines": ["one or two short lines"]},
 ],
 "notes": "<speaker notes>"}
```
- `callout` kind is one of: "tip", "warning", "mistake", "interpretation", "note".
- A line may be a dict for emphasis: `{"text": "...", "bold": True, "color": "0D7377"}`.
- **Fit rule:** at most ~13 text lines total (headers + body). If you include
  callout boxes, use fewer body lines (callouts stack up from y≈4.35M).
  Prefer 2-3 blocks; at most 2 callouts.

### bullets
```python
{"type": "bullets", "title": "...", "intro": "optional italic intro",
 "items": ["point", {"text": "sub-point", "level": 1}, ...],   # <= 9 items
 "notes": "..."}
```

### two_column
```python
{"type": "two_column", "title": "...",
 "left":  {"header": "...", "lines": ["...", "..."], "bullets": True},
 "right": {"header": "...", "lines": ["...", "..."], "bullets": True},
 "notes": "..."}            # <= 8 lines per column
```

### code  (live-demo slides — what the instructor types + console output)
```python
{"type": "code", "title": "...",
 "intro": "optional one-line setup",
 "code": "library(tidyverse)\nhtn <- read_csv(\"Data/file.csv\")\ndim(htn)",
 "output": "Rows: 1503  Columns: 36",     # optional console output
 "note": "optional one-line interpretation (renders as a blue box)",
 "notes": "..."}
```
- **Fit rule:** code <= 12 lines if no output; if `output` present, code <= 9 lines
  and output <= 6 lines. Keep lines < ~70 chars. `code_sz` defaults to 1300.

### image  (embed a real figure from Course/Resources/)
```python
{"type": "image", "title": "...",
 "image": "day4_forest_plot.png",         # filename only; from Resources/
 "aspect": 0.78,                            # height/width of the PNG
 "side_header": "How to read it",          # optional left column
 "side_notes": ["...", "..."],             # optional left column bullets
 "caption": "optional caption (used when no side_notes)",
 "notes": "..."}
```

### table
```python
{"type": "table", "title": "...",
 "headers": ["Col A", "Col B"],
 "rows": [["...", "..."], ["...", "..."]],   # <= 7 rows
 "caption": "optional",
 "notes": "..."}
```

## Speaker notes — REQUIRED on every slide
Write `notes` as several short lines separated by `\n`. Cover, where relevant:
- Key teaching point(s)
- Common misconception / common mistake
- Clinical interpretation
- A suggested audience question and the expected answer
- A demonstration tip

## Available figures in Course/Resources/ (use on image slides)
- day3_hist_age.png (0.75), day3_hist_sbp.png (0.75)
- day3_bar_education.png (0.75), day3_box_sbp_by_treatment.png (0.75)
- day3_box_bmi_by_bpcat.png (0.75), day3_scatter_sbp_bmi.png (0.75)
- day3_fig1_uptake_by_facility.png (0.7), day3_fig2_age_by_treatment.png (0.7)
- day4_forest_plot.png (0.78), forest_plot_or.png (0.78)

## Dataset facts (be accurate)
- Study: Determinants of Hypertension Treatment Uptake among Adults attending
  Primary Healthcare Facilities. Multicentre cross-sectional, 1,500 adults.
- 6 facilities: Bugando PHC, Kisesa HC, Nyamagana PHC, Ilemela HC, Buzuruga PHC, Igoma HC.
- Raw file: 1,503 rows (3 duplicate records), 36 variables.
- Messiness: sex spelled Female/F/female/f & Male/M/male/m; binaries mix Yes/No/Y/N/1/0;
  missing sentinels "", NA, 999, -99; impossible values (age 200 & 0, sbp 0 & 700,
  weight 7, height 17); 3 duplicate IDs; mixed date formats.
- Primary outcome: treatment_uptake (Yes/No), analysed among htn_diagnosed=="Yes" (~1,089).

## Key results (cite these where relevant)
- Treatment uptake ≈ 47% among diagnosed; final model n = 992 complete cases; AUC ≈ 0.71.
- Adjusted ORs: diabetes 3.56 (1.46-9.61); health insurance 2.05 (1.54-2.74);
  family history 1.91 (1.44-2.54); urban residence 1.87 (1.41-2.49);
  higher education trend 1.96 (1.39-2.77); age 1.03 per year (1.02-1.04);
  knowledge 1.10 per point (1.06-1.14); distance to facility not significant.
