# =====================================================================
#  BÀI TẬP 3, Phân tích mô tả
#  Phân tích dữ liệu lâm sàng trong R (Giai đoạn I), Trước khóa học
#  ------------------------------------------------------------------
#  Mục tiêu: tóm tắt dữ liệu bằng các thống kê mô tả đơn giản.
#  Đáp án: Solutions/Solution_3_Descriptive_Analysis.R
# =====================================================================

library(tidyverse)
clinical_data <- read_csv("Data/clinical_data_clean.csv")

# 1. Tuổi trung bình ------------------------------------------------
mean(clinical_data$age, na.rm = TRUE)

# 2. Trung vị BMI ---------------------------------------------------
median(clinical_data$BMI, na.rm = TRUE)

# 3. Tỷ lệ nữ (dưới dạng phần trăm) ---------------------------------
mean(clinical_data$sex == "Female") * 100

# 4. Tỷ lệ hiện mắc tăng huyết áp (dưới dạng phần trăm) -------------
mean(clinical_data$hypertension == "Yes") * 100

# 5. Huyết áp trung bình theo giới tính -----------------------------
clinical_data %>%
  group_by(sex) %>%
  summarise(
    n            = n(),
    mean_systolic  = mean(systolic_bp, na.rm = TRUE),
    mean_diastolic = mean(diastolic_bp, na.rm = TRUE)
  )

# ------------------------------------------------------------------
#  CÂU HỎI
# ------------------------------------------------------------------
# Q1. Tuổi trung bình là bao nhiêu (làm tròn 1 chữ số thập phân)?
#     TRẢ LỜI:
# Q2. Trung vị BMI là bao nhiêu?
#     TRẢ LỜI:
# Q3. Bao nhiêu phần trăm bệnh nhân là nữ?
#     TRẢ LỜI:
# Q4. Tỷ lệ hiện mắc tăng huyết áp là bao nhiêu?
#     TRẢ LỜI:
# Q5. Huyết áp tâm thu trung bình có khác biệt rõ rệt giữa nam và nữ không?
#     TRẢ LỜI:
