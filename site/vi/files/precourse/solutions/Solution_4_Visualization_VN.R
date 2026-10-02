# =====================================================================
#  ĐÁP ÁN 4 — Trực quan hóa
# =====================================================================
library(tidyverse)
clinical_data <- read_csv("Data/clinical_data_clean.csv")

# (Bốn biểu đồ giống hệt bài tập; xem Exercise_4 để biết code.)

# ---- Trả lời (diễn giải) -------------------------------------------
# Q1. Huyết áp tâm thu gần đối xứng và có dạng hình chuông, tập trung quanh
#     120-125 mmHg, với đuôi phải nhẹ — một phân phối khá chuẩn.
# Q2. Nam và nữ có BMI nhìn chung tương tự nhau; các hộp chồng lấn nhiều, nên khác biệt
#     (nếu có) là nhỏ.
# Q3. Riverside Clinic tuyển được nhiều bệnh nhân nhất (104), theo sát là
#     Central Hospital (103). Lakeside Health tuyển ít nhất (51).
# Q4. Huyết áp tâm thu có xu hướng TĂNG theo tuổi — đường khớp dốc lên
#     (điều này khớp với tương quan r ~ 0.55 tìm được ở Bài 4).
