# Sổ tay Giảng viên & Hướng dẫn Điều phối

## Phân tích Dữ liệu Lâm sàng trong R — Giai đoạn I: Nhập môn R cho Nghiên cứu Lâm sàng

**Giảng viên:** Vương Mỹ Lượng (Chuyên gia Thống kê Sinh học Cao cấp, giảng viên chính) · Bernard Osang'ir (Chuyên gia Thống kê Sinh học Cao cấp)
**Đơn vị cung cấp:** Neudata · **#ClearDataClearImpact**
**Hình thức:** 5 buổi học buổi tối · mỗi Thứ Ba, 20:00 (giờ Việt Nam), 90 phút (~7,5 giờ tiếp xúc) · 8 tháng 9 – 6 tháng 10 năm 2026 · workshop lập trình trực tiếp (live-coding)
**Nghiên cứu trường hợp:** *Các yếu tố quyết định việc Tiếp nhận Điều trị Tăng huyết áp ở Người trưởng thành khám tại các Cơ sở Chăm sóc Sức khỏe Ban đầu* (nghiên cứu cắt ngang đa trung tâm mô phỏng, 1.500 người trưởng thành, 6 cơ sở PHC)

---

## Cách sử dụng sổ tay này

Đây là một **hướng dẫn điều phối**, không phải một cuốn giáo trình. Nó được viết cho một giảng viên (hoặc đồng điều phối viên) giảng dạy khóa học lần đầu. Với mỗi buổi bạn sẽ có: một kế hoạch phân bổ thời gian, các mục tiêu của buổi, mạch xuyên suốt của việc giảng dạy, một hướng dẫn chi tiết phần trình diễn trực tiếp (`Scripts/dayN_demo.R`) kèm kết quả console dự kiến và các "lỗi giảng dạy" có chủ đích, những ngộ nhận thường gặp, các ghi chú diễn giải lâm sàng, các câu hỏi dự kiến từ khán giả kèm câu trả lời mẫu, và thế nào là thành công ở bài tập (`Practicals/dayN_exercise.R` → `Solutions/dayN_solution.R`).

Thứ tự đọc gợi ý trước khi bạn giảng dạy:
1. Sổ tay này, từ đầu đến cuối.
2. `Data/data_dictionary.md` — 36 biến và mọi khiếm khuyết chất lượng dữ liệu có chủ đích.
3. `References/key_findings.md` — các kết quả chuẩn mực mà bạn sẽ trích dẫn và dùng để chấm điểm.
4. Năm script trình diễn và năm script lời giải, chạy từ đầu đến cuối trên máy của chính bạn vào tối hôm trước.

**Quy ước trong sổ tay này:** `monospace` = thứ bạn gõ hoặc một tệp; *in nghiêng* = thứ bạn nói hoặc nhấn mạnh bằng lời; "Surface this" (Làm rõ điều này) = một thời điểm để chậm lại và nói ra tường minh.

---

## 1. Tổng quan khóa học

### Mục đích
Trang bị cho các bác sĩ lâm sàng và nhà nghiên cứu y học **không có kinh nghiệm lập trình trước đó** khả năng tự thực hiện một phân tích dữ liệu lâm sàng hoàn chỉnh, tái lập được trong R — từ việc nhập một bộ dữ liệu lộn xộn đến việc báo cáo các tỷ số chênh hiệu chỉnh trong một phần Kết quả sẵn sàng cho bản thảo. Khóa học được xây dựng có chủ đích xoay quanh **một nghiên cứu thực tế duy nhất từ đầu đến cuối**, để mọi kỹ năng đều được học trong bối cảnh lâm sàng, không bao giờ ở dạng trừu tượng.

### Đối tượng
Bác sĩ, điều dưỡng, nhà nghiên cứu lâm sàng, chuyên gia y tế công cộng, bác sĩ nội trú, học viên cao học, và điều phối viên thử nghiệm lâm sàng. **Giả định không có nền tảng lập trình.** Nhiều người sẽ lo lắng về "lập trình". Nhiệm vụ đầu tiên của bạn ở Buổi 1 là làm giảm bớt sự lo lắng đó.

### 13 mục tiêu học tập
Đến cuối khóa học, học viên sẽ có thể:

1. Điều hướng RStudio và chạy mã lệnh R từ một script và console.
2. Sử dụng các đối tượng (object), vector, hàm, và gói (package).
3. Nhập dữ liệu lâm sàng từ CSV và Excel.
4. Kiểm tra một bộ dữ liệu và nhận ra các vấn đề về chất lượng dữ liệu.
5. Làm sạch văn bản phân loại, chuẩn hóa các mã hóa nhị phân, và xử lý các giá trị đại diện cho dữ liệu thiếu.
6. Kiểm định các giá trị lâm sàng so với các khoảng sinh lý hợp lý.
7. Mã hóa lại và tạo biến (ví dụ BMI, phân loại huyết áp) và đặt factor với các mức tham chiếu đúng.
8. Tính toán và diễn giải thống kê mô tả (xu hướng trung tâm, độ phân tán, tần số, bảng chéo).
9. Tạo ra một "Bảng 1" chất lượng xuất bản và các hình chất lượng tạp chí.
10. Chọn và chạy đúng kiểm định giả thuyết cho một câu hỏi cụ thể.
11. Khớp, diễn giải, và báo cáo hồi quy logistic đơn giản và đa biến dưới dạng tỷ số chênh kèm KTC 95%.
12. Kiểm tra các giả định của mô hình và khả năng phân biệt (VIF, tính tuyến tính, ảnh hưởng, AUC).
13. Làm việc theo cách tái lập được (projects, đường dẫn tương đối, các kết quả đã lưu, `set.seed()`, thông tin phiên).

### Cấu trúc năm buổi (mỗi buổi 90 phút)

| Buổi | Chủ đề (khớp với poster & bộ slide) | Ôn tập | Bài giảng + trình diễn | Bài tập | Sản phẩm chính |
|---------|-----------------------------------|-------|----------------|----------|-----------------|
| 1 | Nhập môn R & RStudio | ~10 phút | ~55 phút | ~20 phút | Dữ liệu đã nhập, kiểm tra lần đầu |
| 2 | Hiểu & Làm sạch Dữ liệu Lâm sàng | ~10 phút | ~55 phút | ~20 phút | `analysis_data.rds` (hợp đồng làm sạch) |
| 3 | Thống kê Mô tả, Bảng biểu & Hình | ~10 phút | ~55 phút | ~20 phút | Bảng 1 + các hình đã lưu |
| 4 | Các Kiểm định Thống kê Y học Thường gặp | ~10 phút | ~55 phút | ~20 phút | Kiểm định đúng được chọn & diễn giải |
| 5 | Nhập môn Hồi quy & Diễn giải Kết quả | ~10 phút | ~55 phút | ~20 phút | Mô hình tuyến tính + logistic, biểu đồ rừng, phần Kết quả |

> **Ghi chú về sự đồng bộ với bộ slide.** Bộ slide hiện tại giới thiệu **hồi quy (tuyến tính rồi
> logistic) ở Buổi 5**; Buổi 4 giờ chỉ dành cho các kiểm định. Phần *Buổi 4* chi tiết
> ở phía dưới vẫn còn chứa một phần nhập môn hồi quy logistic — khi giảng dạy theo
> bộ slide hiện tại, hãy dời phần nhập môn đó sang Buổi 5 (nơi bộ slide giờ đặt nó).

