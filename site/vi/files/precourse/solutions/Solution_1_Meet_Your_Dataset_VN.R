# =====================================================================
#  ĐÁP ÁN 1, Làm quen với bộ dữ liệu
# =====================================================================
library(tidyverse)
clinical_data <- read_csv("Data/clinical_data_clean.csv")

dim(clinical_data)
colSums(is.na(clinical_data))

# ---- Trả lời -------------------------------------------------------
# Q1. Bệnh nhân (hàng): 430
# Q2. Biến (cột): 20
# Q3. Biến phân loại (chọn ba biến bất kỳ trong số):
#     sex, smoking, alcohol_use, hypertension, diabetes, treatment, hospital
#     (patient_id là mã định danh; outcome là chỉ báo 0/1;
#      admission_date và followup_date là ngày tháng.)
# Q4. Biến liên tục (chọn ba biến bất kỳ trong số):
#     age, weight_kg, height_cm, BMI, systolic_bp, diastolic_bp,
#     glucose, cholesterol, time_to_event
# Q5. Dữ liệu khuyết: KHÔNG có, tệp CLEAN không có giá trị khuyết nào (đó chính là
#     mục đích của việc làm sạch). Dữ liệu khuyết nằm ở clinical_data_raw.csv, tệp mà
#     bạn làm sạch ở Bài 2 / Bài tập 2.
