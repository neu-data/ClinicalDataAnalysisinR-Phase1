# =====================================================================
#  ĐÁP ÁN 6, Hồi quy
# =====================================================================
library(tidyverse)
library(broom)
clinical_data <- read_csv("Data/clinical_data_clean.csv")

clinical_data <- clinical_data %>%
  mutate(hypertension = factor(hypertension, levels = c("No", "Yes")))

model <- glm(hypertension ~ age + sex + BMI,
             data = clinical_data, family = binomial)

tidy(model, exponentiate = TRUE, conf.int = TRUE)

# ---- Trả lời -------------------------------------------------------
# Q1. Biến kết cục: hypertension (Yes / No).
# Q2. Yếu tố dự báo: age, sex, BMI.
# Q3. OR của age  ~ 1.09  (mỗi năm tuổi tăng thêm làm tăng odds ~9%).
#     OR của BMI  ~ 1.16  (mỗi đơn vị BMI tăng thêm làm tăng odds ~16%).
# Q4. KTC 95% của tỷ số chênh cho BMI: khoảng 1.10 đến 1.22.
# Q5. Có ý nghĩa thống kê: age và BMI (p < 0.001, KTC loại trừ 1).
#     Sex KHÔNG có ý nghĩa (OR ~1.20, KTC 95% 0.76-1.90, p ~ 0.43).
# Q6. Câu ví dụ:
#     "BMI cao hơn có liên quan độc lập với tăng huyết áp: mỗi kg/m2 tăng thêm
#      làm tăng odds tăng huyết áp khoảng 16% (OR 1.16,
#      KTC 95% 1.10-1.22), sau khi hiệu chỉnh theo age và sex."
