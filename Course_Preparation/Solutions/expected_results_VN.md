# Kết quả Mong đợi — Đáp án Tham chiếu (Giảng viên / Tự kiểm tra)

Tất cả các con số dưới đây đến từ việc chạy mã lệnh được cung cấp trên `clinical_data_clean.csv`
(và `clinical_data_raw.csv` cho các phép kiểm tra dữ liệu thô). Chúng có thể tái lập được từ
hạt giống ngẫu nhiên (random seed) cố định trong `Data/generate_precourse_data.py`. Hãy sử dụng chúng để kiểm tra rằng
bản cài đặt và mã lệnh của một học viên đang tạo ra các đáp án đúng.

## Tệp thô (`clinical_data_raw.csv`)
- Số hàng: **433**; số bệnh nhân duy nhất: **430**; số hàng trùng lặp chính xác: **3**
- Giá trị khuyết theo từng cột: `BMI` 9, `alcohol_use` 12, `diastolic_bp` 5, `glucose` 22, `cholesterol` 18, `followup_date` 7
- Các cách mã hóa `sex` hiện có: `f, F, female, Female, m, M, male, Male`

## Tệp sạch (`clinical_data_clean.csv`)
- Số hàng: **430**; số biến: **20**
- Tuổi trung bình: **54.2** năm (SD 12.5)
- BMI trung vị: **26.6** kg/m² (IQR 23.4–29.6)
- Tỷ lệ nữ: **54.7 %**
- Tỷ lệ hiện mắc tăng huyết áp: **36.0 %**
- Tỷ lệ hiện mắc đái tháo đường: **16.0 %**
- Tỷ lệ được điều trị: **51.2 %**
- Tỷ lệ biến cố trong theo dõi: **28.4 %**
- Huyết áp tâm thu trung bình: Nữ **124.3**, Nam **124.5** mmHg

## Các kiểm định thống kê
| Kiểm định | Kết quả |
|------|--------|
| kiểm định t, `systolic_bp` theo `sex` | t = −0.19, df = 422.6, **p = 0.85** (không có ý nghĩa) |
| Chi bình phương, `hypertension` × `diabetes` | χ² = 25.98, df = 1, **p < 0.001** (có ý nghĩa) |
| Tương quan, `age` so với `systolic_bp` | r = **0.55**, p < 0.001 |

## Hồi quy logistic — `hypertension ~ age + sex + BMI` (ví dụ Phần K)
| Số hạng | OR | KTC 95% | p |
|------|----|--------|---|
| age | 1.09 | 1.07–1.12 | < 0.001 |
| sex (Male) | 1.20 | 0.76–1.90 | 0.43 |
| BMI | 1.16 | 1.10–1.22 | < 0.001 |

## Hồi quy logistic — `hypertension ~ age + sex + BMI + diabetes`
| Số hạng | OR | KTC 95% | p |
|------|----|--------|---|
| age | 1.09 | 1.07–1.11 | < 0.001 |
| sex (Male) | 1.17 | 0.74–1.86 | 0.49 |
| BMI | 1.15 | 1.09–1.21 | < 0.001 |
| diabetes (Yes) | 1.96 | 1.06–3.65 | 0.03 |

## Mô hình Cox — `Surv(time_to_event, outcome) ~ age + diabetes + hypertension + treatment`
(cấp độ tham chiếu cho treatment = Untreated)
| Số hạng | HR | KTC 95% | p |
|------|----|--------|---|
| age | 1.05 | 1.03–1.07 | < 0.001 |
| diabetes (Yes) | 2.21 | 1.46–3.33 | < 0.001 |
| hypertension (Yes) | 1.65 | 1.07–2.56 | 0.03 |
| treatment (Treated) | 0.55 | 0.36–0.85 | 0.007 |

**Diễn giải chính:** tuổi cao hơn, đái tháo đường và tăng huyết áp làm tăng nguy cơ
của biến cố trong theo dõi; việc **được điều trị làm giảm khoảng một nửa** nguy cơ (HR 0.55).