Mỗi buổi kết thúc với **Hỏi & Đáp** được lồng ghép xuyên suốt, không phải gắn thêm vào. Các buổi có tính tích lũy: Buổi 2 tạo ra tệp sạch mà các Buổi 3–5 đều đọc. **Nếu một học viên vắng Buổi 2, hãy đưa cho họ tệp `analysis_data.rds` đã chuẩn bị sẵn để họ có thể theo kịp.**

---

## 2. Danh sách kiểm tra thiết lập trước khóa học

### Phần mềm (học viên — lý tưởng là trước Buổi 1)
Hướng dẫn học viên đến `References/package_installation_guide.md`. Những thứ thiết yếu:

- [ ] Cài đặt **R 4.x** (khóa học được xây dựng với R 4.6.0) từ CRAN.
- [ ] Cài đặt **RStudio Desktop** từ posit.co.
- [ ] Mở **RStudio** (không phải R thuần) và xác nhận bốn ô cửa sổ xuất hiện.
- [ ] Cài đặt tất cả các gói trong một khối (`tidyverse, readxl, lubridate, janitor, gtsummary, gt, broom, broom.helpers, car, pROC, scales`).
- [ ] Chạy vòng lặp xác minh ở Bước 3; mỗi dòng đều phải in ra `TRUE`.
- [ ] Tạo một **RStudio Project** đặt gốc tại thư mục `Course/` (File → New Project → Existing Directory).

> Hãy chuẩn bị sẵn **một hoặc hai laptop dự phòng** đã được cấu hình. Sẽ luôn có ai đó cài đặt thất bại; đừng để nó làm hỏng Buổi 1.

### Đoạn mã "Kiểm tra xem có chạy được không"
Yêu cầu mọi người dán đoạn này vào Console vào sáng Buổi 1. Nó xác nhận R chạy, các gói nạp được, và đường dẫn dữ liệu phân giải được:

```r
library(tidyverse)
library(readxl)
htn <- read_csv("Data/hypertension_phc_raw.csv")
dim(htn)              # expect 1503 36
cat("Setup OK — R, tidyverse and the data path all work.\n")
```

Nếu `dim(htn)` trả về `1503 36`, học viên đó đã sẵn sàng. (Lưu ý: **1503**, không phải 1500 — ba bản ghi trùng lặp là một gợi ý mở đầu cho Buổi 2.)

### Yêu cầu về phòng học / thiết bị nghe nhìn
- [ ] Máy chiếu hoặc màn hình lớn; giảng viên có thể chiếu song song RStudio của mình.
- [ ] Nguồn điện ổn định (mỗi chỗ ngồi) và Wi-Fi chỉ cho lần cài đặt đầu tiên.
- [ ] Bảng trắng/bảng lật để phác họa các tỷ số chênh, hàm logit, và cấu trúc thư mục.
- [ ] Lý tưởng là có một **đồng điều phối viên** để đi lại và gỡ vướng cho từng cá nhân trong lúc làm bài tập.

### Phân phối thư mục khóa học
Nén và chia sẻ toàn bộ thư mục `Course/` (Data, Scripts, Practicals, Solutions, References, Resources, Slides). Học viên giải nén và mở nó **như một RStudio Project**, điều này làm cho mọi đường dẫn tương đối (`Data/...`, `Resources/...`) hoạt động giống hệt nhau trên mọi máy. **Đừng** phân phối lời giải trước bài tập của mỗi buổi — chỉ chia sẻ `Solutions/dayN_solution.R` sau khi làm bài tập.

---

## 3. Hướng dẫn điều phối chung

**Nhịp độ.** Đây là một khóa học lập trình trực tiếp; hãy chuẩn bị tinh thần cảm thấy chậm. Bước giới hạn tốc độ là *người gõ chậm nhất trong phòng*, không phải người học nhanh nhất. Hãy dự trù thời gian rộng rãi và cưỡng lại cám dỗ "cứ dán nó vào cho xong". Khi mọi người tự gõ mã lệnh, họ nhớ nó.

**Mô hình trình diễn xem-rồi-làm.** Với mỗi khái niệm:
1. *Xem* — bạn chạy dòng trình diễn, thuyết minh từng phần làm gì, đọc to kết quả console.
2. *Làm* — học viên gõ cùng dòng đó và xác nhận họ nhận được cùng kết quả.
3. *Biến tấu* — đặt ra một biến thể nhỏ ("bây giờ làm cho `dbp_mmhg`") để họ áp dụng, chứ không sao chép.

Chạy các script trình diễn **từng dòng một** bằng `Ctrl+Enter` (Windows) / `Cmd+Enter` (Mac). Đừng bao giờ chạy cả một script trong im lặng.

**Quản lý một lớp có trình độ chênh lệch.** Một số học viên sẽ bay vút; những người khác sẽ lạc lối từ dòng thứ ba. Chiến thuật: ghép người hoàn thành nhanh với người đang chật vật; giao cho người hoàn thành nhanh các nhiệm vụ "nâng cao" (mỗi bài tập có một cái); giữ một đồng điều phối viên đi lại; dùng tín hiệu bằng giấy nhớ có màu ("đỏ = bị kẹt"). Trấn an lặp đi lặp lại rằng **gặp lỗi là chuyện bình thường và không phải là dấu hiệu của thất bại**.

**Khuyến khích đặt câu hỏi.** Mở đầu mỗi buổi bằng: *"Không có câu hỏi nào là ngớ ngẩn — nếu bạn bối rối, thì có ba người khác cũng vậy."* Dừng lại sau mỗi phần trình diễn và hỏi một câu hỏi *cụ thể, đích danh* ("Dấu `$` ở đây làm gì?") thay vì câu "Có câu hỏi nào không?" vốn gây im lặng.

**Chia sẻ màn hình cỡ chữ lớn.** Trước Buổi 1: trong RStudio, **Tools → Global Options → Appearance**, đặt cỡ chữ trình soạn thảo lớn (16–18 pt) và một theme có độ tương phản cao. Phóng to console luôn. Người ngồi ở cuối phòng phải đọc được mã lệnh, không phải nheo mắt.

**Xử lý lỗi trực tiếp như những khoảnh khắc giảng dạy.** Bạn *sẽ* gặp lỗi trực tiếp — hãy đón nhận chúng. Khi một lỗi xuất hiện, hãy chậm lại và nói *"Tốt — hãy cùng đọc lỗi này."* Dạy thói quen **đọc thông báo, không hoảng loạn**. Các phần trình diễn chứa những cái bẫy có chủ đích (tuổi tối đa 200, `mean()` trả về `NA`, việc loại bỏ ca đầy đủ) chính là để lớp học gặp những lỗi này trong một môi trường được kiểm soát. Xem phụ lục Khắc phục sự cố để biết các cách sửa chuẩn mực.

---

## 4. Kế hoạch bài giảng hằng ngày

---

### BUỔI 1 — Nhập môn R & RStudio

**Phân bổ thời gian (90 phút):** Ôn tập 10 phút · Bài giảng & trình diễn trực tiếp 50 phút · Bài tập có hướng dẫn 25 phút · Tổng kết & Hỏi–Đáp 5 phút.
**Script trình diễn:** `Scripts/day1_demo.R` · **Bài tập:** `Practicals/day1_exercise.R` · **Lời giải:** `Solutions/day1_solution.R`

**Mục tiêu học tập (buổi):** 1, 2, 3, 4 — điều hướng RStudio; dùng object/vector/hàm/gói; nhập CSV và Excel; nhìn dữ liệu lần đầu một cách phê phán.

