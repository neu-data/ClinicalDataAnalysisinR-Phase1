# Tôi Nên Sử Dụng Kiểm Định Thống Kê Nào?

*Một hướng dẫn quyết định thực hành cho Phân tích Dữ liệu Lâm sàng trong R — Phase I (Neudata)*

Phần khó nhất của một phân tích thường là **chọn đúng phương pháp**, chứ không phải viết mã R. Hãy bắt đầu từ câu hỏi và *loại* biến liên quan, rồi phương pháp gần như tự nó hiện ra. Sử dụng bảng bên dưới để tìm tình huống của bạn, sau đó đọc ghi chú ngắn tương ứng ở phía dưới.

Xuyên suốt, bộ dữ liệu của chúng ta được đọc vào R với tên `clinical_data` (430 bệnh nhân).

---

## Bảng quyết định

| Tình huống nghiên cứu | Phương pháp thông dụng | Ví dụ (các biến của chúng ta) | Giả định chính (diễn đạt đơn giản) |
|---|---|---|---|
| Biến kết cục liên tục, **2 nhóm độc lập** | kiểm định t (tham số) hoặc Wilcoxon rank-sum (phi tham số) | `systolic_bp` theo `sex` (Female vs Male) | Các quan sát độc lập; biến kết cục xấp xỉ chuẩn *trong từng nhóm* đối với kiểm định t; độ phân tán tương tự. Dùng Wilcoxon nếu lệch hoặc cỡ mẫu nhỏ. |
| Biến kết cục liên tục, **>2 nhóm** | ANOVA một chiều (tham số) hoặc Kruskal–Wallis (phi tham số) | `BMI` theo `hospital` (5 cơ sở) | Tính độc lập; phần dư xấp xỉ chuẩn; phương sai tương tự giữa các nhóm. Dùng Kruskal–Wallis nếu không đạt. |
| **Hai biến phân loại** | kiểm định chi bình phương, hoặc kiểm định chính xác Fisher khi tần số nhỏ | `hypertension` (Yes/No) theo `diabetes` (Yes/No) | Các quan sát độc lập; tần số kỳ vọng > 5 trong (hầu hết) mọi ô. Dùng Fisher khi tần số kỳ vọng nhỏ. |
| **Hai biến liên tục** | tương quan — Pearson (tham số) hoặc Spearman (phi tham số) | `age` vs `systolic_bp` | Pearson: quan hệ tuyến tính, xấp xỉ chuẩn, không có giá trị ngoại lai mạnh. Spearman cho dữ liệu đơn điệu/lệch. |
| Biến kết cục liên tục **+ các yếu tố dự báo** | hồi quy tuyến tính | `systolic_bp ~ age + BMI` | Tính tuyến tính; các quan sát độc lập; phần dư xấp xỉ chuẩn, phương sai không đổi. |
| Biến kết cục nhị phân **+ các yếu tố dự báo** | hồi quy logistic | `hypertension ~ age + BMI` | Các quan sát độc lập; biến kết cục là 0/1; đủ số biến cố trên mỗi yếu tố dự báo (quy tắc kinh nghiệm ~10). |
| **Biến kết cục thời gian đến biến cố** | Kaplan–Meier (mô tả) / hồi quy Cox (hiệu chỉnh) | `Surv(time_to_event, outcome) ~ treatment` | Các quan sát độc lập; kiểm duyệt không liên quan đến biến kết cục; Cox giả định nguy cơ tỷ lệ. |

**Quy tắc kinh nghiệm:** các kiểm định *tham số* (kiểm định t, ANOVA, Pearson) giả định dữ liệu phân phối xấp xỉ chuẩn; các kiểm định *phi tham số* (Wilcoxon, Kruskal–Wallis, Spearman) đưa ra các giả định yếu hơn và an toàn hơn cho dữ liệu lệch, cỡ mẫu nhỏ, hoặc biến kết cục thứ bậc.

---

## Ghi chú ngắn về từng kiểm định

### kiểm định t / Wilcoxon rank-sum — biến kết cục liên tục, hai nhóm
- **Khi nào:** so sánh trung bình của một đại lượng liên tục giữa hai nhóm độc lập.
- **Giả định:** các quan sát độc lập; đối với kiểm định t, biến kết cục nên xấp xỉ chuẩn trong từng nhóm với độ phân tán tương tự. Nếu dữ liệu lệch hoặc cỡ mẫu nhỏ, ưu tiên Wilcoxon (so sánh hạng, không so sánh trung bình).
- **Tham số vs phi tham số:** kiểm định t (trung bình) vs Wilcoxon (trung vị / hạng).
```r
# Compare systolic BP between women and men
t.test(systolic_bp ~ sex, data = clinical_data)
wilcox.test(systolic_bp ~ sex, data = clinical_data)   # non-parametric alternative
```

### ANOVA / Kruskal–Wallis — biến kết cục liên tục, nhiều hơn hai nhóm
- **Khi nào:** so sánh một đại lượng liên tục giữa ba nhóm trở lên.
- **Giả định:** tính độc lập; phần dư xấp xỉ chuẩn; phương sai tương tự giữa các nhóm. Kruskal–Wallis nới lỏng giả định về tính chuẩn.
- **Tham số vs phi tham số:** ANOVA (trung bình) vs Kruskal–Wallis (hạng). Một kết quả có ý nghĩa cho bạn biết *một số* nhóm khác biệt — hãy theo dõi bằng các so sánh từng cặp.
```r
# Compare BMI across the five hospitals
anova_model <- aov(BMI ~ hospital, data = clinical_data)
summary(anova_model)
kruskal.test(BMI ~ hospital, data = clinical_data)      # non-parametric alternative
```

