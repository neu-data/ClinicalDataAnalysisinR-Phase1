# Hướng dẫn cài đặt gói khuyến nghị
### Phân tích Dữ liệu Lâm sàng bằng R — Giai đoạn I | Neudata · #ClearDataClearImpact

Hãy thực hiện các bước này **trước Ngày 1** (hoặc trong buổi thiết lập của Ngày 1). Bạn chỉ cần kết nối internet trong lần đầu tiên.

---

## Bước 1 — Cài đặt R và RStudio
1. **R** (bộ máy xử lý): https://cran.r-project.org → tải về cho Windows / macOS → cài đặt với các tùy chọn mặc định.
2. **RStudio Desktop** (bàn làm việc): https://posit.co/download/rstudio-desktop/ → cài đặt.
3. Mở **RStudio** (không phải R thuần). Bạn sẽ thấy bốn khung: Source, Console, Environment, Files/Plots.

> Khóa học này được chuẩn bị với **R 4.6.0**. Bất kỳ phiên bản 4.x gần đây nào cũng dùng được.

## Bước 2 — Cài đặt các gói của khóa học
Sao chép khối lệnh dưới đây vào **Console** của RStudio và nhấn Enter. Nó sẽ cài đặt mọi thứ được sử dụng xuyên suốt năm ngày trong một lần.

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

Quá trình cài đặt có thể mất vài phút. Windows và macOS nhận các gói nhị phân đã được biên dịch sẵn, nên không cần thêm công cụ build nào.

## Bước 3 — Xác nhận mọi thứ đã được nạp
Chạy đoạn kiểm tra này. Mỗi dòng đều phải in ra `TRUE`.

```r
pkgs <- c("tidyverse","readxl","lubridate","janitor","gtsummary",
          "gt","broom","broom.helpers","car","pROC","scales")
for (p in pkgs) cat(sprintf("%-15s %s\n", p, requireNamespace(p, quietly = TRUE)))
```

## Bước 4 — Thiết lập dự án
1. Tải về/giải nén thư mục **Course** do giảng viên cung cấp.
2. Trong RStudio: **File → New Project → Existing Directory →** chọn thư mục `Course`.
3. Làm việc từ dự án này nghĩa là mọi đường dẫn như `Data/hypertension_phc_raw.csv` sẽ "chạy đúng ngay lập tức" trên bất kỳ máy tính nào.

---

## Các gói bổ sung tùy chọn
| Gói | Vì sao bạn có thể cần đến |
|---------|-----------------------|
| `rmarkdown` / `quarto` | báo cáo tái lập được chỉ với một cú nhấp (PDF/Word/HTML) |
| `webshot2` + `chromote` | xuất bảng `gt` sang PNG/PDF (cần cài Chrome) |
| `here` | đường dẫn tương đối vững chắc trong các dự án lớn hơn |
| `flextable` / `officer` | gửi bảng thẳng sang Word/PowerPoint |

## Xử lý sự cố
- **"there is no package called X"** → bạn đã bỏ qua Bước 2, hoặc `library(X)` được viết khác với `install.packages("X")`.
- **Xuất bảng sang PNG thất bại / "Chrome not found"** → cài Google Chrome, hoặc xuất bảng dưới dạng `.html`/`.csv` để thay thế (các script của khóa học sẽ tự động chuyển sang phương án dự phòng).
- **Mạng nội bộ công ty chặn CRAN** → thiết lập một mirror: `options(repos = c(CRAN = "https://cloud.r-project.org"))` rồi thử lại, hoặc nhờ bộ phận IT cung cấp một mirror đã được phê duyệt.
- **Cài đặt chậm** → cài theo các nhóm nhỏ hơn (core trước, rồi đến reporting, rồi đến stats).
