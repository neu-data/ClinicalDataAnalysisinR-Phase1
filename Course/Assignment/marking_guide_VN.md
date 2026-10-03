# Hướng dẫn chấm điểm (Dành cho giảng viên)

## Bài tập lớn cuối khóa (làm tại nhà) — Phân tích Dữ liệu Lâm sàng trong R, Giai đoạn I

**Khóa học:** Phân tích Dữ liệu Lâm sàng trong R — Giai đoạn I — Vương Mỹ Lượng (Chuyên gia Thống kê Sinh học Cao cấp, giảng viên chính) và Bernard Isekah Osang'ir (Chuyên gia Thống kê Sinh học Cao cấp), Neudata (*#ClearDataClearImpact*)
**Tổng:** 100 điểm

Hướng dẫn này cung cấp một khung chấm điểm có trọng số, một bảng đáp án với các kết quả chuẩn, một danh sách trừ điểm cho các lỗi thường gặp, và các dải xếp loại. Hãy chấm dựa trên **phương pháp đúng và diễn giải hợp lý**, chứ không phải trên việc khớp chính xác đến chữ số thập phân thứ hai — phiên bản gói và R khác nhau sẽ làm dịch chuyển các chữ số thập phân một cách không đáng kể. Hãy tưởng thưởng cho các quyết định được biện giải và ghi chép tốt, ngay cả khi chúng khác biệt đôi chút so với đáp án mẫu.

### Tóm tắt trọng số

| # | Thành phần | Điểm |
|---|-----------|------:|
| 1 | Nhập & làm sạch dữ liệu | 20 |
| 2 | Thống kê mô tả & Bảng 1 | 15 |
| 3 | Các hình | 10 |
| 4 | Kiểm định thống kê | 15 |
| 5 | Mô hình hóa hồi quy | 20 |
| 6 | Diễn giải & viết phần Kết quả | 15 |
| 7 | Tính tái lập & chất lượng mã | 5 |
| | **Tổng** | **100** |

---

## Khung chấm điểm theo thành phần

### 1. Nhập & làm sạch dữ liệu — 20 điểm

| Tiêu chí phụ | Điểm | Đủ điểm | Một phần | Không điểm |
|---|---:|---|---|---|
| Nhập tệp thô & kiểm tra | 3 | Đọc tệp csv/xlsx **thô**; kiểm tra cấu trúc/kích thước; ghi chú các cột bị sai kiểu do mã đại diện | Nhập được nhưng không kiểm tra / không bình luận về kiểu | Bắt đầu từ tệp đã làm sạch, hoặc nhập thất bại |
| Loại bỏ 3 bản trùng lặp → 1.500 | 3 | Loại bỏ bản trùng lặp, xác nhận **1.500 bệnh nhân duy nhất**, báo cáo số đã loại | Khử trùng lặp nhưng không kiểm chứng/báo cáo | Còn để lại bản trùng lặp (1.503 hàng) |
| Mã đại diện khuyết thiếu → NA | 4 | Tất cả ô trống/`NA`/`999`/`-99` được chuyển thành `NA` ở đúng các cột | Xử lý một số mã đại diện, bỏ sót số khác | Để mã đại diện lại như những con số (ví dụ 999 trong glucose) |
| Chuẩn hóa các hạng mục không nhất quán | 4 | `sex`, tất cả các biến nhị phân hỗn hợp, và các trường khoảng trắng được đồng bộ nhất quán | Đồng bộ một phần; còn sót các biến thể | Không mã hóa lại; để lẫn F/Male/1/0 |
| Rà soát các giá trị bất khả thi | 3 | Xác định & xử lý có biện giải age 0/200, SBP 0/700, DBP 5, weight 7, height 17 | Xử lý một số; không nêu quy tắc | Để các giá trị không hợp lý trong phân tích |
| Phân tích ngày tháng | 1 | `enroll_date` được phân tích thành Date trên cả 3 định dạng | Phân tích một phần | Không phân tích |
| Mã hóa lại/tạo biến dẫn xuất + mức tham chiếu factor | 2 | BMI được tính lại; mức tham chiếu hợp lý; education/PA có thứ tự | Làm được một phần | Không làm gì |

