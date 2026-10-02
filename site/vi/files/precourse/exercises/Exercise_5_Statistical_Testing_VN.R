# =====================================================================
#  BÀI TẬP 5 — Kiểm định thống kê (tư duy + thực hành)
#  Phân tích dữ liệu lâm sàng trong R (Giai đoạn I) — Trước khóa học
#  ------------------------------------------------------------------
#  Mục tiêu: luyện tập việc CHỌN kiểm định phù hợp trước khi chạy nó.
#  Với mỗi câu hỏi nghiên cứu, trước tiên hãy quyết định (trong comment):
#     - Biến kết cục            - Kiểu biến
#     - Phơi nhiễm / so sánh    - Kiểm định phù hợp
#     - Giả thuyết không (H0)   - Diễn giải kết quả
#  Sau đó chạy kiểm định và kiểm tra lại tư duy của bạn.
#  Dùng Statistical_Test_Decision_Guide trong Cheat_Sheets/ để hỗ trợ.
#  Đáp án: Solutions/Solution_5_Statistical_Testing.R
# =====================================================================

library(tidyverse)
clinical_data <- read_csv("Data/clinical_data_clean.csv")

# -------------------------------------------------------------------
# CÂU HỎI A: Glucose lúc đói có cao hơn ở bệnh nhân đái tháo đường không?
#   Biến kết cục:       ______
#   Phơi nhiễm/nhóm:    ______
#   Kiểu biến:          ______
#   Kiểm định phù hợp:  ______
#   Giả thuyết không:   ______
# Chạy nó:
t.test(glucose ~ diabetes, data = clinical_data)
#   Diễn giải:          ______

# -------------------------------------------------------------------
# CÂU HỎI B: Tăng huyết áp có liên quan đến đái tháo đường không?
#   Biến kết cục:       ______
#   Phơi nhiễm/nhóm:    ______
#   Kiểu biến:          ______
#   Kiểm định phù hợp:  ______
#   Giả thuyết không:   ______
# Chạy nó:
chisq.test(table(clinical_data$hypertension, clinical_data$diabetes))
#   Diễn giải:          ______

# -------------------------------------------------------------------
# CÂU HỎI C: Tuổi và huyết áp tâm thu có liên quan với nhau không?
#   Biến kết cục:       ______
#   Phơi nhiễm:         ______
#   Kiểu biến:          ______
#   Kiểm định phù hợp:  ______
#   Giả thuyết không:   ______
# Chạy nó:
cor.test(clinical_data$age, clinical_data$systolic_bp)
#   Diễn giải:          ______

# -------------------------------------------------------------------
# CÂU HỎI D (bạn tự chọn kiểm định):
#   "Huyết áp tâm thu có khác nhau giữa nam và nữ không?"
#   Hãy quyết định kiểm định, rồi tự viết và chạy code bên dưới.
#   CODE CỦA BẠN:
#
#   Diễn giải:          ______
