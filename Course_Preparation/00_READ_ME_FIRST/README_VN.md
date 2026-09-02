# Chào mừng bạn đến với bộ tài liệu chuẩn bị trước khóa học R

**Clinical Data Analysis in R — Giai đoạn I — Introduction to R for Clinical Research**
bởi **Neudata**

Kính gửi học viên,

Chào mừng bạn, và cảm ơn bạn đã tham gia cùng chúng tôi. Bộ tài liệu ngắn này là bước khởi đầu nhẹ nhàng của bạn trước khi chúng ta gặp nhau trong các buổi học trực tiếp.

- **Khóa học:** Clinical Data Analysis in R — Giai đoạn I — Introduction to R for Clinical Research
- **Hình thức:** 5 buổi học buổi tối, mỗi Thứ Ba lúc 20:00 (giờ Việt Nam), mỗi buổi 90 phút
- **Thời gian:** 8 tháng 9 – 6 tháng 10 năm 2026
- **Giảng viên:** Bernard Isekah Osang'ir (Chuyên gia Thống kê Sinh học Cao cấp, giảng viên chính) và My Luong Vuong (Nhà thống kê sinh học và dịch tễ học)
- **Đăng ký / hỏi đáp:** My Luong Vuong — myluong1710@gmail.com — www.neu-data.com

## Tuần này để làm gì

Thư mục này được gửi đến bạn khoảng một tuần trước khóa học để bạn có thể đến buổi học trong tâm thế **sẵn sàng và thoải mái** — không phải để kiểm tra bạn. Không có gì ở đây được chấm điểm. Toàn bộ mục đích là sự quen thuộc và tự tin: cài đặt R và RStudio, làm quen với bố cục màn hình, và nhẹ nhàng thực hành với một bộ dữ liệu lâm sàng thực tế để buổi tối đầu tiên trở nên dễ chịu thay vì choáng ngợp. Hãy dự trù khoảng **2–3 giờ tổng cộng**, chia ra trong tuần thành những lần ngắn, dễ chịu. Nếu bạn chưa từng viết một dòng mã nào trong đời, thì bạn chính là người mà tài liệu này được viết cho. Hãy làm từ tốn, và tận hưởng nó.

## Cách sử dụng thư mục này

Vui lòng làm việc theo thứ tự sau:

1. **Đọc tệp này trước** (bạn đang ở đây).
2. **Cài đặt phần mềm** — mở thư mục `01_Install_R_and_RStudio/`, làm theo tài liệu hướng dẫn cài đặt, rồi chạy `installation_test.R` để kiểm tra mọi thứ hoạt động.
3. **Tham quan RStudio** — mở thư mục `02_Getting_Started_with_RStudio/` và, khi được nhắc, nhấp đúp `Clinical_Data_Analysis_PreCourse.Rproj` để mở toàn bộ dự án trong RStudio.
4. **Làm qua các bài học** — đi qua các thư mục `03` đến `07` theo thứ tự.
5. **Thử các bài Exercises** — làm thử các bài tập ngắn trong `Exercises/`, rồi tự đối chiếu với `Solutions/`.
6. **Giữ tài liệu tham khảo trong tầm tay** — tham khảo `Cheat_Sheets/` và `Guides/` bất cứ khi nào bạn muốn.

Không cần phải ghi nhớ bất cứ điều gì. Đọc, nhấp chuột theo, và làm quen dần với công cụ là đã quá đủ.

## Bộ tài liệu này gồm những gì (bản đồ thư mục)