**Được điểm:** dùng `na_if()` / `case_when()` một cách gọn gàng; báo cáo số đếm ở mỗi bước; một quy tắc được ghi chép ("các giá trị nằm ngoài khoảng sinh lý được đặt thành NA").
**Mất điểm:** loại bỏ nguyên các hàng có bất kỳ NA nào trước khi làm sạch; "sửa" bằng cách đoán giá trị mà không biện giải; tin vào `bmi` được cung cấp sẵn.

---

### 2. Thống kê mô tả & Bảng 1 — 15 điểm

| Tiêu chí phụ | Điểm | Đủ điểm | Một phần | Không điểm |
|---|---:|---|---|---|
| Tóm tắt phù hợp theo kiểu biến | 4 | Trung bình±SD hoặc trung vị[IQR] cho biến số; n(%) cho biến hạng mục | Lựa chọn lẫn lộn/không phù hợp | Chỉ đổ dữ liệu thô |
| Bảng 1 phân tầng theo `treatment_uptake` | 5 | Bảng gọn gàng, có nhãn, phân tầng theo kết cục | Có dựng nhưng không phân tầng, hoặc không nhãn | Không có Bảng 1 |
| Cột kiểm định so sánh | 3 | Các giá trị p hợp lý cho từng biến được đưa vào | Một số kiểm định sai/thiếu | Không có |
| Chất lượng công bố & xuất tệp | 3 | Đơn vị/nhãn dễ đọc; đã xuất (docx/html/png) | Định dạng sơ sài | Không xuất |

**Được điểm:** `gtsummary::tbl_summary() |> add_p()` (hoặc flextable) với nhãn và đơn vị rõ ràng.
**Mất điểm:** Bảng 1 được dựng trên toàn bộ 1.500 thay vì cohort đã làm sạch; tỷ lệ phần trăm không tính đến giá trị khuyết thiếu; giá trị không làm tròn (ví dụ 47,382%).

---

### 3. Các hình — 10 điểm

| Tiêu chí phụ | Điểm | Đủ điểm | Một phần | Không điểm |
|---|---:|---|---|---|
| Hai hình phù hợp | 4 | ≥2 hình giải quyết được câu hỏi | Chỉ một hình | Không có |
| Chất lượng (tiêu đề, nhãn trục, đơn vị, dễ đọc) | 3 | Gắn nhãn đầy đủ, dễ đọc, chọn loại biểu đồ hợp lý | Thiếu nhãn/đơn vị | Không nhãn |
| Xuất ở 300 dpi | 3 | Có bằng chứng `ggsave(..., dpi = 300)` (hoặc tương đương) | Có xuất nhưng không đặt dpi | Không xuất |

**Được điểm:** forest plot của các aOR; biểu đồ cột việc tiếp nhận theo yếu tố quyết định kèm số đếm/%; boxplot của điểm kiến thức theo việc tiếp nhận.
**Mất điểm:** ggplot mặc định không nhãn; ảnh chụp màn hình thay vì tệp đã xuất; biểu đồ 3-D / biểu đồ tròn.

---

### 4. Kiểm định thống kê — 15 điểm

| Tiêu chí phụ | Điểm | Đủ điểm | Một phần | Không điểm |
|---|---:|---|---|---|
| Giới hạn ở người đã chẩn đoán (`htn_diagnosed=="Yes"`) | 4 | Lọc còn ~**1.089**; báo cáo n | Lọc nhưng không báo cáo | Chạy kiểm định trên toàn bộ 1.500 |
| Chọn kiểm định đúng | 5 | Chi bình phương/Fisher cho biến hạng mục; t/Wilcoxon cho biến số; có xem xét giả định | Một số chỗ không khớp | Sai kiểm định xuyên suốt |
| Thực hiện & báo cáo đúng | 4 | Thống kê + giá trị p được báo cáo rõ ràng | Báo cáo chưa đầy đủ | Không báo cáo |
| Sàng lọc biến hợp lý | 2 | Các yếu tố quyết định tiềm năng được kiểm định | Chọn lựa tùy tiện | Không có |

