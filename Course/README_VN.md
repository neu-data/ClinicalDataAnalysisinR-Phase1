# Phân tích Dữ liệu Lâm sàng bằng R - Giai đoạn I
### Nhập môn R cho Nghiên cứu Lâm sàng · Khóa học ngắn hạn buổi tối gồm năm buổi học

**Giảng viên:** Vương Mỹ Lượng (Chuyên gia Thống kê Sinh học Cao cấp, giảng viên chính) · Bernard Osang'ir (Chuyên gia Thống kê Sinh học Cao cấp)
**Lịch học:** Năm buổi học buổi tối · mỗi Thứ Ba, 20:00 (giờ Việt Nam), 90 phút · 8 tháng 9 – 6 tháng 10 năm 2026
**Thương hiệu:** Neudata · *#ClearDataClearImpact*

Một gói khóa học hoàn chỉnh, sẵn sàng để giảng dạy. Mọi bài thực hành xuyên suốt năm buổi học
đều sử dụng **một** nghiên cứu lâm sàng mô phỏng duy nhất để các kỹ năng được tích lũy dần
thành một phân tích đầy đủ và có khả năng tái lập.

**Nghiên cứu tình huống:** *Các yếu tố quyết định việc tiếp nhận điều trị tăng huyết áp ở người trưởng thành
đến khám tại các cơ sở chăm sóc sức khỏe ban đầu*, một nghiên cứu cắt ngang đa trung tâm
trên 1.500 người trưởng thành tại 6 cơ sở chăm sóc sức khỏe ban đầu. Biến kết cục chính:
tiếp nhận điều trị ở những người được chẩn đoán tăng huyết áp.

---

## Nội dung trong thư mục này

| Thư mục | Nội dung |
|--------|----------|
| **Slides/** | `Clinical_Data_Analysis_in_R_Phase1.pptx`, 123 slide trên mẫu trình bày Neudata, kèm ghi chú cho người trình bày trên mỗi slide |
| **Data/** | Bộ dữ liệu thô (`hypertension_phc_raw.csv` / `.xlsx`), bảng tham chiếu đã làm sạch (`hypertension_phc_clean.csv`), từ điển dữ liệu (`.md` / `.csv` / `.pdf`), và tập lệnh tạo dữ liệu |
| **Scripts/** | `day1_demo.R` … `day5_demo.R`, các phần trình diễn lập trình trực tiếp của giảng viên |
| **Practicals/** | `day1_exercise.R` … `day5_exercise.R`, các bài thực hành có hướng dẫn trên lớp |
| **Solutions/** | `day1_solution.R` … `day5_solution.R`, lời giải chi tiết |
| **Assignment/** | Bài tập lớn về nhà cuối khóa + hướng dẫn chấm điểm (`.md` và `.pdf`) |
| **Instructor_Notes/** | Sổ tay giảng viên / hướng dẫn điều phối (`.md` và `.pdf`) |
| **References/** | Sổ tay Học viên (PDF), bảng tra cứu lệnh R, hướng dẫn cài đặt gói, các phát hiện chính |
| **Resources/** | Các hình và bảng chất lượng xuất bản được tạo ra (PNG/CSV/HTML) dùng trong bộ slide và bài thực hành |
| **Images/** | Logo Neudata và các tài nguyên hình ảnh |

## Trình tự các buổi học

| Buổi | Chủ đề | Kết quả bạn tạo ra |
|---------|-------|-------------|
| 1 | Nhập môn R & RStudio | Bộ dữ liệu đã được nhập |
| 2 | Hiểu và Làm sạch Dữ liệu Lâm sàng | `Data/analysis_data.rds` (đã làm sạch) |
| 3 | Thống kê Mô tả, Bảng và Hình | Bảng 1 dạng bản thảo |
| 4 | Các Kiểm định Thống kê Y khoa Thường gặp | Chọn đúng và diễn giải kiểm định |
| 5 | Nhập môn Hồi quy và Diễn giải Kết quả | Một phần Kết quả ngắn gọn |

## Bắt đầu (dành cho học viên)

1. Cài đặt **R** và **RStudio**, sau đó cài các gói của khóa học, xem
   `References/package_installation_guide.md`.
2. Mở thư mục `Course` này dưới dạng một **RStudio Project**
   (File → New Project → Existing Directory).
3. Học theo từng buổi: đọc bộ slide, làm theo `Scripts/dayN_demo.R`,
   rồi thực hiện `Practicals/dayN_exercise.R`. Tự kiểm tra bằng cách đối chiếu với `Solutions/`.

> Tất cả các tập lệnh đều sử dụng **đường dẫn tương đối** từ thư mục gốc `Course/` này, nên chúng
> chạy được trên bất kỳ máy nào một khi project đã được mở.

## Tái lập dữ liệu và kết quả đầu ra

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
*Được chuẩn bị cho đối tượng lâm sàng sau đại học, các trường đại học, trung tâm nghiên cứu
lâm sàng, bệnh viện, tổ chức phi chính phủ và các đơn vị thử nghiệm lâm sàng.*
Neudata · *#ClearDataClearImpact*
