# Cài đặt R và RStudio — Trước khóa học

**Clinical Data Analysis in R — Giai đoạn I** · Neudata

Chào mừng bạn! Trước buổi học buổi tối đầu tiên của chúng ta, vui lòng thiết lập phần mềm miễn phí mà chúng ta sẽ sử dụng. Hướng dẫn ngắn này sẽ dẫn bạn đi qua từng bước một. Bạn **không** cần bất kỳ kinh nghiệm lập trình nào, và bạn sẽ không làm hỏng gì cả — chỉ cần làm theo các bước theo thứ tự.

Hãy dành ra khoảng **20–30 phút**. Một tách trà sẽ giúp ích.

---

## 1. Chúng ta đang cài gì, và tại sao?

Chúng ta dùng hai chương trình miễn phí riêng biệt hoạt động cùng nhau:

- **R** là *động cơ*. Đó là phần mềm thực sự thực hiện các phép thống kê và tạo biểu đồ. Nếu đứng một mình, R trông khá đơn sơ và kém thân thiện.
- **RStudio** là *bảng điều khiển* mà bạn ngồi trước. Đó là một không gian làm việc thoải mái, gọn gàng điều khiển R thay cho bạn — với các bảng được bố trí rõ ràng cho mã của bạn, kết quả của bạn, và biểu đồ của bạn.

Hãy hình dung như một chiếc ô tô: **R là động cơ dưới nắp capo**, còn **RStudio là bảng điều khiển và vô lăng**. Bạn cần động cơ mới đi được đến đâu, nhưng gần như không ai muốn lái mà không có bảng điều khiển. Vì vậy chúng ta cài **cả hai** — R trước, rồi đến RStudio.

Cả hai đều **hoàn toàn miễn phí**, được sử dụng rộng rãi trong các bệnh viện và trường đại học trên toàn thế giới, và **an toàn để cài đặt**. Không có gì phải mua và không có phí thuê bao.

> **Thứ tự quan trọng:** Cài **R trước**, rồi **RStudio**. RStudio tìm R trên máy tính của bạn khi khởi động, nên R cần phải có sẵn từ trước.

---

## 2. Bạn sẽ cài những gì (tổng quan)

| Bước | Đó là gì | Mất khoảng bao lâu |
|------|------------|------------------|
| R | Động cơ thống kê | 5 phút |
| RStudio Desktop | Không gian làm việc thân thiện | 5 phút |
| Một bộ các gói R | Các phần bổ trợ chúng ta sẽ dùng trong lớp (bảng, biểu đồ, survival analysis) | 10–15 phút |
| Kiểm tra nhanh | Xác nhận mọi thứ hoạt động | 2 phút |

**Tổng: khoảng 20–30 phút**, phần lớn chỉ là chờ tải xuống.

Bạn sẽ cần một kết nối internet ổn định và quyền cài đặt phần mềm trên máy tính của mình (xem lưu ý về **quyền quản trị (admin rights)** bên dưới).

---

## 3. Cài R

R đến từ một trang web chính thức có tên **CRAN** (the Comprehensive R Archive Network). Địa chỉ là:

**https://cran.r-project.org**

Chọn phần dành cho máy tính của bạn bên dưới — **Windows** hoặc **macOS**.

> **Lưu ý về quyền quản trị (admin rights):** Việc cài phần mềm đôi khi cần quyền "administrator" (quản trị viên) — máy tính có thể bật lên một hộp thoại hỏi *"Do you want to allow this app to make changes?"* (Bạn có muốn cho phép ứng dụng này thực hiện thay đổi không?). Nhấp **Yes**. Trên một laptop cá nhân, điều này là bình thường. Trên một **máy tính của bệnh viện hoặc cơ quan**, bạn có thể không có quyền; nếu vậy, hãy xem phần Khắc phục sự cố ở cuối.

### 3a. Windows

1. Mở trình duyệt web và truy cập **https://cran.r-project.org**
2. Gần đầu trang, dưới mục *"Download and Install R"*, nhấp **"Download R for Windows"**.
3. Ở trang tiếp theo, nhấp **"base"** (đây là phiên bản chính của R — phiên bản mà mọi người bắt đầu).
4. Nhấp vào liên kết lớn ở đầu trang ghi **"Download R-4.x.x for Windows"** ("4.x.x" chỉ là số phiên bản — luôn lấy bản mới nhất được cung cấp).
5. Trình duyệt của bạn sẽ tải xuống một tệp có phần đuôi là **`.exe`** (ví dụ `R-4.x.x-win.exe`). Khi tải xong, **nhấp đúp vào tệp** để chạy. Nếu một hộp thoại bảo mật hỏi có cho phép hay không, nhấp **Yes / Run**.
6. Một trình cài đặt (installer wizard) sẽ mở ra. Bạn chỉ cần **chấp nhận tất cả các lựa chọn mặc định** — nhấp **Next** ở mỗi màn hình, rồi **Finish**. Không có gì bạn cần thay đổi.

