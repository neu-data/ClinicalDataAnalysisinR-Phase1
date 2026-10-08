# Bắt Đầu Từ Câu Hỏi, Không Phải Từ Mã Lệnh

*Khung tư duy phân tích: Phân tích Dữ liệu Lâm sàng trong R - Phase I (Neudata)*

Người mới bắt đầu thường hỏi, *"Lệnh R cho việc này là gì?"* Các nhà phân tích giàu kinh nghiệm hỏi, *"Câu hỏi của tôi là gì, và tôi có loại dữ liệu nào?"* Lệnh là bước **cuối cùng**, không phải bước đầu tiên. Nếu bạn hiểu **tại sao** một phương pháp được sử dụng, mã R trở thành một chi tiết nhỏ và an toàn. Nếu bạn chỉ sao chép các lệnh, cuối cùng bạn sẽ áp dụng đúng mã cho sai câu hỏi, và nhận được một câu trả lời tự tin nhưng sai.

Đây là quy trình mà mọi phân tích tốt đều tuân theo, từ câu hỏi đến câu văn được công bố.

---

## Khung tư duy (đọc từ trên xuống dưới)

```
        Research question
               │
            Outcome
               │
      Exposure / predictors
               │
         Variable types
               │
          Study design
               │
       Descriptive analysis
               │
          Visualisation
               │
       Statistical method
               │
     Assumptions / diagnostics
               │
  Effect estimate + uncertainty
               │
         Interpretation
               │
      Scientific reporting
```

Mỗi bước dưới đây nói **cần làm gì** và đưa ra một **ví dụ lâm sàng** từ `clinical_data`.

---

### 1. Câu hỏi nghiên cứu
Nêu một câu hỏi cụ thể, có thể trả lời được trước khi chạm vào R. Các câu hỏi mơ hồ ("xem qua dữ liệu") tạo ra các phân tích mơ hồ.
- *Ví dụ:* "BMI có liên quan đến huyết áp không?"

### 2. Biến kết cục
Xác định điều duy nhất mà bạn đang cố gắng giải thích hoặc dự báo, biến phụ thuộc.
- *Ví dụ:* `systolic_bp` (huyết áp tâm thu).

### 3. Yếu tố phơi nhiễm / yếu tố dự báo
Nêu tên yếu tố phơi nhiễm chính mà bạn quan tâm và bất kỳ yếu tố dự báo nào khác bạn sẽ xem xét.
- *Ví dụ:* yếu tố dự báo chính `BMI`; bạn có thể hiệu chỉnh cho `age` và `sex` về sau.

### 4. Loại biến
Phân loại từng biến: liên tục, nhị phân, phân loại, hay thời gian đến biến cố. Chỉ riêng bước này thường quyết định phương pháp.
- *Ví dụ:* `systolic_bp` liên tục, `BMI` liên tục → một quan hệ giữa hai biến liên tục.

### 5. Thiết kế nghiên cứu
Lưu ý dữ liệu phát sinh như thế nào (cắt ngang, đoàn hệ, so sánh các nhóm) và liệu các quan sát có độc lập hay không. Thiết kế định hình những gì bạn có thể khẳng định.
- *Ví dụ:* bộ dữ liệu lâm sàng cắt ngang; bệnh nhân độc lập; chúng ta có thể mô tả **liên hệ**, không phải nhân quả.

### 6. Thống kê mô tả
Tóm tắt trước khi mô hình hóa. Trung bình, trung vị, khoảng, tần số và tỷ lệ khuyết cho bạn biết dữ liệu có hợp lý hay không và các giả định có thực tế hay không.
- *Ví dụ:* `summary(clinical_data$systolic_bp)` và `summary(clinical_data$BMI)`; một bảng `gtsummary` của các biến chính.

### 7. Trực quan hóa
Vẽ quan hệ. Một hình ảnh tiết lộ hình dạng, giá trị ngoại lai và độ lệch mà các con số che giấu, và hướng dẫn lựa chọn giữa các phương pháp tham số và phi tham số.
- *Ví dụ:* một biểu đồ phân tán của `BMI` (x) theo `systolic_bp` (y) với một đường làm mượt.

### 8. Phương pháp thống kê
Chọn phương pháp khớp với loại biến và thiết kế, không phải phương pháp mà bạn tình cờ nhớ được. (Xem *Hướng dẫn Quyết định Kiểm định Thống kê*.)
- *Ví dụ:* biến kết cục liên tục với một yếu tố dự báo liên tục → **hồi quy tuyến tính**, `lm(systolic_bp ~ BMI, data = clinical_data)`.

