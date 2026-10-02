# =====================================================================
#  BÀI TẬP 2 — Quản lý dữ liệu
#  Phân tích dữ liệu lâm sàng trong R (Giai đoạn I) — Trước khóa học
#  ------------------------------------------------------------------
#  Mục tiêu: luyện tập các động từ làm sạch dữ liệu hằng ngày trên tệp lộn xộn.
#  Đáp án: Solutions/Solution_2_Data_Management.R
# =====================================================================

library(tidyverse)

# Đọc bộ dữ liệu THÔ (lộn xộn)
raw <- read_csv("Data/clinical_data_raw.csv")

# 1. Xác định các vấn đề --------------------------------------------
colSums(is.na(raw))      # (a) cột nào có giá trị khuyết?
sum(duplicated(raw))     # (b) có bao nhiêu hàng trùng?
table(raw$sex)           # (c) sex được viết theo bao nhiêu cách khác nhau?

# 2. Loại bỏ các bản ghi trùng --------------------------------------
clean <- raw %>% distinct()
nrow(clean)              # còn lại bao nhiêu bệnh nhân duy nhất?

# 3. Mã hóa lại sex thành hai nhãn sạch -----------------------------
clean <- clean %>%
  mutate(sex = case_when(
    sex %in% c("Female", "female", "F", "f") ~ "Female",
    sex %in% c("Male",   "male",   "M", "m") ~ "Male"
  ))
table(clean$sex)

# 4. filter() và select() -------------------------------------------
# Chỉ giữ lại phụ nữ, và chỉ một vài cột
women <- clean %>%
  filter(sex == "Female") %>%
  select(patient_id, age, BMI, systolic_bp)
head(women)

# 5. Tạo biến mới với mutate() + case_when() ------------------------
clean <- clean %>%
  mutate(
    bmi_group = case_when(
      BMI < 18.5 ~ "Underweight",
      BMI < 25   ~ "Normal",
      BMI < 30   ~ "Overweight",
      BMI >= 30  ~ "Obese"
    ),
    age_group = case_when(
      age < 40  ~ "<40",
      age < 55  ~ "40-54",
      age < 70  ~ "55-69",
      age >= 70 ~ "70+"
    ),
    pulse_pressure = systolic_bp - diastolic_bp   # một biến dẫn xuất
  )

table(clean$bmi_group)
table(clean$age_group)

# ------------------------------------------------------------------
#  CÂU HỎI
# ------------------------------------------------------------------
# Q1. Những cột nào chứa giá trị khuyết, và cột nào nhiều nhất?
#     TRẢ LỜI:
# Q2. Có bao nhiêu hàng trùng, và còn lại bao nhiêu bệnh nhân duy nhất?
#     TRẢ LỜI:
# Q3. Có bao nhiêu bệnh nhân thuộc nhóm BMI "Obese"?
#     TRẢ LỜI:
# Q4. Về mặt lâm sàng, 'pulse_pressure' biểu thị điều gì?
#     TRẢ LỜI:
# Q5. Dùng filter() để đếm xem có bao nhiêu bệnh nhân từ 60 tuổi trở lên.
#     (Viết cả đoạn code và câu trả lời.)
#     TRẢ LỜI:
