# Bắt đầu với R và RStudio {#ch-r-basics}

Mọi nghiên cứu lâm sàng rốt cuộc đều trở thành một bảng gồm các con số và chữ: mỗi dòng là một bệnh nhân, mỗi cột là một phép đo. Huyết áp, tuổi, kết quả xét nghiệm, chẩn đoán và quyết định điều trị đều kết thúc trong một bảng tính hoặc cơ sở dữ liệu, và cần có người biến bảng đó thành bằng chứng. Cách làm việc này có ý nghĩa quan trọng. Một phân tích thực hiện bằng cách trỏ và nhấp chuột không để lại dấu vết về những gì đã làm, đồng nghiệp khó kiểm tra lại, và khó lặp lại khi dữ liệu được chỉnh sửa hoặc khi người phản biện yêu cầu một phân tích độ nhạy. Ngược lại, một phân tích được viết dưới dạng mã lệnh trong R là một bản ghi đầy đủ, dễ đọc và có thể chạy lại cho từng bước, từ dữ liệu thô đến bảng kết quả cuối cùng. Chương này đưa bạn đi từ lần đầu mở R đến việc nhập một bộ dữ liệu lâm sàng thực tế (mô phỏng) gồm 1.500 người trưởng thành đến khám tại các cơ sở chăm sóc sức khỏe ban đầu và xem xét nó lần đầu một cách cẩn thận. Trên đường đi, bạn sẽ học một nhóm nhỏ các ý tưởng làm nền tảng cho mọi nội dung khác của cuốn sách: đối tượng, kiểu dữ liệu, vectơ, hàm, gói, dự án và khung dữ liệu (data frame).

::: {.objectives}
- Mô tả R và RStudio là gì, gọi tên bốn khung (pane) của RStudio và giải thích vì sao mã phân tích cần được viết trong script thay vì trong console.
- Dùng R như một máy tính, bao gồm thứ tự ưu tiên của toán tử và các hàm toán học có sẵn, và tính các đại lượng lâm sàng đơn giản như chỉ số khối cơ thể và huyết áp động mạch trung bình.
- Tạo, đặt tên, ghi đè và xóa đối tượng bằng mũi tên gán `<-`.
- Phân biệt các kiểu dữ liệu chính (numeric, integer, character, logical, factor và Date), kiểm tra chúng bằng `class()` và chuyển đổi giữa các kiểu, nhận biết các bẫy chuyển kiểu thường gặp.
- Tạo và truy xuất phần tử của vectơ, thực hiện phép tính số học và phép so sánh logic theo vectơ, và tóm tắt các vectơ có chứa giá trị khuyết.
- Gọi hàm với đối số theo vị trí và đối số có tên, tìm và đọc trang trợ giúp, và hiểu các thông báo lỗi thường gặp.
- Cài đặt và nạp gói, tổ chức công việc trong một RStudio Project và dùng đường dẫn tệp tương đối.
- Nhập một tệp CSV và một tệp Excel vào khung dữ liệu, kiểm tra nó bằng `dim()`, `names()`, `glimpse()`, `summary()` và `table()`, và phát hiện các vấn đề về chất lượng dữ liệu.
- Dùng toán tử pipe `|>` với các "động từ" của `dplyr`: `select()`, `filter()`, `arrange()`, `mutate()` và `count()`.
- Viết một script phân tích có cấu trúc tốt, có chú thích và có thể tái lập.
:::



## R và RStudio là gì {#sec-r-rstudio}

### R: một ngôn ngữ dành cho phân tích dữ liệu

**R** là một ngôn ngữ lập trình và môi trường phần mềm miễn phí, mã nguồn mở, được thiết kế cho tính toán thống kê và đồ họa [@rcore2026]. R ra đời vào những năm 1990 như một phiên bản mở của ngôn ngữ S được phát triển tại Phòng thí nghiệm Bell, và hiện được duy trì bởi Nhóm R Core cùng một cộng đồng người đóng góp rất lớn. Có ba đặc điểm giải thích vì sao R đã trở thành một trong những công cụ tiêu chuẩn của nghiên cứu lâm sàng và dịch tễ học.

Thứ nhất, R là phần mềm **miễn phí và mở**. Bất kỳ ai cũng có thể tải về, bất kỳ ai cũng có thể xem mã nguồn thực hiện một phép tính, và không có khoản phí bản quyền nào ngăn cách một bệnh viện huyện, một bộ môn đại học hay một bộ y tế với một phân tích thống kê hiện đại. Thứ hai, R có tính **mở rộng**. Hàng nghìn *gói* bổ sung do các nhà thống kê và nhà khoa học dữ liệu đóng góp cung cấp các phương pháp từ bảng tần số đơn giản đến phân tích sống còn, quy gán đa bội (multiple imputation), phân tích gộp và học máy. Khi một phương pháp mới được công bố, phiên bản triển khai bằng R thường xuất hiện cùng lúc. Thứ ba, và quan trọng nhất đối với nghiên cứu, R là một **ngôn ngữ**. Bạn không ra lệnh cho R bằng cách nhấp vào menu; bạn viết các chỉ dẫn. Những chỉ dẫn đó có thể được lưu lại, đọc, chia sẻ, kiểm tra và chạy lại, và đó là nền tảng của nghiên cứu có thể tái lập.

### RStudio: một nơi làm việc thuận tiện với R

Bản thân R là "động cơ" thực hiện các phép tính. Nếu dùng riêng, R chỉ cung cấp một cửa sổ khá đơn sơ để bạn gõ lệnh. **RStudio** (do công ty Posit phát triển) là một *môi trường phát triển tích hợp* (integrated development environment, IDE): một chương trình đặt bên trên R, cung cấp cho bạn trình soạn thảo script, console, trình xem dữ liệu và đồ thị, trình duyệt tệp, trình duyệt trợ giúp và nhiều tiện ích như tự động hoàn thành mã và phím tắt. Một phép so sánh hữu ích là chiếc ô tô: R là động cơ, còn RStudio là bảng đồng hồ, vô lăng và ghế ngồi. Bạn cần cả hai, bạn cài R trước, và khi cả hai đã được cài đặt, bạn chỉ cần mở RStudio, phần mềm này sẽ tự khởi động R ở phía sau.

Việc cài đặt phần mềm khá đơn giản. R được tải về từ Mạng lưu trữ R toàn diện (Comprehensive R Archive Network, CRAN) tại [https://cran.r-project.org](https://cran.r-project.org), chọn bộ cài đặt phù hợp với hệ điều hành của bạn. RStudio Desktop (miễn phí) được tải về từ [https://posit.co/download/rstudio-desktop](https://posit.co/download/rstudio-desktop). Hãy chấp nhận các tùy chọn mặc định trong cả hai bộ cài đặt.

### Bốn khung của RStudio

Khi mở RStudio, bạn sẽ thấy một cửa sổ được chia thành (tối đa) bốn khung. Biết mỗi khung dùng để làm gì sẽ xóa bỏ phần lớn sự bối rối trong giờ đầu tiên.

Table: Bốn khung của RStudio ở vị trí mặc định.

| Khung | Vị trí mặc định | Công dụng |
|------|------------------|----------------|
| Source (trình soạn thảo script) | Trên bên trái | Viết, sửa và lưu mã. Đây là bản ghi lâu dài của bản phân tích. |
| Console | Dưới bên trái | Nơi R thực sự chạy mã và in kết quả. Có thể gõ lệnh ở đây nhưng không có gì được lưu lại. |
| Environment / History | Trên bên phải | Liệt kê các đối tượng (bộ dữ liệu, giá trị, kết quả) đang có trong bộ nhớ, và các lệnh đã chạy. |
| Files / Plots / Packages / Help / Viewer | Dưới bên phải | Duyệt thư mục dự án, xem hình, quản lý gói và đọc trang trợ giúp. |

Nếu bạn chỉ thấy ba khung, nghĩa là chưa có script nào được mở: hãy chọn *File > New File > R Script* (hoặc nhấn `Ctrl+Shift+N` trên Windows, `Cmd+Shift+N` trên macOS) và khung soạn thảo sẽ xuất hiện. Các khung có thể được thay đổi kích thước và sắp xếp lại trong *Tools > Global Options > Pane Layout*, nhưng bố cục mặc định đã hợp lý và cuốn sách này giả định bạn dùng bố cục đó.

### Console và script

**Console** (cửa sổ lệnh) là một cuộc đối thoại với R. Bạn gõ một lệnh sau dấu nhắc `>`, nhấn Enter, và R trả lời ngay lập tức. Điều này rất phù hợp cho những câu hỏi nhanh ("trung bình của cột này là bao nhiêu?", "hàm này làm gì?"), nhưng cuộc đối thoại chỉ là tạm thời. Khi bạn đóng RStudio, hoặc sau vài trăm dòng kết quả, sẽ không còn bản ghi gọn gàng nào về những gì bạn đã hỏi và theo thứ tự nào.

Một **script** là một tệp văn bản thuần, có phần mở rộng `.R`, chứa các lệnh R được viết lần lượt, kèm theo các chú thích giải thích chúng. Bạn viết mã trong script, đặt con trỏ trên một dòng và nhấn `Ctrl+Enter` (Windows) hoặc `Cmd+Enter` (macOS); RStudio gửi dòng đó sang console, R chạy nó, và kết quả xuất hiện trong console y như thể bạn đã gõ trực tiếp ở đó. Bôi đen nhiều dòng rồi nhấn `Ctrl+Enter` sẽ chạy tất cả các dòng đó; `Ctrl+Shift+Enter` chạy toàn bộ script từ đầu đến cuối.

Trong cuốn sách này, mã R được trình bày trong các ô màu xám. Những dòng mà R in ra để phản hồi bắt đầu bằng `#>`, để bạn phân biệt được đầu vào và đầu ra. Ví dụ:


``` r
2 + 2
```

```
#> [1] 4
```

Ký hiệu `[1]` ở đầu kết quả là một chỉ số: nó cho biết giá trị đầu tiên hiển thị trên dòng này là phần tử số 1 của kết quả. Chỉ số này trở nên hữu ích khi R in những kết quả dài trải trên nhiều dòng.

### Vì sao script giúp phân tích có thể tái lập

Một phân tích là **có thể tái lập** (reproducible) khi một người khác (hoặc chính bạn, sáu tháng sau) có thể lấy cùng dữ liệu và cùng mã lệnh và thu được chính xác cùng kết quả. @peng2011 lập luận rằng khả năng tái lập là tiêu chuẩn tối thiểu để đánh giá khoa học tính toán: ngay cả khi một nghiên cứu không thể được *lặp lại* (replicated) một cách độc lập với các bệnh nhân mới, người đọc ít nhất phải có khả năng kiểm chứng rằng các con số được báo cáo thực sự xuất phát từ dữ liệu. Trong nghiên cứu lâm sàng, điều này quan trọng vì những lý do rất thực tế. Bộ dữ liệu được chỉnh sửa sau khi các thắc mắc về dữ liệu được giải quyết; người phản biện yêu cầu hiệu chỉnh thêm một biến; hội đồng giám sát an toàn dữ liệu yêu cầu cùng các bảng đó ở lần phân tích giữa kỳ tiếp theo; một học viên tiếp nhận dự án từ người hướng dẫn. Có script, mỗi yêu cầu này chỉ có nghĩa là chạy lại mã. Không có script, nó có nghĩa là cố gắng nhớ lại mình đã nhấp vào những gì.

@wilson2017 mô tả một tập hợp các thực hành tính toán "đủ tốt" mà bất kỳ nhà nghiên cứu nào cũng có thể áp dụng mà không cần trở thành kỹ sư phần mềm. Một số thực hành trong đó được giới thiệu ngay trong chương này: giữ nguyên dữ liệu thô và thực hiện mọi chỉnh sửa bằng mã lệnh, viết mã trong script có chú thích, đặt tên tệp và đối tượng có ý nghĩa, tổ chức mỗi công việc trong một thư mục dự án riêng, và dùng đường dẫn tệp tương đối thay vì tuyệt đối. Không thực hành nào trong số này khó, và kết hợp lại, chúng bảo vệ bạn khỏi phần lớn các lỗi len lỏi vào những phân tích thủ công.

::: {.callout-tip title="Thực hành tốt"}
Hãy viết mọi lệnh quan trọng vào script, ngay cả khi bạn thử nó trước trong console. Một quy tắc hữu ích: nếu một dòng lệnh tạo ra con số sẽ xuất hiện trong báo cáo, dòng đó phải tồn tại trong một script đã được lưu. Console dùng để khám phá; script mới là bản phân tích.
:::

## R như một máy tính {#sec-calculator}

Cách đơn giản nhất để bắt đầu với R là coi nó như một chiếc máy tính rất mạnh.

### Các toán tử số học

R hiểu các toán tử số học quen thuộc.


``` r
140 + 90     # phép cộng
```

```
#> [1] 230
```

``` r
140 - 90     # phép trừ
```

```
#> [1] 50
```

``` r
140 * 2      # phép nhân
```

```
#> [1] 280
```

``` r
140 / 90     # phép chia
```

```
#> [1] 1.556
```

``` r
2^10         # lũy thừa (2 mũ 10)
```

```
#> [1] 1024
```

``` r
17 %/% 5     # chia lấy phần nguyên: 17 chứa được bao nhiêu số 5 trọn vẹn
```

```
#> [1] 3
```

``` r
17 %% 5      # chia lấy dư (modulo): phần còn lại
```

```
#> [1] 2
```

Mọi thứ đứng sau dấu `#` trên một dòng là một **chú thích** (comment). R bỏ qua nó, nhưng người đọc thì không, và chú thích là một trong những phần quan trọng nhất của bất kỳ script nào. Cũng hãy để ý rằng R in ra `1.556` cho `140 / 90`: theo mặc định R hiển thị khoảng bảy chữ số có nghĩa (cuốn sách này dùng bốn chữ số để kết quả gọn hơn), nhưng bên trong R lưu số với độ chính xác khoảng mười lăm đến mười sáu chữ số. (Lưu ý rằng R luôn dùng dấu chấm làm dấu thập phân, khác với cách viết dấu phẩy thập phân trong tiếng Việt.)

### Thứ tự ưu tiên của toán tử

Khi một biểu thức chứa nhiều toán tử, R tuân theo thứ tự thực hiện phép tính quen thuộc trong toán học: ngoặc đơn trước, sau đó đến lũy thừa, rồi nhân và chia (từ trái sang phải), và cuối cùng là cộng và trừ (từ trái sang phải).

Table: Thứ tự R thực hiện các toán tử số học (ưu tiên cao nhất trước).

| Mức ưu tiên | Toán tử | Ý nghĩa |
|----------|----------|---------|
| 1 | `( )` | Ngoặc đơn |
| 2 | `^` | Lũy thừa |
| 3 | `-x` | Dấu trừ một ngôi (dấu âm) |
| 4 | `%%`, `%/%` | Chia lấy dư, chia lấy phần nguyên |
| 5 | `*`, `/` | Nhân, chia |
| 6 | `+`, `-` | Cộng, trừ |

Hệ quả rất dễ thấy:


``` r
2 + 3 * 4      # nhân trước: 2 + 12
```

```
#> [1] 14
```

``` r
(2 + 3) * 4    # ngoặc trước: 5 * 4
```

```
#> [1] 20
```

``` r
-2^2           # lũy thừa trước dấu trừ: -(2^2)
```

```
#> [1] -4
```

``` r
(-2)^2         # bình phương của âm hai
```

```
#> [1] 4
```

Khi còn phân vân, hãy thêm ngoặc đơn. Chúng không tốn gì, chúng thể hiện rõ ý định của bạn với người đọc, và chúng ngăn chặn cả một loại lỗi âm thầm. Một công thức sai do thứ tự ưu tiên không tạo ra thông báo lỗi nào; nó tạo ra một con số trông có vẻ hợp lý nhưng sai, và điều đó nguy hiểm hơn nhiều.

### Các hàm toán học

R có một thư viện lớn các hàm toán học có sẵn. Một **hàm** (function) là một đoạn mã có tên, nhận một hoặc nhiều đầu vào (gọi là *đối số*, arguments) đặt trong ngoặc đơn và trả về một kết quả. Chúng ta sẽ xem xét hàm một cách chi tiết trong Mục 1.6; trước mắt, chỉ cần vài hàm phổ biến là đủ.


``` r
sqrt(16)          # căn bậc hai
```

```
#> [1] 4
```

``` r
abs(-7)           # giá trị tuyệt đối
```

```
#> [1] 7
```

``` r
exp(1)            # số e, cơ số của logarit tự nhiên
```

```
#> [1] 2.718
```

``` r
log(100)          # logarit tự nhiên (cơ số e)
```

```
#> [1] 4.605
```

``` r
log10(100)        # logarit cơ số 10
```

```
#> [1] 2
```

``` r
log(8, base = 2)  # logarit với cơ số tự chọn
```

```
#> [1] 3
```

``` r
round(3.14159, 2) # làm tròn đến 2 chữ số thập phân
```

```
#> [1] 3.14
```

``` r
signif(123456, 2) # làm tròn đến 2 chữ số có nghĩa
```

```
#> [1] 120000
```

Lưu ý rằng `log()` trong R là logarit **tự nhiên**, được viết là $\ln$ trong nhiều sách giáo khoa. Điều này làm nhiều người ngạc nhiên vì họ đã quen với máy tính cầm tay, nơi "log" có nghĩa là cơ số 10. Logarit tự nhiên xuất hiện khắp nơi trong thống kê sinh học (ví dụ trong hồi quy logistic ở Chương 5, nơi tỷ số chênh được tính bằng cách lấy lũy thừa cơ số e của các hệ số bằng `exp()`), vì vậy nên ghi nhớ điều này ngay từ bây giờ.

### Một ví dụ lâm sàng: chỉ số khối cơ thể và huyết áp động mạch trung bình

Hãy dùng R cho hai phép tính mà các bác sĩ lâm sàng thực hiện hằng ngày. Chỉ số khối cơ thể (body mass index, BMI) bằng cân nặng tính theo kilôgam chia cho bình phương chiều cao tính theo mét:

$$
\text{BMI} = \frac{\text{weight (kg)}}{\text{height (m)}^2}
$$

Với một bệnh nhân nặng 78,5 kg và cao 166,2 cm, trước tiên ta phải đổi chiều cao sang mét bằng cách chia cho 100:


``` r
78.5 / (166.2 / 100)^2
```

```
#> [1] 28.42
```

Cặp ngoặc quanh `166.2 / 100` rất quan trọng. Nếu không có chúng, R sẽ tính `100^2` trước (vì lũy thừa có mức ưu tiên cao nhất) và chia 166,2 cho 10.000, cho ra một BMI vô nghĩa trên 470.000.

Huyết áp động mạch trung bình (mean arterial pressure, MAP) ước tính áp lực trung bình trong động mạch trong một chu chuyển tim. Vì tim dành khoảng hai phần ba mỗi chu chuyển ở thì tâm trương, một công thức xấp xỉ thông dụng gán trọng số cho huyết áp tâm trương (DBP) lớn hơn huyết áp tâm thu (SBP):

$$
\text{MAP} \approx \text{DBP} + \frac{\text{SBP} - \text{DBP}}{3}
$$

Với một lần đo 152/95 mmHg:


``` r
95 + (152 - 95) / 3
```

```
#> [1] 114
```

``` r
round(95 + (152 - 95) / 3, 1)
```

```
#> [1] 114
```

MAP vào khoảng 114 mmHg. Một lần nữa, cặp ngoặc quanh `152 - 95` là thiết yếu; biểu thức `95 + 152 - 95 / 3` sẽ chỉ trừ đi một phần ba huyết áp tâm trương và cho ra 215,3 mmHg, một giá trị sai nhưng không hiển nhiên vô lý trước một đôi mắt mệt mỏi.

::: {.callout-note title="Diễn giải lâm sàng"}
MAP khoảng 114 mmHg cao hơn hẳn khoảng giá trị thường gặp ở người trưởng thành có huyết áp bình thường (khoảng 70 đến 100 mmHg), phù hợp với lần đo tăng 152/95 mmHg. Điểm cần nhấn mạnh ở đây không phải là quyết định lâm sàng mà là phép tính: một khi công thức đã được viết đúng trong R, nó có thể được áp dụng y hệt cho một bệnh nhân hoặc cho cả 1.500 bệnh nhân trong một nghiên cứu, không có lỗi sao chép nào.
:::

## Đối tượng và phép gán {#sec-objects}

Tính một giá trị rồi để nó trôi khỏi màn hình thì không mấy hữu ích. Để dùng lại một giá trị, ta lưu nó vào một **đối tượng** (object, đôi khi gọi là biến): một cái tên trỏ tới một giá trị được giữ trong bộ nhớ máy tính.

### Mũi tên gán

Đối tượng được tạo bằng **toán tử gán** `<-`, gõ bằng dấu "nhỏ hơn" theo sau là dấu gạch nối. Trong tiếng Anh nó được đọc là "gets": `sbp <- 152` đọc là "sbp nhận giá trị 152". Trong RStudio, phím tắt `Alt + -` (Windows) hoặc `Option + -` (macOS) sẽ gõ mũi tên kèm khoảng trắng hai bên.


``` r
sbp <- 152    # huyết áp tâm thu của một bệnh nhân
dbp <- 95     # huyết áp tâm trương của cùng bệnh nhân đó
```

Phép gán diễn ra một cách im lặng: R lưu các giá trị nhưng không in gì ra. Để xem một đối tượng chứa gì, hãy gõ tên của nó (thao tác này ngầm gọi hàm `print()`):


``` r
sbp
```

```
#> [1] 152
```

``` r
print(dbp)
```

```
#> [1] 95
```

Đối tượng hoạt động y hệt như giá trị mà nó chứa, vì vậy có thể dùng trong các phép tính, và kết quả lại có thể được lưu thành đối tượng:


``` r
sbp + 10
```

```
#> [1] 162
```

``` r
map <- dbp + (sbp - dbp) / 3   # huyết áp động mạch trung bình
map
```

```
#> [1] 114
```

``` r
pulse_pressure <- sbp - dbp
pulse_pressure
```

```
#> [1] 57
```

Đây là cái nhìn đầu tiên về sức mạnh của lập trình. Công thức tính MAP giờ được viết một lần duy nhất, bằng các đại lượng có tên, và bất kỳ ai đọc mã cũng có thể hiểu ý nghĩa của nó.

::: {.callout-warning title="Lỗi thường gặp"}
R cũng chấp nhận `=` để gán ở cấp cao nhất (`sbp = 152` vẫn chạy), và `->` gán sang phải (`152 -> sbp`). Quy ước của cộng đồng R, được áp dụng xuyên suốt cuốn sách này, là dùng `<-` để gán và dành `=` cho việc đặt tên đối số bên trong lời gọi hàm, ví dụ `round(x, digits = 1)`. Trộn lẫn hai cách làm mã khó đọc hơn. Một lỗi liên quan là gõ `<` và `-` có khoảng trắng ở giữa: `sbp < - 152` hoàn toàn không phải là phép gán mà là câu hỏi "sbp có nhỏ hơn âm 152 không?", trả về `FALSE` và giữ nguyên `sbp`.
:::

### Đặt tên đối tượng

Tên đối tượng phải tuân theo một vài quy tắc:

- Tên có thể chứa chữ cái, chữ số, dấu chấm (`.`) và dấu gạch dưới (`_`).
- Tên phải bắt đầu bằng một chữ cái (hoặc một dấu chấm không đứng trước chữ số).
- Tên không được chứa khoảng trắng hay các ký hiệu khác như `-`, `/` hoặc `%`.
- Tên không được là các từ khóa dành riêng như `if`, `else`, `TRUE`, `FALSE`, `NA`, `function`, `for` hoặc `NULL`.

Trong phạm vi các quy tắc này, bạn được tự do lựa chọn, và đáng để suy nghĩ về việc đặt tên tốt. Tên nên cho biết đối tượng chứa gì, đủ ngắn để gõ và theo một phong cách nhất quán. Cuốn sách này dùng kiểu **snake case**: các từ viết thường nối với nhau bằng dấu gạch dưới, cũng là phong cách của bộ dữ liệu nghiên cứu tình huống (`sbp_mmhg`, `treatment_uptake`). Đưa đơn vị đo vào tên của một phép đo, như `weight_kg` hay `creatinine_umol_l`, giúp phòng tránh một lỗi lâm sàng thường gặp: nhầm lẫn giữa các đơn vị như mmol/L và mg/dL. Nên đặt tên đối tượng bằng tiếng Anh không dấu (hoặc tiếng Việt không dấu), vì chữ có dấu trong tên đối tượng dễ gây lỗi mã hóa ký tự khi chia sẻ mã.

Table: Ví dụ về tên đối tượng.

| Tên | Hợp lệ? | Nhận xét |
|------|--------|---------|
| `sbp_mmhg` | Có | Rõ ràng, có đơn vị, kiểu snake case |
| `mean_age_diagnosed` | Có | Mang tính mô tả; dài nhưng dễ đọc |
| `x2` | Có | Hợp lệ nhưng không nói gì về nội dung |
| `SBP` | Có | Hợp lệ, nhưng là một đối tượng khác với `sbp` |
| `2nd_visit` | Không | Bắt đầu bằng chữ số; hãy dùng `visit_2` |
| `systolic bp` | Không | Chứa khoảng trắng |
| `bp-control` | Không | R hiểu đây là `bp` trừ `control` |

R **phân biệt chữ hoa và chữ thường**. Các đối tượng `sbp`, `SBP` và `Sbp` là ba đối tượng khác nhau, và yêu cầu một đối tượng không tồn tại sẽ gây ra lỗi:


``` r
SBP
```

```
#> Error:
#> ! object 'SBP' not found
```

Thông báo "object 'SBP' not found" (không tìm thấy đối tượng 'SBP') có lẽ là thông báo lỗi phổ biến nhất trong R. Nó hầu như luôn có nghĩa là gõ nhầm (một chữ hoa, thiếu dấu gạch dưới) hoặc dòng lệnh tạo đối tượng đó chưa bao giờ được chạy.

### Ghi đè đối tượng và môi trường làm việc

Gán một giá trị mới cho một tên đã tồn tại sẽ **thay thế** giá trị cũ mà không có cảnh báo nào:


``` r
age <- 60
age
```

```
#> [1] 60
```

``` r
age <- 61     # giá trị cũ 60 đã mất
age
```

```
#> [1] 61
```

``` r
age <- age + 1  # dùng giá trị cũ để tính giá trị mới
age
```

```
#> [1] 62
```

Dòng `age <- age + 1` trông kỳ lạ với những ai có nền tảng toán học, nhưng lại hoàn toàn tự nhiên trong R: vế phải được tính trước bằng giá trị hiện tại của `age`, rồi kết quả được lưu ngược lại dưới cùng tên đó.

Mọi đối tượng bạn tạo ra đều nằm trong **môi trường toàn cục** (global environment), chính là nội dung mà khung Environment trong RStudio hiển thị. Bạn cũng có thể liệt kê chúng bằng mã, và xóa những đối tượng không còn cần:


``` r
ls()               # liệt kê các đối tượng trong môi trường
```

```
#> [1] "age"            "dbp"            "map"            "pulse_pressure"
#> [5] "sbp"
```

``` r
rm(pulse_pressure) # xóa một đối tượng
ls()
```

```
#> [1] "age" "dbp" "map" "sbp"
```

::: {.callout-tip title="Thực hành tốt"}
Đừng dựa vào nội dung của môi trường làm việc. Những đối tượng được tạo bởi các dòng lệnh bạn đã xóa khỏi script có thể vẫn đang ẩn trong bộ nhớ, và script của bạn có thể chỉ có vẻ chạy được là nhờ chúng. Hãy khởi động lại R thường xuyên (*Session > Restart R*, hoặc `Ctrl+Shift+F10`) và chạy script từ đầu. Trong *Tools > Global Options > General*, bỏ chọn "Restore .RData into workspace at startup" và đặt "Save workspace to .RData on exit" thành "Never", để mỗi phiên làm việc đều bắt đầu sạch sẽ [@wickham2023r4ds].
:::

## Các kiểu dữ liệu {#sec-data-types}

Mọi giá trị trong R đều có một **kiểu** (type), và kiểu quyết định R có thể làm gì với giá trị đó. Bạn có thể cộng hai con số nhưng không thể cộng hai cái tên; bạn có thể sắp xếp ngày tháng theo thứ tự thời gian, nhưng sắp xếp chúng như văn bản sẽ cho thứ tự sai. Phần lớn công việc làm sạch dữ liệu trong Chương 2, về bản chất, là đảm bảo mỗi biến có đúng kiểu.

### Các kiểu cơ bản

Table: Các kiểu dữ liệu chính dùng trong phân tích dữ liệu lâm sàng.

| Kiểu (class) | Ví dụ | Ứng dụng lâm sàng điển hình |
|--------------|---------|----------------------|
| numeric (double) | `152`, `23.4`, `-0.5` | Huyết áp, BMI, giá trị xét nghiệm |
| integer | `3L`, `0L` | Số đếm như số bệnh đồng mắc |
| character | `"Female"`, `"PHC-0142"` | Mã định danh, văn bản tự do, nhãn phân loại thô |
| logical | `TRUE`, `FALSE` | Điều kiện có/không như "SBP từ 140 trở lên" |
| factor | `Female`, `Male` (có các mức) | Biến phân loại: giới tính, cơ sở y tế, học vấn |
| Date | `2024-03-15` | Ngày tuyển chọn, ngày chẩn đoán |

Giá trị **numeric** (số) là các số thực được lưu ở dạng "độ chính xác kép" (double precision). Đây là kiểu mặc định cho mọi thứ trông giống một con số. **Integer** (số nguyên) là các số nguyên; bạn hiếm khi cần tạo chúng một cách tường minh (hậu tố `L`, như trong `3L`, làm việc đó), và với mục đích phân tích, integer và double hoạt động gần như giống hệt nhau. Giá trị **character** (ký tự), còn gọi là *chuỗi* (strings), là văn bản và luôn phải được viết trong dấu nháy, đơn hoặc kép. Giá trị **logical** (logic) là `TRUE` và `FALSE` (luôn viết hoa) và được tạo ra từ các phép so sánh. **Factor** là cách R lưu trữ dữ liệu phân loại: một tập giá trị bị giới hạn trong một danh sách nhóm cố định, gọi là các *mức* (levels). **Date** (ngày tháng) lưu ngày theo lịch ở dạng cho phép tính toán (có bao nhiêu ngày giữa lần tuyển chọn và lần theo dõi?) và sắp xếp đúng theo thứ tự thời gian.

### Kiểm tra kiểu: `class()` và các hàm `is.*()`

Hàm `class()` cho biết kiểu của bất kỳ đối tượng nào.


``` r
class(152)
```

```
#> [1] "numeric"
```

``` r
class(3L)
```

```
#> [1] "integer"
```

``` r
class("Female")
```

```
#> [1] "character"
```

``` r
class(TRUE)
```

```
#> [1] "logical"
```

``` r
class(sbp > 140)
```

```
#> [1] "logical"
```

Một nhóm hàm bắt đầu bằng `is.` đặt một câu hỏi có/không về kiểu:


``` r
is.numeric(152)
```

```
#> [1] TRUE
```

``` r
is.character(152)
```

```
#> [1] FALSE
```

``` r
is.character("152")
```

```
#> [1] TRUE
```

``` r
is.logical(FALSE)
```

```
#> [1] TRUE
```

Cặp ví dụ cuối cùng đáng được chú ý. `152` và `"152"` trông giống nhau trên màn hình, nhưng cái đầu là một con số, còn cái sau là một đoạn văn bản tình cờ được tạo thành từ các chữ số. Bạn không thể làm phép tính với cái sau:


``` r
"152" + 10
```

```
#> Error in `"152" + 10`:
#> ! non-numeric argument to binary operator
```

"Non-numeric argument to binary operator" (đối số không phải số cho toán tử hai ngôi) có nghĩa là một vế của phép `+` không phải là số. Khi gặp thông báo này trên dữ liệu thực tế, nguyên nhân thường gặp là một cột *đáng lẽ* là số nhưng lại được nhập ở dạng ký tự vì có vài ô chứa văn bản, như `"missing"`, `"<0.5"` hoặc `"n/a"`.

### Chuyển đổi kiểu: các hàm `as.*()`

Mỗi hàm `is.` có một hàm `as.` tương ứng, cố gắng chuyển một giá trị sang kiểu tương ứng. Việc này được gọi là **ép kiểu** (coercion).


``` r
as.numeric("152")       # văn bản thành số
```

```
#> [1] 152
```

``` r
as.character(152)       # số thành văn bản
```

```
#> [1] "152"
```

``` r
as.numeric(TRUE)        # TRUE trở thành 1
```

```
#> [1] 1
```

``` r
as.numeric(FALSE)       # FALSE trở thành 0
```

```
#> [1] 0
```

``` r
as.logical("TRUE")      # văn bản thành giá trị logic
```

```
#> [1] TRUE
```

``` r
as.integer(3.9)         # cắt bỏ phần thập phân về phía 0; KHÔNG làm tròn
```

```
#> [1] 3
```

### Những cái bẫy khi ép kiểu

Không phải lúc nào cũng chuyển đổi được. Khi R không thể chuyển một giá trị, nó không dừng lại với một lỗi; nó tạo ra `NA` (mã của R cho giá trị khuyết) và đưa ra một cảnh báo:


``` r
as.numeric(c("120", "135", "missing", "<90"))
```

```
#> [1] 120 135  NA  NA
```

(Cảnh báo "NAs introduced by coercion" (NA được tạo ra do ép kiểu) được ẩn đi trong kết quả của cuốn sách này nhưng sẽ xuất hiện trên màn hình của bạn.) Hành vi này tiện lợi nhưng nguy hiểm: một phép chuyển đổi bất cẩn có thể âm thầm biến thông tin thật, chẳng hạn "dưới ngưỡng phát hiện", thành dữ liệu khuyết. Hãy luôn đếm số giá trị khuyết trước và sau khi chuyển đổi, và tìm hiểu bất kỳ giá trị khuyết nào mới xuất hiện.

Cái bẫy thứ hai nảy sinh khi kết hợp các giá trị có kiểu khác nhau. Một vectơ (xem Mục 1.5) chỉ có thể chứa một kiểu, vì vậy R âm thầm chuyển mọi thứ sang kiểu linh hoạt nhất hiện có, theo thứ bậc logical < integer < numeric < character:


``` r
c(152, 138, "145")   # một giá trị văn bản biến tất cả thành văn bản
```

```
#> [1] "152" "138" "145"
```

``` r
c(TRUE, FALSE, 3)    # giá trị logic trở thành số 0/1
```

```
#> [1] 1 0 3
```

Vì vậy, chỉ cần một ô ký tự lạc lõng trong một cột huyết áp là đủ để biến cả cột thành văn bản. Đây chính xác là điều đã xảy ra với một số cột trong dữ liệu thô của nghiên cứu tình huống, như chúng ta sẽ thấy ở Mục 1.10.

Cái bẫy thứ ba là việc chuyển factor thành số. Bên trong, một factor được lưu dưới dạng các mã số nguyên (1, 2, 3, ...) có gắn nhãn, và `as.numeric()` trả về các mã, chứ không phải các nhãn:


``` r
dose <- factor(c("10", "5", "20", "5"))
dose
```

```
#> [1] 10 5  20 5 
#> Levels: 10 20 5
```

``` r
as.numeric(dose)                 # các mã nội bộ: sai!
```

```
#> [1] 1 3 2 3
```

``` r
as.numeric(as.character(dose))   # chuyển sang văn bản trước: đúng
```

```
#> [1] 10  5 20  5
```

### Factor

Các biến lâm sàng dạng phân loại, như giới tính, cơ sở y tế, trình độ học vấn hay tình trạng hút thuốc, tốt nhất nên được lưu dưới dạng factor. Một factor biết các nhóm được phép của nó (các mức) và thứ tự của chúng, điều quan trọng đối với bảng, đồ thị và, đặc biệt, đối với các mô hình hồi quy, nơi mức đầu tiên trở thành *nhóm tham chiếu* (reference category) (Chương 5).


``` r
smoking <- factor(c("Never", "Current", "Former", "Never", "Never"),
                  levels = c("Never", "Former", "Current"))
smoking
```

```
#> [1] Never   Current Former  Never   Never  
#> Levels: Never Former Current
```

``` r
levels(smoking)
```

```
#> [1] "Never"   "Former"  "Current"
```

``` r
table(smoking)
```

```
#> smoking
#>   Never  Former Current 
#>       3       1       1
```

Nếu không có đối số `levels`, R sẽ sắp xếp các mức theo thứ tự bảng chữ cái (Current, Former, Never), hiếm khi là thứ tự mà bác sĩ lâm sàng muốn đọc (ở đây `"Never"` là chưa bao giờ hút, `"Former"` là đã bỏ, `"Current"` là đang hút). Một giá trị không nằm trong các mức sẽ trở thành `NA`, đây là một cơ chế bảo vệ hữu ích chống lại lỗi chính tả: `factor("Curent", levels = c("Never", "Former", "Current"))` cho ra `NA` thay vì tạo ra một nhóm thứ tư giả tạo.

### Ngày tháng

Ngày tháng được lưu dưới dạng số ngày tính từ 1 tháng 1 năm 1970, điều này cho phép tính toán, nhưng chúng được in ra ở định dạng năm-tháng-ngày quen thuộc. Hàm `as.Date()` chuyển văn bản ở định dạng tiêu chuẩn quốc tế (ISO 8601, `YYYY-MM-DD`) thành ngày tháng:


``` r
enrol <- as.Date("2024-03-15")
followup <- as.Date("2024-09-11")
class(enrol)
```

```
#> [1] "Date"
```

``` r
followup - enrol                  # hiệu số tính bằng ngày
```

```
#> Time difference of 180 days
```

``` r
as.numeric(followup - enrol) / 7  # tính bằng tuần
```

```
#> [1] 25.71
```

``` r
format(enrol, "%d %B %Y")         # in ra theo định dạng dễ đọc hơn
```

```
#> [1] "15 March 2024"
```

Ngày tháng được nhập theo các định dạng khác, như `15/03/2024` hoặc `15-Mar-2024`, cần được cho biết định dạng của chúng, và các bộ dữ liệu trộn lẫn nhiều định dạng là chuyện thường gặp. Gói **lubridate** [@grolemund2011] giúp việc đọc những ngày tháng như vậy dễ dàng hơn nhiều, và chúng ta sẽ dùng nó trong Chương 2.

::: {.callout-note title="Diễn giải lâm sàng"}
Kiểu dữ liệu không phải là một chi tiết kỹ thuật vụn vặt. Nếu việc sử dụng điều trị được lưu dưới dạng văn bản `"1"` và `"0"` ở một số dòng và `"Yes"` và `"No"` ở các dòng khác, bảng tần số sẽ hiện bốn nhóm thay vì hai và mọi tỷ lệ đều sai. Nếu ngày tuyển chọn được lưu dưới dạng văn bản, "01/02/2024" sẽ được xếp trước "2024-01-12" bất kể ngày nào thực sự đến trước. Xác định đúng kiểu dữ liệu là bước đầu tiên của một phân tích hợp lệ.
:::

## Vectơ {#sec-vectors}

Cho đến giờ, mỗi đối tượng chỉ chứa một giá trị. Dĩ nhiên, dữ liệu lâm sàng gồm rất nhiều giá trị: huyết áp tâm thu của tất cả bệnh nhân trong một phòng khám, giới tính của tất cả người tham gia. Cấu trúc cơ bản của R cho một tập hợp giá trị là **vectơ** (vector): một dãy giá trị có thứ tự, tất cả cùng một kiểu. Thực ra, một con số đơn lẻ như `152` chỉ đơn giản là một vectơ có độ dài bằng một, và đó là lý do R in `[1]` phía trước nó.

### Tạo vectơ

Hàm `c()`, viết tắt của "combine" (kết hợp), tạo một vectơ từ các đối số của nó.


``` r
sbp_readings <- c(152, 138, 145, 160, 129, 142)   # số
sex <- c("Female", "Male", "Female", "Female", "Male", "Female")  # ký tự
on_treatment <- c(TRUE, FALSE, TRUE, TRUE, FALSE, FALSE)          # logic
sbp_readings
```

```
#> [1] 152 138 145 160 129 142
```

``` r
length(sbp_readings)
```

```
#> [1] 6
```

Sáu giá trị này có thể là huyết áp tâm thu của sáu bệnh nhân khám trong một buổi sáng tại phòng khám, với giới tính và tình trạng điều trị của họ ở các vị trí tương ứng.

### Dãy số đều: `seq()`, `:` và `rep()`

Các dãy số thường xuyên được cần đến, ví dụ để xác định các nhóm tuổi hay các thời điểm theo dõi. Toán tử dấu hai chấm tạo dãy số nguyên, `seq()` tạo dãy với bước nhảy bất kỳ, và `rep()` lặp lại các giá trị.


``` r
1:10                                  # các số nguyên từ 1 đến 10
```

```
#>  [1]  1  2  3  4  5  6  7  8  9 10
```

``` r
seq(from = 18, to = 88, by = 10)      # ranh giới các nhóm tuổi
```

```
#> [1] 18 28 38 48 58 68 78 88
```

``` r
seq(0, 1, length.out = 5)             # năm giá trị cách đều nhau
```

```
#> [1] 0.00 0.25 0.50 0.75 1.00
```

``` r
rep("Control", times = 3)             # lặp lại một giá trị
```

```
#> [1] "Control" "Control" "Control"
```

``` r
rep(c("A", "B"), times = 3)           # lặp lại một mẫu
```

```
#> [1] "A" "B" "A" "B" "A" "B"
```

``` r
rep(c("A", "B"), each = 3)            # lặp lại từng phần tử
```

```
#> [1] "A" "A" "A" "B" "B" "B"
```

Hai dòng cuối cho thấy sự khác biệt giữa đối số `times` và `each`, điều hữu ích khi xây dựng, chẳng hạn, một danh sách phân bổ điều trị theo thiết kế khối.

### Truy xuất phần tử: lấy ra các phần tử

Từng phần tử của một vectơ được lấy ra bằng dấu ngoặc vuông `[ ]`. Vị trí trong R bắt đầu từ 1 (không phải 0 như trong một số ngôn ngữ khác).


``` r
sbp_readings[1]          # lần đo thứ nhất
```

```
#> [1] 152
```

``` r
sbp_readings[c(1, 3)]    # lần đo thứ nhất và thứ ba
```

```
#> [1] 152 145
```

``` r
sbp_readings[2:4]        # từ lần đo thứ hai đến thứ tư
```

```
#> [1] 138 145 160
```

``` r
sbp_readings[-1]         # tất cả trừ lần đo thứ nhất
```

```
#> [1] 138 145 160 129 142
```

``` r
sbp_readings[length(sbp_readings)]  # lần đo cuối cùng
```

```
#> [1] 142
```

Một chỉ số âm sẽ loại bỏ phần tử thay vì chọn chúng. Truy xuất vượt quá cuối vectơ sẽ trả về `NA` thay vì báo lỗi, đây là một tình huống khác mà R lặng lẽ trả cho bạn một giá trị khuyết.

Cách truy xuất hữu ích nhất dùng một **vectơ logic**: R giữ lại những phần tử ở các vị trí mà chỉ số là `TRUE`.


``` r
sbp_readings[on_treatment]          # SBP của các bệnh nhân đang điều trị
```

```
#> [1] 152 145 160
```

``` r
sbp_readings[sex == "Male"]         # SBP của các bệnh nhân nam
```

```
#> [1] 138 129
```

Đây là ý tưởng làm nền tảng cho mọi thao tác lọc dữ liệu, từ việc chọn ra các bệnh nhân tăng huyết áp trong một nghiên cứu đến việc loại bỏ các giá trị không hợp lý.

### Phép tính theo vectơ

Phép tính số học trong R được **vectơ hóa** (vectorised): một phép toán áp dụng cho một vectơ sẽ được áp dụng cho mọi phần tử cùng lúc, không cần viết vòng lặp.


``` r
sbp_readings - 10           # trừ 10 khỏi mỗi lần đo
```

```
#> [1] 142 128 135 150 119 132
```

``` r
sbp_readings / 7.5          # đổi mmHg sang kPa (1 kPa = 7,5 mmHg)
```

```
#> [1] 20.27 18.40 19.33 21.33 17.20 18.93
```

``` r
dbp_readings <- c(95, 88, 90, 101, 79, 85)
map_readings <- dbp_readings + (sbp_readings - dbp_readings) / 3
round(map_readings, 1)
```

```
#> [1] 114.0 104.7 108.3 120.7  95.7 104.0
```

Khi hai vectơ có cùng độ dài được kết hợp, R ghép cặp chúng theo từng phần tử: SBP thứ nhất với DBP thứ nhất, thứ hai với thứ hai, và cứ thế. Đây chính xác là điều ta muốn khi mỗi vị trí đại diện cho một bệnh nhân. (Nếu độ dài khác nhau, R sẽ *tái sử dụng* (recycle) vectơ ngắn hơn, kèm cảnh báo nếu độ dài này không phải là bội số của độ dài kia. Việc tái sử dụng thỉnh thoảng hữu ích nhưng thường là dấu hiệu của một sai sót.)

### Phép so sánh logic

Các toán tử so sánh tạo ra vectơ logic.

Table: Các toán tử so sánh và toán tử logic trong R.

| Toán tử | Ý nghĩa | Ví dụ |
|----------|---------|---------|
| `==` | bằng | `sex == "Female"` |
| `!=` | khác | `sex != "Female"` |
| `<`, `<=` | nhỏ hơn (hoặc bằng) | `sbp < 140` |
| `>`, `>=` | lớn hơn (hoặc bằng) | `dbp >= 90` |
| `&` | và (cả hai đều đúng) | `sbp >= 140 & dbp >= 90` |
| `!` | phủ định (không) | `!on_treatment` |
| `%in%` | thuộc một tập hợp | `sex %in% c("F", "f")` |

Bảng trên bỏ qua một toán tử vì ký hiệu của nó xung đột với cách trình bày bảng: dấu gạch đứng `|` có nghĩa là *hoặc*, vì vậy `sbp >= 140 | dbp >= 90` là `TRUE` khi ít nhất một trong hai điều kiện đúng. Cũng hãy lưu ý dấu bằng kép `==` dùng để so sánh; một dấu `=` đơn là phép gán hoặc tên đối số, không bao giờ là phép kiểm tra bằng nhau.


``` r
high_sbp <- sbp_readings >= 140
high_sbp
```

```
#> [1]  TRUE FALSE  TRUE  TRUE FALSE  TRUE
```

``` r
high_bp <- sbp_readings >= 140 | dbp_readings >= 90   # một trong hai tăng
high_bp
```

```
#> [1]  TRUE FALSE  TRUE  TRUE FALSE  TRUE
```

Vì trong phép tính số học `TRUE` được coi là 1 và `FALSE` là 0, hàm `sum()` của một vectơ logic sẽ đếm số giá trị `TRUE` và `mean()` cho ra tỷ lệ của chúng. Mẹo nhỏ này được dùng liên tục trong phân tích dữ liệu.


``` r
sum(high_bp)    # bao nhiêu bệnh nhân có chỉ số huyết áp tăng
```

```
#> [1] 4
```

``` r
mean(high_bp)   # tỷ lệ
```

```
#> [1] 0.6667
```

Bốn trong sáu bệnh nhân (67%) có huyết áp tâm thu từ 140 mmHg trở lên hoặc huyết áp tâm trương từ 90 mmHg trở lên, là các ngưỡng quy ước cho huyết áp tăng khi đo tại phòng khám [@who2021htn]. Trong ví dụ nhỏ này, những bệnh nhân có huyết áp tâm trương tăng tình cờ cũng có huyết áp tâm thu tăng, nên `high_bp` và `high_sbp` trùng nhau; trong một mẫu lớn hơn thì điều này sẽ không xảy ra.

### Các hàm tóm tắt

R có nhiều hàm thu gọn một vectơ thành một giá trị tóm tắt duy nhất. Chúng ta sẽ tìm hiểu chúng một cách đầy đủ, cùng với ý nghĩa thống kê, trong Chương 3; dưới đây là phần giới thiệu trước.


``` r
mean(sbp_readings)
```

```
#> [1] 144.3
```

``` r
median(sbp_readings)
```

```
#> [1] 143.5
```

``` r
sd(sbp_readings)       # độ lệch chuẩn
```

```
#> [1] 10.82
```

``` r
min(sbp_readings)
```

```
#> [1] 129
```

``` r
max(sbp_readings)
```

```
#> [1] 160
```

``` r
range(sbp_readings)
```

```
#> [1] 129 160
```

``` r
summary(sbp_readings)  # tóm tắt sáu con số
```

```
#>    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
#>     129     139     144     144     150     160
```

Kết quả của `summary()` cho biết, từ trái sang phải, giá trị nhỏ nhất, tứ phân vị thứ nhất (25% số giá trị nằm dưới nó), trung vị, trung bình, tứ phân vị thứ ba và giá trị lớn nhất. Với sáu lần đo này, trung bình (144,3) và trung vị (143,5) gần nhau, cho thấy các giá trị phân bố khá đối xứng quanh trung tâm.

Với một vectơ ký tự, cách tóm tắt tự nhiên là bảng tần số:


``` r
table(sex)
```

```
#> sex
#> Female   Male 
#>      4      2
```

### Giá trị khuyết: `NA`

Dữ liệu thực tế luôn có những chỗ trống. Một mẫu máu bị vỡ hồng cầu, một bệnh nhân từ chối cân, một phiếu bị bỏ trống. R biểu diễn một giá trị khuyết bằng ký hiệu đặc biệt `NA` ("not available", không có sẵn), có thể xuất hiện trong vectơ thuộc bất kỳ kiểu nào. Giá trị khuyết có tính "lây lan": bất kỳ phép tính nào có một giá trị chưa biết thì kết quả cũng chưa biết.


``` r
weights <- c(61.3, 68.3, NA, 78.5, 71.6)
weights + 1
```

```
#> [1] 62.3 69.3   NA 79.5 72.6
```

``` r
mean(weights)
```

```
#> [1] NA
```

Trung bình của năm số trong đó có một số chưa biết thì không thể biết được, vì vậy R trả lời `NA`. Đây là mặc định đúng đắn, vì nó buộc bạn phải để ý đến giá trị khuyết. Để tính trung bình của các giá trị *quan sát được*, hãy đặt đối số `na.rm = TRUE` ("NA remove", loại bỏ NA):


``` r
mean(weights, na.rm = TRUE)
```

```
#> [1] 69.92
```

``` r
sum(is.na(weights))    # có bao nhiêu giá trị bị khuyết?
```

```
#> [1] 1
```

Hàm `is.na()` trả về `TRUE` cho mỗi phần tử bị khuyết, vì vậy `sum(is.na(x))` đếm số giá trị khuyết. Bạn không thể kiểm tra giá trị khuyết bằng `x == NA`, vì so sánh bất kỳ thứ gì với một giá trị chưa biết cũng cho kết quả chưa biết: `NA == NA` là `NA`.

::: {.callout-warning title="Lỗi thường gặp"}
Đừng tự động dùng ngay `na.rm = TRUE`. Rất dễ tính ra một giá trị trung bình "của tất cả bệnh nhân" mà thực chất chỉ là trung bình của 60% số người đã làm xét nghiệm. Hãy luôn báo cáo số giá trị bị khuyết kèm theo mọi giá trị tóm tắt, và suy nghĩ xem vì sao chúng bị khuyết: những giá trị bị khuyết vì một lý do liên quan đến biến kết cục có thể làm sai lệch kết quả [@little2019]. Dữ liệu khuyết được thảo luận thêm trong Chương 2 và Chương 3.
:::

## Hàm, đối số và trợ giúp {#sec-functions}

### Cấu trúc của một lời gọi hàm

Bạn đã dùng nhiều hàm: `sqrt()`, `round()`, `mean()`, `c()`, `seq()`. Mọi lời gọi hàm đều có cùng một hình dạng: tên hàm, theo sau là cặp ngoặc đơn chứa các **đối số** của nó, phân cách nhau bằng dấu phẩy. Đối số là các đầu vào cho hàm biết cần xử lý cái gì và xử lý như thế nào.


``` r
round(144.33333, digits = 1)
```

```
#> [1] 144.3
```

Ở đây `round` là hàm, `144.33333` là đối số thứ nhất (con số cần làm tròn) và `digits = 1` là đối số thứ hai điều khiển cách hàm hoạt động. Hàm trả về một giá trị, mà R sẽ in ra hoặc bạn có thể lưu vào một đối tượng.

### Đối số theo vị trí và đối số có tên

Đối số có thể được cung cấp theo hai cách. Đối số **theo vị trí** (positional) được ghép theo thứ tự của chúng trong định nghĩa hàm; đối số **có tên** (named) được ghép theo tên, với thứ tự bất kỳ. Định nghĩa của `seq()` bắt đầu bằng `seq(from, to, by, ...)`, vì vậy các lời gọi sau là tương đương:


``` r
seq(18, 88, 10)                   # theo vị trí
```

```
#> [1] 18 28 38 48 58 68 78 88
```

``` r
seq(from = 18, to = 88, by = 10)  # có tên
```

```
#> [1] 18 28 38 48 58 68 78 88
```

``` r
seq(by = 10, to = 88, from = 18)  # có tên, thứ tự bất kỳ
```

```
#> [1] 18 28 38 48 58 68 78 88
```

Nhiều đối số có **giá trị mặc định**, được dùng khi bạn không cung cấp chúng. Giá trị mặc định của `digits` trong `round()` là 0, và giá trị mặc định của `na.rm` trong `mean()` là `FALSE`, đó là lý do `mean()` trả về `NA` ở ví dụ trên.

::: {.callout-tip title="Thực hành tốt"}
Một thói quen tốt là cung cấp một hoặc hai đối số đầu tiên theo vị trí (chúng thường là dữ liệu, và ý nghĩa của chúng là hiển nhiên) và tất cả các đối số khác theo tên, như trong `mean(weights, na.rm = TRUE)` hoặc `round(map, digits = 1)`. Đối số có tên khiến mã tự giải thích được và bảo vệ bạn nếu thứ tự đối số của hàm có lúc thay đổi.
:::

Các hàm có thể được **lồng nhau**, khi đầu ra của hàm này trở thành đầu vào của hàm khác. R tính chúng từ trong ra ngoài:


``` r
round(mean(weights, na.rm = TRUE), 1)
```

```
#> [1] 69.9
```

Ở đây `mean()` được tính trước và kết quả của nó (69,925) được chuyển cho `round()`. Lồng hàm quá sâu sẽ nhanh chóng trở nên khó đọc, và đó là vấn đề mà toán tử pipe giải quyết (Mục 1.11).

### Tìm trợ giúp

Không ai nhớ hết mọi hàm và mọi đối số. Biết cách tra cứu là một kỹ năng cốt lõi. Mỗi hàm trong R đều có một trang trợ giúp, mà bạn mở bằng `?` hoặc `help()`:


``` r
?mean                 # trang trợ giúp của mean()
help("read_csv")      # tương tự, dưới dạng lời gọi hàm
??"standard deviation" # tìm một cụm từ trong tất cả các trang trợ giúp
example(mean)         # chạy các ví dụ ở cuối trang trợ giúp
vignette("dplyr")     # một bài hướng dẫn dài hơn đi kèm với gói
```

Các trang trợ giúp hiện ra trong khung Help và luôn có cùng một cấu trúc: *Description* (hàm làm gì), *Usage* (các đối số và giá trị mặc định), *Arguments* (ý nghĩa của từng đối số), *Value* (giá trị trả về), *Details*, *See Also* và, hữu ích nhất, *Examples* ở cuối trang, mà bạn có thể sao chép vào console để chạy. Trang trợ giúp được viết ngắn gọn và lúc đầu có thể cảm thấy khô khan; đọc phần Usage và Examples trước là một chiến lược tốt. Ngoài trợ giúp của chính R, cuốn sách trực tuyến miễn phí *R for Data Science* [@wickham2023r4ds] và trang web của các gói là những tài liệu tham khảo tuyệt vời. Khi tìm kiếm trên internet, hãy thêm "R" và tên gói cùng với thông báo lỗi hoặc tác vụ cần làm (tìm bằng tiếng Anh thường cho nhiều kết quả hơn).

### Đọc thông báo lỗi

Lỗi là một phần bình thường của lập trình, không phải dấu hiệu thất bại. R dừng lại và in ra một thông báo bắt đầu bằng `Error`; thông báo mô tả điều gì đã sai, và học cách đọc nó sẽ tiết kiệm cho bạn hàng giờ. Cảnh báo (warnings), bắt đầu bằng `Warning`, có nghĩa là R đã hoàn thành lệnh nhưng có thể có điều gì đó không ổn; không bao giờ được bỏ qua chúng. Dưới đây là một số lỗi thường gặp và nguyên nhân thường thấy:

Table: Các thông báo lỗi R thường gặp và nguyên nhân thường thấy.

| Thông báo | Nguyên nhân thường thấy |
|---------|-------------|
| `object 'x' not found` | Gõ nhầm, sai chữ hoa/thường, hoặc dòng tạo ra `x` chưa được chạy |
| `could not find function "x"` | Viết sai tên hàm, hoặc gói chứa hàm chưa được nạp bằng `library()` |
| `non-numeric argument to binary operator` | Tính toán trên văn bản, thường là một con số được lưu dưới dạng ký tự |
| `unexpected symbol` / `unexpected ')'` | Lỗi cú pháp: thiếu dấu phẩy, dấu ngoặc hoặc dấu nháy |
| `'file.csv' does not exist in current working directory` | Sai đường dẫn tệp hoặc sai thư mục làm việc |
| `there is no package called 'x'` | Gói chưa được cài đặt |

Dưới đây là một trong số đó trong thực tế. Ta thử dùng một hàm từ một gói chưa được nạp trong phiên làm việc hiện tại:


``` r
clean_names(data.frame(Patient.ID = 1))
```

```
#> Error in `clean_names()`:
#> ! could not find function "clean_names"
```

Cách khắc phục là nạp gói cung cấp `clean_names()` (ở đây là **janitor**) hoặc gọi hàm kèm tiền tố tên gói, như `janitor::clean_names()`.

Một nguồn gây bối rối thường gặp là lệnh *chưa hoàn chỉnh*. Nếu bạn quên một dấu ngoặc đóng hoặc dấu nháy, dấu nhắc của console chuyển từ `>` thành `+`, nghĩa là R đang chờ bạn hoàn thành lệnh. Hãy hoàn thành nó hoặc nhấn `Esc` để hủy và bắt đầu lại.

::: {.callout-warning title="Lỗi thường gặp"}
Quên dấu nháy quanh văn bản là một lỗi kinh điển. `sex == Female` yêu cầu R so sánh `sex` với một *đối tượng* có tên `Female`, vốn không tồn tại ("object 'Female' not found"). Giá trị văn bản luôn cần dấu nháy: `sex == "Female"`. Ngược lại, tên đối tượng và tên cột không cần dấu nháy trong hầu hết các hàm: `mean(sbp)`, chứ không phải `mean("sbp")`.
:::

## Gói {#sec-packages}

### Cài đặt một lần, nạp mỗi phiên làm việc

Các hàm đi kèm R ("base R") bao quát rất nhiều thứ, nhưng phần lớn sức mạnh của R đến từ các **gói** (packages): những tập hợp hàm, dữ liệu và tài liệu do cộng đồng viết và phân phối qua CRAN. Năm 2026, CRAN lưu trữ hơn hai mươi nghìn gói. Sử dụng một gói gồm hai bước riêng biệt:

1. **Cài đặt** gói, tức là tải gói về từ internet và lưu trên máy tính của bạn. Bạn làm việc này *một lần* trên mỗi máy tính (và chỉ làm lại khi nâng cấp R hoặc muốn có phiên bản mới hơn của gói).
2. **Nạp** gói bằng `library()`, giúp các hàm của gói có sẵn trong phiên làm việc R hiện tại. Bạn làm việc này *mỗi lần* khởi động R, ở đầu mỗi script.

Một phép so sánh hữu ích: cài đặt một gói giống như mua một cuốn sách và đặt nó lên giá; nạp gói giống như lấy sách từ giá xuống để đọc. Bạn mua sách một lần, nhưng lấy nó xuống bất cứ khi nào cần.


``` r
install.packages("tidyverse")   # một lần trên mỗi máy tính: tải về từ CRAN
install.packages("readxl")
```


``` r
library(tidyverse)   # mỗi phiên: nhập, xử lý dữ liệu, ggplot2
library(readxl)      # mỗi phiên: đọc tệp Excel
```

Khi được nạp, tidyverse in ra một thông báo ngắn liệt kê các gói nó đã gắn vào và một vài "xung đột" (conflicts), tức là các hàm trong những gói khác nhau có cùng tên. Ví dụ, cả gói **stats** của base R và **dplyr** đều có một hàm tên là `filter()`; sau `library(tidyverse)`, tên `filter` chỉ phiên bản của dplyr. Nếu cần nói rõ, toán tử hai dấu hai chấm `package::function()` gọi một hàm từ một gói cụ thể, dù gói đó đã được nạp hay chưa, như `dplyr::filter()` hoặc `stats::filter()`.

::: {.callout-warning title="Lỗi thường gặp"}
Đừng đặt `install.packages()` trong một script phân tích được chạy mỗi lần. Làm vậy vừa chậm, cần kết nối internet, có thể âm thầm cập nhật một gói lên phiên bản hoạt động khác đi, và sẽ thất bại trên những máy tính mà bạn không có quyền cài đặt phần mềm. Hãy cài đặt gói một lần từ console (hoặc bằng một dòng đã được biến thành chú thích, như ở trên); nạp chúng bằng `library()` ở đầu mỗi script.
:::

### Tidyverse

**Tidyverse** là một bộ sưu tập các gói có chung triết lý thiết kế, ngữ pháp và cấu trúc dữ liệu [@wickham2019tidyverse]. Nạp nó bằng `library(tidyverse)` sẽ gắn các thành viên cốt lõi cùng một lúc:

- **readr** để đọc các tệp dữ liệu dạng bảng như CSV;
- **dplyr** để xử lý khung dữ liệu (chọn, lọc, tóm tắt);
- **tidyr** để thay đổi hình dạng dữ liệu;
- **ggplot2** để vẽ đồ thị [@wickham2016ggplot2];
- **stringr** để làm việc với văn bản, **forcats** cho factor và **lubridate** cho ngày tháng;
- **tibble**, một phiên bản hiện đại của khung dữ liệu, và **purrr** cho các thao tác lặp lại.

Tidyverse được xây dựng quanh ý tưởng **dữ liệu gọn gàng** (tidy data), trong đó mỗi biến là một cột, mỗi quan sát là một dòng và mỗi giá trị là một ô [@wickham2014tidy]. Một bộ dữ liệu lâm sàng ở cấp độ bệnh nhân với mỗi dòng là một bệnh nhân vốn đã gọn gàng một cách tự nhiên, và đó là một lý do khiến tidyverse rất phù hợp với nghiên cứu lâm sàng. Cuốn sách này dùng các hàm của tidyverse cho phần lớn việc xử lý dữ liệu và vẽ đồ thị, và dùng base R khi cách đó đơn giản hơn. Các gói khác, như **readxl** cho tệp Excel, **janitor** cho làm sạch dữ liệu, **gtsummary** cho các bảng sẵn sàng xuất bản [@sjoberg2021] và **broom** cho kết quả mô hình gọn gàng, sẽ được giới thiệu khi cần đến.

## Dự án, thư mục làm việc và đường dẫn tệp {#sec-projects}

### Thư mục làm việc

Khi bạn yêu cầu R đọc một tệp, R phải biết cần tìm ở đâu. **Thư mục làm việc** (working directory) là thư mục mà R coi là vị trí hiện tại của nó; một tên tệp không có đường dẫn đầy đủ sẽ được tìm ở đó.


``` r
getwd()   # in ra thư mục làm việc hiện tại
```

Trên máy tính dùng để biên soạn cuốn sách này, `getwd()` trả về một đường dẫn kết thúc bằng `.../Course`, thư mục chứa thư mục `Data/` của nghiên cứu tình huống. Trên máy tính của bạn, đường dẫn sẽ khác.

### Đường dẫn tuyệt đối và tương đối

Một **đường dẫn tuyệt đối** (absolute path) cho biết vị trí đầy đủ của một tệp tính từ gốc của ổ đĩa, ví dụ `C:/Users/amina/Documents/htn_study/Data/hypertension_phc_raw.csv`. Một **đường dẫn tương đối** (relative path) cho biết vị trí so với thư mục làm việc, ví dụ `Data/hypertension_phc_raw.csv`. Đường dẫn tuyệt đối chỉ hoạt động trên chiếc máy tính nơi nó được viết ra, và chỉ cho đến khi một thư mục bị đổi tên; đường dẫn tương đối vẫn hoạt động khi toàn bộ thư mục dự án được sao chép sang máy tính xách tay của đồng nghiệp, một máy chủ hay một chiếc USB.

Lưu ý rằng R dùng dấu gạch chéo xuôi `/` trong đường dẫn, ngay cả trên Windows. Nếu bạn sao chép một đường dẫn từ Windows Explorer, vốn dùng dấu gạch chéo ngược, hãy thay chúng bằng `/` hoặc gấp đôi chúng (`\\`), vì một dấu gạch chéo ngược đơn có ý nghĩa đặc biệt bên trong chuỗi ký tự của R.

### RStudio Project

Cách đáng tin cậy để quản lý thư mục làm việc là dùng một **RStudio Project**. Một project đơn giản là một thư mục chứa một tệp nhỏ có phần mở rộng `.Rproj`. Khi bạn mở project (bằng cách nhấp đúp vào tệp `.Rproj`, hoặc qua *File > Open Project*), RStudio khởi động một phiên R mới với thư mục làm việc là thư mục của project. Khi đó, mọi đường dẫn tương đối trong script của bạn đều được hiểu đúng, bất kể project nằm trên máy tính nào.

Để tạo một project, chọn *File > New Project*, sau đó chọn *New Directory* (để bắt đầu từ đầu) hoặc *Existing Directory* (để biến một thư mục sẵn có thành project). Một bố cục đơn giản phù hợp với hầu hết các phân tích lâm sàng, theo tinh thần của @wilson2017, như sau:


``` r
htn_study/
  htn_study.Rproj
  Data/        # dữ liệu thô (không bao giờ sửa bằng tay) và dữ liệu đã làm sạch
  Scripts/     # các script R, đánh số theo thứ tự chạy
  Outputs/     # bảng và hình do các script tạo ra
  Reports/     # bản thảo bài báo và báo cáo
```

::: {.callout-warning title="Lỗi thường gặp"}
Tránh bắt đầu script bằng `setwd("C:/Users/yourname/Desktop/analysis")`. Dòng lệnh này chỉ hoạt động trên đúng một máy tính, và script sẽ thất bại với thông báo "cannot change working directory" (không thể thay đổi thư mục làm việc) đối với bất kỳ ai khác, kể cả chính bạn trên một máy tính mới. Thay vào đó, hãy dùng RStudio Project và đường dẫn tương đối. Tương tự, tránh lưu dữ liệu ở một thư mục khác với các script phân tích chúng; hãy giữ mọi thứ thuộc về một nghiên cứu trong cùng một project.
:::

## Nghiên cứu tình huống và nhập dữ liệu {#sec-import}

### Nghiên cứu tình huống

Mọi ví dụ trong cuốn sách này đều dùng một bộ dữ liệu duy nhất, để bạn có thể theo dõi một phân tích từ dữ liệu thô đến mô hình cuối cùng. Bộ dữ liệu đến từ một nghiên cứu cắt ngang đa trung tâm, *Các yếu tố quyết định việc sử dụng điều trị tăng huyết áp ở người trưởng thành đến khám tại các cơ sở chăm sóc sức khỏe ban đầu*, trong đó 1.500 người trưởng thành đến khám tại sáu cơ sở chăm sóc sức khỏe ban đầu (primary healthcare, PHC) được đưa vào nghiên cứu. Câu hỏi nghiên cứu là: trong số những người trưởng thành đã được chẩn đoán tăng huyết áp, những yếu tố nào quyết định việc họ hiện có đang dùng thuốc hạ huyết áp hay không? Tăng huyết áp ảnh hưởng tới hơn một tỷ người trưởng thành trên toàn thế giới, và một phần lớn những người đã được chẩn đoán không được điều trị [@ncdrisc2021; @mills2020], vì vậy hiểu được các rào cản đối với việc sử dụng điều trị là một ưu tiên y tế công cộng thực sự.

Bộ dữ liệu ghi nhận các đặc điểm nhân khẩu học (tuổi, giới tính, nơi cư trú, học vấn, nghề nghiệp, tình trạng hôn nhân, bảo hiểm y tế), hành vi (hút thuốc, uống rượu bia, hoạt động thể lực), các số đo lâm sàng (chiều cao, cân nặng, BMI, huyết áp, bệnh đồng mắc, tiền sử gia đình, đái tháo đường), các dấu ấn sinh học xét nghiệm (lipid máu, glucose, creatinine, điện giải), điểm hiểu biết về tăng huyết áp, khoảng cách đến cơ sở y tế, và các biến kết cục: bệnh nhân có được chẩn đoán tăng huyết áp hay không (`htn_diagnosed`), có đang điều trị hay không (`treatment_uptake`, biến kết cục chính), mức độ tuân thủ điều trị và huyết áp có được kiểm soát hay không. Định nghĩa đầy đủ có trong từ điển dữ liệu, `Data/data_dictionary.md`.

Dữ liệu được **mô phỏng cho mục đích giảng dạy**. Chúng được tạo ra để giống với dữ liệu thực tế từ tuyến chăm sóc ban đầu, bao gồm các mối quan hệ thực tế giữa các biến và, một cách có chủ ý, những loại lỗi thường thấy trong các tệp thu thập dữ liệu thực tế. Các kết quả thu được từ dữ liệu này minh họa phương pháp; chúng không phải là phát hiện lâm sàng.

### Khung dữ liệu và tibble

Một vectơ chứa một biến. Một nghiên cứu cần nhiều biến được đo trên cùng các bệnh nhân, và R lưu chúng trong một **khung dữ liệu** (data frame): một bảng hình chữ nhật trong đó mỗi cột là một vectơ (tất cả cùng một kiểu) và mọi cột đều có cùng độ dài. Mỗi dòng là một quan sát, ở đây là một bệnh nhân. Các cột khác nhau có thể có kiểu khác nhau: một mã định danh dạng ký tự, tuổi dạng số, một factor cho giới tính. Một khung dữ liệu nhỏ có thể được tạo bằng tay:


``` r
clinic <- data.frame(
  patient_id = c("P01", "P02", "P03", "P04"),
  age        = c(54, 61, 47, 70),
  sex        = c("Female", "Male", "Female", "Male"),
  sbp_mmhg   = c(152, 138, 145, 160)
)
clinic
```

```
#>   patient_id age    sex sbp_mmhg
#> 1        P01  54 Female      152
#> 2        P02  61   Male      138
#> 3        P03  47 Female      145
#> 4        P04  70   Male      160
```

Một **tibble** là phiên bản hiện đại của khung dữ liệu trong tidyverse. Tibble hoạt động giống khung dữ liệu ở gần như mọi khía cạnh, nhưng được in ra hữu ích hơn (hiển thị kiểu của từng cột và chỉ in số dòng, số cột vừa với màn hình) và chặt chẽ hơn trong một số tình huống mà khung dữ liệu âm thầm làm những điều gây bất ngờ. Các hàm nhập dữ liệu của tidyverse trả về tibble; trong cuốn sách này, "khung dữ liệu" được dùng để chỉ cả hai.


``` r
as_tibble(clinic)
```

```
#> # A tibble: 4 × 4
#>   patient_id   age sex    sbp_mmhg
#>   <chr>      <dbl> <chr>     <dbl>
#> 1 P01           54 Female      152
#> 2 P02           61 Male        138
#> 3 P03           47 Female      145
#> 4 P04           70 Male        160
```

Dòng `<chr> <dbl> <chr> <dbl>` bên dưới tên cột cho biết kiểu của từng cột: `chr` là ký tự (character) và `dbl` là số thực (double, numeric).

Một cột đơn lẻ được lấy ra từ khung dữ liệu dưới dạng vectơ bằng dấu đô la `$`, và có thể thêm một cột theo cùng cách:


``` r
clinic$sbp_mmhg
```

```
#> [1] 152 138 145 160
```

``` r
mean(clinic$age)
```

```
#> [1] 58
```

``` r
clinic$high_sbp <- clinic$sbp_mmhg >= 140
clinic
```

```
#>   patient_id age    sex sbp_mmhg high_sbp
#> 1        P01  54 Female      152     TRUE
#> 2        P02  61   Male      138    FALSE
#> 3        P03  47 Female      145     TRUE
#> 4        P04  70   Male      160     TRUE
```

### Nhập tệp CSV bằng `read_csv()`

Dữ liệu lâm sàng thường được gửi đến dưới dạng tệp **CSV** (comma-separated values, giá trị phân cách bằng dấu phẩy): một tệp văn bản thuần trong đó mỗi dòng là một hàng và các giá trị được phân cách bằng dấu phẩy. Tệp CSV có thể được mở bằng bất kỳ phần mềm nào và là định dạng có tính di động cao nhất để chia sẻ dữ liệu. Gói **readr** (thuộc tidyverse) cung cấp hàm `read_csv()`:


``` r
htn <- read_csv("Data/hypertension_phc_raw.csv")
```

Không có gì được in ra ở đây vì thiết lập của cuốn sách này đã tắt báo cáo cột của readr. Trên màn hình của bạn, `read_csv()` sẽ in ra một thông báo như `Rows: 1503 Columns: 36` kèm theo bản tóm tắt các kiểu cột mà nó đã đoán. readr xem xét 1.000 dòng đầu tiên của mỗi cột và chọn kiểu cụ thể nhất phù hợp với tất cả các dòng đó: logic, rồi số, rồi ngày tháng, và quay về kiểu ký tự nếu không có kiểu nào khác phù hợp. Theo mặc định, hàm coi ô trống và văn bản `NA` là giá trị khuyết, và loại bỏ khoảng trắng ở đầu và cuối các giá trị (`trim_ws = TRUE`).

Điều đầu tiên cần lưu ý là tệp thô có **1.503 dòng**, chứ không phải 1.500 bệnh nhân đã được đưa vào nghiên cứu. Đã có điều gì đó không ổn: như từ điển dữ liệu cảnh báo, ba bệnh nhân đã bị nhập hai lần. Chúng ta sẽ loại bỏ các bản ghi trùng lặp này trong Chương 2.

### Nhập tệp Excel bằng `read_excel()`

Nhiều bộ dữ liệu lâm sàng được thu thập hoặc chia sẻ dưới dạng bảng tính Excel. Gói **readxl** [@wickham2023r4ds] đọc các tệp `.xls` và `.xlsx` mà không cần cài đặt Excel. Một bảng tính có thể chứa nhiều trang tính (sheet), vì vậy nên kiểm tra tên các trang tính và chỉ rõ tên trang tính bạn muốn đọc:


``` r
excel_sheets("Data/hypertension_phc_raw.xlsx")
```

```
#> [1] "data"
```

``` r
htn_xl <- read_excel("Data/hypertension_phc_raw.xlsx", sheet = "data")
dim(htn)
```

```
#> [1] 1503   36
```

``` r
dim(htn_xl)
```

```
#> [1] 1503   36
```

``` r
identical(names(htn), names(htn_xl))
```

```
#> [1] TRUE
```

Cả hai tệp đều chứa cùng 1.503 dòng và 36 cột với tên cột giống hệt nhau. Hàm `identical()` chỉ trả về một giá trị `TRUE` duy nhất nếu hai đối số của nó giống hệt nhau, đây là một cách tiện lợi để kiểm tra rằng hai phiên bản của một bộ dữ liệu khớp nhau. Các định dạng khác cũng dễ đọc như vậy: gói **haven** đọc các tệp SPSS (`read_sav()`), Stata (`read_dta()`) và SAS (`read_sas()`), vốn phổ biến trong nghiên cứu lâm sàng.

::: {.callout-tip title="Thực hành tốt"}
Hãy coi tệp dữ liệu thô là tệp chỉ đọc. Không bao giờ sửa nó bằng tay trong Excel để "sửa" một lỗi, vì khi đó việc chỉnh sửa không để lại dấu vết gì. Thay vào đó, hãy thực hiện mọi thay đổi trong script R, để con đường từ dữ liệu thô đến bộ dữ liệu phân tích được ghi lại đầy đủ và có thể được xem xét lại. Nếu dữ liệu được gửi đến dưới dạng bảng tính, các khuyến nghị của @broman2018 (mỗi cột một biến, mỗi ô một giá trị, không dùng màu sắc để mã hóa dữ liệu, ngày tháng và mã thống nhất) giúp việc phân tích dễ dàng hơn nhiều.
:::

## Kiểm tra dữ liệu lần đầu {#sec-inspection}

Trước khi tính bất kỳ thống kê nào, hãy nhìn vào dữ liệu. Vài phút kiểm tra sẽ cho thấy cấu trúc của bộ dữ liệu, các kiểu mà R đã gán và rất thường xuyên là những vấn đề dữ liệu đầu tiên. Các hàm trong mục này tạo thành một quy trình thường quy mà bạn nên chạy trên mọi bộ dữ liệu mới.

### Kích thước và tên biến


``` r
dim(htn)      # số dòng và số cột
```

```
#> [1] 1503   36
```

``` r
nrow(htn)
```

```
#> [1] 1503
```

``` r
ncol(htn)
```

```
#> [1] 36
```

``` r
names(htn)
```

```
#>  [1] "patient_id"              "facility"               
#>  [3] "enroll_date"             "age"                    
#>  [5] "sex"                     "residence"              
#>  [7] "education"               "occupation"             
#>  [9] "marital_status"          "health_insurance"       
#> [11] "height_cm"               "weight_kg"              
#> [13] "bmi"                     "smoking"                
#> [15] "alcohol"                 "physical_activity"      
#> [17] "family_history_htn"      "diabetes"               
#> [19] "sbp_mmhg"                "dbp_mmhg"               
#> [21] "total_chol_mmol_l"       "hdl_mmol_l"             
#> [23] "ldl_mmol_l"              "triglycerides_mmol_l"   
#> [25] "fasting_glucose_mmol_l"  "creatinine_umol_l"      
#> [27] "sodium_mmol_l"           "potassium_mmol_l"       
#> [29] "knowledge_score"         "distance_to_facility_km"
#> [31] "comorbidity_count"       "htn_diagnosed"          
#> [33] "months_since_diagnosis"  "treatment_uptake"       
#> [35] "adherence"               "bp_controlled"
```

`dim()` trả về số dòng và số cột, theo đúng thứ tự đó. `names()` liệt kê 36 tên biến. Các tên này đã theo phong cách snake case nhất quán và có chứa đơn vị khi cần, nhờ đó dễ làm việc.

### In ra và xem các dòng đầu tiên

Gõ tên của một tibble sẽ in ra mười dòng đầu tiên và số cột vừa với màn hình:


``` r
htn
```

```
#> # A tibble: 1,503 × 36
#>    patient_id facility enroll_date   age sex   residence education occupation
#>    <chr>      <chr>    <chr>       <dbl> <chr> <chr>     <chr>     <chr>     
#>  1 PHC-1224   Igoma HC 01/02/2024     74 Fema… Urban     Primary   Trader    
#>  2 PHC-1169   Kisesa … 2024-09-03     56 Fema… Urban     Primary   Professio…
#>  3 PHC-1391   Bugando… 2024-11-26     54 Fema… Urban     None      Farmer    
#>  4 PHC-0142   Ilemela… 2024-10-23     33 Fema… Urban     Primary   Farmer    
#>  5 PHC-0112   Kisesa … 2024-06-03     86 Male  Urban     Primary   Unemployed
#>  6 PHC-0102   Igoma HC 2024-04-22     70 Male  Urban     Primary   Trader    
#>  7 PHC-1019   Nyamaga… 08/08/2024     45 Fema… Urban     None      Unemployed
#>  8 PHC-1431   Bugando… 18/02/2024     59 f     Urban     Primary   Professio…
#>  9 PHC-0119   Bugando… 2024-01-12     46 Male  Urban     Primary   Trader    
#> 10 PHC-0397   Bugando… 2024-10-19     61 Fema… Rural     None      Trader    
#> # ℹ 1,493 more rows
#> # ℹ 28 more variables: marital_status <chr>, health_insurance <chr>,
#> #   height_cm <dbl>, weight_kg <dbl>, bmi <dbl>, smoking <chr>,
#> #   alcohol <chr>, physical_activity <chr>, family_history_htn <chr>,
#> #   diabetes <chr>, sbp_mmhg <dbl>, dbp_mmhg <dbl>, total_chol_mmol_l <dbl>,
#> #   hdl_mmol_l <dbl>, ldl_mmol_l <dbl>, triglycerides_mmol_l <dbl>,
#> #   fasting_glucose_mmol_l <dbl>, creatinine_umol_l <dbl>, …
```

Dòng tiêu đề cho biết tibble có 1.503 dòng và 36 cột. Bên dưới mỗi tên cột là kiểu của cột đó, và phần chân liệt kê các cột không vừa màn hình. `head()` hiển thị một số dòng tùy chọn; để xem một vài cột cụ thể, ta có thể kết hợp nó với `select()`, hàm mà chúng ta sẽ tìm hiểu đầy đủ ở Mục 1.11:


``` r
head(select(htn, patient_id, facility, age, sex, sbp_mmhg, dbp_mmhg), 5)
```

```
#> # A tibble: 5 × 6
#>   patient_id facility      age sex    sbp_mmhg dbp_mmhg
#>   <chr>      <chr>       <dbl> <chr>     <dbl>    <dbl>
#> 1 PHC-1224   Igoma HC       74 Female      140       92
#> 2 PHC-1169   Kisesa HC      56 Female      185       91
#> 3 PHC-1391   Bugando PHC    54 Female      147       85
#> 4 PHC-0142   Ilemela HC     33 Female      124      102
#> 5 PHC-0112   Kisesa HC      86 Male        131       95
```

Trong RStudio, `View(htn)` mở dữ liệu trong một trình xem giống bảng tính, nơi bạn có thể cuộn, sắp xếp và lọc (mà không thay đổi dữ liệu). Nó hữu ích để duyệt dữ liệu nhưng, vì mang tính tương tác, nó không để lại bản ghi nào, vì vậy đừng dựa vào nó cho bất cứ việc gì bạn cần lặp lại.

### Cấu trúc: `glimpse()` và `str()`

`glimpse()` (của dplyr) là cái nhìn tổng quan đơn lẻ giàu thông tin nhất. Nó liệt kê mỗi cột trên một dòng riêng, kèm kiểu và vài giá trị đầu tiên:


``` r
glimpse(htn)
```

```
#> Rows: 1,503
#> Columns: 36
#> $ patient_id              <chr> "PHC-1224", "PHC-1169", "PHC-1391", "PHC-01…
#> $ facility                <chr> "Igoma HC", "Kisesa HC", "Bugando PHC", "Il…
#> $ enroll_date             <chr> "01/02/2024", "2024-09-03", "2024-11-26", "…
#> $ age                     <dbl> 74, 56, 54, 33, 86, 70, 45, 59, 46, 61, 70,…
#> $ sex                     <chr> "Female", "Female", "Female", "Female", "Ma…
#> $ residence               <chr> "Urban", "Urban", "Urban", "Urban", "Urban"…
#> $ education               <chr> "Primary", "Primary", "None", "Primary", "P…
#> $ occupation              <chr> "Trader", "Professional", "Farmer", "Farmer…
#> $ marital_status          <chr> "Married", "Married", "Single", "Single", "…
#> $ health_insurance        <chr> "Yes", "No", "No", "Yes", "0", "No", "No", …
#> $ height_cm               <dbl> 164.6, 160.0, 152.8, 166.2, 182.0, 175.6, 1…
#> $ weight_kg               <dbl> 61.3, 68.3, 49.9, 78.5, 71.6, 97.4, 106.7, …
#> $ bmi                     <dbl> 22.6, 26.7, 21.4, 28.4, 21.6, 31.6, NA, 25.…
#> $ smoking                 <chr> "Former", "Current", "Never", "Never", "For…
#> $ alcohol                 <chr> "None", "Moderate", "Moderate", "None", "He…
#> $ physical_activity       <chr> "Low", "Low", "Moderate", "Low", "High", "M…
#> $ family_history_htn      <chr> "Yes", "1", "1", "1", "0", "No", "No", "No"…
#> $ diabetes                <chr> "No", "No", "No", "No", "0", "No", "0", "No…
#> $ sbp_mmhg                <dbl> 140, 185, 147, 124, 131, 153, 162, 108, 152…
#> $ dbp_mmhg                <dbl> 92, 91, 85, 102, 95, 95, 100, 100, 87, 69, …
#> $ total_chol_mmol_l       <dbl> -99.0, 5.4, 5.4, 5.9, 4.8, 3.6, 5.3, 2.9, 6…
#> $ hdl_mmol_l              <dbl> 1.93, 0.70, 1.67, 0.65, 1.69, 1.20, 1.83, 1…
#> $ ldl_mmol_l              <dbl> 3.5, NA, 2.3, 4.1, 2.4, 1.4, 2.2, NA, 3.4, …
#> $ triglycerides_mmol_l    <dbl> 1.0, 2.1, 2.7, 1.7, 2.0, 1.3, 1.0, 1.5, 2.5…
#> $ fasting_glucose_mmol_l  <dbl> 6.6, 5.5, 6.0, 5.2, 5.1, 5.8, 5.5, 4.1, 6.2…
#> $ creatinine_umol_l       <dbl> 61, 66, 75, 86, 87, 72, 103, 57, 98, 76, 99…
#> $ sodium_mmol_l           <dbl> 134, 134, 139, 140, 142, 138, 141, 141, 140…
#> $ potassium_mmol_l        <dbl> 4.1, 3.6, 4.4, 4.4, 4.2, 4.0, 4.5, 5.0, 4.7…
#> $ knowledge_score         <dbl> 14, 7, 9, 12, NA, 12, 17, 8, 13, NA, 11, 6,…
#> $ distance_to_facility_km <dbl> 2.9, 10.5, 2.4, 2.2, 5.4, 6.7, 0.2, 0.4, 5.…
#> $ comorbidity_count       <dbl> 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0…
#> $ htn_diagnosed           <chr> "1", "Y", "Yes", "Yes", "Yes", "Yes", "Yes"…
#> $ months_since_diagnosis  <dbl> 95, 87, 116, 31, 80, 28, 6, 96, 114, 53, 39…
#> $ treatment_uptake        <chr> "Yes", "No", "N", "Yes", "No", "No", "1", "…
#> $ adherence               <chr> "Poor", NA, NA, "Good", NA, NA, "Good", NA,…
#> $ bp_controlled           <chr> "No", NA, NA, "No", NA, NA, "No", NA, NA, "…
```

Hãy đọc kết quả này thật cẩn thận, từng cột một, với từ điển dữ liệu bên cạnh. Nó kể một câu chuyện:

- `patient_id`, `facility`, `sex`, `residence` và các biến nhân khẩu học khác có kiểu ký tự (`<chr>`), đúng như mong đợi đối với văn bản.
- `enroll_date` có kiểu ký tự, **không phải** ngày tháng. Các giá trị đầu tiên, `"01/02/2024"` và `"2024-09-03"`, dùng các định dạng khác nhau, vì vậy readr không thể nhận ra một định dạng ngày duy nhất và giữ nguyên văn bản.
- Các số đo (`age`, `height_cm`, `weight_kg`, `bmi`, `sbp_mmhg`, các giá trị xét nghiệm) có kiểu số (`<dbl>`), điều này là đúng.
- `total_chol_mmol_l` bắt đầu bằng giá trị `-99.0`. Cholesterol âm là điều không thể: đây là một **mã giá trị khuyết** (một giá trị "canh gác", sentinel) được dùng trong quá trình nhập liệu, mà R đã coi là một con số thật.
- `health_insurance`, `family_history_htn`, `diabetes`, `htn_diagnosed` và `treatment_uptake` đáng lẽ là các biến Yes/No (có/không), nhưng ta thấy các giá trị như `"1"`, `"0"` và `"Y"` lẫn với `"Yes"` và `"No"`. Do sự pha trộn này, chúng được lưu ở kiểu ký tự.
- `adherence` và `bp_controlled` chứa `NA` ở những bệnh nhân không điều trị, vì với họ các biến kết cục này không được xác định.

Hàm `str()` ("structure", cấu trúc) của base R cho thông tin tương tự với cách trình bày hơi khác. Áp dụng cho toàn bộ một tibble thì kết quả rất dài dòng, vì vậy ở đây chúng tôi chỉ trình bày cho vài cột:


``` r
str(select(htn, age, sex, sbp_mmhg, treatment_uptake))
```

```
#> tibble [1,503 × 4] (S3: tbl_df/tbl/data.frame)
#>  $ age             : num [1:1503] 74 56 54 33 86 70 45 59 46 61 ...
#>  $ sex             : chr [1:1503] "Female" "Female" "Female" "Female" ...
#>  $ sbp_mmhg        : num [1:1503] 140 185 147 124 131 153 162 108 152 127 ...
#>  $ treatment_uptake: chr [1:1503] "Yes" "No" "N" "Yes" ...
```

### Tóm tắt các biến số

`summary()` áp dụng cho một vectơ số cho ra bản tóm tắt sáu con số, kèm theo số giá trị khuyết nếu có. Đây là cách nhanh nhất để phát hiện các giá trị không thể có.


``` r
summary(htn$age)
```

```
#>    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
#>     0.0    43.0    52.0    52.3    62.0   200.0
```

Tuổi trung vị là 52 tuổi và một nửa số bệnh nhân ở giữa có tuổi từ 43 đến 62, điều này hợp lý đối với người trưởng thành đến khám ở tuyến ban đầu. Nhưng giá trị nhỏ nhất là 0 và giá trị lớn nhất là 200. Không giá trị nào có thể có ở một người tham gia trưởng thành: đây là lỗi nhập liệu. Áp dụng `summary()` cho nhiều cột cùng lúc cho thấy thêm nhiều vấn đề:


``` r
summary(select(htn, sbp_mmhg, dbp_mmhg, weight_kg, height_cm))
```

```
#>     sbp_mmhg      dbp_mmhg       weight_kg       height_cm  
#>  Min.   :  0   Min.   :  5.0   Min.   :  7.0   Min.   : 17  
#>  1st Qu.:126   1st Qu.: 79.0   1st Qu.: 60.9   1st Qu.:158  
#>  Median :139   Median : 86.0   Median : 70.1   Median :164  
#>  Mean   :140   Mean   : 85.9   Mean   : 70.9   Mean   :164  
#>  3rd Qu.:153   3rd Qu.: 93.0   3rd Qu.: 80.3   3rd Qu.:169  
#>  Max.   :700   Max.   :121.0   Max.   :132.8   Max.   :193  
#>                                NAs    :45
```

Huyết áp tâm thu dao động từ 0 đến 700 mmHg, huyết áp tâm trương xuống tới 5 mmHg, cân nặng thấp nhất là 7 kg và chiều cao thấp nhất là 17 cm (có lẽ là 170 cm bị đặt sai dấu thập phân). `weight_kg` còn có 45 giá trị khuyết (`NA's`). Không giá trị nào trong số này qua được ánh mắt của một bác sĩ lâm sàng khi xem phiếu thu thập thông tin ca bệnh, thế nhưng chúng sẽ âm thầm làm sai lệch giá trị trung bình, độ lệch chuẩn và hệ số hồi quy nếu được phân tích nguyên trạng. Các mã "canh gác" cũng hiện rõ trong các biến xét nghiệm:


``` r
summary(htn$total_chol_mmol_l)
```

```
#>    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.     NAs 
#>  -99.00    4.30    5.10    2.59    5.80    8.30      55
```

``` r
summary(htn$fasting_glucose_mmol_l)
```

```
#>    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.     NAs 
#>     3.0     4.8     5.4    32.5     6.1   999.0      35
```

Cholesterol toàn phần có giá trị nhỏ nhất là -99 và glucose lúc đói có giá trị lớn nhất là 999 mmol/L: đây là các mã cho "khuyết", không phải số đo.

### Bảng tần số của các biến phân loại

Với các biến ký tự và factor, `table()` đếm từng giá trị khác nhau.


``` r
table(htn$sex)
```

```
#> 
#>      f      F female Female      m      M   male   Male 
#>     74     73     68    672     40     39     42    495
```

Đáng lẽ phải có hai nhóm; thực tế có tám. Cùng hai giới tính đã được gõ thành `Female`, `female`, `F` và `f` (nữ), và `Male`, `male`, `M` và `m` (nam). Vì R phân biệt chữ hoa, chữ thường và so sánh văn bản một cách chính xác, nó coi mỗi cách viết là một nhóm riêng biệt. Một bảng giới tính theo việc sử dụng điều trị, hay một mô hình hồi quy hiệu chỉnh theo giới tính, sẽ vô nghĩa cho đến khi các cách viết này được chuẩn hóa.


``` r
table(htn$treatment_uptake, useNA = "ifany")
```

```
#> 
#>   0   1   N  No   Y Yes 
#> 134  79  95 766  52 377
```

Biến kết cục chính được mã hóa theo sáu cách khác nhau: `Yes`, `Y` và `1` cho nhóm được điều trị, và `No`, `N` và `0` cho nhóm không được điều trị. Đối số `useNA = "ifany"` yêu cầu `table()` hiển thị số giá trị khuyết nếu có; theo mặc định `table()` lặng lẽ bỏ qua chúng, một cái bẫy mà chúng ta sẽ quay lại trong Chương 3. Ở đây không có giá trị khuyết nào, nên không có cột `NA` nào xuất hiện.


``` r
table(htn$facility)
```

```
#> 
#>   Bugando PHC  Buzuruga PHC      Igoma HC    Ilemela HC     Kisesa HC 
#>           337           175           175           283           228 
#> Nyamagana PHC 
#>           305
```

Sáu cơ sở y tế hiện ra gọn gàng, và Bugando PHC đóng góp nhiều bệnh nhân nhất. Tuy nhiên, từ điển dữ liệu cảnh báo rằng một số tên cơ sở có chứa khoảng trắng thừa ở đầu hoặc cuối. Chúng ta không thấy chúng vì `read_csv()` mặc định cắt bỏ khoảng trắng. Đọc lại tệp với `trim_ws = FALSE` sẽ làm lộ ra vấn đề:


``` r
htn_untrimmed <- read_csv("Data/hypertension_phc_raw.csv", trim_ws = FALSE)
table(htn_untrimmed$facility)
```

```
#> 
#>    Bugando PHC    Buzuruga PHC        Igoma HC      Ilemela HC  
#>              25              16              11              16 
#>      Kisesa HC   Nyamagana PHC      Bugando PHC    Buzuruga PHC 
#>              16              24             312             159 
#>        Igoma HC      Ilemela HC       Kisesa HC   Nyamagana PHC 
#>             164             267             212             281
```

``` r
# có bao nhiêu giá trị khác với phiên bản đã cắt khoảng trắng của chúng?
sum(htn_untrimmed$facility != str_trim(htn_untrimmed$facility))
```

```
#> [1] 108
```

Giờ đây mỗi cơ sở xuất hiện hai lần. Sáu số đếm đầu tiên thuộc về các phiên bản tên có khoảng trắng ở đầu và cuối (như `" Igoma HC "`), mà R xếp trước các chữ cái; sáu số đếm cuối là các phiên bản sạch. Tổng cộng có 108 giá trị mang khoảng trắng vô hình. Nếu không cắt khoảng trắng, mọi bảng theo cơ sở y tế sẽ hiện mười hai cơ sở thay vì sáu. Các phần mềm khác, và một số hàm nhập dữ liệu của R, không tự động cắt khoảng trắng, vì vậy thật yên tâm khi biết readr đang làm gì thay cho bạn, và điều quan trọng là phải kiểm tra thay vì giả định.

### Hình đầu tiên

Các con số trong một bản tóm tắt dễ nắm bắt hơn khi được vẽ thành đồ thị. Biểu đồ tần suất (histogram) của tuổi cho thấy toàn bộ phân phối cùng một lúc. Chúng ta dùng **ggplot2**, gói sẽ được giới thiệu đầy đủ trong Chương 3; tạm thời, hãy đọc đoạn mã như sau: "lấy dữ liệu `htn`, đặt `age` lên trục x, và vẽ một biểu đồ tần suất".


``` r
ggplot(htn, aes(x = age)) +
  geom_histogram(binwidth = 5, fill = "#1F6F8B", colour = "white") +
  labs(title = "Tuổi của người tham gia, dữ liệu thô",
       x = "Tuổi (năm)", y = "Số bệnh nhân")
```

![Biểu đồ tần suất của tuổi được ghi nhận trong dữ liệu thô của nghiên cứu tình huống (n = 1.503). Hầu hết bệnh nhân có tuổi từ 18 đến 95, nhưng hai giá trị không thể có, ở mức 0 và 200 tuổi, nổi bật tách riêng.](figures/01-r-basics-c1-hist-age-1.png)

Phần lớn phân phối là một "bướu" duy nhất nằm giữa 18 và 95 tuổi, có tâm ở khoảng đầu tuổi năm mươi và tương đối đối xứng. Những cột nhỏ xíu tách biệt ở mức 0 và 200 là các giá trị không thể có đã được `summary()` phát hiện; mỗi cột chỉ là một bệnh nhân, vì vậy chúng hầu như không nhô lên khỏi trục. Biểu đồ tần suất khiến những giá trị ngoại lai như vậy không thể bị bỏ sót, và đó là lý do vẽ đồ thị dữ liệu là một bước thiết yếu của mọi lần kiểm tra chất lượng dữ liệu.

Biểu đồ cột làm cùng nhiệm vụ đó cho một biến phân loại. Ở đây chúng ta hiển thị số bệnh nhân được tuyển chọn tại mỗi cơ sở y tế, sắp xếp từ lớn nhất đến nhỏ nhất:


``` r
htn |>
  count(facility) |>
  ggplot(aes(x = n, y = fct_reorder(facility, n))) +
  geom_col(fill = "#1F6F8B") +
  geom_text(aes(label = n), hjust = -0.2, size = 3.5) +
  labs(title = "Số bản ghi theo cơ sở y tế",
       x = "Số bản ghi", y = NULL) +
  expand_limits(x = 380)
```

![Số bản ghi theo từng cơ sở chăm sóc sức khỏe ban đầu trong dữ liệu thô của nghiên cứu tình huống. Bugando PHC và Nyamagana PHC đóng góp nhiều người tham gia nhất; Buzuruga PHC và Igoma HC ít nhất.](figures/01-r-basics-c1-bar-facility-1.png)

Quy mô các cơ sở chênh lệch nhau gần gấp đôi, từ 175 bản ghi tại Buzuruga PHC và Igoma HC đến 337 bản ghi tại Bugando PHC. Trong một nghiên cứu đa trung tâm, điều này đáng được lưu ý: các cơ sở lớn hơn sẽ chi phối các ước lượng gộp, và bệnh nhân đến khám tại cùng một cơ sở có thể giống nhau hơn so với bệnh nhân từ các cơ sở khác nhau.

### Tổng kết: những vấn đề đã lộ rõ

Không cần tính một thống kê nào, lần kiểm tra đầu tiên đã phát hiện phần lớn các vấn đề chất lượng dữ liệu được ghi trong từ điển dữ liệu. Bảng dưới đây tập hợp chúng lại. Quyết định cách xử lý từng vấn đề là chủ đề của Chương 2.


``` r
problems <- tibble(
  Problem = c("Bản ghi trùng lặp", "Giá trị không hợp lý",
              "Mã giá trị khuyết", "Cách viết không nhất quán",
              "Mã nhị phân pha trộn", "Định dạng ngày pha trộn",
              "Khoảng trắng thừa"),
  Evidence = c("1.503 dòng cho 1.500 bệnh nhân",
               "tuổi 0 và 200; SBP 0 và 700; cân nặng 7 kg",
               "cholesterol -99; glucose 999",
               "sex: Female/female/F/f, Male/male/M/m",
               "treatment_uptake: Yes/Y/1, No/N/0",
               "enroll_date: 01/02/2024 và 2024-09-03",
               "tên cơ sở có khoảng trắng ở đầu/cuối")
)
knitr::kable(problems, col.names = c("Vấn đề", "Bằng chứng"),
             caption = "Các vấn đề dữ liệu phát hiện qua lần kiểm tra đầu tiên.")
```



Table: Các vấn đề dữ liệu phát hiện qua lần kiểm tra đầu tiên.

|Vấn đề                    |Bằng chứng                                 |
|:-------------------------|:------------------------------------------|
|Bản ghi trùng lặp         |1.503 dòng cho 1.500 bệnh nhân             |
|Giá trị không hợp lý      |tuổi 0 và 200; SBP 0 và 700; cân nặng 7 kg |
|Mã giá trị khuyết         |cholesterol -99; glucose 999               |
|Cách viết không nhất quán |sex: Female/female/F/f, Male/male/M/m      |
|Mã nhị phân pha trộn      |treatment_uptake: Yes/Y/1, No/N/0          |
|Định dạng ngày pha trộn   |enroll_date: 01/02/2024 và 2024-09-03      |
|Khoảng trắng thừa         |tên cơ sở có khoảng trắng ở đầu/cuối       |

::: {.callout-note title="Diễn giải lâm sàng"}
Mỗi vấn đề trong số này đều sẽ làm thay đổi một kết luận lâm sàng nếu bị bỏ mặc. Một SBP 700 mmHg làm tăng giả tạo huyết áp trung bình; một giá trị cholesterol -99 mmol/L kéo trung bình cholesterol xuống; ba bệnh nhân bị trùng lặp được đếm hai lần; và tám cách viết giới tính khiến "tỷ lệ phụ nữ đang điều trị" thậm chí không thể tính được. Vì vậy, lần kiểm tra đầu tiên không phải là việc dọn dẹp tùy chọn: nó là một phần của phương pháp khoa học, và những phát hiện của nó cần được ghi lại trong script phân tích.
:::

## Toán tử pipe và làm quen với dplyr {#sec-pipe}

### Toán tử pipe `|>`

Phân tích dữ liệu là một chuỗi các bước: lấy dữ liệu, giữ lại một số dòng, giữ lại một số cột, tính toán điều gì đó, sắp xếp kết quả. Khi được viết dưới dạng các lời gọi hàm lồng nhau, các bước phải được đọc từ trong ra ngoài, ngược với thứ tự chúng diễn ra:


``` r
head(arrange(select(htn, patient_id, age), desc(age)), 3)
```

```
#> # A tibble: 3 × 2
#>   patient_id   age
#>   <chr>      <dbl>
#> 1 PHC-0174     200
#> 2 PHC-0144      95
#> 3 PHC-1062      92
```

Toán tử **pipe** `|>` (có sẵn trong R từ phiên bản 4.1) chuyển kết quả ở bên trái nó thành đối số thứ nhất của hàm ở bên phải. Cùng phép tính đó trở thành một "công thức nấu ăn" dễ đọc, đọc từ trên xuống dưới, với `|>` được hiểu là "rồi thì":


``` r
htn |>
  select(patient_id, age) |>
  arrange(desc(age)) |>
  head(3)
```

```
#> # A tibble: 3 × 2
#>   patient_id   age
#>   <chr>      <dbl>
#> 1 PHC-0174     200
#> 2 PHC-0144      95
#> 3 PHC-1062      92
```

"Lấy `htn`, rồi chọn mã bệnh nhân và tuổi, rồi sắp xếp theo tuổi giảm dần, rồi hiển thị ba dòng đầu tiên." Kết quả xác định được bệnh nhân duy nhất được ghi nhận 200 tuổi (PHC-0174), tiếp theo là hai bệnh nhân thực sự cao tuổi nhưng hợp lý, 95 và 92 tuổi: đây là cách bạn tìm ra chính xác những bản ghi nào cần được gửi thắc mắc về điểm nghiên cứu. Trong RStudio, phím tắt `Ctrl+Shift+M` (`Cmd+Shift+M` trên macOS) sẽ gõ toán tử pipe. Bạn cũng sẽ thấy toán tử pipe cũ hơn `%>%` của gói **magrittr** trong nhiều sách và câu trả lời trực tuyến; trong sử dụng hằng ngày, hai toán tử này có thể thay thế cho nhau.

### Năm "động từ" thiết yếu của dplyr

Gói **dplyr** cung cấp một nhóm nhỏ các hàm, thường được gọi là *động từ* (verbs), mỗi hàm làm một việc với một khung dữ liệu. Mọi động từ đều nhận một khung dữ liệu làm đối số thứ nhất và trả về một khung dữ liệu mới, điều này giúp chúng dễ dàng được nối với nhau bằng pipe [@wickham2023r4ds]. Tên cột được viết không có dấu nháy.

Table: Năm động từ của dplyr được giới thiệu trong chương này.

| Động từ | Công dụng | Ví dụ |
|------|--------------|---------|
| `select()` | Giữ lại (hoặc bỏ đi) các cột | `select(htn, age, sex)` |
| `filter()` | Giữ lại các dòng thỏa mãn một điều kiện | `filter(htn, age >= 60)` |
| `arrange()` | Sắp xếp các dòng | `arrange(htn, desc(sbp_mmhg))` |
| `mutate()` | Tạo mới hoặc sửa đổi cột | `mutate(htn, pp = sbp_mmhg - dbp_mmhg)` |
| `count()` | Đếm số dòng theo từng nhóm | `count(htn, facility)` |

**`select()`** giữ lại các cột được nêu tên. Một dấu trừ sẽ bỏ một cột, và các hàm hỗ trợ chọn cột theo mẫu tên:


``` r
htn |>
  select(patient_id, ends_with("_mmhg")) |>
  head(3)
```

```
#> # A tibble: 3 × 3
#>   patient_id sbp_mmhg dbp_mmhg
#>   <chr>         <dbl>    <dbl>
#> 1 PHC-1224        140       92
#> 2 PHC-1169        185       91
#> 3 PHC-1391        147       85
```

**`filter()`** giữ lại các dòng mà điều kiện là `TRUE`. Điều kiện dùng các toán tử so sánh và toán tử logic ở Mục 1.5; nhiều điều kiện phân cách bằng dấu phẩy thì tất cả đều phải đúng.


``` r
htn |>
  filter(facility == "Kisesa HC", age >= 70) |>
  select(patient_id, facility, age, sbp_mmhg) |>
  head(4)
```

```
#> # A tibble: 4 × 4
#>   patient_id facility    age sbp_mmhg
#>   <chr>      <chr>     <dbl>    <dbl>
#> 1 PHC-0112   Kisesa HC    86      131
#> 2 PHC-0035   Kisesa HC    81      174
#> 3 PHC-0379   Kisesa HC    72      135
#> 4 PHC-0737   Kisesa HC    80      154
```

Cùng ý tưởng đó giúp tìm ra các giá trị huyết áp không hợp lý mà ta đã thấy trong bản tóm tắt:


``` r
htn |>
  filter(sbp_mmhg < 60 | sbp_mmhg > 260) |>
  select(patient_id, facility, sbp_mmhg, dbp_mmhg)
```

```
#> # A tibble: 2 × 4
#>   patient_id facility    sbp_mmhg dbp_mmhg
#>   <chr>      <chr>          <dbl>    <dbl>
#> 1 PHC-0768   Bugando PHC        0       73
#> 2 PHC-0360   Bugando PHC      700       81
```

Hai bản ghi, đều từ Bugando PHC, có huyết áp tâm thu là 0 và 700 mmHg, những giá trị không tương thích với sự sống; huyết áp tâm trương của họ (73 và 81 mmHg) trông bình thường, gợi ý rằng lỗi gõ phím chỉ xảy ra ở trường huyết áp tâm thu. Lưu ý rằng `filter()` loại bỏ cả những dòng có điều kiện là `NA` lẫn những dòng có điều kiện là `FALSE`.

**`arrange()`** sắp xếp các dòng, theo thứ tự tăng dần theo mặc định hoặc giảm dần với `desc()`. Chúng ta đã dùng nó ở trên để tìm những tuổi cao nhất được ghi nhận.

**`mutate()`** thêm các cột mới được tính từ các cột hiện có. Ở đây chúng ta tính huyết áp động mạch trung bình cho mọi bệnh nhân cùng một lúc, dùng cùng công thức như ở Mục 1.2:


``` r
htn |>
  mutate(map_mmhg = dbp_mmhg + (sbp_mmhg - dbp_mmhg) / 3,
         map_mmhg = round(map_mmhg, 1)) |>
  select(patient_id, sbp_mmhg, dbp_mmhg, map_mmhg) |>
  head(5)
```

```
#> # A tibble: 5 × 4
#>   patient_id sbp_mmhg dbp_mmhg map_mmhg
#>   <chr>         <dbl>    <dbl>    <dbl>
#> 1 PHC-1224        140       92    108  
#> 2 PHC-1169        185       91    122.3
#> 3 PHC-1391        147       85    105.7
#> 4 PHC-0142        124      102    109.3
#> 5 PHC-0112        131       95    107
```

Công thức từng được viết cho một bệnh nhân giờ chạy trên cả 1.503 dòng. Lưu ý rằng `mutate()` không thay đổi chính `htn`: cột mới chỉ tồn tại trong kết quả được in ra. Để giữ nó, hãy gán kết quả cho một đối tượng (ví dụ, `htn <- htn |> mutate(...)`). Đây là một nguyên tắc chung: các động từ của dplyr không bao giờ sửa đổi trực tiếp đầu vào của chúng.

**`count()`** lập bảng các giá trị của một hoặc nhiều biến và trả về một tibble, khác với kết quả của `table()`, có thể tiếp tục được chuyển qua pipe:


``` r
htn |>
  count(residence, sort = TRUE)
```

```
#> # A tibble: 2 × 2
#>   residence     n
#>   <chr>     <int>
#> 1 Urban       799
#> 2 Rural       704
```

Số bệnh nhân sống ở thành thị (799) nhỉnh hơn một chút so với nông thôn (704) (các giá trị `"Urban"` và `"Rural"`); `sort = TRUE` liệt kê nhóm có tần số cao nhất trước. Đếm theo hai biến cho ra một bảng chéo ở dạng dài:


``` r
htn |>
  count(facility, residence) |>
  head(6)
```

```
#> # A tibble: 6 × 3
#>   facility     residence     n
#>   <chr>        <chr>     <int>
#> 1 Bugando PHC  Rural       147
#> 2 Bugando PHC  Urban       190
#> 3 Buzuruga PHC Rural        75
#> 4 Buzuruga PHC Urban       100
#> 5 Igoma HC     Rural        92
#> 6 Igoma HC     Urban        83
```

Chúng ta sẽ dùng các động từ này, cùng với `summarise()` và `group_by()`, xuyên suốt phần còn lại của cuốn sách.

::: {.callout-tip title="Mẹo"}
Hãy xây dựng một chuỗi pipe từng bước một. Chạy dòng đầu tiên, kiểm tra kết quả, thêm động từ tiếp theo, chạy lại. Khi một chuỗi pipe dài cho ra câu trả lời bất ngờ, hãy xóa dần các bước từ cuối lên cho đến khi kết quả trở lại hợp lý; vấn đề nằm ở bước bạn vừa xóa.
:::

## Viết một script có thể tái lập {#sec-script}

### Lưu và tổ chức script

Lưu script bằng *File > Save* (`Ctrl+S` hoặc `Cmd+S`) vào thư mục `Scripts/` của dự án, với một cái tên cho biết script làm gì, như `01_import_and_inspect.R`. Đánh số các script theo thứ tự cần chạy giúp một phân tích nhiều bước dễ theo dõi. Hãy lưu thường xuyên; RStudio hiển thị tên tệp màu đỏ kèm dấu hoa thị khi còn những thay đổi chưa được lưu.

### Chú thích

Chú thích giải thích *tại sao* mã làm điều nó làm; bản thân mã cho thấy nó làm *gì*. Chú thích tốt ghi lại các quyết định ("loại SBP > 260 mmHg vì không hợp lý về sinh lý, theo mục 8.2 của đề cương"), nguồn gốc của một công thức, và bất cứ điều gì mà người đọc nếu không có chú thích sẽ phải đoán. Các tiêu đề mục được tạo từ các dòng chú thích, như `# 2. Import data ----`, được RStudio nhận diện và xuất hiện trong mục lục tài liệu (nút ở góc trên bên phải của trình soạn thảo script), giúp dễ dàng di chuyển trong những script dài.

### Mẫu cho một script phân tích

Mọi script phân tích trong cuốn sách này đều theo cùng một bộ khung: phần đầu cho biết script dùng để làm gì, ai viết và viết khi nào; các gói; dữ liệu; phân tích; và, khi cần, lưu kết quả đầu ra. Dưới đây là một script hoàn chỉnh cho công việc của chương này. Vì script không ghi gì ra ổ đĩa, bạn có thể chạy nó bao nhiêu lần tùy thích một cách an toàn.


``` r
# ==============================================================
# Dự án:    Các yếu tố quyết định việc sử dụng điều trị tăng huyết áp
# Script:   01_import_and_inspect.R
# Mục đích: Nhập dữ liệu thô và kiểm tra dữ liệu lần đầu
# Tác giả:  <tên của bạn>            Ngày: <ngày>
# Đầu vào:  Data/hypertension_phc_raw.csv
# Đầu ra:   không có (chỉ kiểm tra)
# ==============================================================

# 1. Các gói ----
library(tidyverse)

# 2. Nhập dữ liệu ----
htn <- read_csv("Data/hypertension_phc_raw.csv")

# 3. Kiểm tra ----
dim(htn)                                  # kỳ vọng 1.500 bệnh nhân
```

```
#> [1] 1503   36
```

``` r
n_distinct(htn$patient_id)                # số bệnh nhân duy nhất
```

```
#> [1] 1500
```

``` r
summary(htn$age)                          # kiểm tra khoảng giá trị
```

```
#>    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
#>     0.0    43.0    52.0    52.3    62.0   200.0
```

``` r
sum(htn$sbp_mmhg > 260 | htn$sbp_mmhg < 60, na.rm = TRUE)  # SBP không hợp lý
```

```
#> [1] 2
```

``` r
# 4. Ghi chú cho bước làm sạch (Chương 2) ----
# - 1.503 dòng nhưng 1.500 mã duy nhất: loại bỏ 3 bản ghi trùng lặp
# - tuổi 0 và 200; SBP 0 và 700: đặt thành giá trị khuyết
```

Kết quả xác nhận các phát hiện của chương này chỉ trong bốn dòng: 1.503 dòng nhưng chỉ có 1.500 mã bệnh nhân khác nhau (hàm `n_distinct()` đếm số giá trị duy nhất), tuổi trải từ 0 đến 200, và hai giá trị huyết áp tâm thu nằm ngoài khoảng hợp lý.

Khi một phân tích có ghi tệp, chẳng hạn một bộ dữ liệu đã làm sạch hoặc một hình, đoạn mã lưu chúng nên đặt ở cuối script. Ví dụ (được trình bày nhưng không chạy ở đây, để không có gì bị ghi vào dự án):


``` r
write_csv(htn, "Outputs/htn_inspected.csv")  # lưu một khung dữ liệu thành CSV
ggsave("Outputs/age_histogram.png", width = 7, height = 4.3)  # lưu hình vừa vẽ
```

::: {.callout-tip title="Thực hành tốt"}
Một phép thử nhanh về khả năng tái lập: khởi động lại R (`Ctrl+Shift+F10`), rồi chạy toàn bộ script từ đầu (`Ctrl+Shift+Enter`). Nếu script chạy không lỗi và cho cùng kết quả, nó là một script độc lập, tự đủ. Nếu thất bại, nó đã phụ thuộc vào điều gì đó bạn làm bằng tay hoặc vào một đối tượng còn sót lại trong bộ nhớ. Hãy biến phép thử này thành thói quen trước khi chia sẻ bất kỳ kết quả nào. Với các báo cáo kết hợp văn bản, mã và kết quả trong một tài liệu, R Markdown và phiên bản kế nhiệm của nó là Quarto đưa khả năng tái lập tiến thêm một bước [@xie2015].
:::

## Tóm tắt {#sec-ch1-summary}

Chương này đã giới thiệu các công cụ và thói quen mà phần còn lại của cuốn sách dựa vào. R là một ngôn ngữ miễn phí dành cho tính toán thống kê, và RStudio là môi trường mà chúng ta dùng để làm việc với nó. Viết phân tích dưới dạng script, thay vì gõ trong console hay nhấp chuột vào menu, giúp mọi kết quả đều có thể truy ngược về dữ liệu và mã lệnh đã tạo ra nó, và đó là cốt lõi của nghiên cứu có thể tái lập.

Đầu tiên chúng ta dùng R như một máy tính, chú ý đến thứ tự ưu tiên của toán tử, và tính BMI cùng huyết áp động mạch trung bình. Chúng ta lưu giá trị vào đối tượng bằng `<-`, làm quen với các kiểu dữ liệu chính và thấy rằng lỗi về kiểu, đặc biệt là số được lưu dưới dạng văn bản và việc âm thầm ép kiểu thành `NA`, là nguồn gốc phổ biến của những sai sót ẩn. Vectơ chứa nhiều giá trị cùng một kiểu; có thể truy xuất phần tử của chúng theo vị trí hoặc theo điều kiện logic, và phép tính số học trên vectơ được vectơ hóa. Giá trị khuyết (`NA`) lan truyền qua các phép tính trừ khi được loại bỏ có chủ ý bằng `na.rm = TRUE`. Hàm nhận đối số theo vị trí hoặc theo tên, và các trang trợ giúp cùng thông báo lỗi của chúng tồn tại để được đọc. Gói mở rộng khả năng của R; chúng được cài đặt một lần và nạp trong mỗi phiên làm việc, và tidyverse cung cấp một bộ công cụ nhất quán cho phần lớn công việc của chúng ta. RStudio Project và đường dẫn tương đối giúp bản phân tích có tính di động.

Cuối cùng, chúng ta đã nhập dữ liệu thô của nghiên cứu tình huống từ cả tệp CSV lẫn tệp Excel và kiểm tra nó bằng `dim()`, `glimpse()`, `summary()`, `table()` và hai hình nhanh. Ngay cả cái nhìn đầu tiên này cũng đã phát hiện các bản ghi trùng lặp, giá trị không thể có, mã giá trị khuyết, cách viết không nhất quán, mã hóa pha trộn, định dạng ngày pha trộn và khoảng trắng thừa. Chương 2 sẽ hướng dẫn cách khắc phục tất cả những vấn đề này theo cách được ghi chép đầy đủ và có thể tái lập.

::: {.callout-important title="Điểm chính"}
- Viết mã phân tích trong một script đã lưu, có chú thích, nằm trong một RStudio Project; chỉ dùng console để khám phá.
- Dùng `<-` để gán và `==` để so sánh; nhớ rằng R phân biệt chữ hoa với chữ thường và văn bản cần có dấu nháy.
- Mọi giá trị đều có một kiểu. Kiểm tra kiểu bằng `class()` hoặc `glimpse()`; số được lưu dưới dạng văn bản và việc âm thầm ép kiểu thành `NA` là những lỗi ẩn thường gặp.
- Vectơ chứa các giá trị cùng một kiểu; phép toán trên vectơ được vectơ hóa; `sum()` và `mean()` của một vectơ logic cho ra số đếm và tỷ lệ.
- `NA` đánh dấu một giá trị khuyết và lan truyền qua các phép tính; hãy dùng `na.rm = TRUE` một cách có chủ ý và luôn báo cáo số giá trị bị khuyết.
- Cài đặt gói một lần bằng `install.packages()`; nạp gói bằng `library()` ở đầu mỗi script.
- Dùng đường dẫn tương đối trong một Project; không bao giờ dùng `setwd()` với một đường dẫn tuyệt đối.
- Nhập dữ liệu bằng `read_csv()` hoặc `read_excel()`, sau đó luôn kiểm tra bằng `dim()`, `glimpse()`, `summary()` và `table()` trước khi phân tích.
- Toán tử pipe `|>` nối các bước thành một công thức dễ đọc; `select()`, `filter()`, `arrange()`, `mutate()` và `count()` đáp ứng phần lớn công việc xử lý dữ liệu hằng ngày.
:::

## Đọc thêm {#sec-ch1-reading}

- @wickham2023r4ds, *R for Data Science* (ấn bản thứ 2, miễn phí trực tuyến): tài liệu nhập môn tiêu chuẩn về tidyverse; các chương về quy trình làm việc, nhập dữ liệu và biến đổi dữ liệu mở rộng mọi nội dung trong chương này.
- @wilson2017, "Good enough practices in scientific computing": những lời khuyên ngắn gọn, thiết thực về cách tổ chức dự án, dữ liệu và mã lệnh mà mọi nhà nghiên cứu có thể áp dụng ngay.
- @broman2018, "Data organization in spreadsheets": cách thiết lập bảng tính thu thập dữ liệu để có thể nhập và phân tích mà không gặp những vấn đề đã thấy trong chương này.
- @peng2011, "Reproducible research in computational science": một lập luận dài hai trang về lý do mã lệnh và dữ liệu cần đi kèm các kết quả được công bố.
- @wickham2019tidyverse, "Welcome to the tidyverse": tổng quan ngắn gọn về thiết kế và các thành phần của tidyverse.

## Bài tập {#sec-ch1-exercises}

::: {.exercise title="Bài tập 1.1"}
**R như một máy tính.** Một bệnh nhân nặng 82 kg, cao 168 cm và có huyết áp 148/96 mmHg.

1. Lưu bốn số đo này vào các đối tượng có tên hợp lý.
2. Dùng chúng để tính BMI và huyết áp động mạch trung bình của bệnh nhân, mỗi giá trị làm tròn đến một chữ số thập phân.
3. Điều gì xảy ra nếu bạn quên dấu ngoặc khi đổi chiều cao sang mét? Giải thích kết quả dựa trên thứ tự ưu tiên của toán tử.
:::

::: {.exercise title="Bài tập 1.2"}
**Vectơ và phép so sánh logic.** Huyết áp tâm trương của tám bệnh nhân khám trong một buổi sáng tại phòng khám là 88, 92, 79, 101, 95, NA, 84 và 90 mmHg.

1. Lưu chúng vào một vectơ `dbp` và tìm độ dài của vectơ.
2. Tính trung bình khi có và không có `na.rm = TRUE`, và giải thích sự khác biệt.
3. Có bao nhiêu lần đo đạt ít nhất 90 mmHg, và con số đó chiếm tỷ lệ bao nhiêu trong số các lần đo *quan sát được*?
4. Lấy ra các lần đo từ thứ ba đến thứ năm, sau đó lấy tất cả các lần đo trừ giá trị bị khuyết.
:::

::: {.exercise title="Bài tập 1.3"}
**Kiểu dữ liệu và ép kiểu.** Xét vectơ `glucose <- c("5.4", "6.1", "<2.0", "7.3", "999", "4.8")`, giống như khi nó được xuất ra từ một hệ thống phòng xét nghiệm.

1. Class của nó là gì, và tại sao?
2. Chuyển nó sang kiểu số bằng `as.numeric()`. Những giá trị nào trở thành `NA`, và tại sao?
3. Giá trị nào còn lại gần như chắc chắn không phải là một số đo thật? Điều gì sẽ xảy ra với giá trị trung bình nếu để nguyên giá trị đó?
:::

::: {.exercise title="Bài tập 1.4"}
**Nhập dữ liệu.** Nạp tidyverse và readxl. Nhập `Data/hypertension_phc_raw.csv` vào một đối tượng `htn` và trang tính `data` của `Data/hypertension_phc_raw.xlsx` vào `htn_xl`.

1. Mỗi đối tượng có bao nhiêu dòng và cột? Bạn kỳ vọng có bao nhiêu dòng, và vì sao chúng khác nhau?
2. Xác nhận rằng hai đối tượng có cùng tên cột.
3. Dùng `n_distinct()` để đếm số giá trị duy nhất của `patient_id`.
:::

::: {.exercise title="Bài tập 1.5"}
**Kiểm tra cấu trúc.** Dùng `glimpse(htn)` để trả lời các câu hỏi sau.

1. Liệt kê ba biến được lưu ở kiểu số và ba biến được lưu ở kiểu ký tự.
2. Kể tên hai biến được lưu ở kiểu ký tự nhưng sau khi làm sạch nên là factor Yes/No. Những giá trị nào trong đó khiến R không thể xử lý chúng đơn giản hơn?
3. Tại sao `enroll_date` không được lưu ở kiểu ngày tháng?
:::

::: {.exercise title="Bài tập 1.6"}
**Phát hiện vấn đề dữ liệu.** Dùng `summary()` và `table()` trên dữ liệu thô.

1. Báo cáo giá trị nhỏ nhất và lớn nhất của `sbp_mmhg`, `dbp_mmhg` và `height_cm`. Những giá trị nào không hợp lý?
2. Lập bảng tần số của `diabetes` và của `htn_diagnosed`. Mỗi biến dùng bao nhiêu mã khác nhau?
3. Có bao nhiêu giá trị của `weight_kg` bị khuyết?
:::

::: {.exercise title="Bài tập 1.7"}
**Sử dụng pipe và dplyr.** Bắt đầu từ `htn`, hãy viết một chuỗi pipe giữ lại các bệnh nhân ở Nyamagana PHC, tạo một cột `map_mmhg` chứa huyết áp động mạch trung bình làm tròn đến một chữ số thập phân, giữ lại `patient_id`, `age`, `sbp_mmhg`, `dbp_mmhg` và `map_mmhg`, và sắp xếp kết quả từ MAP cao nhất đến thấp nhất. Hiển thị năm dòng đầu tiên. Các giá trị cao nhất có hợp lý không? Sau đó dùng `count()` để cho biết tại mỗi cơ sở có bao nhiêu bệnh nhân được ghi nhận mắc đái tháo đường với mã chính xác là `"Yes"`.
:::

::: {.exercise title="Bài tập 1.8"}
**Thử thách: hình đầu tiên.** Vẽ biểu đồ tần suất của huyết áp tâm thu cho dữ liệu thô, dùng `ggplot()` và `geom_histogram()` như ở Mục 1.10. Sau đó vẽ biểu đồ tần suất thứ hai sau khi chỉ giữ lại các giá trị từ 60 đến 260 mmHg bằng `filter()`. Có bao nhiêu bản ghi bị loại bỏ, và hình dạng phân phối thay đổi như thế nào? Viết hai câu mô tả phân phối của các giá trị hợp lý.
:::