Vậy là R đã được cài. Bạn sẽ không mở R trực tiếp — RStudio (bước tiếp theo) sẽ dùng nó thay cho bạn.

### 3b. macOS (máy Apple Mac)

1. Mở trình duyệt web và truy cập **https://cran.r-project.org**
2. Gần đầu trang, dưới mục *"Download and Install R"*, nhấp **"Download R for macOS"**.
3. Ở trang này bạn sẽ thấy **hai** lựa chọn tải xuống. Bạn cần chọn đúng bản cho máy Mac của mình:
   - Nếu máy Mac của bạn có **Apple Silicon** (một chip **M1, M2, M3 hoặc M4** — hầu hết các máy Mac từ cuối năm 2020 trở đi), hãy chọn gói có tên chứa **`-arm64`** (ví dụ `R-4.x.x-arm64.pkg`).
   - Nếu máy Mac của bạn dùng bộ xử lý **Intel cũ hơn**, hãy chọn gói **không có** `-arm64` (ví dụ `R-4.x.x.pkg`).
4. **Không chắc máy Mac của bạn là loại nào?** Nhấp vào **Apple menu** (biểu tượng quả táo, góc trên bên trái màn hình) → **About This Mac**. Nếu nó nhắc đến **Apple M1/M2/M3/M4**, bạn có Apple Silicon; nếu nó nhắc đến **Intel**, bạn có máy Mac Intel.
5. Nhấp vào liên kết bạn đã chọn. Trình duyệt tải xuống một tệp có phần đuôi là **`.pkg`**. Khi tải xong, **nhấp đúp vào tệp** để chạy.
6. Một trình cài đặt sẽ mở ra. **Chấp nhận các lựa chọn mặc định** — nhấp **Continue** / **Agree** / **Install** qua các màn hình. Bạn có thể được yêu cầu nhập mật khẩu máy Mac để cho phép cài đặt; hãy nhập và tiếp tục.

Vậy là R đã được cài. Bạn sẽ không mở R trực tiếp — RStudio (bước tiếp theo) sẽ dùng nó thay cho bạn.

---

## 4. Cài RStudio Desktop

Giờ hãy cài không gian làm việc thân thiện. Nó đến từ một công ty tên là **Posit** (họ làm ra RStudio). Địa chỉ là:

**https://posit.co/download/rstudio-desktop/**

Chúng ta muốn bản **RStudio Desktop miễn phí, mã nguồn mở** — đây là phiên bản được hiển thị mặc định trên trang đó. Bạn **không** cần bất kỳ phiên bản trả phí ("Pro") nào.

1. Truy cập **https://posit.co/download/rstudio-desktop/**
2. Cuộn xuống nút tải xuống. Trang web thường **tự động nhận diện máy tính của bạn** và cung cấp đúng tệp — hãy tìm một nút như **"Download RStudio Desktop for Windows"** hoặc **"…for macOS"**. (Nếu nó không nhận diện được, hãy cuộn xuống thêm một chút đến bảng *"All Installers"* và chọn hàng dành cho hệ thống của bạn.)
3. Nhấp vào nút để tải xuống.

**Trên Windows:**
- Bạn sẽ nhận được một tệp có phần đuôi là **`.exe`**. Nhấp đúp vào nó, nhấp **Yes** nếu được hỏi về quyền, và **chấp nhận các lựa chọn mặc định** qua trình cài đặt (Next → Next → Finish).

**Trên macOS:**
- Bạn sẽ nhận được một tệp có phần đuôi là **`.dmg`**. Nhấp đúp để mở nó. Một cửa sổ xuất hiện hiển thị **biểu tượng RStudio** và một lối tắt đến thư mục **Applications** của bạn.
- **Kéo biểu tượng RStudio vào thư mục Applications** trong chính cửa sổ đó. Đó chính là việc cài đặt.
- Lần đầu bạn mở RStudio (từ thư mục Applications hoặc từ Launchpad), macOS có thể cảnh báo bạn về việc mở phần mềm tải từ internet — chỉ cần nhấp **Open** để xác nhận.

**Hãy mở RStudio ngay bây giờ** để kiểm tra nó có khởi động không. Bạn sẽ thấy một cửa sổ được chia thành các bảng. Bảng lớn ở **bên trái** (hoặc dưới cùng bên trái) được gọi là **Console** — đó là nơi chúng ta sẽ gõ ở bước tiếp theo.

> Nếu RStudio mở ra nhưng báo lỗi rằng nó **can't find R** (không tìm thấy R), thường có nghĩa là R chưa được cài trước. Hãy quay lại làm Bước 3, rồi mở lại RStudio.

---