**Được điểm:** dùng Fisher khi một ô thưa (ví dụ diabetes × uptake); dùng Wilcoxon khi phân phối bị lệch.
**Mất điểm:** dùng chi bình phương trên tần số kỳ vọng rất nhỏ mà không bình luận; dùng toàn bộ mẫu; giá trị p không nêu tên kiểm định.

---

### 5. Mô hình hóa hồi quy — 20 điểm

| Tiêu chí phụ | Điểm | Đủ điểm | Một phần | Không điểm |
|---|---:|---|---|---|
| Các mô hình logistic đơn biến | 4 | OR thô + KTC 95% cho từng biến dự báo | OR không có KTC | Không làm |
| Đặc tả mô hình đa biến | 5 | `glm(..., family=binomial)` với các yếu tố quyết định đã định trước, trên cohort đã chẩn đoán | Thiếu một số biến dự báo/đặc tả sai | Sai kết cục/quần thể |
| Kết quả trên thang OR | 5 | Các hệ số được **lấy lũy thừa** thành aOR kèm KTC 95% | OR không có KTC | **Log-odds được báo cáo như thể là OR** |
| Báo cáo số ca đầy đủ dữ liệu | 2 | Nêu ~**992** ca đầy đủ dữ liệu được dùng | Không báo cáo | — |
| Khả năng phân biệt của mô hình | 4 | AUC/thống kê C được báo cáo (~**0,71**) kèm bình luận ngắn | Báo cáo nhưng không bình luận | Không có |

**Được điểm:** `broom::tidy(model, exponentiate = TRUE, conf.int = TRUE)`; chọn mức tham chiếu sao cho các OR đọc lên trực quan; AUC qua `pROC`.
**Mất điểm:** hồi quy tuyến tính trên một kết cục nhị phân; đảo ngược kết cục (No là biến cố); đọc `coef()` thô như là tỷ số chênh; loại bỏ `diabetes` vì KTC rộng.

---

### 6. Diễn giải & viết phần Kết quả — 15 điểm

| Tiêu chí phụ | Điểm | Đủ điểm | Một phần | Không điểm |
|---|---:|---|---|---|
| Đọc đúng các aOR về mặt lâm sàng | 6 | Chiều hướng + độ lớn đúng; nêu tên các yếu tố quyết định độc lập | Một số chỗ đọc sai | Đảo ngược/sai xuyên suốt |
| Xử lý đúng trường hợp không có ý nghĩa thống kê | 3 | Khoảng cách được mô tả là NS / không kết luận được, **không phải** "không có tác động" | Diễn đạt thiếu chặt chẽ | "Khoảng cách không có tác động" |
| Phần Kết quả (250–400 từ, văn phong bản thảo) | 4 | Tích hợp dòng chảy cỡ mẫu, Bảng 1, mô hình; con số kèm KTC; trong giới hạn số từ | Có nhưng sơ sài / sai độ dài | Thiếu |
| Ý thức về độ chính xác / hạn chế | 2 | Ghi chú KTC rộng ở diabetes (nhóm nhỏ), yếu tố gây nhiễu (residence thô so với hiệu chỉnh) | Đề cập mơ hồ | Không có |

**Được điểm:** "Đái tháo đường có liên quan đến odds tiếp nhận cao hơn hơn ba lần (aOR 3,56, KTC 95% 1,46–9,61), mặc dù KTC rộng phản ánh một nhóm nhỏ bệnh nhân đái tháo đường."
**Mất điểm:** ngôn ngữ nhân quả ("sống ở thành thị gây ra việc tiếp nhận"); diễn giải NS như bằng chứng của việc không có liên quan; báo cáo OR mà không có KTC trong phần văn xuôi.

---

### 7. Tính tái lập & chất lượng mã — 5 điểm

