# Từ Điển Dữ Liệu: Bộ Dữ Liệu Lâm sàng Tiền khóa học

**Tệp:** `clinical_data_raw.csv` (lộn xộn), `clinical_data_clean.csv` (sẵn sàng để phân tích), `clinical_data_raw.xlsx` (bản sao Excel của tệp thô)

Đây là một bộ dữ liệu **hoàn toàn tổng hợp** được tạo ra để giảng dạy. Nó **không chứa dữ liệu bệnh nhân thật**. Nó mô tả 430 bệnh nhân trưởng thành được tuyển vào tại năm cơ sở chăm sóc ban đầu / bệnh viện, mỗi bệnh nhân được theo dõi tối đa 24 tháng cho một biến cố tim mạch hoặc tử vong.

> **Ghi chú về đơn vị:** `glucose` và `cholesterol` tính bằng **mmol/L** (đơn vị được dùng ở hầu hết các nơi trên thế giới). Glucose lúc đói ≥ 7.0 mmol/L và cholesterol toàn phần ≥ 5.0 mmol/L là các mốc tham chiếu lâm sàng thông dụng.

| # | Biến | Nhãn | Loại | Đơn vị / giá trị | Mô tả |
|---|----------|-------|------|----------------|-------------|
| 1 | `patient_id` | Mã định danh bệnh nhân | văn bản | P1000–P1429 | Mã ẩn danh duy nhất |
| 2 | `age` | Tuổi | số nguyên | năm (30–88) | Tuổi lúc nhập viện |
| 3 | `sex` | Giới tính | phân loại | Female / Male | Giới tính sinh học |
| 4 | `weight_kg` | Cân nặng | số | kilôgam | Cân nặng cơ thể được đo |
| 5 | `height_cm` | Chiều cao | số | xăng-ti-mét | Chiều cao được đo |
| 6 | `BMI` | Chỉ số khối cơ thể | số | kg/m² | `weight_kg / (height_cm/100)^2` |
| 7 | `smoking` | Tình trạng hút thuốc | phân loại | Never / Former / Current | Tự khai báo |
| 8 | `alcohol_use` | Sử dụng rượu | phân loại | None / Moderate / Heavy | Tự khai báo |
| 9 | `systolic_bp` | Huyết áp tâm thu | số nguyên | mmHg | Huyết áp tâm thu |
| 10 | `diastolic_bp` | Huyết áp tâm trương | số nguyên | mmHg | Huyết áp tâm trương |
| 11 | `hypertension` | Tăng huyết áp | phân loại | Yes / No | Tăng huyết áp đã được chẩn đoán |
| 12 | `diabetes` | Đái tháo đường | phân loại | Yes / No | Đái tháo đường đã được chẩn đoán |
| 13 | `glucose` | Glucose lúc đói | số | mmol/L | Glucose huyết tương lúc đói |
| 14 | `cholesterol` | Cholesterol toàn phần | số | mmol/L | Cholesterol huyết thanh toàn phần |
| 15 | `treatment` | Nhóm điều trị | phân loại | Treated / Untreated | Đã nhận điều trị hạ huyết áp |
| 16 | `hospital` | Bệnh viện tuyển bệnh | phân loại | 5 cơ sở | Địa điểm tuyển bệnh |
| 17 | `admission_date` | Ngày nhập viện | ngày | YYYY-MM-DD | Ngày ghi danh / nhập viện |
| 18 | `followup_date` | Ngày theo dõi | ngày | YYYY-MM-DD | Ngày theo dõi cuối hoặc ngày xảy ra biến cố |
| 19 | `outcome` | Biến cố theo dõi | số nguyên | 0 / 1 | 1 = biến cố tim mạch hoặc tử vong; 0 = không có biến cố (bị kiểm duyệt) |
| 20 | `time_to_event` | Thời gian đến biến cố | số | tháng (0–24) | Số tháng từ nhập viện đến biến cố hoặc kiểm duyệt |

## Các biến liên hệ với nhau như thế nào ("sự thật" được cài sẵn)

Dữ liệu được mô phỏng sao cho các mô hình thống kê tạo ra các kết quả **thực tế, có thể diễn giải** thay vì nhiễu:

- **Tăng huyết áp** trở nên nhiều khả năng hơn với **age** và **BMI** cao hơn, và ở các bệnh nhân có **diabetes**.
- **Đái tháo đường** được phản ánh mạnh mẽ trong **glucose** lúc đói (bệnh nhân đái tháo đường có glucose cao hơn nhiều).
- **Huyết áp** tăng theo tuổi, BMI và tăng huyết áp.
- **Điều trị** chủ yếu được cung cấp cho các bệnh nhân tăng huyết áp và cao tuổi hơn.
- **Biến cố theo dõi** (`outcome` / `time_to_event`) trở nên nhiều khả năng hơn với tuổi cao hơn, đái tháo đường và tăng huyết áp, và **điều trị làm giảm nguy cơ**.

Những mối liên hệ này là điều mà các phân tích của bạn trong khóa học sẽ *khám phá lại* từ dữ liệu.