**Mạch xuyên suốt.** *"R chỉ là một chiếc máy tính bỏ túi rất biết vâng lời, rất máy móc và không bao giờ quên những gì bạn đã bảo nó."* Hôm nay là về việc loại bỏ nỗi sợ và đưa dữ liệu lâm sàng **vào**. Chúng ta không làm thống kê nào — chúng ta nhập, nhìn, và phát hiện dữ liệu lộn xộn, điều này chuẩn bị cho Buổi 2.

**Các điểm giảng dạy chính.**
- **Script** là thứ bạn lưu và chạy lại (khả năng tái lập); **Console** là nơi kết quả xuất hiện. Mã lệnh sống trong script, không phải được gõ một lần vào console rồi mất.
- Việc gán dùng `<-` (đọc to là *"nhận giá trị"*): `sbp <- 152` nghĩa là *sbp nhận giá trị 152*.
- R **phân biệt chữ hoa chữ thường**: `sbp` và `SBP` là các đối tượng khác nhau.
- `install.packages()` chạy **một lần** (cần internet); `library()` chạy **mỗi phiên**.
- Các đường dẫn tương đối bên trong một RStudio Project làm cho phân tích có thể chuyển đổi được.

**Hướng dẫn trình diễn trực tiếp (`day1_demo.R`).**

1. R như một máy tính bỏ túi (dòng ~18–21):
   ```r
   2 + 2
   mean(c(120, 130, 145, 150))   # mean of four systolic readings
   ```
   Dự kiến: `[1] 4`, rồi `[1] 136.25`. *Chỉ ra tiền tố `[1]` — nó chỉ là một chỉ số, không phải một phần của câu trả lời.*

2. Đối tượng và tính phân biệt chữ hoa chữ thường (dòng ~31–37):
   ```r
   sbp <- 152
   sbp + 10
   ```
   Dự kiến `[1] 162`. **Lỗi giảng dạy #1 — làm rõ điều này:** gõ `SBP` và để nó báo lỗi `Error: object 'SBP' not found`. *"R rất máy móc: S-B-P viết hoa chưa bao giờ được tạo ra."*

3. Vector và biến logical (dòng ~43–55):
   ```r
   sbp_readings <- c(152, 138, 145, 160, 129, 142)
   high_bp <- sbp_readings >= 140
   sum(high_bp)
   ```
   Dự kiến `sum(high_bp)` → `[1] 4`. *Giải thích rằng `TRUE` được tính là 1 — nên `sum()` của một biến logical đếm xem có bao nhiêu giá trị TRUE.*

4. Các gói (dòng ~64–65): `library(tidyverse)` rồi `library(readxl)`. **Lỗi giảng dạy #2:** nếu ai đó gõ `library(tidyverse)` trước khi cài đặt, họ sẽ nhận được `there is no package called 'tidyverse'` — dấu hiệu để xem lại hướng dẫn thiết lập.

5. Nhập dữ liệu (dòng ~87–90):
   ```r
   htn <- read_csv("Data/hypertension_phc_raw.csv")
   ```
   Kết quả console dự kiến: một khối đặc tả cột và **`Rows: 1503 Columns: 36`**. *Dừng lại ở đây.* Nghiên cứu đã ghi danh 1.500 người — *"Tại sao lại là 1503?"* Ba hàng trùng lặp. Gieo mầm điều này cho Buổi 2.

6. Nhìn lần đầu (dòng ~99–114):
   ```r
   glimpse(htn)
   summary(htn$age)      # max = 200 -> impossible!
   table(htn$sex)        # Female, F, female, f ... messy
   ```
   **Lỗi giảng dạy #3 / khoảnh khắc gỡ lỗi:** `summary(htn$age)` cho thấy một **giá trị Max là 200**, và `table(htn$sex)` cho thấy nhiều cách viết. Để lớp học phản ứng. *"Trước bất kỳ thống kê nào, R đã đang bảo chúng ta rằng dữ liệu cần được làm sạch."*

**Các ngộ nhận thường gặp & cách sửa.**
- *"Tôi phải học thuộc lòng tất cả các lệnh."* Không — bạn tra cứu chúng; xem `References/R_command_reference_sheet.md`. Sự thành thạo đến từ việc lặp lại, không phải học thuộc lòng.
- *"`=` và `<-` là như nhau."* Chúng thường hành xử như nhau khi gán, nhưng quy ước của khóa học là `<-`; `=` được dành để đặt tên cho các đối số của hàm. Hãy giữ đơn giản và nhất quán.
- *"Chữ màu đỏ nghĩa là tôi đã làm hỏng R."* Đỏ thường chỉ là một **thông báo (message)** (ví dụ đặc tả cột từ `read_csv`), không phải một lỗi. Dạy họ đọc xem nó có ghi `Error` hay không.

**Ghi chú diễn giải lâm sàng.** Ngay cả việc kiểm tra thô cũng có ý nghĩa lâm sàng: một tuổi tối đa 200 và một `sbp` là 700 là bất khả thi về mặt sinh lý và gắn cờ các vấn đề nhập liệu. Kiến thức chuyên môn của một bác sĩ lâm sàng là công cụ kiểm định dữ liệu tốt nhất.

**Câu hỏi gợi ý từ khán giả (kèm câu trả lời).**
- *H: Tại sao dùng R thay vì Excel/SPSS?* Đ: Khả năng tái lập. R ghi lại mọi bước dưới dạng mã lệnh, để phân tích có thể được chạy lại, kiểm toán, và chia sẻ — điều thiết yếu cho nghiên cứu lâm sàng và xuất bản.
- *H: "tibble" là gì?* Đ: Một data frame hiện đại; nó in ra gọn gàng (10 hàng đầu, các kiểu cột) và hành xử một cách dự đoán được.
- *H: Tôi có cần internet để dùng R không?* Đ: Chỉ lần đầu tiên, để cài đặt các gói. Sau đó nó chạy ngoại tuyến.

**Bài tập — thế nào là thành công.** Học viên tự làm: nạp `tidyverse` và `readxl`; nhập CSV vào `htn` (1503 × 36) và trang tính Excel `"data"` vào `htn_xl` (cùng kích thước); chạy `glimpse()` và nêu tên 3 biến số và 3 biến phân loại; phát hiện **max age = 200** (bất hợp lý) và các **cách viết khác nhau của `sex`**; ghi nhận khoảng trắng thừa trong `facility`. **Điểm trả lời chính:** hai vấn đề dữ liệu họ nên nêu tên là *các giá trị bất hợp lý/bất khả thi* và *cách viết danh mục không nhất quán* — chính xác là chương trình của Buổi 2.

---

### BUỔI 2 — Hiểu & làm sạch dữ liệu lâm sàng

**Phân bổ thời gian (90 phút):** Ôn tập 10 phút · Bài giảng & trình diễn trực tiếp 50 phút · Bài tập có hướng dẫn 25 phút · Tổng kết & Hỏi–Đáp 5 phút.
**Script trình diễn:** `Scripts/day2_demo.R` · **Bài tập:** `Practicals/day2_exercise.R` · **Lời giải:** `Solutions/day2_solution.R`

**Mục tiêu học tập (buổi):** 5, 6, 7 — làm sạch văn bản và biến nhị phân, xử lý các giá trị đại diện dữ liệu thiếu, kiểm định các khoảng lâm sàng, mã hóa lại/tạo biến, đặt factor với các mức tham chiếu đúng.

