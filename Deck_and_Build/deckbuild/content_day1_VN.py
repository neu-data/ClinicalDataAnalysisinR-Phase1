SLIDES_DAY1 = [

    {"type": "divider", "title": "Ngày 1: Giới thiệu về R & RStudio",
     "plan_title": "Kế hoạch hôm nay",
     "agenda": [
        "Vì sao dùng R cho nghiên cứu lâm sàng",
        "R và RStudio: cài đặt và giao diện",
        "Project, tập lệnh, đối tượng và vector",
        "Data frame và các gói (tidyverse)",
        "Nhập và xem qua dữ liệu nghiên cứu lần đầu",
        "Bài thực hành"],
     "notes": "Điểm mấu chốt: cả ngày hôm nay là để làm quen, không phải học thuộc. Đến tối nay mỗi học viên sẽ đã nhập được một bộ dữ liệu lâm sàng thật và xem qua nó.\nNgộ nhận thường gặp: rằng bạn phải là lập trình viên. Không cần; R là một công cụ như máy tính bỏ túi hay ống nghe.\nDiễn giải lâm sàng: phân tích có thể tái lập nghĩa là một đồng nghiệp hay cơ quan quản lý có thể chạy lại công việc của bạn và thu được cùng những con số.\nHỏi khán giả: ai đã từng dùng Excel cho nghiên cứu? Câu trả lời mong đợi: gần như tất cả. Nhịp cầu: R làm được những gì Excel làm, nhưng nó ghi lại mọi bước.\nMẹo trình diễn: để RStudio mở trên màn hình phía sau bạn để mọi người thấy thứ thật, không chỉ là slide."},

    {"type": "content", "title": "Vì sao dùng R cho nghiên cứu lâm sàng",
     "blocks": [
        {"header": "R mang lại điều gì cho bạn", "lines": [
            "Một ngôn ngữ miễn phí, mã nguồn mở cho thống kê và dữ liệu",
            "Được dùng trong thử nghiệm lâm sàng, dịch tễ học và các tạp chí",
            "Xử lý nhập, làm sạch, phân tích và vẽ đồ thị ở cùng một nơi"]},
        {"header": "Vì sao điều đó quan trọng", "lines": [
            "Mọi bước đều được ghi lại, nên phân tích có thể lặp lại được",
            "Không tốn phí và không cần bản quyền: cài trên bất kỳ máy tính nào",
            "Một cộng đồng khổng lồ và các gói dành cho nghiên cứu y học"]},
        {"callout": "interpretation", "header": "Khả năng tái lập",
         "lines": ["Nếu bạn có thể chạy lại tập lệnh, bạn có thể bảo vệ kết quả."]}],
     "notes": "Điểm mấu chốt: lợi thế nổi bật là khả năng tái lập cộng với chi phí bằng không. Bấm-từng-bước trong Excel thì khó tái lập; một tập lệnh là công thức.\nNgộ nhận thường gặp: rằng miễn phí nghĩa là chất lượng thấp. R được dùng bởi các chuyên gia thẩm định của FDA, EMA, và hầu hết các nhóm dịch tễ học lớn.\nDiễn giải lâm sàng: khi một người thẩm định hỏi bạn đã tính ra một con số như thế nào, bạn chỉ vào một dòng mã, không phải trí nhớ của bạn.\nHỏi khán giả: điều gì xảy ra nếu bạn làm lại phân tích của năm ngoái trong Excel bằng tay? Câu trả lời mong đợi: bạn có thể thu được các con số hơi khác. Một tập lệnh loại bỏ rủi ro đó.\nMẹo trình diễn: nhắc rằng các hình trong nhiều bài báo NEJM và Lancet được tạo bằng R."},

    {"type": "two_column", "title": "R và RStudio: Hai thứ khác nhau",
     "left": {"header": "R (động cơ)",
        "lines": [
            "Ngôn ngữ thống kê thực sự",
            "Thực hiện việc tính toán",
            "Bạn cài nó trước",
            "Hiếm khi được mở riêng lẻ"],
        "bullets": True},
     "right": {"header": "RStudio (bảng điều khiển)",
        "lines": [
            "Một không gian làm việc thân thiện bao quanh R",
            "Trình soạn thảo, console, đồ thị, trợ giúp",
            "Cài nó thứ hai",
            "Đây là thứ bạn mở hằng ngày"],
        "bullets": True},
     "notes": "Điểm mấu chốt: R là động cơ, RStudio là bảng điều khiển. Bạn cần cả hai, và bạn cài R trước.\nLỗi thường gặp: người ta cố mở R trực tiếp và thấy một console trống trơn. Luôn mở RStudio thay vào đó.\nDiễn giải lâm sàng: hãy hình dung R như máy phân tích trong phòng xét nghiệm và RStudio như giao diện của kỹ thuật viên với nó.\nHỏi khán giả: mỗi sáng bạn nhấp đúp vào cái nào? Câu trả lời mong đợi: RStudio.\nMẹo trình diễn: hiện cả hai biểu tượng trên màn hình nền để sự phân biệt trở nên cụ thể."},

    {"type": "content", "title": "Giao diện RStudio: Bốn khung",
     "blocks": [
        {"header": "Trên-trái: Source (Trình soạn thảo tập lệnh)", "lines": [
            "Nơi bạn viết và lưu mã của mình"]},
        {"header": "Dưới-trái: Console (bảng điều khiển)", "lines": [
            "Nơi mã chạy và kết quả hiện ra"]},
        {"header": "Trên-phải: Environment (môi trường)", "lines": [
            "Các đối tượng và dữ liệu bạn đã tạo"]},
        {"header": "Dưới-phải: Files / Plots / Help (Tệp / Đồ thị / Trợ giúp)", "lines": [
            "Thư mục, đồ thị của bạn, và tài liệu"]},
        {"callout": "tip", "header": "Định hướng",
         "lines": ["Dành hai phút tìm từng khung trước khi bạn gõ."]}],
     "notes": "Điểm mấu chốt: chỉ bốn khung. Source và Console bên trái, Environment và các tab Files/Plots/Help bên phải.\nNgộ nhận thường gặp: rằng bố cục là cố định; nó có thể tùy chỉnh, nhưng cấu hình mặc định là ổn cho người mới.\nDiễn giải lâm sàng: khung Environment là mặt bàn làm việc của bạn, nó cho thấy dữ liệu nào hiện đang được nạp.\nHỏi khán giả: đồ thị sẽ xuất hiện ở đâu? Câu trả lời mong đợi: dưới-phải, tab Plots.\nMẹo trình diễn: gõ một dòng trong Console và cùng dòng đó trong Source, rồi cho thấy chỉ Source đã lưu mới tồn tại lâu dài."},

    {"type": "content", "title": "Project của RStudio và thư mục làm việc",
     "blocks": [
        {"header": "Thư mục làm việc", "lines": [
            "Thư mục mà R tìm vào khi bạn mở một tệp",
            "Kiểm tra nó bằng getwd()"]},
        {"header": "Dùng Project, không dùng setwd()", "lines": [
            "File > New Project giữ mọi thứ trong một thư mục",
            "Các đường dẫn trở nên tương đối, như Data/file.csv",
            "Công việc chạy được trên mọi máy tính, không cần thay đổi"]},
        {"callout": "warning", "header": "Tránh setwd()",
         "lines": ["Một đường dẫn cứng sẽ hỏng trên mọi máy khác."]}],
     "notes": "Điểm mấu chốt: một Project của RStudio đặt thư mục làm việc giúp bạn và làm cho các đường dẫn có thể mang đi được.\nLỗi thường gặp: setwd(\"C:/Users/me/Desktop/...\") ở đầu một tập lệnh. Nó chỉ chạy trên đúng một máy tính đó.\nDiễn giải lâm sàng: tính di động quan trọng khi bạn chia sẻ một phân tích với một nhà thống kê hay một cộng tác viên ở cơ sở khác.\nHỏi khán giả: viết đường dẫn C: đầy đủ thì có gì sai? Câu trả lời mong đợi: không ai khác có đúng thư mục đó.\nMẹo trình diễn: chạy getwd() một lần để mọi người thấy thư mục hiện tại thực sự là gì, rồi mở Project của khóa học."},

    {"type": "two_column", "title": "Tập lệnh và Console",
     "intro": "Cả hai đều chạy mã R, nhưng chỉ một là bản ghi của bạn.",
     "left": {"header": "Console",
        "lines": [
            "Gõ, nhấn Enter, nhận câu trả lời",
            "Tốt cho những lần thử nhanh",
            "Không được lưu khi bạn đóng"],
        "bullets": True},
     "right": {"header": "Tập lệnh (Source)",
        "lines": [
            "Bạn viết, rồi lưu thành tệp .R",
            "Chạy lại bất cứ lúc nào, từng dòng một",
            "Đây là bản ghi có thể tái lập của bạn"],
        "bullets": True},
     "notes": "Điểm mấu chốt: tập lệnh là bản ghi có thể tái lập; console là chỗ nháp.\nNgộ nhận thường gặp: rằng gõ trong console là đủ. Nó biến mất khi đóng.\nDiễn giải lâm sàng: tập lệnh đã lưu là dấu vết kiểm toán của phân tích, như một sổ tay phòng xét nghiệm đã ký.\nHỏi khán giả: phân tích thật nên nằm ở đâu? Câu trả lời mong đợi: trong một tập lệnh đã lưu.\nMẹo trình diễn: chạy một dòng bằng Ctrl+Enter từ tập lệnh và cho thấy kết quả xuất hiện trong console bên dưới."},

    {"type": "code", "title": "Những bước đầu: R như một máy tính bỏ túi",
     "intro": "Cách đơn giản nhất để bắt đầu - chỉ cần gõ các phép tính vào Console.",
     "code": '2 + 2\n140 / 90        # a blood-pressure ratio\nsqrt(16)\n(120 + 130 + 145 + 150) / 4   # mean of four readings',
     "output": "[1] 4\n[1] 1.555556\n[1] 4\n[1] 136.25",
     "note": "Mọi thứ trong R đều được xây từ những bước nhỏ như thế này - bắt đầu đơn giản, rồi xây dần lên.",
     "notes": ("Điểm dạy mấu chốt: trước hết R là một máy tính bỏ túi - các hàm như sqrt() "
               "và số học (+, -, *, /) hoạt động đúng như bạn mong đợi.\n"
               "Ngộ nhận thường gặp: rằng bạn phải học thuộc các lệnh trước khi có thể làm bất cứ điều gì. "
               "Bạn có thể khám phá bằng cách chỉ gõ các phép tính.\n"
               "Diễn giải lâm sàng: một tỷ số huyết áp hay một giá trị trung bình nhanh của vài lần đo là "
               "công việc thật, hữu ích ngay ngày đầu tiên.\n"
               "Câu hỏi cho khán giả: 140 / 90 cho ra gì, và nó có thể biểu thị điều gì? "
               "Câu trả lời mong đợi: khoảng 1.56 - một tỷ số tâm thu trên tâm trương thô sơ.\n"
               "Mẹo trình diễn: để học viên đọc to các phép tính và gõ trực tiếp; xây dựng sự tự tin trước khi "
               "giới thiệu đối tượng.")},

    {"type": "content", "title": "Đối tượng và mũi tên phép gán",
     "blocks": [
        {"header": "Lưu một giá trị vào một đối tượng", "lines": [
            "sbp <- 152 nghĩa là lưu 152 vào một đối tượng tên sbp",
            "Gõ tên sbp để in nó ra lại",
            "Mũi tên <- là toán tử phép gán"]},
        {"header": "R phân biệt chữ hoa chữ thường", "lines": [
            "SBP và sbp là hai đối tượng khác nhau"]},
        {"callout": "mistake", "header": "Những sơ suất thường gặp",
         "lines": ["Dùng = thay cho <-; nhầm lẫn giữa chữ hoa và chữ thường."]}],
     "notes": "Điểm mấu chốt: <- lưu một giá trị vào một đối tượng có tên; tên đó sau đó hành xử như chính giá trị.\nLỗi thường gặp: viết sbp = 152 (chạy được nhưng không được khuyến khích) hoặc gọi nó là Sbp về sau và gặp lỗi.\nDiễn giải lâm sàng: một đối tượng chỉ là một hộp chứa có dán nhãn, như một ống đựng mẫu bệnh phẩm có dán nhãn.\nHỏi khán giả: Age có giống age trong R không? Câu trả lời mong đợi: không, R phân biệt chữ hoa chữ thường.\nMẹo trình diễn: gõ phím tắt Alt+- (Alt và dấu trừ) để chèn <- tự động, và cho thấy lỗi phân biệt hoa-thường trực tiếp."},

    {"type": "code", "title": "Đối tượng và vector trong thực tế",
     "intro": "Một vector chứa nhiều giá trị cùng kiểu.",
     "code": "sbp <- 152\nsbp\nsbp_readings <- c(152, 138, 145, 160, 129, 142)\nlength(sbp_readings)\nmean(sbp_readings)\nsd(sbp_readings)",
     "output": "[1] 152\n[1] 6\n[1] 144.3333\n[1] 11.23239",
     "note": "c() nghĩa là kết hợp; mean() và sd() tóm tắt toàn bộ vector.",
     "notes": "Điểm mấu chốt: c() kết hợp các giá trị thành một vector; các hàm như length(), mean() và sd() tác động lên cả vector cùng một lúc.\nLỗi thường gặp: quên dấu phẩy bên trong c(), hoặc trộn lẫn văn bản và số trong một vector.\nDiễn giải lâm sàng: một vector là một cột các lần đo, ở đây là sáu lần đo huyết áp tâm thu.\nHỏi khán giả: length() cho ta biết điều gì? Câu trả lời mong đợi: có bao nhiêu giá trị trong vector, ở đây là sáu.\nMẹo trình diễn: cũng chạy summary(sbp_readings) và max(sbp_readings) để họ thấy thêm nhiều hàm trên cùng một đối tượng."},

    {"type": "content", "title": "Các kiểu dữ liệu bạn sẽ gặp",
     "blocks": [
        {"header": "Ba kiểu thường ngày", "lines": [
            "numeric: số, như age hay sbp (60, 152)",
            "character: văn bản trong dấu ngoặc kép, như \"Female\"",
            "logical: TRUE hay FALSE, như sbp >= 140"]},
        {"header": "Vì sao kiểu dữ liệu quan trọng", "lines": [
            "Bạn có thể lấy trung bình các số, chứ không phải văn bản",
            "R chọn kiểu khi nó đọc dữ liệu của bạn"]},
        {"callout": "note", "header": "Mẹo",
         "lines": ["glimpse() cho thấy kiểu của từng cột trong nháy mắt."]}],
     "notes": "Điểm mấu chốt: numeric, character và logical là ba kiểu mà người mới cần. Mỗi cột dữ liệu là một kiểu.\nNgộ nhận thường gặp: rằng một số được lưu dưới dạng văn bản sẽ hành xử như một số; không phải vậy, bạn không thể lấy trung bình nó.\nDiễn giải lâm sàng: nếu age được nhập dưới dạng văn bản (vì một giá trị lạc như 200 hay một chữ cái), việc tính trung bình sẽ thất bại cho tới khi được sửa.\nHỏi khán giả: \"Yes\"/\"No\" là kiểu gì? Câu trả lời mong đợi: văn bản character; ta sẽ mã hoá lại nó sau.\nMẹo trình diễn: tạo high_bp <- sbp_readings >= 140 và cho thấy vector logical TRUE/FALSE, rồi sum() nó để đếm."},

    {"type": "content", "title": "Data frame và tibble",
     "blocks": [
        {"header": "Hình dạng của một bộ dữ liệu", "lines": [
            "Một data frame là một bảng: các hàng và các cột",
            "Mỗi hàng là một bệnh nhân (một quan sát)",
            "Mỗi cột là một biến (age, sex, sbp)"]},
        {"header": "Tibble", "lines": [
            "Phiên bản data frame của tidyverse",
            "In ra gọn gàng và hiển thị kiểu của cột"]},
        {"callout": "interpretation", "header": "Đọc nó như một phòng khám",
         "lines": ["Các hàng là người; các cột là những gì bạn đo được."]}],
     "notes": "Điểm mấu chốt: một data frame (hay tibble) là bảng hình chữ nhật chứa nghiên cứu của bạn, hàng = bệnh nhân, cột = biến.\nNgộ nhận thường gặp: rằng dữ liệu trong R trông như bảng tính với các ô gộp và màu sắc; nó là các cột gọn gàng, thuần túy.\nDiễn giải lâm sàng: bố cục hàng-là-bệnh-nhân, cột-là-biến này chính là cấu trúc gọn gàng mà các phân tích mong đợi.\nHỏi khán giả: trong dữ liệu của ta, một hàng đại diện cho điều gì? Câu trả lời mong đợi: một người lớn đến khám tại một cơ sở CSSKBĐ.\nMẹo trình diễn: đối chiếu bản in của một tibble (gọn, hiển thị kiểu) với bản in của data.frame cơ sở để họ trân trọng tibble."},

    {"type": "content", "title": "Gói: Cài một lần, nạp mỗi phiên",
     "blocks": [
        {"header": "Hai lệnh khác nhau", "lines": [
            "install.packages(\"tidyverse\") tải nó về một lần",
            "library(tidyverse) nạp nó mỗi phiên mới"]},
        {"header": "Các gói ta dùng hôm nay", "lines": [
            "tidyverse: nhập, xử lý, vẽ đồ thị",
            "readxl: đọc tệp Excel .xlsx"]},
        {"callout": "mistake", "header": "Lỗi thường gặp",
         "lines": ["Chạy install.packages() mỗi lần (chậm, cần internet)."]}],
     "notes": "Điểm mấu chốt: cài một lần (tải từ internet), library() mỗi lần bạn khởi động R. Hai việc riêng biệt.\nLỗi thường gặp: đặt install.packages() ở đầu một tập lệnh chạy hằng ngày; nó tải lại một cách không cần thiết và thất bại khi ngoại tuyến.\nDiễn giải lâm sàng: một gói là một hộp công cụ chứa các hàm bổ sung; tidyverse và readxl là những gói ta cần để nhập dữ liệu.\nHỏi khán giả: bạn có cài một gói mỗi phiên không? Câu trả lời mong đợi: không, bạn chỉ library() nó thôi.\nMẹo trình diễn: cho thấy library(tidyverse) in ra thông báo đính kèm của nó, và lưu ý rằng đó là bình thường, không phải lỗi."},

    {"type": "code", "title": "Nhập dữ liệu nghiên cứu",
     "intro": "Nạp các gói trước, rồi đọc tệp.",
     "code": "library(tidyverse)\nlibrary(readxl)\nhtn <- read_csv(\"Data/hypertension_phc_raw.csv\")\nhtn_xl <- read_excel(\n  \"Data/hypertension_phc_raw.xlsx\", sheet = \"data\")\ndim(htn)",
     "output": "Rows: 1503  Columns: 36\n[1] 1503   36",
     "note": "read_csv cho CSV, read_excel cho Excel. Lưu ý 1503, không phải 1500.",
     "notes": "Điểm mấu chốt: read_csv() đọc tệp CSV, read_excel() đọc tệp Excel; cả hai đều nằm trong một tibble. Các đường dẫn là tương đối vì ta đang ở trong một Project.\nLỗi thường gặp: quên library(readxl) trước read_excel, hoặc sai đường dẫn/tên tệp (hoa-thường và chính tả phải khớp chính xác).\nDiễn giải lâm sàng: 1503 hàng nhưng nghiên cứu thu nhận 1.500, nên ba bản ghi trùng đang ẩn trong này.\nHỏi khán giả: vì sao 1503 chứ không phải 1500? Câu trả lời mong đợi: có 3 bản ghi trùng, mà ta sẽ sửa vào Ngày 2.\nMẹo trình diễn: chỉ ra thông báo đặc tả cột mà read_csv in ra; nó mang tính thông tin, không phải lỗi."},

    {"type": "bullets", "title": "Xem lần đầu: Hiểu dữ liệu của bạn",
     "intro": "Chạy những lệnh này ngay khoảnh khắc bất kỳ bộ dữ liệu nào được nhập.",
     "items": [
        "dim(htn): bao nhiêu hàng và cột",
        "names(htn): tên các biến",
        "glimpse(htn): mỗi cột cùng với kiểu của nó",
        "head(htn): vài hàng đầu tiên",
        "View(htn): mở trình xem dạng bảng tính",
        "htn$age: rút một cột ra bằng dấu đô-la",
        "summary(htn$age): min, trung bình, max của một biến",
        "table(htn$sex): số đếm của mỗi phân loại"],
     "notes": "Điểm mấu chốt: một quy trình xem-lần-đầu cố định, dim, names, glimpse, head, View, rồi $ để xem xét từng biến với summary và table.\nLỗi thường gặp: nhảy thẳng vào phân tích mà không xem; nhiều vấn đề dữ liệu có thể thấy được trong ba mươi giây đầu.\nDiễn giải lâm sàng: summary() và table() là các xét nghiệm sàng lọc cho dữ liệu của bạn; chúng đánh dấu các giá trị bất khả và các phân loại lộn xộn.\nHỏi khán giả: htn$age trả về gì? Câu trả lời mong đợi: cột age dưới dạng một vector đơn.\nMẹo trình diễn: chạy View(htn) để mọi người thấy lưới bảng tính quen thuộc, rồi đóng nó và dựa vào glimpse()."},

    {"type": "code", "title": "Xem xét từng biến",
     "intro": "Dấu $ rút một cột ra để tóm tắt.",
     "code": "summary(htn$age)\ntable(htn$sex)",
     "output": "   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.\n   0.0    38.0    52.0    53.4    66.0   200.0\n\n     f      F female Female      m ...\n    11     63    402    498     14 ...",
     "note": "Tuổi cao nhất 200 và tám cách viết của sex: dữ liệu này cần được làm sạch.",
     "notes": "Điểm mấu chốt: summary() trên age và table() trên sex lập tức phơi bày các vấn đề, một giá trị max bất khả là 200 và nhiều cách viết của cùng một phân loại.\nNgộ nhận thường gặp: rằng dữ liệu được nhập vào là sạch; dữ liệu lâm sàng thô hầu như không bao giờ sạch.\nDiễn giải lâm sàng: tuổi 200 (và một số 0) không thể là thật; Female/female/F/f đều là cùng một nhóm được ghi lại không nhất quán.\nHỏi khán giả: nên có bao nhiêu phân loại sex thật sự? Câu trả lời mong đợi: hai, nhưng bảng cho thấy tám nhãn.\nMẹo trình diễn: cũng chạy table(htn$facility) để lộ ra các khoảng trắng lạc, và nói với họ rằng Ngày 2 sẽ sửa tất cả những điều này."},

    {"type": "content", "title": "Lỗi thường gặp và gỡ lỗi nhanh",
     "blocks": [
        {"header": "Khi nó không chạy, hãy kiểm tra", "lines": [
            "Bạn đã chạy library() cho gói chưa?",
            "Bạn đã dùng <- chứ không phải = cho phép gán chưa?",
            "Chính tả và HOA-thường có đúng chính xác không?",
            "Đường dẫn và tên tệp có đúng không?"]},
        {"callout": "warning", "header": "could not find function",
         "lines": ["Thường nghĩa là gói chưa được nạp: hãy chạy library()."]},
        {"callout": "mistake", "header": "cannot open file",
         "lines": ["Sai đường dẫn hoặc tên tệp; kiểm tra khung Files."]}],
     "notes": "Điểm mấu chốt: hầu hết lỗi của người mới là một trong bốn thứ, thiếu library(), sai toán tử, một sơ suất hoa-thường/chính tả, hoặc một đường dẫn sai.\nLỗi thường gặp: hoảng loạn trước dòng chữ đỏ. Hãy đọc thông báo; nó thường nêu tên vấn đề.\nDiễn giải lâm sàng: gỡ lỗi giống như chẩn đoán phân biệt, đọc dấu hiệu (lỗi), hình thành giả thuyết, thử cách sửa.\nHỏi khán giả: bạn gặp could not find function read_csv, sai ở đâu? Câu trả lời mong đợi: tidyverse chưa được nạp; hãy chạy library(tidyverse).\nMẹo trình diễn: cố ý kích hoạt một lỗi trực tiếp (gõ sai tên tệp) và đi qua việc đọc thông báo một cách bình tĩnh."},

    {"type": "content", "title": "Dữ liệu đã cho ta biết điều gì",
     "blocks": [
        {"header": "Các vấn đề nhìn thấy ngay lần xem đầu", "lines": [
            "Age = 200 và age = 0: giá trị bất khả",
            "Sex được ghi theo tám cách khác nhau",
            "1503 hàng cho 1.500 người: bản ghi trùng"]},
        {"header": "Vì sao đây là tin tốt", "lines": [
            "Ta phát hiện nó trong vài giây, trước mọi phân tích",
            "Làm sạch là chủ đề của Ngày 2"]},
        {"callout": "interpretation", "header": "Rác vào, rác ra",
         "lines": ["Không thống kê nào đáng tin trên dữ liệu chưa được làm sạch."]}],
     "notes": "Điểm mấu chốt: lần xem đầu đã làm nổi lên ba vấn đề lớn, giá trị bất khả, phân loại không nhất quán, và các hàng trùng.\nNgộ nhận thường gặp: rằng phát hiện vấn đề nghĩa là bạn đã làm sai điều gì đó; phát hiện chúng sớm chính là mục tiêu.\nDiễn giải lâm sàng: phân tích trước khi làm sạch sẽ làm sai lệch mọi kết quả, tuổi trung bình sẽ bị kéo lên bởi số 200.\nHỏi khán giả: ngay bây giờ ta có nên tính tuổi trung bình không? Câu trả lời mong đợi: không, hãy sửa các giá trị bất khả trước.\nMẹo trình diễn: báo trước Ngày 2 bằng cách cho thấy một số 200 duy nhất làm méo mean(htn$age) như thế nào; nó tạo động lực cho ngày làm sạch."},

    {"type": "content", "title": "Bài thực hành Ngày 1: Nhập bộ dữ liệu lâm sàng",
     "blocks": [
        {"header": "Nhiệm vụ của bạn", "lines": [
            "Mở Project RStudio của khóa học",
            "library(tidyverse) và library(readxl)",
            "Nhập tệp CSV bằng read_csv()",
            "Nhập tệp Excel bằng read_excel()",
            "Chạy glimpse() trên dữ liệu",
            "summary() cột age, table() cột sex"]},
        {"callout": "tip", "header": "Cần chú ý điều gì",
         "lines": ["Phát hiện tuổi bất khả, nhiều cách viết của sex, 1503 hàng."]}],
     "notes": "Điểm mấu chốt: bài thực hành là toàn bộ quy trình Ngày 1 từ đầu đến cuối, project, các gói, nhập cả hai định dạng, rồi xem xét.\nLỗi thường gặp: quên một lệnh library(), hoặc gõ sai đường dẫn; hãy đi vòng và kiểm tra những thứ này trước.\nDiễn giải lâm sàng: bằng cách nhập và xem xét, học viên trải nghiệm chính những cờ đỏ về chất lượng dữ liệu mà ta vừa bàn.\nHỏi khán giả: sau table(sex), bạn thấy bao nhiêu nhãn khác nhau? Câu trả lời mong đợi: tám, cho hai phân loại thật.\nMẹo trình diễn: cho một thời gian cố định (khoảng 15 phút), rồi đúc kết bằng cách hỏi ai tìm ra tuổi 200 đầu tiên."},

    {"type": "content", "title": "Ôn tập và bắc cầu sang Ngày 2",
     "blocks": [
        {"header": "Hôm nay bạn đã học được cách", "lines": [
            "Phân biệt R với RStudio và tìm bốn khung",
            "Làm việc trong một Project với một tập lệnh đã lưu",
            "Tạo đối tượng (<-) và vector (c())",
            "Nạp các gói và nhập dữ liệu CSV và Excel",
            "Xem xét dữ liệu với glimpse, summary và table"]},
        {"header": "Ngày mai: Ngày 2", "lines": [
            "Làm sạch mớ hỗn độn: sửa tuổi, hợp nhất các phân loại",
            "Loại bỏ bản ghi trùng và xử lý giá trị khuyết"]},
        {"callout": "note", "header": "Làm tốt lắm",
         "lines": ["Bạn đã nhập dữ liệu lâm sàng thật ngay ngày đầu tiên."]}],
     "notes": "Điểm mấu chốt: củng cố cả chặng đường, từ chỗ chưa từng mở R đến chỗ nhập và xem xét một bộ dữ liệu thật, rồi xem trước việc làm sạch.\nNgộ nhận thường gặp: rằng ta sẽ bắt đầu phân tích vào ngày mai; trước tiên ta làm sạch, vì phân tích đáng tin cần dữ liệu sạch.\nDiễn giải lâm sàng: hôm nay là dữ liệu VÀO và một lần xem đầu; Ngày 2 biến tệp thô, lộn xộn thành một bộ dữ liệu sẵn sàng để phân tích.\nHỏi khán giả: ba vấn đề dữ liệu ta phải sửa ngày mai là gì? Câu trả lời mong đợi: giá trị bất khả, phân loại không nhất quán, các hàng trùng.\nMẹo trình diễn: kết thúc bằng cách mở lại tập lệnh của họ và chạy lại nó từ trên xuống dưới, chứng minh khả năng tái lập chỉ trong một lần gõ phím."},

]
