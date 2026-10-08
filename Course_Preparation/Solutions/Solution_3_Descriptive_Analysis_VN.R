# =====================================================================
#  ĐÁP ÁN 3, Phân tích mô tả
# =====================================================================
library(tidyverse)
clinical_data <- read_csv("Data/clinical_data_clean.csv")

mean(clinical_data$age)                          # 54.2
median(clinical_data$BMI)                        # 26.6
mean(clinical_data$sex == "Female") * 100        # 54.7 %
mean(clinical_data$hypertension == "Yes") * 100  # 36.0 %

clinical_data %>%
  group_by(sex) %>%
  summarise(mean_systolic = mean(systolic_bp),
            mean_diastolic = mean(diastolic_bp))

# ---- Trả lời -------------------------------------------------------
# Q1. Tuổi trung bình = 54.2 năm.
# Q2. Trung vị BMI = 26.6 kg/m2.
# Q3. 54.7 % bệnh nhân là nữ.
# Q4. Tỷ lệ hiện mắc tăng huyết áp = 36.0 %.
# Q5. Không, huyết áp tâm thu trung bình gần như giống hệt nhau ở nam (~124.5) và nữ
#     (~124.3). (Bài 4 xác nhận điều này bằng kiểm định t: p ~ 0.85.)