**Mạch xuyên suốt.** *"Rác vào, rác ra — 80% của phân tích thực tế là làm sạch."* Hôm nay chúng ta biến tệp thô lộn xộn thành một bộ dữ liệu gọn gàng, sẵn sàng cho phân tích và **lưu nó lại**. Script này là **hợp đồng làm sạch**: các Buổi 3, 4 và 5 đều bắt đầu từ `Data/analysis_data.rds`. Nhấn mạnh rằng chúng ta **không bao giờ làm sạch lại bằng tay về sau**.

**Các điểm giảng dạy chính.**
- Báo cho `read_csv` biết cái gì được tính là thiếu: `na = c("", "NA", "999", "-99")`.
- Loại bỏ trùng lặp bằng `distinct()`; xác nhận bằng `n_distinct(patient_id)`.
- Chuẩn hóa các danh mục lộn xộn bằng `str_to_lower()` + `case_when()`; viết một **hàm trợ giúp tái sử dụng** (`to_yesno()`) để cùng một logic áp dụng cho mọi biến nhị phân.
- Kiểm định so với các khoảng sinh lý → ngoài khoảng trở thành `NA`.
- **Tính lại** BMI từ chiều cao/cân nặng nguồn thay vì tin cột được cung cấp (bị lỗi).
- Đặt **factor với các mức tham chiếu có chủ đích** — đối với biến nhị phân, liệt kê `"No"` đầu tiên để mô hình ước lượng khả năng của biến cố.

**Hướng dẫn trình diễn trực tiếp (`day2_demo.R`).**

1. Nhập với các giá trị đại diện (dòng ~19–24): `nrow(raw)` → `1503`.
2. Trùng lặp (dòng ~30–33):
   ```r
   sum(duplicated(raw))   # 3
   raw <- distinct(raw)
   nrow(raw)              # 1500
   ```
3. Làm sạch `sex` và các biến nhị phân (dòng ~43–63):
   ```r
   table(raw$sex, useNA = "ifany")              # now only Female / Male
   table(raw$treatment_uptake, useNA = "ifany") # now only Yes / No
   ```
4. Kiểm định (dòng ~70–78): `age`, `sbp_mmhg`, v.v. bất khả thi được đặt thành `NA`; `summary()` giờ cho thấy các giá trị Max hợp lý. **Khoảnh khắc gỡ lỗi:** hỏi *"Tuổi 200 đã đi đâu?"* — nó giờ được tính dưới `NA's`.
5. Tạo BMI và các phân loại (dòng ~84–96). **Lỗi giảng dạy #1:** cột `bmi` được cung cấp bị sai vì các lỗi `height_cm = 17` và `weight_kg = 7`; việc tính lại sau khi kiểm định sẽ sửa nó.
6. Ngày tháng (dòng ~104–108): `parse_date_time(..., orders = c("ymd","dmy","d-b-Y"))`; `sum(is.na(enroll_date))` cho thấy có cái nào không phân tích được.
7. Factor (dòng ~114–138). **Lỗi giảng dạy #2 — làm rõ điều này thật kỹ:** nếu bạn đặt `treatment_uptake = factor(..., levels = c("Yes","No"))` (sai thứ tự), mọi tỷ số chênh ở Buổi 4–5 sẽ đảo ngược. Mức tham chiếu **phải** là `"No"`.
8. Lưu hợp đồng (dòng ~153–154):
   ```r
   saveRDS(analysis_data, "Data/analysis_data.rds")
   write_csv(analysis_data, "Data/analysis_data.csv")
   ```

**Các ngộ nhận thường gặp & cách sửa.**
- *"Tôi cứ sửa nó trong Excel."* Điều đó phá vỡ khả năng tái lập và không kiểm toán được. Việc làm sạch thuộc về mã lệnh.
- *"Một giá trị thiếu là số không."* Không — `NA` nghĩa là *không rõ*, không phải 0. Mã hóa lại `999`/`-99`/ô trống thành `NA` chính là toàn bộ mục đích.
- *"Thứ tự factor không quan trọng."* Nó âm thầm quyết định danh mục tham chiếu của hồi quy — nó cực kỳ quan trọng.
- *"`|>` khác với `%>%`."* Đối với khóa học này chúng hành xử như nhau (chuyển vế trái vào hàm tiếp theo); dùng cái nào mà script dùng.

**Ghi chú diễn giải lâm sàng.** Các khoảng kiểm định là các phán đoán lâm sàng: tuổi 18–110, SBP 70–260 mmHg, DBP 40–150, chiều cao 120–210 cm, cân nặng 30–200 kg. Thảo luận *tại sao* — đây là các giới hạn của sinh lý con người. BMI được tính lại cung cấp cho các phân loại chuẩn của WHO (Underweight/Normal/Overweight/Obese).

**Câu hỏi gợi ý từ khán giả (kèm câu trả lời).**
- *H: Tại sao lưu dưới dạng `.rds` thay vì `.csv`?* Đ: `.rds` bảo toàn các kiểu của R — quan trọng nhất là **các mức factor và thứ tự**. Một CSV đọc lại sẽ mất thiết lập mức tham chiếu.
- *H: Tôi có nên xóa các hàng có bất kỳ dữ liệu thiếu nào không?* Đ: Không ở giai đoạn làm sạch. Giữ chúng lại; mô hình chỉ dùng các ca đầy đủ cho các biến của nó (Buổi 4). Loại bỏ sớm sẽ vứt đi dữ liệu dùng được.
- *H: `to_yesno()` có cần thiết không?* Đ: Nó tránh các lỗi sao chép-dán — một hàm đã được kiểm thử áp dụng cho năm cột an toàn hơn năm khối được sửa bằng tay.

**Bài tập — thế nào là thành công.** Một quy trình làm sạch tái lập được kết thúc bằng `analysis_data.rds`: nhập với các giá trị đại diện; `distinct()` → **1500 hàng**; `sex` rút gọn còn Female/Male; `diabetes` và `treatment_uptake` chuẩn hóa thành Yes/No; `age`/`sbp` ngoài khoảng → `NA`; BMI được tính lại với `bmi_cat`; các biến chính chuyển thành factor với **mức tham chiếu của `treatment_uptake` = "No"**; dữ liệu được lưu. **Điểm trả lời chính:** số lượng `total_chol_mmol_l` bị thiếu sau khi nhập (qua `sum(is.na(...))`) — xác nhận họ đã dùng đối số `na =` để các giá trị đại diện `-99`/ô trống được bắt.

---

### BUỔI 3 — Thống kê mô tả, bảng biểu & hình

**Phân bổ thời gian (90 phút):** Ôn tập 10 phút · Bài giảng & trình diễn trực tiếp 50 phút · Bài tập có hướng dẫn 25 phút · Tổng kết & Hỏi–Đáp 5 phút.
**Script trình diễn:** `Scripts/day3_demo.R` · **Bài tập:** `Practicals/day3_exercise.R` · **Lời giải:** `Solutions/day3_solution.R`

**Mục tiêu học tập (buổi):** 8, 9 — xu hướng trung tâm/độ phân tán, tần số, bảng chéo; Bảng 1 và các hình chất lượng xuất bản.

**Mạch xuyên suốt.** *"Mô tả trước khi kiểm định."* Hôm nay chúng ta tóm tắt mẫu bằng số và bằng hình ảnh và xây dựng **Bảng 1** mà mọi bản thảo lâm sàng đều mở đầu. Luôn nạp lại từ `analysis_data.rds` — không bao giờ làm sạch lại.

