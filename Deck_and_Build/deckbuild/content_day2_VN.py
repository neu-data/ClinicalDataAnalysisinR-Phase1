SLIDES_DAY2 = [

    # 1. Divider
    {"type": "divider", "title": "Ngày 2: Hiểu & Làm sạch dữ liệu lâm sàng",
     "plan_title": "Kế hoạch",
     "agenda": [
         "Vì sao làm sạch quan trọng: rác vào, rác ra",
         "Các kiểu biến và mã hoá lâm sàng",
         "Dữ liệu khuyết, bản ghi trùng, phân loại không nhất quán",
         "Kiểm định, mã hoá lại, ngày tháng và biến phân loại (factor)",
         "Lưu bộ dữ liệu sạch: bản giao ước cho các Ngày 3-5"],
     "notes": "Điểm mấu chốt: hôm nay ta biến một tệp thô lộn xộn thành một bộ dữ liệu gọn gàng, sẵn sàng phân tích và lưu nó một lần cho cả tuần.\nNgộ nhận: làm sạch không phải một bước nhanh trước công việc 'thật'; nó CHÍNH LÀ phần lớn công việc.\nDiễn giải lâm sàng: mọi kết quả về sau đều phụ thuộc vào các quyết định đưa ra hôm nay.\nHỏi: ai từng phát hiện lỗi trong dữ liệu của mình sau khi đã chạy phân tích? Mong đợi: hầu hết giơ tay, thường là sau khi đã nộp.\nMẹo trình diễn: để tệp thô mở bên cạnh tập lệnh để mọi người thấy mớ hỗn độn mà ta đang thuần hóa."},

    # 2. Why cleaning matters
    {"type": "content", "title": "Vì sao làm sạch dữ liệu quan trọng",
     "blocks": [
         {"header": "Rác vào, rác ra",
          "lines": [
              "Một giá trị p không thể cứu một huyết áp gõ nhầm.",
              "Lỗi không tự thông báo; chúng ẩn trong những con số hợp lý.",
              "Dữ liệu sạch là nền tảng của một kết quả đáng tin."]},
         {"header": "Làm sạch chiếm bao nhiêu phần của một dự án?",
          "lines": [
              "Thường là 60-80% tổng thời gian phân tích.",
              "Bỏ qua nó không tiết kiệm thời gian; nó chuyển chi phí sang khâu bình duyệt."]},
         {"callout": "interpretation", "header": "Vì sao bác sĩ lâm sàng nên quan tâm",
          "lines": ["Một ngưỡng cắt hay đơn vị sai có thể lật ngược một kết luận lâm sàng."]},
     ],
     "notes": "Điểm mấu chốt: làm sạch là phần lớn thời gian phân tích thực tế và là phần mà người thẩm định soi kỹ nhất.\nNgộ nhận: 'người quản lý dữ liệu đã làm sạch rồi' - vẫn phải có ai đó đối chiếu nó với ý nghĩa lâm sàng.\nDiễn giải lâm sàng: một SBP bằng 7 hay một tuổi 200 sẽ âm thầm làm méo các giá trị trung bình và mô hình.\nHỏi: khoảng SBP lúc nghỉ thực tế của một người lớn là bao nhiêu? Mong đợi: khoảng 90-180; chính trực giác này là thứ ta mã hoá thành các quy tắc kiểm định.\nMẹo trình diễn: hiện một giá trị bất khả và hỏi nó sẽ làm gì với một giá trị trung bình."},

    # 3. Variable types overview (table)
    {"type": "table", "title": "Các kiểu biến trong dữ liệu lâm sàng",
     "headers": ["Kiểu", "Nó là gì", "Ví dụ trong dữ liệu của ta"],
     "rows": [
         ["Liên tục", "Số trên một thang đo", "age, sbp_mmhg, weight_kg"],
         ["Nhị phân", "Hai phân loại", "diabetes (Yes/No)"],
         ["Phân loại", "Các nhóm không thứ tự", "facility, occupation"],
         ["Thứ tự", "Các nhóm có thứ tự", "education (None to Tertiary)"],
         ["Ngày tháng", "Thời gian theo lịch", "enroll_date"]],
     "caption": "Kiểu quyết định cách R lưu trữ, tóm tắt và mô hình hóa một biến.",
     "notes": "Điểm mấu chốt: chọn đúng kiểu ngay từ đầu chi phối mọi tóm tắt, đồ thị và mô hình về sau.\nNgộ nhận: 'một con số luôn là liên tục' - các phân loại được mã hoá (1=Yes) là số nhưng lại mang tính phân loại.\nDiễn giải lâm sàng: education có thứ tự nên giữ nguyên thứ tự của nó; facility không nên bị coi là một thang đo có xếp hạng.\nHỏi: điểm đau Likert 0-10 là liên tục hay thứ tự? Mong đợi: có thể biện hộ theo cả hai cách; điểm mấu chốt là quyết định một cách có chủ đích.\nMẹo trình diễn: ánh xạ mỗi hàng tới một cột trong tệp thô đang mở."},

    # 4. Clinical coding
    {"type": "content", "title": "Mã hoá lâm sàng: Các mã nhất quán",
     "blocks": [
         {"header": "Mã hoá nghĩa là gì",
          "lines": [
              "Thống nhất một giá trị viết duy nhất cho mỗi phân loại ngoài đời.",
              "Sex được lưu là Female / Male, không phải F / f / female.",
              "Các biến nhị phân được lưu là Yes / No, không phải một mớ lẫn lộn Y, 1, true."]},
         {"header": "Vì sao điều đó quan trọng",
          "lines": [
              "R coi 'Yes' và 'yes' là hai nhóm khác nhau.",
              "Các mã không nhất quán chia một phân loại thành nhiều phân loại.",
              "Các mã nhất quán làm cho bảng và mô hình đáng tin cậy."]},
         {"callout": "warning", "header": "Cái bẫy thường gặp",
          "lines": ["Tám cách viết của sex trở thành tám phân loại ma."]},
     ],
     "notes": "Điểm mấu chốt: một phân loại chỉ tồn tại nếu nhãn của nó được viết giống hệt nhau mỗi lần.\nNgộ nhận: R đủ thông minh để biết 'Y' nghĩa là 'Yes' - không phải vậy.\nDiễn giải lâm sàng: một biến sex bị chia tách sẽ làm sai lệch mọi ước lượng có hiệu chỉnh theo sex.\nHỏi: một trường văn bản tự do có thể tạo ra bao nhiêu giá trị khác nhau của sex? Mong đợi: nhiều đến bất ngờ; ta sẽ thấy tám.\nMẹo trình diễn: chạy table() trước khi làm sạch để lộ ra sự hỗn loạn."},

    # 5. Missing data
    {"type": "content", "title": "Dữ liệu khuyết: Nó ẩn mình ra sao",
     "blocks": [
         {"header": "Nó hiếm khi trông giống một thứ",
          "lines": [
              "Ô trống, chữ NA, và các mã báo hiệu 999 hay -99.",
              "Nếu R không nhận ra chúng, 999 bị coi là một giá trị thật.",
              "Chỉ một số 999 có thể phá hỏng một giá trị trung bình hay một hồi quy."]},
         {"header": "Đọc nó cho đúng ngay khi nhập",
          "lines": [
              "Nói cho read_csv biết chuỗi nào nghĩa là khuyết.",
              "na = c(\"\", \"NA\", \"999\", \"-99\")"]},
         {"callout": "note", "header": "Các dạng khuyết (tóm tắt)",
          "lines": ["MCAR, MAR, MNAR - dạng khuyết ảnh hưởng đến cách ta xử lý nó về sau."]},
     ],
     "notes": "Điểm mấu chốt: định nghĩa tình trạng khuyết ngay khi nhập để các mã báo hiệu không bao giờ lọt vào phân tích dưới dạng số.\nNgộ nhận: ô trống là dạng khuyết duy nhất - các mã báo hiệu dạng số mới là loại nguy hiểm.\nDiễn giải lâm sàng: một SBP 999 sẽ thổi phồng giá trị trung bình và làm tăng giả tạo tỷ lệ tăng huyết áp.\nHỏi: điều gì xảy ra với mean(sbp) nếu một số 999 được đọc như một giá trị thật? Mong đợi: nó nhảy vọt; ví dụ này thuyết phục cho đối số na=.\nMẹo trình diễn: nhập một lần không có na= và một lần có nó; so sánh summary()."},

    # 6. Duplicates
    {"type": "content", "title": "Bản ghi trùng: 1503 so với 1500",
     "blocks": [
         {"header": "Câu chuyện",
          "lines": [
              "Tệp thô có 1503 hàng nhưng chỉ 1500 bệnh nhân.",
              "Ba bản ghi bị nhập hai lần - trùng hoàn toàn.",
              "Bản ghi trùng thổi phồng cỡ mẫu và làm méo ước lượng."]},
         {"header": "Phát hiện và loại bỏ",
          "lines": [
              "sum(duplicated(raw)) cho thấy có bao nhiêu bản ghi trùng toàn phần.",
              "distinct(raw) giữ lại một bản của mỗi hàng duy nhất.",
              "n_distinct(raw$patient_id) khi đó phải bằng nrow(raw)."]},
         {"callout": "tip", "header": "Luôn kiểm tra lại",
          "lines": ["Xác nhận số hàng là 1500 sau distinct()."]},
     ],
     "notes": "Điểm mấu chốt: bản ghi trùng là một sự tăng cỡ mẫu giả và phải bị loại trước khi đếm bất cứ thứ gì.\nNgộ nhận: distinct() bỏ đi những hàng bạn muốn giữ - ở đây nó chỉ loại các bản sao toàn-hàng chính xác.\nDiễn giải lâm sàng: một bệnh nhân bị lặp sẽ đếm hai lần kết cục của họ, làm sai lệch tỷ lệ hiện mắc.\nHỏi: vì sao kiểm tra n_distinct(patient_id) cùng với nrow? Mong đợi: để bắt các lỗi nhập liệu cùng-ID-khác-hàng mà distinct() sẽ giữ lại.\nMẹo trình diễn: in nrow trước và sau để thấy được sự giảm từ 1503 xuống 1500."},

    # 7. Inconsistent categories - sex
    {"type": "content", "title": "Phân loại không nhất quán: 8 cách viết của Sex",
     "blocks": [
         {"header": "Mớ hỗn độn",
          "lines": [
              "Female, F, female, f và Male, M, male, m.",
              "Các khoảng trắng lạc tạo ra thêm nhiều biến thể.",
              "Tám nhãn cho hai nhóm thật."]},
         {"header": "Cách sửa",
          "lines": [
              "str_trim() loại bỏ khoảng trắng đầu và cuối.",
              "str_to_lower() làm cho hoa-thường không còn quan trọng.",
              "case_when() ánh xạ mọi biến thể sang Female hoặc Male."]},
         {"callout": "interpretation", "header": "Ý nghĩa lâm sàng",
          "lines": ["Bất cứ điều gì ngoài dự kiến đều thành NA, không phải một phỏng đoán."]},
     ],
     "notes": "Điểm mấu chốt: chuẩn hóa hoa-thường và khoảng trắng trước, rồi ánh xạ một tập nhỏ các giá trị đã biết.\nNgộ nhận: bạn phải liệt kê từng biến thể bằng tay - chuyển về chữ thường thu gọn phân nửa số đó ngay lập tức.\nDiễn giải lâm sàng: đừng bao giờ bịa ra một giới tính cho một mục không đọc được; NA là trung thực.\nHỏi: vì sao đưa các giá trị chưa biết về NA thay vì về nhóm lớn hơn? Mong đợi: phỏng đoán tạo ra sai lệch; NA là minh bạch.\nMẹo trình diễn: cho thấy table(sex) trước và sau case_when."},

    # 8. Standardising binaries (code slide)
    {"type": "code", "title": "Chuẩn hóa biến nhị phân bằng một hàm trợ giúp",
     "intro": "Một hàm tái sử dụng sửa mọi biến Yes/No.",
     "code": "to_yesno <- function(x) {\n  x <- str_to_lower(str_trim(as.character(x)))\n  case_when(\n    x %in% c(\"yes\",\"y\",\"1\",\"true\") ~ \"Yes\",\n    x %in% c(\"no\",\"n\",\"0\",\"false\") ~ \"No\",\n    TRUE ~ NA_character_)\n}\nraw <- raw |> mutate(across(\n  c(diabetes, family_history_htn, health_insurance,\n    htn_diagnosed, treatment_uptake), to_yesno))",
     "note": "Viết quy tắc một lần, áp dụng nó cho nhiều cột bằng across().",
     "notes": "Điểm mấu chốt: một hàm trợ giúp làm cho cùng một quy tắc làm sạch trở nên nhất quán và có thể kiểm toán trên nhiều cột.\nNgộ nhận: bạn nên lặp lại case_when cho từng biến - across() tránh các lỗi sao-chép-dán.\nDiễn giải lâm sàng: treatment_uptake phải là Yes/No sạch trước khi nó có thể là một kết cục.\nHỏi: vì sao ép về as.character trước? Mong đợi: một cột được đọc là numeric 0/1 sẽ không khớp các mẫu văn bản nếu không làm vậy.\nMẹo trình diễn: gọi to_yesno(c(\"Y\",\" no \",1)) riêng lẻ để cho thấy nó hoạt động."},

    # 9. Data validation - impossible values
    {"type": "content", "title": "Kiểm định: Các giá trị sinh lý bất khả",
     "blocks": [
         {"header": "Phát hiện điều bất khả",
          "lines": [
              "age 200 và age 0; sbp 0 và sbp 700.",
              "weight 7 kg; height 17 cm.",
              "Đây là lỗi nhập liệu, không phải bệnh nhân thật."]},
         {"header": "Sửa bằng các khoảng giá trị hợp lý",
          "lines": [
              "if_else(age >= 18 & age <= 110, age, NA_real_)",
              "Ngoài khoảng thì thành NA, không phải xóa cả hàng."]},
         {"callout": "interpretation", "header": "Chọn các khoảng",
          "lines": ["Đặt giới hạn từ kiến thức lâm sàng và dân số nghiên cứu của bạn, không phải chỉ từ dữ liệu."]},
     ],
     "notes": "Điểm mấu chốt: mã hoá tính hợp lý lâm sàng thành các khoảng rõ ràng và chuyển các vi phạm thành NA.\nNgộ nhận: giá trị ngoại lai và giá trị bất khả là như nhau - một SBP thật 185 là hợp lý và phải được giữ lại.\nDiễn giải lâm sàng: các khoảng nên phản ánh dân số; một nghiên cứu ở người lớn biện minh cho age >= 18.\nHỏi: có nên xóa cả hàng vì một chiều cao sai không? Mong đợi: không - chỉ để trống ô đó thôi để các trường hợp lệ khác còn được giữ.\nMẹo trình diễn: cho thấy summary() trước và sau; giá trị min và max sẽ khớp vào một khoảng hợp lý."},

    # 10. Recode / derive (two_column)
    {"type": "two_column", "title": "Mã hoá lại và tạo biến dẫn xuất",
     "left": {"header": "Tính lại BMI từ nguồn",
              "lines": [
                  "bmi = weight_kg / (height_cm/100)^2",
                  "Tạo biến dẫn xuất sau khi làm sạch height và weight.",
                  "Đừng bao giờ tin một BMI đã tính sẵn một cách mù quáng."],
              "bullets": True},
     "right": {"header": "Tạo các phân loại lâm sàng",
               "lines": [
                   "bmi_cat bằng cut(): từ Underweight tới Obese.",
                   "bp_category bằng case_when().",
                   "Normal, Elevated, Hypertension."],
               "bullets": True},
     "notes": "Điểm mấu chốt: tạo biến dẫn xuất từ các đầu vào đã làm sạch để giá trị dẫn xuất thừa hưởng việc làm sạch.\nNgộ nhận: tính lại BMI là thừa - cột được cung cấp có thể cũ hoặc sai.\nDiễn giải lâm sàng: bp_category dùng các ngưỡng cắt theo hướng dẫn (>=140/90 tăng huyết áp, >=130/80 tăng cao).\nHỏi: vì sao tính lại BMI thay vì giữ cột của tệp? Mong đợi: nó bảo đảm tính nhất quán với height và weight đã được kiểm định.\nMẹo trình diễn: cho thấy một hàng mà BMI được cung cấp không khớp với giá trị được tính lại."},

    # 11. Recode / derive (code slide)
    {"type": "code", "title": "Trình diễn: Tính lại BMI và phân loại",
     "code": "raw <- raw |> mutate(\n  bmi = round(weight_kg / (height_cm/100)^2, 1),\n  bmi_cat = cut(bmi,\n    breaks = c(-Inf, 18.5, 25, 30, Inf),\n    labels = c(\"Underweight\",\"Normal\",\n               \"Overweight\",\"Obese\")),\n  bp_category = case_when(\n    is.na(sbp_mmhg) | is.na(dbp_mmhg) ~ NA_character_,\n    sbp_mmhg >= 140 | dbp_mmhg >= 90 ~ \"Hypertension\",\n    sbp_mmhg >= 130 | dbp_mmhg >= 80 ~ \"Elevated\",\n    TRUE ~ \"Normal\"))",
     "note": "Xử lý NA một cách tường minh trước để một BP khuyết không bao giờ bị đọc là Normal.",
     "notes": "Điểm mấu chốt: sắp xếp case_when từ cụ thể nhất tới tổng quát nhất, và chặn NA trước nhánh TRUE.\nNgộ nhận: NA rơi xuống nhánh TRUE cuối - nên một BP khuyết sẽ bị dán nhãn sai là Normal.\nDiễn giải lâm sàng: phân loại nhầm một BP khuyết thành Normal sẽ đánh giá thấp gánh nặng tăng huyết áp.\nHỏi: điều gì xảy ra nếu dòng is.na bị xóa? Mong đợi: bệnh nhân có BP khuyết bị dán nhãn Normal - một lỗi âm thầm.\nMẹo trình diễn: cố ý bỏ dòng is.na, chạy table(bp_category), rồi khôi phục nó."},

    # 12. Dates (code slide)
    {"type": "code", "title": "Trình diễn: Phân tích các định dạng ngày hỗn hợp",
     "intro": "enroll_date đến với vài định dạng khác nhau.",
     "code": "library(lubridate)\nraw <- raw |> mutate(\n  enroll_date = parse_date_time(\n    enroll_date,\n    orders = c(\"ymd\",\"dmy\",\"d-b-Y\")) |>\n  as_date())\nsum(is.na(raw$enroll_date))",
     "output": "[1] 0",
     "note": "orders liệt kê các định dạng để thử, theo thứ tự ưu tiên.",
     "notes": "Điểm mấu chốt: parse_date_time của lubridate thử từng định dạng lần lượt, thuần hóa các kiểu nhập liệu hỗn hợp.\nNgộ nhận: ngày tháng chỉ là văn bản - lưu dưới dạng văn bản thì không thể sắp xếp hay lấy hiệu.\nDiễn giải lâm sàng: một Date thật cho phép bạn tính thời gian theo dõi và kiểm tra các cửa sổ thu nhận.\nHỏi: vì sao kiểm tra sum(is.na(enroll_date)) sau đó? Mong đợi: một sự tăng đột biến nghĩa là một định dạng ta chưa liệt kê và phải thêm vào.\nMẹo trình diễn: cho parse_date_time vài chuỗi mẫu để cho thấy mỗi order khớp như thế nào."},

    # 13. Factors and labels
    {"type": "content", "title": "Biến phân loại (factor) và mức tham chiếu",
     "blocks": [
         {"header": "Factor cho các phân loại một cấu trúc",
          "lines": [
              "factor() lưu các phân loại với các mức được định nghĩa.",
              "Factor có thứ tự giữ nguyên ý nghĩa thứ tự (education, activity).",
              "Các mức chi phối thứ tự trong bảng và đồ thị."]},
         {"header": "Đặt mức tham chiếu một cách có chủ đích",
          "lines": [
              "Với các kết cục nhị phân, liệt kê 'No' trước.",
              "factor(treatment_uptake, levels = c(\"No\",\"Yes\"))",
              "Mức đầu tiên là mốc so sánh cơ sở trong các mô hình."]},
         {"callout": "interpretation", "header": "Vì sao 'No' trước",
          "lines": ["Tỷ số chênh khi đó đọc là chênh lệch của Yes so với No - hướng lâm sàng tự nhiên."]},
     ],
     "notes": "Điểm mấu chốt: mức factor đầu tiên là mức tham chiếu, và nó quy định cách diễn giải mọi tỷ số chênh.\nNgộ nhận: thứ tự mức chỉ mang tính hình thức - nó âm thầm đảo ngược hướng của các ước lượng mô hình.\nDiễn giải lâm sàng: với 'No' làm tham chiếu, OR > 1 nghĩa là chênh lệch cao hơn của kết cục, đúng như bác sĩ mong đợi.\nHỏi: một OR bằng 3.56 cho diabetes nghĩa là gì khi 'No' làm tham chiếu? Mong đợi: người tiểu đường có chênh lệch tiếp nhận điều trị gấp 3.56 lần so với người không tiểu đường.\nMẹo trình diễn: khớp lại mô hình với các mức đảo ngược để cho thấy OR đảo thành 1/3.56."},

    # 14. Missing-data audit (code slide)
    {"type": "code", "title": "Trình diễn: Kiểm tra dữ liệu khuyết cuối cùng",
     "code": "colSums(is.na(analysis_data)) |>\n  sort(decreasing = TRUE) |>\n  head(12)",
     "output": "adherence        411\nbp_controlled    411\nbmi               18\nsbp_mmhg          12\nage                9",
     "note": "adherence và bp_controlled là NA theo thiết kế đối với bệnh nhân chưa điều trị.",
     "notes": "Điểm mấu chốt: kiểm tra tình trạng khuyết theo từng cột và phân biệt NA có tính cấu trúc với các vấn đề dữ liệu.\nNgộ nhận: mọi NA đều xấu - adherence không được xác định với người không điều trị, nên NA của nó là điều mong đợi.\nDiễn giải lâm sàng: chỉ bệnh nhân đang điều trị mới có thể có trạng thái adherence hoặc kiểm soát BP.\nHỏi: có nên quy nạp adherence cho bệnh nhân chưa điều trị không? Mong đợi: không - nó khuyết một cách cấu trúc, không phải chưa biết.\nMẹo trình diễn: lập bảng chéo tình trạng khuyết của adherence với treatment_uptake để cho thấy dạng khuyết theo-thiết-kế."},

    # 15. Saving the clean data
    {"type": "content", "title": "Lưu dữ liệu sạch: bản giao ước",
     "blocks": [
         {"header": "Lưu một lần, dùng lại cả tuần",
          "lines": [
              "saveRDS giữ nguyên các kiểu factor và mức của chúng.",
              "write_csv cho một bản sao lưu con người đọc được.",
              "Các Ngày 3, 4 và 5 đều bắt đầu từ một tệp này."]},
         {"header": "Các lệnh",
          "lines": [
              "saveRDS(analysis_data, \"Data/analysis_data.rds\")",
              "write_csv(analysis_data, \"Data/analysis_data.csv\")"]},
         {"callout": "tip", "header": "Nạp lại về sau",
          "lines": ["analysis_data <- readRDS(\"Data/analysis_data.rds\")"]},
     ],
     "notes": "Điểm mấu chốt: tệp .rds đã lưu là nguồn chân lý duy nhất cho phần còn lại của khóa học.\nNgộ nhận: CSV giữ được mọi thứ - nó làm mất các mức factor và thứ tự, nên .rds mới là tệp phân tích.\nDiễn giải lâm sàng: một bộ dữ liệu sạch cố định làm cho mọi kết quả về sau có thể tái lập và kiểm toán được.\nHỏi: vì sao ưu tiên .rds hơn .csv cho phân tích? Mong đợi: nó khôi phục các factor và các mức có thứ tự một cách chính xác, không cần làm sạch lại.\nMẹo trình diễn: lưu, xóa không gian làm việc, rồi readRDS để chứng minh các factor còn nguyên."},

    # 16. Common mistakes / debugging
    {"type": "content", "title": "Lỗi thường gặp và gỡ lỗi",
     "blocks": [
         {"header": "Hãy để ý những điều này",
          "lines": [
              "Quên na= nên 999 lọt vào như một số thật.",
              "Sai thứ tự mức factor làm đảo mọi tỷ số chênh.",
              "Để NA rơi qua case_when xuống nhầm nhóm."]},
         {"callout": "mistake", "header": "Lan truyền NA",
          "lines": ["Bất kỳ phép số học nào với NA đều trả về NA; kiểm tra is.na trước khi tính."]},
         {"callout": "tip", "header": "Thói quen gỡ lỗi",
          "lines": ["Sau mỗi bước hãy chạy summary() hoặc table(..., useNA = \"ifany\")."]},
     ],
     "notes": "Điểm mấu chốt: hầu hết lỗi làm sạch đều âm thầm; hãy tạo thói quen xem xét sau mỗi bước.\nNgộ nhận: không có thông báo lỗi nghĩa là bước đó đã chạy đúng - kết quả sai thường chạy mà không phàn nàn.\nDiễn giải lâm sàng: một kết cục bị mã hoá sai một cách âm thầm có thể thay đổi toàn bộ kết luận nghiên cứu.\nHỏi: bạn sẽ bắt một đối số na= bị quên như thế nào? Mong đợi: một giá trị max phi lý trong summary(), ví dụ một SBP bằng 999.\nMẹo trình diễn: kích hoạt từng lỗi trực tiếp, rồi cho thấy công cụ chẩn đoán bắt được nó."},

    # 17. Exercise
    {"type": "bullets", "title": "Bài thực hành Ngày 2: Làm sạch bộ dữ liệu mô phỏng",
     "intro": "Làm việc trong Practicals/day2_exercise.R và mô phỏng lại quy trình hôm nay.",
     "items": [
         "Nhập tệp CSV thô với các mã báo hiệu na= đúng.",
         "Loại bỏ bản ghi trùng bằng distinct(); xác nhận 1500 hàng.",
         "Mã hoá lại sex thành Female/Male; chuẩn hóa các biến nhị phân Yes/No.",
         "Áp dụng các khoảng hợp lý; đặt các giá trị bất khả thành NA.",
         "Tính lại BMI; tạo bmi_cat và bp_category.",
         "Phân tích enroll_date; đặt các factor và mức tham chiếu.",
         "Chạy kiểm tra dữ liệu khuyết cuối cùng và giải thích từng NA.",
         "Lưu kết quả vào Data/analysis_data.rds."],
     "notes": "Điểm mấu chốt: bài thực hành tái lập toàn bộ bản giao ước để mỗi học viên kết thúc với một tệp sạch giống hệt nhau.\nNgộ nhận: bỏ qua một bước cũng không sao nếu các con số 'trông ổn' - các ngày sau sẽ không nạp được một tệp sai kiểu.\nDiễn giải lâm sàng: trạng thái kết thúc mong đợi là bộ dữ liệu đã được kiểm định dùng cho mọi phân tích về sau.\nHỏi: làm sao bạn biết tệp của mình đúng? Mong đợi: 1500 hàng, các factor sạch, và bản kiểm tra khớp với số đếm của phần trình diễn.\nMẹo trình diễn: cho họ readRDS tệp của chính mình và glimpse() nó để tự kiểm tra so với của bạn."},

    # 18. Recap / bridge
    {"type": "content", "title": "Ôn tập và bắc cầu sang Ngày 3",
     "blocks": [
         {"header": "Hôm nay ta đạt được gì",
          "lines": [
              "Đã nhập, khử trùng lặp và chuẩn hóa dữ liệu thô.",
              "Đã kiểm định các giá trị, tạo biến dẫn xuất, phân tích ngày tháng.",
              "Đã đặt các factor và lưu analysis_data.rds."]},
         {"header": "Ngày mai: Ngày 3",
          "lines": [
              "Khám phá và mô tả dữ liệu sạch.",
              "Bảng tóm tắt, phân phối và các đồ thị đầu tiên.",
              "Ta bắt đầu từ analysis_data.rds - không làm sạch lại."]},
         {"callout": "note", "header": "Ghi nhớ",
          "lines": ["Dữ liệu sạch tác động rõ ràng - mọi thứ ở hạ nguồn đều dựa trên hôm nay."]},
     ],
     "notes": "Điểm mấu chốt: bộ dữ liệu sạch, đã lưu là nhịp cầu bước vào phân tích mô tả ở Ngày 3.\nNgộ nhận: làm sạch đã xong mãi mãi - hãy quay lại nó nếu các đồ thị Ngày 3 làm lộ ra các bất thường mới.\nDiễn giải lâm sàng: mô tả đáng tin cậy đòi hỏi dữ liệu đã kiểm định mà ta đã xây hôm nay.\nHỏi: điều đầu tiên bạn làm vào Ngày 3 là gì? Mong đợi: readRDS tệp phân tích và glimpse nó, không phải nhập lại tệp CSV thô.\nMẹo trình diễn: mở phần đầu tập lệnh của ngày mai để cho thấy nó bắt đầu bằng readRDS."},

]