## 5. Cài các gói R cần thiết

**Gói (package) là gì?** Gói đơn giản là một **phần bổ trợ (add-on)** cho R — một tập hợp các công cụ bổ sung cho một công việc cụ thể, hơi giống như cài một ứng dụng trên điện thoại. R đi kèm những công cụ cơ bản; chúng ta thêm một vài gói cho công việc lâm sàng mà chúng ta sẽ làm trong lớp.

Sau đây là cách cài tất cả cùng một lúc:

1. Mở **RStudio**.
2. Nhấp một lần vào bên trong bảng **Console** (bảng lớn, thường ở dưới cùng bên trái, hiển thị ký hiệu **`>`**). Đây là nơi R chờ chỉ dẫn.
3. **Sao chép toàn bộ khối bên dưới**, dán vào Console, và nhấn **Enter**:

```r
install.packages(c("tidyverse", "readxl", "gtsummary", "broom", "survival", "survminer"))
```

4. R giờ sẽ tải xuống và thiết lập các gói. Bạn sẽ thấy rất nhiều dòng chữ trôi qua trong Console — **điều này hoàn toàn bình thường**, đó chỉ là R báo cáo tiến trình. Việc này có thể mất **vài phút**, nên hãy kiên nhẫn và để nó hoàn tất. Nó xong khi ký hiệu **`>`** xuất hiện lại trên một dòng riêng và các dòng chữ ngừng trôi.

**Mỗi gói dùng để làm gì (giải thích đơn giản):**

| Gói | Chúng ta sẽ dùng nó để làm gì |
|---------|----------------------|
| **tidyverse** | Bộ công cụ cốt lõi để xử lý dữ liệu và tạo biểu đồ |
| **readxl** | Đọc dữ liệu trực tiếp từ các tệp Excel |
| **gtsummary** | Tạo các bảng tóm tắt gọn gàng, sẵn sàng để xuất bản |
| **broom** | Chuyển kết quả mô hình thống kê thành các bảng gọn gàng, dễ đọc |
| **survival** | Survival analysis (ví dụ Kaplan–Meier, mô hình Cox) |
| **survminer** | Vẽ các đường cong sống còn (survival curve) đẹp mắt |

**Một vài điều bạn có thể được hỏi trong quá trình:**

- Nếu R hỏi *"Do you want to install from sources the package which needs compilation? (Yes/no/cancel)"*, an toàn nhất là gõ **`no`** và nhấn Enter (cách này dùng bản dựng sẵn và tránh các bước phụ).
- Nếu R hỏi có nên **restart R** (khởi động lại R) trước khi cài không, hãy trả lời **Yes**.
- Nếu bạn thấy từ **`Warning`**, đừng hoảng — các cảnh báo thường vô hại. Chỉ khi có thông báo bắt đầu bằng **`Error`** mới có nghĩa là thực sự có điều gì đó cần chú ý (xem Khắc phục sự cố).

---

## 6. Xác nhận nó đã hoạt động

Có hai cách kiểm tra dễ dàng. Hãy làm cách nhanh trước, rồi chạy tập lệnh (script) kiểm tra.

### Kiểm tra nhanh (gõ trong Console)

Nhấp vào **Console**, gõ từng dòng sau và nhấn **Enter** sau mỗi dòng. Kết quả mong đợi được hiển thị sau dấu `#`:

```r
2 + 2                 # should print: 4
x <- c(10, 12, 14, 16)  # stores four numbers (nothing prints — that's fine)
mean(x)               # should print: 13
library(dplyr)        # loads part of the tidyverse; a few startup messages are fine
```

Nếu `2 + 2` cho ra `4` và `mean(x)` cho ra `13`, thì R đang chạy. Nếu `library(dplyr)` tạo ra một ít chữ khởi động màu xanh hoặc đen nhưng **không có `Error`**, thì các gói của bạn đang hoạt động.

### Kiểm tra đầy đủ (tập lệnh kiểm tra)

Trong **cùng thư mục này** bạn sẽ thấy một tệp tên là **`installation_test.R`**. Đây là một tập lệnh nhỏ kiểm tra mọi thứ giúp bạn.

1. Trong RStudio, vào **File → Open File…** và mở **`installation_test.R`** (từ thư mục này).
2. Nó mở ra ở bảng trên cùng bên trái (trình soạn thảo). Để chạy toàn bộ, nhấp nút **"Source"** ở gần góc trên bên phải của bảng đó — hoặc chọn tất cả các dòng (Ctrl+A trên Windows, Cmd+A trên Mac) và nhấn **Ctrl+Enter** (Windows) / **Cmd+Enter** (Mac).
3. Quan sát Console. Nếu mọi thứ ổn, điều cuối cùng nó in ra sẽ là:

   > **My R and RStudio installation is working.**