### kiểm định chi bình phương / chính xác Fisher — hai biến phân loại
- **Khi nào:** kiểm tra xem hai biến phân loại có liên quan với nhau hay không (tức là phân bố của một biến có khác nhau giữa các mức của biến kia hay không).
- **Giả định:** các quan sát độc lập; tần số ô kỳ vọng trên ~5 để xấp xỉ chi bình phương đáng tin cậy. Khi tần số kỳ vọng nhỏ (bảng thưa, hạng mục hiếm), hãy dùng kiểm định chính xác Fisher thay thế.
- **Tham số vs phi tham số:** không áp dụng theo nghĩa thông thường — chi bình phương vốn đã là một kiểm định cho tần số; Fisher là phiên bản chính xác cho cỡ mẫu nhỏ của nó.
```r
# Is hypertension associated with diabetes?
table(clinical_data$hypertension, clinical_data$diabetes)
chisq.test(clinical_data$hypertension, clinical_data$diabetes)
fisher.test(clinical_data$hypertension, clinical_data$diabetes)   # when counts are small
```

### Tương quan (Pearson / Spearman) — hai biến liên tục
- **Khi nào:** đo lường độ mạnh và chiều của liên hệ giữa hai đại lượng liên tục. Tương quan mô tả liên hệ, không phải nguyên nhân.
- **Giả định:** Pearson giả định một quan hệ xấp xỉ tuyến tính, xấp xỉ chuẩn và không có giá trị ngoại lai chiếm ưu thế; Spearman chỉ cần một quan hệ đơn điệu và bền vững với độ lệch và giá trị ngoại lai.
- **Tham số vs phi tham số:** Pearson (tuyến tính, trên giá trị) vs Spearman (đơn điệu, trên hạng).
```r
# Association between age and systolic BP
cor.test(clinical_data$age, clinical_data$systolic_bp, method = "pearson")
cor.test(clinical_data$age, clinical_data$systolic_bp, method = "spearman")
```

### hồi quy tuyến tính — biến kết cục liên tục với các yếu tố dự báo
- **Khi nào:** mô hình hóa một biến kết cục liên tục từ một hoặc nhiều yếu tố dự báo, và thu được một ước lượng hiệu ứng đã hiệu chỉnh cho từng yếu tố.
- **Giả định:** một quan hệ xấp xỉ tuyến tính; các quan sát độc lập; phần dư xấp xỉ chuẩn với phương sai không đổi. Kiểm tra bằng các biểu đồ chẩn đoán (`plot(model)`).
```r
# Systolic BP explained by age and BMI
model <- lm(systolic_bp ~ age + BMI, data = clinical_data)
summary(model)
```

### hồi quy logistic — biến kết cục nhị phân với các yếu tố dự báo
- **Khi nào:** mô hình hóa một biến kết cục có/không (0/1) và ước lượng các yếu tố dự báo thay đổi odds như thế nào. Kết quả được báo cáo dưới dạng **tỷ số chênh (OR)**.
- **Giả định:** các quan sát độc lập; biến kết cục là nhị phân; một quan hệ xấp xỉ tuyến tính giữa các yếu tố dự báo và *log-odds*; đủ số biến cố trên mỗi yếu tố dự báo.
```r
# Odds of hypertension by age and BMI
# First make the Yes/No outcome a factor (No = reference), as glm needs 0/1 or a factor
clinical_data$hypertension <- factor(clinical_data$hypertension, levels = c("No", "Yes"))
model <- glm(hypertension ~ age + BMI, data = clinical_data, family = binomial)
summary(model)
```

### Kaplan–Meier / hồi quy Cox — biến kết cục thời gian đến biến cố
- **Khi nào:** biến kết cục là *thời gian cho đến khi xảy ra một biến cố* (ở đây là một biến cố tim mạch hoặc tử vong), và một số bệnh nhân bị kiểm duyệt (biến cố chưa quan sát được). Các đường cong Kaplan–Meier mô tả sống còn theo thời gian; hồi quy Cox cho các **tỷ số nguy cơ (HR)** đã hiệu chỉnh.
- **Giả định:** các quan sát độc lập; kiểm duyệt không liên quan đến tiên lượng; Cox thêm vào giả định nguy cơ tỷ lệ (hiệu ứng xấp xỉ không đổi theo thời gian).
```r
library(survival); library(survminer)
# Describe survival by treatment group
km <- survfit(Surv(time_to_event, outcome) ~ treatment, data = clinical_data)
ggsurvplot(km, pval = TRUE)
# Adjusted hazard ratio
cox <- coxph(Surv(time_to_event, outcome) ~ treatment, data = clinical_data)
summary(cox)
```

---

> **Ghi chú kết thúc.** Một giá trị p **không** phải là độ lớn hiệu ứng. Nó chỉ cho bạn biết dữ liệu tương thích đến mức nào với "không có hiệu ứng" — chứ không cho biết một hiệu ứng lớn hay có ý nghĩa lâm sàng đến đâu. Luôn báo cáo **ước lượng** (chênh lệch trung bình, tỷ số chênh, tỷ số nguy cơ, tương quan) **cùng với khoảng tin cậy 95% của nó**, và diễn giải nó theo thuật ngữ lâm sàng.