| Tiêu chí phụ | Điểm | Đủ điểm | Một phần | Không điểm |
|---|---:|---|---|---|
| Chạy từ đầu đến cuối từ dữ liệu thô, phiên làm việc sạch | 2 | Chạy từ trên xuống, không có bước thủ công | Chạy được với vài chỉnh sửa nhỏ | Không chạy được |
| Đường dẫn tương đối / tính di động | 1 | Đường dẫn tương đối; không có đường dẫn riêng của máy | Lẫn lộn | **Đường dẫn tuyệt đối** (`C:\Users\...`) |
| Tính dễ đọc | 1 | Có chú thích, chia mục, nạp các gói ở đầu | Sơ sài | Không cấu trúc |
| Ghi lại môi trường | 1 | `sessionInfo()` / seed khi cần | Một phần | Không có |

**Mất điểm:** đường dẫn tuyệt đối cứng; `rm(list=ls())`/`setwd()` tới một thư mục cá nhân; các gói được dùng nhưng không bao giờ được nạp.

---

## Đáp án mẫu / Bảng đáp án

> Chấm cho **phương pháp đúng + diễn giải**. Các KTC và chiều hướng là ổn định; khác biệt ở chữ số thập phân thứ hai giữa các phiên bản R/gói là **có thể chấp nhận được**.

**Dòng chảy cỡ mẫu kỳ vọng**
- Đã nhập: **1.503** hàng →
- Sau khi loại bỏ 3 bản trùng lặp: **1.500** bệnh nhân duy nhất →
- Giới hạn ở người đã chẩn đoán tăng huyết áp (`htn_diagnosed == "Yes"`): **≈ 1.089** →
- Số ca đầy đủ dữ liệu trong mô hình hiệu chỉnh: **≈ 992**.
- Tỷ lệ tiếp nhận điều trị tổng thể ở người đã chẩn đoán: **≈ 47%**.

**Các tỷ số chênh hiệu chỉnh chuẩn (mô hình đa biến cuối cùng)**

| Biến dự báo | aOR | KTC 95% | p | Chiều hướng |
|---|---:|---|---|---|
| Age (mỗi năm tuổi) | **1,03** | 1,02–1,04 | <0,001 | ↑ tiếp nhận |
| Sex: Male (so với Female) | **0,74** | 0,56–0,97 | 0,031 | ↓ tiếp nhận (nữ giới thuận lợi hơn) |
| Education (xu hướng tuyến tính) | **1,96** | 1,39–2,77 | <0,001 | ↑ khi học vấn cao hơn |
| Residence: Urban (so với Rural) | **1,87** | 1,41–2,49 | <0,001 | ↑ tiếp nhận |
| Diabetes: Yes | **3,56** | 1,46–9,61 | 0,007 | ↑ tiếp nhận (tác động lớn nhất, KTC rộng nhất) |
| Tiền sử gia đình mắc HTN: Yes | **1,91** | 1,44–2,54 | <0,001 | ↑ tiếp nhận |
| Health insurance: Yes | **2,05** | 1,54–2,74 | <0,001 | ↑ tiếp nhận |
| Điểm kiến thức (mỗi điểm) | **1,10** | 1,06–1,14 | <0,001 | ↑ tiếp nhận |
| Khoảng cách đến cơ sở (mỗi km) | **0,98** | 0,96–1,01 | 0,128 | **NS** (xu hướng ↓) |

**Khả năng phân biệt của mô hình:** AUC ≈ **0,71** (chấp nhận được).

**Một diễn giải đúng cần nêu:**
- Các yếu tố quyết định độc lập của việc tiếp nhận: tuổi cao hơn, giới **nữ**, học vấn cao hơn, sống ở thành thị, đái tháo đường, tiền sử gia đình, bảo hiểm y tế, và kiến thức về tăng huyết áp nhiều hơn.
- **Đái tháo đường** có tác động lớn nhất (>3× odds) nhưng **KTC rộng nhất** (nhóm nhỏ) — một điểm dạy học về độ chính xác.
- **Khoảng cách** đi theo chiều hướng kỳ vọng (bảo hộ chống lại việc tiếp nhận) nhưng **không có ý nghĩa thống kê** sau khi hiệu chỉnh — hãy mô tả là không kết luận được, chứ không phải "không có tác động".
- Residence: so sánh OR thô với OR hiệu chỉnh minh họa **yếu tố gây nhiễu nhẹ**.

