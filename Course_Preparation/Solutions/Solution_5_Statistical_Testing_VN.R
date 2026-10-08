# =====================================================================
#  ĐÁP ÁN 5, Kiểm định thống kê
# =====================================================================
library(tidyverse)
clinical_data <- read_csv("Data/clinical_data_clean.csv")

# CÂU HỎI A: glucose theo diabetes
t.test(glucose ~ diabetes, data = clinical_data)
#   Biến kết cục:     glucose (liên tục)
#   Phơi nhiễm/nhóm:  diabetes (Yes / No), 2 nhóm
#   Kiểu biến:        biến kết cục liên tục, nhóm nhị phân
#   Kiểm định:        kiểm định t hai mẫu (Wilcoxon nếu bị lệch)
#   H0:               glucose trung bình GIỐNG nhau ở cả hai nhóm
#   Diễn giải:        glucose cao hơn nhiều khi có đái tháo đường; p < 0.001, nên ta
#                     bác bỏ H0. Bệnh nhân đái tháo đường có glucose lúc đói cao hơn.

# CÂU HỎI B: hypertension so với diabetes
chisq.test(table(clinical_data$hypertension, clinical_data$diabetes))
#   Biến kết cục/biến: hypertension và diabetes (cả hai đều phân loại)
#   Kiểm định:        kiểm định chi bình phương về sự liên quan (Fisher nếu số đếm nhỏ)
#   H0:               hai tình trạng ĐỘC LẬP (không liên quan)
#   Diễn giải:        chi bình phương = 26.0, p < 0.001 -> bác bỏ H0. Tăng huyết áp và
#                     đái tháo đường có liên quan (chúng đồng xuất hiện nhiều hơn ngẫu nhiên).

# CÂU HỎI C: age so với systolic BP
cor.test(clinical_data$age, clinical_data$systolic_bp)
#   Biến kết cục:     systolic_bp (liên tục)
#   Phơi nhiễm:       age (liên tục)
#   Kiểm định:        tương quan Pearson (Spearman nếu phi tuyến/bị lệch)
#   H0:               KHÔNG có tương quan (r = 0)
#   Diễn giải:        r ~ 0.55, p < 0.001 -> tương quan dương, mức trung bình.
#                     Bệnh nhân lớn tuổi có xu hướng có huyết áp tâm thu cao hơn.

# CÂU HỎI D: systolic BP theo sex  (bạn tự chọn kiểm định)
t.test(systolic_bp ~ sex, data = clinical_data)
#   Kiểm định:        kiểm định t hai mẫu (biến kết cục liên tục, hai nhóm)
#   H0:               huyết áp tâm thu trung bình giống nhau ở nam và nữ
#   Diễn giải:        trung bình ~124 ở cả hai; p ~ 0.85 -> KHÔNG bác bỏ H0. Không có
#                     bằng chứng về khác biệt giới tính ở huyết áp tâm thu.