- **00_READ_ME_FIRST/** — thư mục này; bắt đầu ở đây.
- **01_Install_R_and_RStudio/** — tài liệu hướng dẫn cài đặt từng bước cùng với `installation_test.R` để xác nhận thiết lập của bạn.
- **02_Getting_Started_with_RStudio/** — một tài liệu thân thiện về giao diện RStudio.
- **03_R_Basics/** — `01_R_Basics.Rmd`: những kiến thức cơ bản nhất về R.
- **04_Data_Management/** — `02_Data_Management.Rmd`: đọc, sắp xếp và xử lý dữ liệu.
- **05_Exploratory_Data_Analysis/** — `03_Exploratory_Analysis.Rmd`: tóm tắt và trực quan hóa dữ liệu.
- **06_Statistical_Tests/** — `04_Statistical_Tests.Rmd`: các kiểm định thường gặp cho câu hỏi lâm sàng.
- **07_Regression/** — `05_Regression.Rmd`: mô hình hồi quy nhập môn.- **Data/** — `clinical_data_raw.csv`, `clinical_data_clean.csv`, một từ điển dữ liệu, và ghi chú chất lượng dữ liệu.
- **Exercises/** — sáu bài tập ngắn trước khóa học.
- **Solutions/** — lời giải chi tiết đầy đủ để đối chiếu.
- **Cheat_Sheets/** — một cheat sheet R và hướng dẫn chọn kiểm định thống kê.
- **Guides/** — một khung tư duy phân tích, ví dụ theo ngành nghề, và hướng dẫn chuyển kết quả R thành kết quả sẵn sàng cho bài báo.- **Clinical_Data_Analysis_PreCourse.Rproj** — nhấp đúp vào tệp này để mở dự án trong RStudio.

## Gợi ý kế hoạch cho tuần trước khóa học

Năm buổi tối ngắn, thư thái — mỗi buổi khoảng 20–40 phút. Hãy điều chỉnh cho phù hợp với bạn.

- **Buổi tối 1 (~30–40 phút):** Cài đặt R và RStudio (thư mục `01`) và chạy `installation_test.R` cho đến khi bạn thấy thông báo thành công.
- **Buổi tối 2 (~30 phút):** Mở `.Rproj`, tham quan RStudio (thư mục `02`), rồi bắt đầu R Basics (thư mục `03`).
- **Buổi tối 3 (~30 phút):** Làm qua Data Management (thư mục `04`) và nạp bộ dữ liệu lâm sàng.
- **Buổi tối 4 (~30–40 phút):** Khám phá dữ liệu với EDA (thư mục `05`) và làm thử một vài bài Exercises.
- **Buổi tối 5 (~20–30 phút):** Đọc lướt Statistical Tests (thư mục `06`) và Regression (thư mục `07`), và hoàn thành các bài Exercises còn lại.

Nếu một buổi tối bị rút ngắn, cứ dừng lại — bạn luôn có thể tiếp tục từ chỗ đã dừng.

## Bạn cần những gì

- Một chiếc **laptop** (Windows hoặc macOS).
- Khoảng **1 GB dung lượng đĩa trống**.
- Một **kết nối internet** để tải xuống và cài đặt phần mềm.
- Khoảng **2–3 giờ** tổng cộng, chia ra trong tuần.

## Nếu bạn gặp khó khăn

Xin đừng lo lắng — gặp khó khăn là hoàn toàn bình thường, và ai lúc đầu cũng vậy. Vài lời trấn an:

- Thư mục `01_Install_R_and_RStudio/` có một **phần khắc phục sự cố** cho những trục trặc cài đặt thường gặp nhất.
- Nếu bạn vẫn gặp khó khăn, hãy liên hệ **My Luong Vuong** qua **myluong1710@gmail.com** để được giúp đỡ.
- Đến buổi học với phần cài đặt mới **hoàn thành một nửa** cũng hoàn toàn ổn — sẽ có người hỗ trợ trong buổi tối đầu tiên. Nhưng việc thử trước sẽ giúp buổi học đầu tiên diễn ra suôn sẻ hơn nhiều, nên hãy thử nhé.

## Hẹn sớm gặp lại

Vậy là xong. Hãy thong thả, nhẹ nhàng với bản thân, và nhớ rằng không có câu hỏi nào là ngớ ngẩn. Chúng tôi rất mong được cùng nhau học tập.

Trân trọng,
**Bernard Isekah Osang'ir** và đội ngũ **Neudata**