**Các điểm giảng dạy chính.**
- **Cái bẫy #1 của người mới bắt đầu:** `mean()`/`sd()` trả về `NA` nếu *bất kỳ* giá trị nào bị thiếu → luôn `na.rm = TRUE`.
- Trung bình so với trung vị: khi trung bình nằm trên trung vị, biến bị lệch phải (thường gặp với huyết áp, BMI) → báo cáo **trung vị (IQR)**.
- `table()` **âm thầm bỏ `NA`** → dùng `useNA = "ifany"` để phần trăm không gây hiểu lầm.
- `prop.table(margin = 1)` = % theo hàng, `margin = 2` = % theo cột; **chọn chiều trả lời câu hỏi của bạn.**
- `gtsummary::tbl_summary()` xây dựng Bảng 1; `ggsave(..., dpi = 300)` lưu các hình cho xuất bản.
- Định nghĩa kiểu định dạng **một lần** (`course_teal <- "#0D7377"`) và tái sử dụng.

**Hướng dẫn trình diễn trực tiếp (`day3_demo.R`).**

1. Cái bẫy `na.rm` (dòng ~56–57):
   ```r
   mean(analysis_data$sbp_mmhg)              # NA
   mean(analysis_data$sbp_mmhg, na.rm = TRUE)  # the correct value
   ```
   **Khoảnh khắc gỡ lỗi #1:** *"Tại sao cái đầu tiên lại cho NA khi chúng ta có 1500 bệnh nhân? Vì ít nhất một SBP bị thiếu."*
2. Độ phân tán và các phân vị (dòng ~60–66): `median`, `sd`, `IQR`, `quantile()`.
3. Tóm tắt theo nhóm theo biến kết cục (dòng ~101–116): `group_by(treatment_uptake)` + `across()` — lưu ý bệnh nhân đang điều trị có xu hướng lớn tuổi hơn / SBP cao hơn (tín hiệu sớm).
4. Tần số (dòng ~129–148). **Khoảnh khắc gỡ lỗi #2:** so sánh `table(analysis_data$education)` với `table(..., useNA = "ifany")` — cái thứ hai bộc lộ các ô trống.
5. Bảng chéo (dòng ~155–163): % theo hàng so với % theo cột; **bắt lớp học nêu câu hỏi trước** để họ chọn đúng chiều.
6. Bảng 1 (dòng ~181–207): `tbl_summary(by = treatment_uptake) |> add_p() |> add_overall() |> bold_labels()`. **Lỗi giảng dạy / phương án dự phòng:** nếu `gtsummary` chưa được cài, hãy chỉ cách dự phòng bằng `table()`/`aggregate()` của base-R được ghi trong script.
7. Hình (dòng ~229–309): histogram của tuổi, histogram+mật độ SBP, biểu đồ cột học vấn, boxplot theo nhóm, tán xạ SBP-vs-BMI với `geom_smooth(method = "lm")`. Mỗi cái được lưu bằng `ggsave(..., dpi = 300)`.

**Các ngộ nhận thường gặp & cách sửa.**
- *"Một giá trị p trong Bảng 1 chứng minh quan hệ nhân quả."* Không — các giá trị p trong Bảng 1 là các so sánh nhóm mô tả, không phải các hiệu ứng đã hiệu chỉnh (đó là Buổi 4–5).
- *"Luôn báo cáo trung bình."* Không phải cho dữ liệu bị lệch — báo cáo trung vị (IQR).
- *"`geom_bar()` cần tôi đếm trước."* Không — nó đếm các danh mục giúp bạn; tóm tắt trước sẽ đếm hai lần.
- *"Biểu đồ biến mất."* `ggsave()` đã lưu biểu đồ được in cuối cùng; kiểm tra thư mục `Resources/`.

**Ghi chú diễn giải lâm sàng.** Độ dốc lên của biểu đồ tán xạ (BMI vs SBP) nhất quán với béo phì là một yếu tố nguy cơ tăng huyết áp — nhưng **liên quan, không phải nhân quả**. Độ lệch trong SBP/BMI là điều được kỳ vọng về mặt sinh lý (một vài giá trị rất cao). Chọn đúng chiều `prop.table` là một cạm bẫy thực sự của bản thảo: *"% người đái tháo đường đang điều trị" = % theo cột*; *"% người đang điều trị bị đái tháo đường" = % theo hàng*.

**Câu hỏi gợi ý từ khán giả (kèm câu trả lời).**
- *H: Khi trung bình ≠ trung vị, tôi báo cáo cái nào?* Đ: Đối với một biến lâm sàng lệch rõ ràng, trung vị (IQR). Khi chúng gần nhau, trung bình (SD) là ổn.
- *H: Làm sao đưa Bảng 1 vào Word?* Đ: `as_flex_table()` → `flextable::save_as_docx()`, hoặc xuất HTML/CSV (script chỉ cả hai cách).
- *H: Tại sao 300 dpi?* Đ: Các tạp chí yêu cầu nó cho các hình chất lượng in.

**Bài tập — thế nào là thành công.** Nạp lại dữ liệu sạch; báo cáo tuổi trung bình (SD) và khoảng cách trung vị (IQR) (với `na.rm = TRUE`); các bảng tần số (n và %) của học vấn và bp_category; bảng chéo của treatment_uptake × diabetes với % theo hàng; một **Bảng 1 phân tầng theo `treatment_uptake` với `add_p()`** bao gồm các biến đã liệt kê; hai hình được lưu (boxplot của SBP theo tiếp nhận, biểu đồ cột học vấn) ở 300 dpi; Bảng 1 được xuất ra. **Điểm trả lời chính:** nêu tên hai đặc điểm khác nhau giữa nhóm điều trị/không điều trị (ví dụ tuổi, bảo hiểm, đái tháo đường, học vấn) và đánh giá chúng có hợp lý về mặt lâm sàng.

---

### BUỔI 4 — Phân tích thống kê (kiểm định giả thuyết + nhập môn hồi quy logistic)

**Phân bổ thời gian (90 phút):** Ôn tập 10 phút · Bài giảng & trình diễn trực tiếp 50 phút · Bài tập có hướng dẫn 25 phút · Tổng kết & Hỏi–Đáp 5 phút.
**Script trình diễn:** `Scripts/day4_demo.R` · **Bài tập:** `Practicals/day4_exercise.R` · **Lời giải:** `Solutions/day4_solution.R`

**Mục tiêu học tập (buổi):** 10, 11 (nhập môn) — khớp câu hỏi với kiểm định; chạy/diễn giải kiểm định t, Wilcoxon, ANOVA, chi bình phương/Fisher, tương quan; khớp và diễn giải hồi quy logistic đơn giản dưới dạng tỷ số chênh.

**Mạch xuyên suốt.** *"Chuyển từ mô tả dữ liệu sang đặt câu hỏi cho nó."* Ý tưởng then chốt hôm nay là **quần thể phân tích**: tiếp nhận điều trị chỉ có ý nghĩa với những người **đã được chẩn đoán**, nên chúng ta lọc `htn_diagnosed == "Yes"` (~1.089). *"Bạn không thể tiếp nhận điều trị cho một bệnh mà bạn chưa được chẩn đoán."*

