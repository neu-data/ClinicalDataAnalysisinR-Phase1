# =====================================================================
#  BÀI TẬP 6 — Hồi quy
#  Phân tích dữ liệu lâm sàng trong R (Giai đoạn I) — Trước khóa học
#  ------------------------------------------------------------------
#  Mục tiêu: khớp một mô hình hồi quy logistic đơn giản và đọc các tỷ số chênh.
#  Đáp án: Solutions/Solution_6_Regression.R
# =====================================================================

library(tidyverse)
library(broom)
clinical_data <- read_csv("Data/clinical_data_clean.csv")

# Đặt hypertension thành factor với "No" làm nhóm tham chiếu
clinical_data <- clinical_data %>%
  mutate(hypertension = factor(hypertension, levels = c("No", "Yes")))

# 1. Khớp một mô hình hồi quy logistic ------------------------------
#    Biến kết cục: hypertension (Yes/No).  Yếu tố dự báo: age, sex, BMI.
model <- glm(hypertension ~ age + sex + BMI,
             data = clinical_data,
             family = binomial)

# 2. Xem kết quả thô (thang log-odds) -------------------------------
summary(model)

# 3. Chuyển sang tỷ số chênh với khoảng tin cậy 95% -----------------
tidy(model, exponentiate = TRUE, conf.int = TRUE)

# ------------------------------------------------------------------
#  CÂU HỎI
# ------------------------------------------------------------------
# Q1. BIẾN KẾT CỤC trong mô hình này là gì?
#     TRẢ LỜI:
# Q2. Các YẾU TỐ DỰ BÁO là gì?
#     TRẢ LỜI:
# Q3. Tỷ số chênh (OR) của age là bao nhiêu? Của BMI?
#     TRẢ LỜI:
# Q4. Cho biết khoảng tin cậy (KTC 95%) của tỷ số chênh cho BMI.
#     TRẢ LỜI:
# Q5. Những yếu tố dự báo nào có ý nghĩa (thống kê)?
#     (Gợi ý: giá trị p có < 0.05 không, và KTC có loại trừ 1 không?)
#     TRẢ LỜI:
# Q6. Viết MỘT câu lâm sàng diễn giải tác động của BMI.
#     TRẢ LỜI:
