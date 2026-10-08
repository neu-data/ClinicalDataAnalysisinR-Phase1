# Các Vấn Đề Chất Lượng Dữ Liệu Cố Ý trong `clinical_data_raw.csv`

Dữ liệu lâm sàng thực tế **không bao giờ** sạch. Để làm cho các bài học làm sạch dữ liệu trở nên thực tế, chúng tôi
đã cố ý đưa vào các vấn đề dưới đây trong `clinical_data_raw.csv`. Mỗi
vấn đề đều là một *ví dụ dạy học*: bạn sẽ học cách **tìm** nó và **sửa** nó
trong bài học **04: Data Management**.

`clinical_data_clean.csv` là tệp tham chiếu gọn gàng với tất cả các vấn đề này đã được giải quyết.

---

### 1. Bản ghi trùng
- **3 hàng là bản sao chính xác** của các bệnh nhân khác (cùng `patient_id` và các giá trị).
- Do đó tệp thô có **433 hàng** nhưng chỉ có **430 bệnh nhân duy nhất**.
- **Phát hiện:** `sum(duplicated(clinical_data_raw))` hoặc `janitor::get_dupes()`.
- **Sửa:** `dplyr::distinct()`.

### 2. Giá trị khuyết
- Các giá trị đã bị loại bỏ ngẫu nhiên từ một số cột:
  `glucose` (22), `cholesterol` (18), `alcohol_use` (12), `BMI` (9),
  `followup_date` (7), `diastolic_bp` (5).
- **Phát hiện:** `colSums(is.na(clinical_data_raw))`.
- **Sửa:** quyết định theo từng biến, để nguyên là `NA`, dùng phân tích ca đầy đủ, hoặc gán giá trị. Trong khóa học này, chúng ta chỉ đơn giản giữ chúng là `NA` và để R bỏ qua chúng bằng `na.rm = TRUE`.

### 3. Mã hóa phân loại không nhất quán
- `sex` xuất hiện dưới dạng **Female, female, F, f, Male, male, M, m**.
- `hypertension` và `diabetes` trộn lẫn **Yes / No / yes / no / 1 / 0**.
- `smoking` chứa một giá trị chữ thường lạc lõng **"current"** bên cạnh "Current".
- **Phát hiện:** `table(clinical_data_raw$sex)`.
- **Sửa:** `dplyr::case_when()` / `forcats` để gộp về các nhãn nhất quán.

### 4. Giá trị bất khả thi
| Biến | Giá trị sai | Vì sao bất khả thi |
|----------|-----------|----------------|
| `age` | 219 | Không ai 219 tuổi |
| `age` | 2 | Một đứa trẻ 2 tuổi không phải là bệnh nhân người lớn |
| `height_cm` | 17 | 17 cm không phải là chiều cao của con người |
| `weight_kg` | 400 | Cân nặng cơ thể không hợp lý |
| `BMI` | 4.2 | BMI dưới ~12 là không thể sống sót |
| `systolic_bp` | 350 | Vượt xa mọi giá trị huyết áp thực tế |

- **Phát hiện:** `summary()`, `range()`, biểu đồ hộp, hoặc các phép kiểm tra logic như `age > 110`.
- **Sửa:** đặt các giá trị bất khả thi thành `NA` (chúng ta không thể biết giá trị thật).

### 5. Giá trị xét nghiệm cực đoan
- Giá trị `glucose` là **41 mmol/L** (glucose lúc đói thực tế hiếm khi trên ~30).
- Giá trị `cholesterol` là **−3.0 mmol/L** (một giá trị xét nghiệm không thể âm).
- **Phát hiện:** `summary()` / sắp xếp cột / biểu đồ hộp.
- **Sửa:** đặt thành `NA` (lỗi nhập liệu).

### 6. Ngày tháng không nhất quán
- Đối với **2 bệnh nhân**, `followup_date` **trước** `admission_date`.
- **Phát hiện:** `clinical_data_raw$followup_date < clinical_data_raw$admission_date`.
- **Sửa:** đặt ngày theo dõi bất khả thi thành `NA` (hoặc truy vấn nguồn).

---

## "Hợp đồng" làm sạch (một phiên bản sạch trông như thế nào)

Sau bài học 04, bạn sẽ có thể biến tệp thô thành một bộ dữ liệu mà:

1. có **430 bệnh nhân duy nhất** (đã loại bỏ bản ghi trùng);
2. sử dụng **các nhãn nhất quán** (`Female`/`Male`, `Yes`/`No`, `Never`/`Former`/`Current`);
3. **không có giá trị bất khả thi** (tuổi, chiều cao, cân nặng, BMI, huyết áp, xét nghiệm bất khả thi → `NA`);
4. **không có ngày theo dõi trước ngày nhập viện**;
5. có một **`BMI` được tính lại, nhất quán nội tại**.

Tệp `clinical_data_clean.csv` được cung cấp là đáp án tham chiếu.