**Các điểm giảng dạy chính.**
- Xác định tập con phân tích một cách tường minh và một lần: `dx <- filter(analysis_data, htn_diagnosed == "Yes")`.
- Khớp câu hỏi với kiểm định (bảng ôn tập Buổi 4):
  - hai nhóm, liên tục → `t.test()` (hoặc `wilcox.test()` nếu bị lệch)
  - >2 nhóm, liên tục → `aov()` (hoặc `kruskal.test()`)
  - hai biến phân loại → `chisq.test()` (hoặc `fisher.test()` nếu thưa thớt)
  - hai biến liên tục → `cor.test()` (Pearson/Spearman)
  - biến kết cục nhị phân + yếu tố tác động → `glm(..., family = binomial)` → tỷ số chênh
- **Vẽ trước khi kiểm định.** Histogram + Q-Q trước; Shapiro-Wilk quá mạnh ở n≈1.089.
- Tỷ số chênh = `exp(coef())`; KTC = `exp(confint())`; đổi thang đo các yếu tố dự báo liên tục sang các đơn vị có ý nghĩa (ví dụ mỗi 10 năm).

**Hướng dẫn trình diễn trực tiếp (`day4_demo.R`).**

1. Xây dựng tập con (dòng ~41–49): `nrow(dx)` ≈ **1089**; `table(dx$treatment_uptake)`. **Khoảnh khắc gỡ lỗi #1 — làm rõ điều này:** chạy trên toàn bộ 1500 sẽ pha trộn những người chưa được chẩn đoán mà biến kết cục không xác định, làm sai lệch mọi thứ.
2. Tính chuẩn (dòng ~63–83): `hist`, `qqnorm`/`qqline`, rồi `shapiro.test()`. *"Với ~1089 hàng, Shapiro gắn cờ các sai lệch tầm thường — hãy tin biểu đồ Q-Q."*
3. Kiểm định t / Wilcoxon (dòng ~104–114): `t.test(age ~ treatment_uptake, data = dx)` — đọc hai giá trị trung bình, KTC cho sự khác biệt, giá trị p. Kỳ vọng tuổi lớn hơn ở nhóm đang điều trị.
4. ANOVA + Tukey (dòng ~129–139): `aov(age ~ education)` rồi `TukeyHSD()`. *"ANOVA nói một số nhóm khác nhau; Tukey nói nhóm nào."*
5. Chi bình phương / Fisher (dòng ~151–165): xây dựng `table(dx$treatment_uptake, dx$diabetes)`, chạy `chisq.test()`, **kiểm tra `$expected`**, chuyển sang `fisher.test()` nếu có bất kỳ giá trị kỳ vọng nào < 5.
6. Tương quan (dòng ~178–181): Pearson so với Spearman cho SBP vs BMI. *"Trong các mẫu lớn một r rất nhỏ có thể 'có ý nghĩa' nhưng tầm thường về mặt lâm sàng — báo cáo r, không chỉ p."*
7. Hồi quy logistic đơn giản (dòng ~202–229):
   ```r
   m_diab <- glm(treatment_uptake ~ diabetes, data = dx, family = binomial)
   exp(coef(m_diab)); exp(confint(m_diab))
   m_age <- glm(treatment_uptake ~ age, data = dx, family = binomial)
   exp(coef(m_age)["age"] * 10)   # OR per decade
   ```
   *"OR > 1 = khả năng tiếp nhận cao hơn; một KTC loại trừ giá trị 1 = có ý nghĩa."*
8. Đa biến ngắn gọn + `broom` (dòng ~241–264). **Khoảnh khắc gỡ lỗi #2:** `nobs(m_multi)` < 1089 vì `glm()` dùng **các ca đầy đủ** — bất kỳ giá trị thiếu nào trong bất kỳ biến mô hình nào cũng âm thầm loại bỏ hàng đó. `tidy(m_multi, exponentiate = TRUE, conf.int = TRUE)` cho bảng sẵn sàng để báo cáo.

**Các ngộ nhận thường gặp & cách sửa.**
- *"Có ý nghĩa = quan trọng."* Không — ý nghĩa là về bằng chứng chống lại giả thuyết không; tầm quan trọng lâm sàng là cỡ hiệu ứng (OR, khác biệt trung bình, r).
- *"Một giá trị p Shapiro nhỏ nghĩa là tôi không thể dùng kiểm định t."* Không phải ở cỡ mẫu này; hãy đánh giá biểu đồ Q-Q.
- *"OR cho mỗi năm tuổi rất nhỏ nên tuổi không quan trọng."* Nó là cho **một năm**; đổi thang đo sang một thập kỷ để thấy hiệu ứng thực.
- *"glm đã dùng tất cả bệnh nhân của tôi."* Kiểm tra `nobs()` — phân tích ca đầy đủ lặng lẽ làm giảm n.

**Ghi chú diễn giải lâm sàng.** Người đái tháo đường khám tại PHC bệnh nặng hơn và gắn kết hơn với chăm sóc, nên một tỷ lệ tiếp nhận cao hơn (OR > 1) là hợp lý. Diễn đạt các OR theo hướng lâm sàng: *"Bệnh nhân đái tháo đường có khả năng tiếp nhận điều trị cao gấp khoảng X lần so với người không đái tháo đường (OR X.X, KTC 95% a–b)."* Nhắc họ: chi bình phương cho một giá trị p, không phải một cỡ hiệu ứng — OR mới cho.

**Câu hỏi gợi ý từ khán giả (kèm câu trả lời).**
- *H: Kiểm định t hay Wilcoxon?* Đ: Nếu biến gần đối xứng trong một mẫu lớn, kiểm định t; nếu lệch rõ ràng hoặc n nhỏ, Wilcoxon. Khi chúng đồng thuận, báo cáo kiểm định t.
- *H: Tại sao logistic mà không phải hồi quy tuyến tính?* Đ: Biến kết cục là nhị phân (Yes/No); logistic mô hình hóa log-odds, cho các tỷ số chênh diễn giải được.
- *H: Tại sao mức tham chiếu là "No"?* Đ: Chúng ta đã đặt nó ở Buổi 2 để mô hình ước lượng khả năng của việc **tiếp nhận** (biến cố quan tâm).

**Bài tập — thế nào là thành công.** Giới hạn ở `dx` (≈1089); quyết định kiểm định t so với Wilcoxon cho tuổi theo tiếp nhận và diễn giải; chi bình phương của tiếp nhận × diabetes; OR logistic đơn giản cho diabetes với KTC và một câu đọc lâm sàng; OR cho tuổi mỗi năm và mỗi thập kỷ (`OR^10`); một mô hình đa biến (`age + sex + diabetes + residence + health_insurance`) được làm gọn bằng `broom`. **Điểm trả lời chính:** họ nên liệt kê các yếu tố quyết định có ý nghĩa kèm chiều hướng, khớp đại thể với `key_findings.md` (diabetes ↑, insurance ↑, urban ↑, tuổi lớn ↑). Chấm dựa trên **phương pháp và diễn giải đúng**, không phải việc khớp chữ số thập phân thứ hai.

---

### BUỔI 5 — Mô hình hóa hồi quy & khả năng tái lập (capstone)

**Phân bổ thời gian (90 phút):** Ôn tập 10 phút · Bài giảng & trình diễn trực tiếp 50 phút · Bài tập có hướng dẫn 25 phút · Tổng kết & Hỏi–Đáp 5 phút.
**Script trình diễn:** `Scripts/day5_demo.R` · **Bài tập:** `Practicals/day5_exercise.R` · **Lời giải:** `Solutions/day5_solution.R`

