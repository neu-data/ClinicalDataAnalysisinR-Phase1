# =====================================================================
#  BÀI TẬP 1 — Làm quen với bộ dữ liệu
#  Phân tích dữ liệu lâm sàng trong R (Giai đoạn I) — Trước khóa học
#  ------------------------------------------------------------------
#  Mục tiêu: làm quen với việc mở một bộ dữ liệu và xem xét nó.
#  Đây là luyện tập, KHÔNG phải bài kiểm tra. Chạy từng dòng và đọc kết quả.
#  Đáp án nằm ở  Solutions/Solution_1_Meet_Your_Dataset.R
# =====================================================================

# 1. Nạp tidyverse và đọc bộ dữ liệu đã làm sạch --------------------
library(tidyverse)

clinical_data <- read_csv("Data/clinical_data_clean.csv")
# LƯU Ý: đường dẫn này giả định bạn đã mở dự án qua
# Clinical_Data_Analysis_PreCourse.Rproj (để R nằm trong thư mục chính).

# 2. Xem bộ dữ liệu bằng năm lệnh thiết yếu -------------------------
dim(clinical_data)       # số hàng và số cột
names(clinical_data)     # tên các biến
head(clinical_data)      # 6 hàng đầu tiên
str(clinical_data)       # cấu trúc: từng biến và kiểu dữ liệu của nó
summary(clinical_data)   # tóm tắt nhanh mọi biến

# 3. Vài cách xem có mục tiêu ----------------------------------------
table(clinical_data$sex)            # mỗi giới tính có bao nhiêu người?
colSums(is.na(clinical_data))       # số giá trị khuyết theo từng cột

# ------------------------------------------------------------------
#  CÂU HỎI  (viết câu trả lời của bạn dưới dạng comment bên dưới mỗi câu)
# ------------------------------------------------------------------
# Q1. Bộ dữ liệu có bao nhiêu bệnh nhân (hàng)?
#     TRẢ LỜI:
#
# Q2. Có bao nhiêu biến (cột)?
#     TRẢ LỜI:
#
# Q3. Nêu tên ba biến thuộc loại PHÂN LOẠI (văn bản/nhóm).
#     TRẢ LỜI:
#
# Q4. Nêu tên ba biến thuộc loại LIÊN TỤC (số).
#     TRẢ LỜI:
#
# Q5. Những biến nào chứa dữ liệu khuyết trong tệp đã làm sạch này?
#     (Gợi ý: xem kết quả của colSums(is.na(...)).)
#     TRẢ LỜI:
