# =====================================================================
#  ĐÁP ÁN 2, Quản lý dữ liệu
# =====================================================================
library(tidyverse)
raw <- read_csv("Data/clinical_data_raw.csv")

colSums(is.na(raw))
sum(duplicated(raw))

clean <- raw %>%
  distinct() %>%
  mutate(sex = case_when(
    sex %in% c("Female", "female", "F", "f") ~ "Female",
    sex %in% c("Male",   "male",   "M", "m") ~ "Male"
  )) %>%
  mutate(
    bmi_group = case_when(
      BMI < 18.5 ~ "Underweight",
      BMI < 25   ~ "Normal",
      BMI < 30   ~ "Overweight",
      BMI >= 30  ~ "Obese"
    ),
    pulse_pressure = systolic_bp - diastolic_bp
  )

# Code cho Q5: bệnh nhân từ 60 tuổi trở lên
clean %>% filter(age >= 60) %>% nrow()

# ---- Trả lời -------------------------------------------------------
# Q1. Giá trị khuyết nằm ở: glucose (22 - nhiều nhất), cholesterol (18),
#     alcohol_use (12), BMI (9), followup_date (7), diastolic_bp (5).
# Q2. Có 3 hàng trùng; còn lại 430 bệnh nhân duy nhất.
# Q3. Khoảng 92 bệnh nhân thuộc nhóm "Obese" ở đây. (Con số này được tính trên dữ liệu
#     thô mới làm sạch một phần, vẫn còn một vài giá trị BMI bất khả thi/khuyết; sau khi
#     làm sạch hoàn toàn, Bài 2, con số là 93.)
# Q4. pulse_pressure = huyết áp tâm thu - tâm trương. Nó phản ánh độ cứng động mạch;
#     áp lực mạch rộng thường gặp ở bệnh nhân lớn tuổi.
# Q5. 148 bệnh nhân từ 60 tuổi trở lên.