**Mục tiêu học tập (buổi):** 11 (đầy đủ), 12, 13 — khớp/báo cáo một mô hình đa biến; nhiễu và tương tác; chẩn đoán (VIF, tính tuyến tính, ảnh hưởng, AUC); khả năng tái lập.

**Mạch xuyên suốt.** *"Xây dựng mô hình từ kiến thức lâm sàng, không phải từ các giá trị p; rồi báo cáo nó một cách tái lập được."* Đây là bài capstone: một mô hình đa biến đã được định trước, được chẩn đoán đúng cách, trình bày dưới dạng các OR hiệu chỉnh với một biểu đồ rừng, tất cả đều tái lập được.

**Các điểm giảng dạy chính.**
- **Định trước** các yếu tố dự báo từ kiến thức lâm sàng và y văn — tránh đào bới dữ liệu và lựa chọn từng bước thiếu phê phán.
- **Nhiễu:** so sánh OR thô so với OR hiệu chỉnh cho nơi cư trú; một dịch chuyển >10% báo hiệu nhiễu.
- **Tương tác (biến đổi hiệu ứng):** thêm `diabetes:age`, so sánh các mô hình lồng nhau bằng một LRT (`anova(..., test = "LRT")`); kỳ vọng không có ý nghĩa → giữ mô hình đơn giản hơn.
- **Chẩn đoán:** `car::vif()` (>5 đáng xem, >10 nghiêm trọng); tính tuyến tính trên **logit** (kiểm tra loess); khoảng cách Cook qua `broom::augment()`; **AUC** qua `pROC` (0,7–0,8 chấp nhận được).
- **Khả năng tái lập:** `set.seed()`, đường dẫn tương đối, các kết quả đã lưu, `sessionInfo()`, và con đường đến các báo cáo một-cú-nhấp R Markdown/Quarto.

**Hướng dẫn trình diễn trực tiếp (`day5_demo.R`).**

1. Nạp + tập con (dòng ~36–49): `dx`, xác nhận `levels(dx$treatment_uptake)` là `c("No","Yes")` (mức tham chiếu = No).
2. Mô hình đầy đủ đã định trước (dòng ~65–77): `treatment_uptake ~ age + sex + education + residence + diabetes + family_history_htn + health_insurance + knowledge_score + distance_to_facility_km`.
3. Nhiễu (dòng ~86–90): OR thô so với OR hiệu chỉnh cho `residenceUrban` — lưu ý sự dịch chuyển.
4. Tương tác (dòng ~105–114): `anova(model_full, model_interax, test = "LRT")` — **kỳ vọng p > 0,05**, giữ `model_full`. **Điểm giảng dạy:** khi có tương tác trong mô hình, hiệu ứng chính của `diabetes` là hiệu ứng *tại tuổi 0* — vô nghĩa; đừng diễn giải các hiệu ứng chính khi một tương tác được giữ lại.
5. Thận trọng với từng bước (dòng ~130–144): `step()` được trình bày rồi **bị bác bỏ** để nghiêng về mô hình lâm sàng. Nói to các điểm thận trọng.
6. Chẩn đoán (dòng ~153–200): `vif()`; kiểm tra tính tuyến tính bằng loess cho `knowledge_score`; khoảng cách Cook với ngưỡng `4/n`; **AUC ≈ 0,71**.
7. Báo cáo (dòng ~207–259): `tidy(model_final, exponentiate = TRUE, conf.int = TRUE)`; `tbl_regression()`; biểu đồ rừng trên **thang log** với đường tham chiếu tại OR = 1, được lưu vào `Resources/`.
8. Khả năng tái lập (dòng ~271): `sessionInfo()`; đề cập việc ghi nó vào `References/session_info.txt`.

**Các kết quả chuẩn mực dự kiến (từ `key_findings.md` — để chấm điểm).** Mẫu phân tích 1.089 người đã được chẩn đoán; **992 ca đầy đủ**; tiếp nhận ≈ 47%. Các OR hiệu chỉnh: diabetes **3.56**, insurance **2.05**, tiền sử gia đình **1.91**, urban **1.87**, xu hướng học vấn **1.96**, tuổi **1.03/năm**, kiến thức **1.10/điểm**, giới nam **0.74**, khoảng cách **0.98 (NS)**; **AUC ≈ 0.71**. Các số thập phân thay đổi tầm thường qua các phiên bản — chấm dựa trên phương pháp và diễn giải.

**Các ngộ nhận thường gặp & cách sửa.**
- *"Loại bỏ mọi biến không có ý nghĩa."* Không — đối với một nghiên cứu **giải thích**, giữ các yếu tố nhiễu được chọn về mặt lâm sàng ngay cả khi p > 0,05; loại bỏ chúng tái đưa vào thiên lệch.
- *"Từng bước/AIC tìm ra mô hình 'thật'."* Nó tối ưu hóa sự đánh đổi giữa độ khớp và độ phức tạp, tạo ra các KTC lạc quan, và không tái lập được qua các bộ dữ liệu. Chỉ dành nó chủ yếu cho dự đoán.
- *"Một điểm ảnh hưởng được gắn cờ nên bị xóa."* Kiểm tra nó trước; báo cáo một phân tích độ nhạy nếu kết quả thay đổi.
- *"AUC cao hơn luôn là mục tiêu."* Đối với một nghiên cứu giải thích về các yếu tố quyết định, AUC tóm tắt khả năng phân biệt, không phải tính hợp lệ của các OR; 0,71 là chấp nhận được ở đây.

**Ghi chú diễn giải lâm sàng.** Diabetes cho **hiệu ứng lớn nhất** (OR ~3.56) nhưng **KTC rộng nhất** — một nhóm nhỏ hơn nghĩa là độ chính xác thấp hơn; một điểm giảng dạy hoàn hảo về cỡ hiệu ứng so với độ chính xác. So sánh thô-so-với-hiệu-chỉnh của nơi cư trú chứng minh nhiễu nhẹ. Khoảng cách có xu hướng bảo vệ nhưng **không có ý nghĩa** sau khi hiệu chỉnh — một lời nhắc rằng một chiều hướng được kỳ vọng không giống với ý nghĩa thống kê.

**Câu hỏi gợi ý từ khán giả (kèm câu trả lời).**
- *H: Tại sao giữ khoảng cách nếu nó không có ý nghĩa?* Đ: Nó là một biến tiếp cận đã được định trước; báo cáo OR hiệu chỉnh (không có ý nghĩa) của nó là trung thực và hữu ích.
- *H: AUC = 0,71 nghĩa là gì?* Đ: Cho một bệnh nhân đang điều trị và một bệnh nhân không điều trị ngẫu nhiên, mô hình xếp hạng người đang điều trị cao hơn 71% số lần — khả năng phân biệt chấp nhận được.
- *H: Làm sao để cái này hoàn toàn tái lập được?* Đ: RStudio Project + đường dẫn tương đối + `set.seed()` + các kết quả đã lưu + `sessionInfo()`, lý tưởng là được knit từ một tài liệu R Markdown/Quarto.