Nếu bạn thấy thông báo đó, bạn đã sẵn sàng. Nếu thay vào đó bạn thấy một **`Error`**, hãy ghi lại nội dung của nó và xem phần Khắc phục sự cố bên dưới — hoặc mang đến buổi học đầu tiên và chúng ta sẽ cùng nhau giải quyết.

---

## 7. Khắc phục sự cố

Đừng lo nếu có gì đó không hoạt động ngay lần đầu — đây là những trục trặc thường gặp và có thể khắc phục.

| Vấn đề bạn thấy | Nó có nghĩa là gì | Phải làm gì |
|-----------------|---------------|------------|
| **Một gói "won't install"** (không cài được), hoặc một thông báo có chữ **"non-zero exit status"** | Việc cài một gói nào đó chưa hoàn tất | Chạy lại dòng `install.packages(...)` — thường lần thử thứ hai sẽ được. Hãy chắc chắn bạn đang trực tuyến. Nếu được hỏi *"install from sources… which needs compilation?"*, hãy trả lời **`no`**. |
| **"there is no package called ..."** | Gói đó chưa được cài | Chạy lại khối cài đặt ở Bước 5. Rồi nạp lại nó bằng `library(...)`. |
| **Trên máy tính bệnh viện / cơ quan, việc tải xuống thất bại, hết thời gian chờ, hoặc nhắc đến "proxy" hay "firewall"** | Mạng đang chặn việc tải xuống | Thử lại trên một **mạng khác** (ví dụ Wi-Fi ở nhà hoặc điểm phát sóng cá nhân), hoặc nhờ **bộ phận IT** cho phép truy cập `cran.r-project.org` và `posit.co`. |
| **macOS: "cannot be opened because the developer cannot be verified"** | Một cảnh báo an toàn của macOS đối với các tệp tải từ internet | **Nhấp chuột phải** (hoặc Control-click) vào tệp → chọn **Open** → nhấp **Open** lần nữa trong hộp thoại. Chỉ cần làm một lần. |
| **"Do you want to allow this app to make changes?" / hỏi mật khẩu** | Trình cài đặt cần quyền quản trị (admin) | Nhấp **Yes** và nhập mật khẩu nếu bạn có. Trên máy tính cơ quan bị khóa quyền, hãy nhờ **IT** cài đặt, hoặc dùng một laptop cá nhân cho khóa học. |
| **Một phiên bản R rất cũ đã được cài từ trước** | Một bản R từ nhiều năm trước có thể gây ra vấn đề | Cứ cài bản R mới nhất từ Bước 3 — nó cài song song. Trong RStudio, vào **Tools → Global Options → General** và đảm bảo phiên bản R mới nhất được chọn. |
| **RStudio mở ra nhưng báo không tìm thấy R** | R chưa được cài, hoặc được cài sau RStudio | Đảm bảo bạn đã làm Bước 3, rồi khởi động lại RStudio. Nếu vẫn không tìm thấy, hãy cài lại R. |
| **Mọi thứ rất chậm / laptop đã cũ** | Việc tải và cài đặt chỉ đơn giản là mất nhiều thời gian hơn | Hãy kiên nhẫn và để mỗi bước hoàn tất trước khi bắt đầu bước tiếp theo. Đóng các chương trình nặng khác. Nó vẫn sẽ hoạt động. |
| **Bạn chạy một dòng và không có gì xảy ra** | Con trỏ của bạn có thể không nằm trong Console, hoặc một gói cần thiết chưa được nạp | Nhấp **vào bên trong Console** trước, rồi gõ. Nếu một lệnh về dữ liệu hoặc biểu đồ bị lỗi, hãy đảm bảo bạn đã chạy `library(tidyverse)` (hoặc `library(...)` liên quan) trong phiên đó. |

Nếu bạn gặp khó khăn, **đến buổi học với nó chưa hoàn toàn hoạt động cũng thực sự không sao** — hãy đến sớm vài phút ở buổi học đầu tiên, hoặc gửi email cho chúng tôi, và chúng tôi sẽ giúp bạn hoàn tất việc thiết lập.

---

## 8. Bạn đã sẵn sàng khi…

- [ ] **R** đã được cài (Bước 3).
- [ ] **RStudio Desktop** đã được cài và **mở ra** hiển thị các bảng của nó (Bước 4).
- [ ] **Sáu gói** đã được cài mà không có `Error` (Bước 5).
- [ ] Gõ `2 + 2` trong Console cho ra `4`, và `mean(x)` cho ra `13` (Bước 6).
- [ ] Chạy **`installation_test.R`** in ra **"My R and RStudio installation is working."** (Bước 6).

Nếu cả năm ô đều được đánh dấu, **bạn đã thiết lập xong hoàn toàn — làm tốt lắm, và hẹn gặp bạn ở buổi học đầu tiên!**