### 9. Giả định / chẩn đoán
Kiểm tra rằng các giả định của phương pháp có được thỏa mãn, tính chuẩn, tính tuyến tính, phương sai không đổi, tần số ô kỳ vọng, nguy cơ tỷ lệ, tùy theo tình huống. Báo cáo trung thực nếu chúng không thỏa và điều chỉnh.
- *Ví dụ:* các biểu đồ phần dư cho mô hình tuyến tính (`plot(model)`); cân nhắc một phép biến đổi hoặc một phương án bền vững/phi tham số nếu các giả định thất bại.

### 10. Ước lượng hiệu ứng + độ bất định
Báo cáo độ lớn của hiệu ứng **cùng với một khoảng tin cậy**, không chỉ một giá trị p. Ước lượng là thông điệp lâm sàng; KTC là sự trung thực của bạn về độ chính xác.
- *Ví dụ:* độ dốc từ `lm()`: ví dụ mmHg tăng lên của huyết áp tâm thu trên mỗi đơn vị BMI, cùng với KTC 95% của nó (`confint(model)`).

### 11. Diễn giải
Chuyển ước lượng thành ngôn ngữ lâm sàng, trong bối cảnh. Điều này có ý nghĩa gì đối với một bệnh nhân hay một quần thể?
- *Ví dụ:* "Mỗi đơn vị BMI liên quan đến áp lực tâm thu cao hơn X mmHg, phù hợp với việc tình trạng thừa mỡ góp phần làm tăng huyết áp."

### 12. Trình bày báo cáo khoa học
Viết các câu Phương pháp và Kết quả mà người đọc có thể hiểu được, ước lượng, KTC, phương pháp, không bao giờ là kết quả console thô.
- *Ví dụ:* "Trong hồi quy tuyến tính, BMI liên quan với huyết áp tâm thu (β = X mmHg mỗi kg/m², 95% CI …)."

> **Xuyên suốt: hiểu TẠI SAO, đừng chỉ sao chép.** Cùng ba dòng R có ý nghĩa khác nhau cho các câu hỏi khác nhau. Biết tại sao phương pháp phù hợp là điều biến kết quả thành bằng chứng.

---

## Ví dụ minh họa đầy đủ

**Câu hỏi:** *Những yếu tố nào liên quan đến tăng huyết áp?*

1. **Câu hỏi nghiên cứu**: Những yếu tố nào của bệnh nhân liên quan đến việc bị tăng huyết áp?
2. **Biến kết cục**: `hypertension` (Yes/No).
3. **Yếu tố dự báo**: `age`, `sex`, `BMI` (các ứng viên được gợi ý bởi kiến thức lâm sàng).
4. **Loại biến**: biến kết cục **nhị phân**; `age` và `BMI` liên tục; `sex` phân loại.
5. **Thiết kế nghiên cứu**: cắt ngang; bệnh nhân độc lập; chỉ liên hệ, không phải nhân quả.
6. **Thống kê mô tả**: tỷ lệ có tăng huyết áp (`table(clinical_data$hypertension)`); so sánh tuổi và BMI ở nhóm có so với không có, ví dụ một bảng `gtsummary`.
7. **Trực quan hóa**: biểu đồ hộp của `age` và của `BMI` theo trạng thái `hypertension` để xem các nhóm có tách biệt hay không.
8. **Phương pháp thống kê**, biến kết cục nhị phân với vài yếu tố dự báo → **hồi quy logistic**:
   ```r
   # make the Yes/No outcome a factor first (No = reference)
   clinical_data$hypertension <- factor(clinical_data$hypertension, levels = c("No", "Yes"))
   model <- glm(hypertension ~ age + sex + BMI,
                data = clinical_data, family = binomial)
   ```
9. **Giả định / chẩn đoán**, các quan sát độc lập; đủ số biến cố trên mỗi yếu tố dự báo; quan hệ xấp xỉ tuyến tính trên thang log-odds; kiểm tra các điểm có ảnh hưởng.
10. **Ước lượng hiệu ứng + độ bất định**, tỷ số chênh cùng KTC 95%:
    ```r
    library(broom)
    tidy(model, exponentiate = TRUE, conf.int = TRUE)
    ```
11. **Diễn giải**: ví dụ tuổi cao hơn và BMI cao hơn liên quan đến odds tăng đối với tăng huyết áp; một yếu tố dự báo có KTC đi qua 1 thì không liên quan một cách rõ ràng.
12. **Trình bày báo cáo khoa học**, "Trong hồi quy logistic đa biến, tuổi và BMI liên quan độc lập với tăng huyết áp (tỷ số chênh cùng KTC 95% được báo cáo), trong khi giới tính thì không."

---

Mười hai bước, một thói quen: **quyết định bạn đang hỏi gì và dữ liệu của bạn là gì, thì phương pháp, và sau đó là R, sẽ theo sau.** Đó là điều phân biệt một phân tích mà bạn có thể bảo vệ với một lệnh mà bạn chỉ đơn thuần chạy.