*Chấp nhận sự khác biệt hợp lý trong danh sách biến tiềm năng và cách mã hóa tham chiếu, miễn là các yếu tố quyết định cốt lõi đã định trước đều có mặt, các OR được lấy lũy thừa kèm KTC, và cohort đã chẩn đoán được sử dụng.*

---

## Các lỗi thường gặp và mức trừ điểm

| Lỗi | Trừ điểm |
|---|---|
| Để các mã đại diện `999` / `-99` / ô trống lại như những con số thực | **−4** (Thành phần 1) |
| Không loại bỏ bản trùng lặp (phân tích 1.503 hàng) | **−3** (Thành phần 1) |
| Để lại các giá trị bất khả thi (age 200, SBP 700, v.v.) | **−3** (Thành phần 1) |
| Phân tích toàn bộ **1.500** thay vì người đã chẩn đoán tăng huyết áp | **−4** (Thành phần 4) và lan truyền nếu mô hình cũng sai |
| Báo cáo **log-odds** thay vì các OR đã lấy lũy thừa | **−5** (Thành phần 5) |
| Đảo ngược kết cục / sai mức biến cố | **−3** (Thành phần 5) |
| Hồi quy tuyến tính trên kết cục nhị phân | **−5** (Thành phần 5) |
| Báo cáo OR mà không có KTC 95% | **−2 đến −3** (Thành phần 5/6) |
| Diễn giải một kết quả **không có ý nghĩa thống kê** là "không có tác động" | **−3** (Thành phần 6) |
| Ngôn ngữ nhân quả cho một mối liên quan cắt ngang | **−2** (Thành phần 6) |
| **Đường dẫn tệp tuyệt đối** / `setwd()` tới một thư mục cá nhân | **−1** (Thành phần 7) |
| Tập lệnh không chạy được từ đầu đến cuối | **−2** (Thành phần 7) |
| Không xuất Bảng 1 / các hình | **−3** (trải trên Thành phần 2 & 3) |

*Mức trừ điểm được giới hạn ở số điểm khả dụng của thành phần liên quan — một lỗi đơn lẻ không thể kéo một thành phần xuống dưới không.*

---

## Các dải xếp loại

| Dải | Điểm | Mô tả |
|---|---|---|
| **Xuất sắc (Distinction)** | 80–100 | Chuỗi xử lý có thể tái lập gọn gàng từ dữ liệu thô; đúng cohort và dòng chảy cỡ mẫu; Bảng 1 và các hình 300-dpi trau chuốt; các mô hình logistic được đặc tả đúng với các aOR đã lấy lũy thừa và KTC; có báo cáo AUC; diễn giải lâm sàng chính xác, thận trọng phù hợp và một phần Kết quả có cấu trúc tốt. |
| **Khá giỏi (Merit)** | 65–79 | Phân tích trọn vẹn từ đầu đến cuối hợp lý với việc làm sạch phần lớn đúng, đúng quần thể, và một mô hình hiệu chỉnh hợp lệ trên thang OR. Có các thiếu sót nhỏ (bỏ sót một mã đại diện, một phần Kết quả sơ sài, một kiểm định chọn sai) nhưng các kết luận là đúng. |
| **Đạt (Pass)** | 50–64 | Có thực hiện phân tích cốt lõi và về cơ bản đúng, nhưng có những điểm yếu đáng chú ý — làm sạch chưa đầy đủ, Bảng 1/các hình yếu, báo cáo KTC một phần, hoặc diễn giải quá mức. Cho thấy năng lực nhưng chưa trau chuốt. |
| **Trượt (Fail)** | <50 | Các lỗi nền tảng: sai quần thể, để lại mã đại diện/bản trùng lặp, báo cáo log-odds như là OR, mô hình tuyến tính trên kết cục nhị phân, hoặc một bài nộp không thể tái lập/không chạy được. |
