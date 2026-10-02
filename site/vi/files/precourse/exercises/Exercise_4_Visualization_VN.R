# =====================================================================
#  BÀI TẬP 4 — Trực quan hóa
#  Phân tích dữ liệu lâm sàng trong R (Giai đoạn I) — Trước khóa học
#  ------------------------------------------------------------------
#  Mục tiêu: tạo bốn biểu đồ cốt lõi và diễn giải từng biểu đồ.
#  Đáp án: Solutions/Solution_4_Visualization.R
# =====================================================================

library(tidyverse)
clinical_data <- read_csv("Data/clinical_data_clean.csv")

# 1. Biểu đồ tần suất — phân phối của huyết áp tâm thu --------------
ggplot(clinical_data, aes(x = systolic_bp)) +
  geom_histogram(binwidth = 5, fill = "#0D7377", colour = "white") +
  labs(title = "Distribution of systolic BP",
       x = "Systolic BP (mmHg)", y = "Number of patients")

# 2. Biểu đồ hộp — BMI theo giới tính -------------------------------
ggplot(clinical_data, aes(x = sex, y = BMI, fill = sex)) +
  geom_boxplot() +
  labs(title = "BMI by sex", x = "Sex", y = "BMI (kg/m2)") +
  theme(legend.position = "none")

# 3. Biểu đồ cột — số bệnh nhân theo từng bệnh viện -----------------
ggplot(clinical_data, aes(x = hospital, fill = hospital)) +
  geom_bar() +
  labs(title = "Patients per hospital", x = NULL, y = "Number of patients") +
  theme(legend.position = "none") +
  coord_flip()          # cột nằm ngang để nhãn dễ đọc

# 4. Biểu đồ phân tán — tuổi so với huyết áp tâm thu ----------------
ggplot(clinical_data, aes(x = age, y = systolic_bp)) +
  geom_point(alpha = 0.5, colour = "#0D7377") +
  geom_smooth(method = "lm", se = TRUE, colour = "#C1440E") +
  labs(title = "Systolic BP against age",
       x = "Age (years)", y = "Systolic BP (mmHg)")

# ------------------------------------------------------------------
#  CÂU HỎI  (diễn giải từng biểu đồ)
# ------------------------------------------------------------------
# Q1. Phân phối của huyết áp tâm thu gần đối xứng hay bị lệch?
#     TRẢ LỜI:
# Q2. Nam và nữ có khác nhau nhiều về BMI không?
#     TRẢ LỜI:
# Q3. Bệnh viện nào tuyển được nhiều bệnh nhân nhất?
#     TRẢ LỜI:
# Q4. Huyết áp tâm thu có xu hướng tăng, giảm, hay giữ nguyên theo tuổi?
#     TRẢ LỜI:
