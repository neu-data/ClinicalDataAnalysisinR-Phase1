# Vietnamese edition — translation guide

Translate `Book/chapters/en/<name>.Rmd` into `Book/chapters/vi/<name>.Rmd` (same file name).
The Vietnamese edition is a full, natural, professional translation for Vietnamese health
professionals and researchers — not word-for-word. Keep the meaning, depth and length.

## What to translate and what to keep

* Translate: all prose, headings, list items, callout titles, objectives, exercise texts,
  figure captions (`fig.cap`), table captions, kable `col.names`, plot titles and axis labels
  inside `labs()`, legend titles, and **R comments** in code (`# ...`).
* Keep exactly: R code (function and object names, variable names such as `treatment_uptake`,
  file paths), chunk labels and chunk options other than `fig.cap`, maths, citation keys
  (`[@altman1991]`), URLs, the restricted Markdown syntax, and the `{#ch-...}` labels.
* Data values stay in English because they are the values stored in the dataset
  ("Yes", "No", "Female", facility names). When the text mentions them, keep the English value
  in code font and explain it once if needed, e.g. `"Yes"` (có).
* Callout titles: Clinical interpretation → **Diễn giải lâm sàng**; Good practice → **Thực hành tốt**;
  Tip → **Mẹo**; Common mistake → **Lỗi thường gặp**; Key points → **Điểm chính**.
* Exercises: `::: {.exercise title="Bài tập 3.1"}`. In solutions files: `## Chương 3: <tên chương>`
  and `### Bài tập 3.1`.
* Chapter headings: keep the `{#ch-...}` label. Preface: `# Lời nói đầu {.unnumbered}`.
* Section names used in every chapter: Summary → **Tóm tắt**; Further reading → **Đọc thêm**;
  Exercises → **Bài tập**; Learning objectives box needs no title (added automatically).
* Cross-references: "Chapter 3" → "Chương 3", "Section 3.4" → "Mục 3.4", "Figure 3.2" → "Hình 3.2",
  "Table 3.1" → "Bảng 3.1", "the appendix" → "phụ lục".
* Book title in text: *Nhập môn Phân tích Dữ liệu Lâm sàng bằng R* (subtitle *Hướng dẫn thực hành về quản lý dữ liệu, phân tích thống kê và diễn giải kết quả*), but keep the English title the first time with the Vietnamese in brackets if helpful.

## Terminology (use consistently)

| English | Tiếng Việt |
|---|---|
| hypertension / blood pressure | tăng huyết áp / huyết áp |
| systolic / diastolic blood pressure | huyết áp tâm thu / huyết áp tâm trương |
| treatment uptake | việc sử dụng điều trị (tiếp nhận điều trị) |
| primary healthcare facility | cơ sở chăm sóc sức khỏe ban đầu |
| cross-sectional study | nghiên cứu cắt ngang |
| outcome / exposure / predictor | biến kết cục / phơi nhiễm / biến dự báo |
| confounding / confounder | nhiễu / yếu tố gây nhiễu |
| mean / median / mode | trung bình / trung vị / yếu vị |
| standard deviation / variance | độ lệch chuẩn / phương sai |
| interquartile range | khoảng tứ phân vị |
| standard error | sai số chuẩn |
| confidence interval | khoảng tin cậy |
| hypothesis test / null hypothesis | kiểm định giả thuyết / giả thuyết không |
| p-value / significance level | giá trị p / mức ý nghĩa |
| Type I / Type II error / power | sai lầm loại I / sai lầm loại II / lực thống kê |
| normal distribution | phân phối chuẩn |
| skewed | lệch |
| t-test / chi-square test | kiểm định t / kiểm định khi bình phương |
| Fisher's exact test | kiểm định chính xác Fisher |
| Wilcoxon rank-sum test | kiểm định tổng hạng Wilcoxon |
| ANOVA | phân tích phương sai (ANOVA) |
| correlation | tương quan |
| odds / odds ratio | odds / tỷ số chênh (OR) |
| relative risk / risk difference | nguy cơ tương đối / hiệu số nguy cơ |
| logistic regression / linear regression | hồi quy logistic / hồi quy tuyến tính |
| crude / adjusted | thô / hiệu chỉnh |
| reference level | nhóm tham chiếu |
| missing data / missing values | dữ liệu khuyết / giá trị khuyết |
| data cleaning | làm sạch dữ liệu |
| data frame / variable / observation | khung dữ liệu (data frame) / biến / quan sát |
| package / function / argument / object | gói / hàm / đối số / đối tượng |
| working directory / project | thư mục làm việc / dự án |
| reproducible | có thể tái lập |
| script / console | script / console (cửa sổ lệnh) |
| figure / table | hình / bảng |
| sensitivity / specificity / ROC curve / AUC | độ nhạy / độ đặc hiệu / đường cong ROC / AUC |

Keep common English technical terms in brackets the first time they appear in a chapter where
Vietnamese readers will meet the English term in R or papers, e.g. "khoảng tin cậy (confidence
interval, CI)".

## Testing

From the repository root:

```
"/c/Program Files/R/R-4.6.1/bin/Rscript.exe" Book/tools/knit_chapter.R vi 03-descriptive
```

It must finish without error. Check `Book/_knit/vi/<name>.md`: Vietnamese text, translated plot
labels in the figures, output lines ≤ 80 characters. Follow `Book/AUTHORING.md` for all syntax.