**Bài tập — thế nào là thành công.** Khớp mô hình đầy đủ đã định trước trên `dx`; `vif()` (không giá trị nào > 5); một bảng OR sẵn sàng cho xuất bản (`tbl_regression` hoặc `broom::tidy`) được lưu vào `Resources/`; một biểu đồ rừng được lưu; AUC qua `pROC` (≈0,71); một phần Kết quả 150–250 từ bằng tiếng Anh dễ hiểu nêu tên các yếu tố quyết định có ý nghĩa kèm các OR hiệu chỉnh và KTC 95% cùng một câu về khả năng phân biệt. **Điểm trả lời chính:** hiệu ứng lớn nhất = diabetes; KTC rộng nhất = diabetes — độ rộng phản ánh độ chính xác thấp hơn từ nhóm nhỏ hơn. So sánh với `References/results_section_draft.txt`.

---

## 5. Phụ lục khắc phục sự cố — các lỗi R thường gặp mà bác sĩ lâm sàng vấp phải

| Triệu chứng / thông báo | Nguyên nhân có thể | Cách khắc phục |
|---|---|---|
| `could not find function "glimpse"` / `"tbl_summary"` | Gói chưa được nạp trong phiên này | `library(tidyverse)` / `library(gtsummary)` trước khi dùng. `install.packages()` một lần; `library()` mỗi phiên. |
| `there is no package called 'X'` | Chưa bao giờ cài, hoặc gõ sai tên | `install.packages("X")`; kiểm tra chính tả/chữ hoa thường khớp với `library(X)`. |
| `cannot open file 'Data/...': No such file or directory` | Sai thư mục làm việc / không ở trong Project | Mở **RStudio Project** `Course/`; kiểm tra `getwd()`; dùng đường dẫn tương đối, không bao giờ `setwd("C:/Users/...")`. |
| `Error: object 'sbp' not found` | Đối tượng chưa bao giờ được tạo, hoặc **sai chữ hoa thường** (`SBP` so với `sbp`) | Chạy lại dòng tạo ra nó; khớp chính xác cách viết hoa. |
| Một tóm tắt trả về `NA` cho một biến số | Một giá trị thiếu lan truyền qua `mean`/`sd` | Thêm `na.rm = TRUE`. |
| Một danh mục bị thiếu khỏi một bảng tần số | `table()` âm thầm bỏ `NA` | `table(x, useNA = "ifany")`. |
| Các tỷ số chênh bị đảo ngược / "bảo vệ khi lẽ ra phải có hại" | Sai thứ tự mức tham chiếu của factor | Đặt các mức với `"No"`/`"Rural"` đầu tiên: `factor(x, levels = c("No","Yes"))`. |
| `Error: unexpected '=' ` hoặc nhầm lẫn đối số-so-với-gán | Dùng `=` nơi lẽ ra dùng `<-` (hoặc ngược lại) | Dùng `<-` để tạo đối tượng; `=` chỉ cho các đối số của hàm. |
| `nobs()` của mô hình thấp hơn dự kiến | `glm()` dùng các ca đầy đủ; các giá trị thiếu loại bỏ hàng | Kiểm tra dữ liệu thiếu; quyết định về việc gán giá trị (imputation) hoặc báo cáo n ca đầy đủ. |
| `chisq.test` cảnh báo "approximation may be incorrect" | Các số lượng ô kỳ vọng < 5 | Dùng `fisher.test()`. |
| Xuất bảng ra PNG thất bại / "Chrome not found" | Xuất PNG của `gt` cần Chrome | Xuất `.html`/`.csv` thay vào đó (các script tự động dự phòng). |
| `read_csv` hiển thị `1503` hàng | Có bản ghi trùng lặp (theo thiết kế) | Buổi 2: `distinct()` → 1500. |

> **Siêu-kỹ năng:** dạy học viên **đọc to thông báo lỗi** và định vị đối tượng/tệp/hàm gây lỗi trước khi thay đổi bất cứ điều gì. Hầu hết các lỗi ở đây là một trong: gói chưa được nạp, sai đường dẫn, sai chữ hoa thường, hoặc một vấn đề về giá trị thiếu/mức factor.

---

## 6. Tổng quan đánh giá

**Bài tập cuối khóa mang về nhà.** Học viên tự tái tạo phân tích đầy đủ về các yếu tố quyết định trên `analysis_data.rds`, giới hạn ở những người đã được chẩn đoán tăng huyết áp: khớp mô hình logistic đa biến đã được định trước, kiểm tra đa cộng tuyến (VIF), trình bày các OR hiệu chỉnh kèm KTC 95% (bảng sẵn sàng cho xuất bản), tạo ra một biểu đồ rừng, báo cáo khả năng phân biệt của mô hình (AUC), và viết một phần Kết quả 150–250 từ bằng tiếng Anh lâm sàng dễ hiểu. Điều này phản chiếu **bài tập trên lớp của Buổi 5** (`Practicals/day5_exercise.R`), vốn tường minh là buổi thực hành cho bài tập cuối khóa; các đáp án chuẩn mực nằm trong `Solutions/day5_solution.R` và `References/key_findings.md`.

**Chấm điểm.** Một hướng dẫn chấm điểm chi tiết được cung cấp **riêng** cho các giảng viên. Chấm dựa trên **phương pháp đúng và diễn giải hợp lý**, không phải khớp chính xác chữ số thập phân thứ hai — các KTC và chiều hướng ổn định qua các phiên bản R/gói; các số thập phân chính xác thì không. Ghi nhận: quần thể phân tích đúng (chỉ người đã được chẩn đoán), các mức tham chiếu đúng, các OR hiệu chỉnh (không phải thô), báo cáo trung thực các biến đã định trước không có ý nghĩa, và một đoạn Kết quả am hiểu lâm sàng.

---

## 7. Điều chỉnh khóa học cho các định dạng ngắn hơn / dài hơn

**Ngắn hơn (buổi giới thiệu nửa ngày hoặc 1 ngày).** Nén lại thành Buổi 1–3: đưa dữ liệu vào, làm sạch nó, tạo ra Bảng 1 và các hình. Cung cấp tệp `analysis_data.rds` đã chuẩn bị sẵn để việc làm sạch có thể được trình diễn thay vì thực hiện đầy đủ. Bỏ các kiểm định giả thuyết và hồi quy, hoặc chỉ đưa ra một bản xem trước 20 phút "đây là nơi điều này dẫn tới" về các tỷ số chênh.

**Tiêu chuẩn (khóa học 5 buổi này).** Như đã viết — một khái niệm mỗi buổi, tích lũy, ~2 giờ/buổi.

**Dài hơn (7–10 buổi hoặc một học phần cả kỳ).** Mở rộng với: một buổi thực hành làm sạch dữ liệu chuyên biệt trên một bộ dữ liệu lộn xộn thứ hai; các động từ (verb) `dplyr` của tidyverse chuyên sâu; trực quan hóa dữ liệu như một buổi riêng; xử lý dữ liệu thiếu và gán giá trị bội (multiple imputation); phân tích sống còn hoặc các mô hình hỗn hợp/đa mức cho tính phân cụm đa trung tâm; và một buổi báo cáo R Markdown/Quarto đầy đủ đỉnh điểm là một bản thảo được knit. Thêm các bài kiểm tra hình thành giữa các buổi và một buổi bình duyệt mã lệnh đồng đẳng trước bài tập cuối khóa.

---

*Được chuẩn bị cho các giảng viên của* **Phân tích Dữ liệu Lâm sàng trong R — Giai đoạn I** *· Giảng viên: Vương Mỹ Lượng (Chuyên gia Thống kê Sinh học Cao cấp, giảng viên chính) & Bernard Osang'ir (Chuyên gia Thống kê Sinh học Cao cấp) · Neudata · #ClearDataClearImpact*
