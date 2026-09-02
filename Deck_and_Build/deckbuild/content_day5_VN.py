# -*- coding: utf-8 -*-
"""Day 5 (capstone) slides: Introduction to regression (linear + logistic),
model building, publication-ready reporting, and reproducibility."""

SLIDES_DAY5 = [

    {"type": "divider", "title": "Ngày 5: Giới Thiệu Hồi Quy & Diễn Giải Kết Quả",
     "agenda": ["Hồi quy tuyến tính: mô hình hóa một biến kết cục liên tục",
                "Hồi quy logistic: tỷ số chênh cho một biến kết cục Có/Không",
                "Hiệu chỉnh cho nhiều yếu tố, và nhiễu",
                "Bảng, hình và phần Kết quả sẵn sàng cho xuất bản",
                "Khả năng tái lập: script, seed và project"],
     "notes": "Chào mừng đến với ngày tổng kết.\nÝ chính: hôm nay chúng ta biến một mô hình đã khớp thành một kết quả có thể xuất bản và tái lập.\nĐiều này kết nối tất cả những gì từ Ngày 1-4: nhập, làm sạch, tóm tắt, và giờ là mô hình hóa và báo cáo.\nNói với lớp rằng mục tiêu không phải là thêm thống kê mà là phán đoán tốt hơn và báo cáo gọn gàng hơn.\nMẹo trình diễn: mở sẵn day5_demo.R trong RStudio suốt buổi."},

    {"type": "bullets", "title": "Mục Tiêu Hôm Nay",
     "intro": "Đến cuối Ngày 5 bạn sẽ có thể:",
     "items": [
        "Khớp và đọc một hồi quy tuyến tính cho một biến kết cục liên tục.",
        "Khớp một hồi quy logistic và đọc tỷ số chênh với KTC 95%.",
        "Hiểu tại sao chúng ta hiệu chỉnh cho nhiều yếu tố, và nhận diện nhiễu.",
        "Trình bày kết quả hiệu chỉnh dưới dạng một bảng rõ ràng và một biểu đồ forest.",
        "Viết một phần Kết quả ngắn gọn, trung thực từ các con số của chính bạn.",
        "Làm cho toàn bộ phân tích có thể tái lập từ đầu đến cuối."],
     "notes": "Đặt mục tiêu cụ thể, có thể kiểm chứng cho cả ngày.\nĐiểm dạy chính: các mục tiêu này khớp một-một với sản phẩm bàn giao của bài tập.\nDiễn giải lâm sàng: mỗi kỹ năng là thứ họ sẽ dùng cho nghiên cứu của chính mình, không phải lý thuyết trừu tượng.\nCâu hỏi cho học viên: cái nào cảm thấy ít quen thuộc nhất? Dùng việc giơ tay để điều chỉnh nhịp độ cho cả ngày.\nMẹo trình diễn: quay lại danh sách này lúc tổng kết và đánh dấu từng mục đã xong."},

    {"type": "content", "title": "Chúng Ta Đang Ở Đâu Trong Hành Trình",
     "blocks": [
        {"header": "Xuyên suốt tuần", "lines": [
            "Buổi 1-2: nhập và làm sạch bộ dữ liệu tăng huyết áp.",
            "Buổi 3: tóm tắt và trực quan hóa (Bảng 1, các hình).",
            "Buổi 4: các kiểm định thống kê thường gặp (kiểm định t, chi bình phương, tương quan).",
            "Buổi 5: hồi quy - mô hình hóa, diễn giải, báo cáo và tái lập."]},
        {"header": "Ví dụ xuyên suốt hôm nay", "lines": [
            "Biến kết cục: treatment_uptake ở người tăng huyết áp đã được chẩn đoán.",
            "Mẫu phân tích: 1,089 người đã chẩn đoán; 992 trường hợp đầy đủ được mô hình hóa."]},
        {"callout": "note", "header": "Một bộ dữ liệu, từ đầu đến cuối",
         "lines": ["Mọi kết quả hôm nay đều đến từ cùng nghiên cứu bạn đã làm sạch trước đó."]},
     ],
     "notes": "Định hướng cho khán giả: đây là một quy trình mạch lạc, không phải các mẹo rời rạc.\nHiểu lầm thường gặp: rằng mô hình hóa là phần khó. Phán đoán (chọn biến nào, báo cáo thế nào) mới khó hơn.\nDiễn giải lâm sàng: chỉ bệnh nhân đã chẩn đoán mới có thể tiếp nhận điều trị, nên chúng ta giới hạn ở họ.\nCâu hỏi cho học viên: tại sao chỉ mô hình hóa 1,089 người đã chẩn đoán mà không phải cả 1,500? Trả lời mong đợi: người không có chẩn đoán không thể có quyết định tiếp nhận điều trị; bao gồm họ sẽ làm sai lệch ước lượng."},

    {"type": "content", "title": "Hồi Quy Tuyến Tính: Mô Hình Hóa Một Con Số",
     "blocks": [
        {"header": "Khi biến kết cục là một con số", "lines": [
            "Hồi quy tuyến tính mô hình hóa một biến kết cục LIÊN TỤC, chẳng hạn huyết áp.",
            "Biến kết cục = một phần hệ thống (các yếu tố dự báo) + biến thiên không giải thích được.",
            "Nó ước lượng biến kết cục thay đổi bao nhiêu cho mỗi đơn vị của một yếu tố dự báo."]},
        {"header": "Đọc kết quả", "lines": [
            "Hệ số (độ dốc) là thay đổi của biến kết cục cho mỗi mức tăng một đơn vị.",
            "Mỗi hệ số đi kèm một KTC 95% và một giá trị p.",
            "Thêm các yếu tố dự báo cho ta hiệu ứng ĐÃ HIỆU CHỈNH của mỗi cái, giữ những cái khác không đổi."]},
        {"callout": "interpretation", "header": "Câu hỏi lâm sàng",
         "lines": ["Huyết áp tâm thu có liên quan với tuổi không - và nó có còn đúng sau khi hiệu chỉnh cho giới và BMI?"]},
     ],
     "notes": "Điểm dạy chính: hồi quy tuyến tính dành cho biến kết cục liên tục; độ dốc là thay đổi trên mỗi đơn vị.\nDiễn giải lâm sàng: hệ số chặn hiếm khi có ý nghĩa; các độ dốc mới là thứ chúng ta báo cáo.\nSai lầm thường gặp: dùng hồi quy tuyến tính cho một biến kết cục Có/Không - điều đó cần hồi quy logistic (tiếp theo).\nCâu hỏi cho học viên: biến kết cục là huyết áp tâm thu (một con số) và yếu tố dự báo là tuổi - dùng mô hình nào? Trả lời: hồi quy tuyến tính."},

    {"type": "code", "title": "Demo: Hồi Quy Tuyến Tính Của SBP Theo Tuổi",
     "intro": "Huyết áp tâm thu có tăng theo tuổi không, khi hiệu chỉnh cho giới và BMI?",
     "code": "m1 <- lm(sbp_mmhg ~ age, data = analysis_data)\nsummary(m1)\n\n# adjust for sex and BMI\nm2 <- lm(sbp_mmhg ~ age + sex + bmi,\n         data = analysis_data)\ntidy(m2, conf.int = TRUE)",
     "output": "term        estimate conf.low conf.high p.value\n(Intercept)   87.31    81.01    93.61   <0.001\nage            0.26     0.19     0.33   <0.001\nsexMale        0.33    -1.57     2.22    0.74\nbmi            1.45     1.26     1.64   <0.001",
     "note": "Mỗi năm tuổi thêm khoảng 0.26 mmHg vào SBP và mỗi đơn vị BMI khoảng 1.45 mmHg; giới không có ý nghĩa thống kê.",
     "notes": "Điểm dạy chính: đọc mỗi độ dốc như một thay đổi đã hiệu chỉnh trên mỗi đơn vị, cùng với KTC 95% của nó.\nDiễn giải lâm sàng: tuổi và BMI liên quan độc lập với SBP; giới thì không (KTC vượt qua 0, p = 0.74).\nSai lầm thường gặp: báo cáo hệ số chặn như thể nó có ý nghĩa lâm sàng.\nMẹo demo: chạy summary(m1) trước (thô), rồi m2 đã hiệu chỉnh, và lưu ý độ dốc của tuổi gần như không đổi."},

    {"type": "content", "title": "Tại Sao Dùng Hồi Quy Logistic?",
     "blocks": [
        {"header": "Biến kết cục là nhị phân", "lines": [
            "Tiếp nhận điều trị là Có/Không - không phải một con số, nên không phải hồi quy tuyến tính.",
            "Hồi quy logistic mô hình hóa SỐ CHÊNH của biến kết cục 'Có'.",
            "Nó xử lý một yếu tố dự báo hoặc nhiều yếu tố cùng lúc."]},
        {"header": "Số chênh và tỷ số chênh", "lines": [
            "Số chênh = xác suất Có chia cho xác suất Không.",
            "Một tỷ số chênh (OR) so sánh số chênh giữa hai nhóm.",
            "OR là con số duy nhất mà các bác sĩ lâm sàng đọc từ mô hình."]},
        {"callout": "tip", "header": "Tại sao số chênh, không phải xác suất",
         "lines": ["Số chênh cho phép nhân các hiệu ứng một cách gọn gàng và cho một OR không đổi theo nhóm."]},
     ],
     "notes": "Điểm dạy chính: một biến kết cục nhị phân cần hồi quy logistic, mô hình hóa số chênh thay vì một trung bình.\nDiễn giải lâm sàng: tỷ số chênh là sản phẩm bàn giao - nó đi thẳng vào bản thảo và biểu đồ forest.\nSai lầm thường gặp: cố khớp một mô hình tuyến tính cho một biến kết cục Có/Không.\nCâu hỏi cho học viên: số chênh là bao nhiêu nếu 3 trong 4 bệnh nhân tiếp nhận điều trị? Trả lời: 3 trên 1, tức số chênh = 3."},

    {"type": "content", "title": "Đọc Một Tỷ Số Chênh",
     "blocks": [
        {"header": "Hướng của hiệu ứng", "lines": [
            "OR = 1: yếu tố dự báo không có hiệu ứng lên số chênh tiếp nhận.",
            "OR > 1: số chênh tiếp nhận cao hơn (một yếu tố thúc đẩy dương).",
            "OR < 1: số chênh tiếp nhận thấp hơn (một yếu tố bảo vệ / âm)."]},
        {"header": "Độ chính xác và ý nghĩa thống kê", "lines": [
            "KTC 95% cho thấy khoảng hợp lý cho OR thật.",
            "Nếu KTC không chứa 1, hiệu ứng có ý nghĩa thống kê.",
            "Một KTC rộng nghĩa là một ước lượng thiếu chính xác, không chắc chắn."]},
        {"callout": "interpretation", "header": "Cách diễn đạt ví dụ",
         "lines": ["Người đái tháo đường có số chênh tiếp nhận gấp 3.6 lần (aOR 3.56, KTC 95% 1.46 đến 9.61)."]},
     ],
     "notes": "Điểm dạy chính: đọc một OR theo hướng (so với 1) cộng với ý nghĩa thống kê (KTC có vượt qua 1 không?).\nSai lầm thường gặp: đọc hệ số thô (log số chênh) như thể nó là OR - luôn lấy lũy thừa (exponentiate) trước.\nDiễn giải lâm sàng: 'OR không chứa 1' là tương đương hồi quy của p < 0.05, nhưng có kèm độ lớn.\nCâu hỏi cho học viên: OR 0.7 với KTC 0.5 đến 0.9 - nghĩa là gì? Trả lời: một hiệu ứng bảo vệ thật, số chênh thấp hơn 30%."},

    {"type": "code", "title": "Demo: Hồi Quy Logistic Đơn Biến (Đái Tháo Đường)",
     "intro": "Đái tháo đường có làm tăng số chênh tiếp nhận điều trị không?",
     "code": "m_diab <- glm(treatment_uptake ~ diabetes,\n              data = dx, family = binomial)\nexp(coef(m_diab))      # odds ratio\nexp(confint(m_diab))   # 95% CI",
     "output": "(Intercept)   diabetesYes\n      0.74          2.85\n            2.5 %   97.5 %\ndiabetesYes  2.01     4.07",
     "note": "OR chưa hiệu chỉnh ~2.85: người đái tháo đường có số chênh tiếp nhận cao gần gấp ba; KTC không chứa 1.",
     "notes": "Điểm dạy chính: family = binomial cho glm biết biến kết cục là 0/1; exp() biến log số chênh thành một OR có thể diễn giải.\nSai lầm thường gặp: báo cáo exp(coef) nhưng quên mức tham chiếu - ở đây diabetesYes được so sánh với No.\nDiễn giải lâm sàng: OR chưa hiệu chỉnh sẽ co lại khi chúng ta hiệu chỉnh cho các yếu tố nhiễu như tuổi.\nMẹo demo: hiển thị summary(m_diab) trước để họ thấy log số chênh, rồi exp() để biến nó thành một OR thân thiện với bác sĩ lâm sàng."},

    {"type": "content", "title": "Một Yếu Tố Dự Báo Liên Tục: Tuổi",
     "blocks": [
        {"header": "OR trên mỗi một đơn vị", "lines": [
            "glm(treatment_uptake ~ age) cho OR trên mỗi MỘT năm tuổi thêm.",
            "OR đó gần bằng 1 vì một năm là một bước rất nhỏ.",
            "Ở đây khoảng 1.03 mỗi năm - dễ bị bỏ qua."]},
        {"header": "Đổi thang đo sang một đơn vị có ý nghĩa", "lines": [
            "OR trên mỗi 10 năm = OR trên 1 năm nâng lên lũy thừa 10.",
            "exp(coef(m_age)[\"age\"] * 10) cho OR trên mỗi thập niên.",
            "1.03 mỗi năm trở thành khoảng 1.34 mỗi thập niên."]},
        {"callout": "tip", "header": "Truyền đạt bằng đơn vị lâm sàng",
         "lines": ["Mỗi thập niên dễ hiểu hơn nhiều so với mỗi năm đối với khán giả lâm sàng."]},
     ],
     "notes": "Điểm dạy chính: với một yếu tố dự báo liên tục, OR là trên mỗi thay đổi một đơn vị - chọn một đơn vị mà người ta quan tâm.\nSai lầm thường gặp: bỏ qua tuổi như không quan trọng vì OR ~1.03 trông tầm thường trên mỗi năm đơn lẻ.\nDiễn giải lâm sàng: cách diễn đạt theo thập niên (khoảng 1.34) cho thấy tuổi là một yếu tố thúc đẩy đáng kể của tiếp nhận.\nMẹo demo: chạy exp(coef(m_age)['age'] * 10) trực tiếp để đổi từ mỗi năm sang mỗi thập niên."},

    {"type": "content", "title": "Xây Dựng Mô Hình: Kiến Thức Lâm Sàng Trước Tiên",
     "blocks": [
        {"header": "Chọn yếu tố dự báo trước khi nhìn giá trị p", "lines": [
            "Tính hợp lý về sinh học hoặc lâm sàng (đái tháo đường thúc đẩy các lần khám).",
            "Các yếu tố nhiễu đã biết từ y văn (tuổi, giới, học vấn).",
            "Các yếu tố quyết định đã nêu của nghiên cứu (khoảng cách, kiến thức)."]},
        {"header": "Rồi khớp MỘT mô hình đã định trước", "lines": [
            "Quyết định danh sách biến trước, khớp một lần, báo cáo nó.",
            "Đây là cách tiếp cận trung thực, có thể lặp lại cho một nghiên cứu về yếu tố quyết định."]},
        {"callout": "mistake", "header": "Đãi cát tìm vàng dữ liệu",
         "lines": ["Thử nhiều mô hình và chỉ báo cáo những mô hình có ý nghĩa thống kê sẽ làm tăng dương tính giả."]},
     ],
     "notes": "Slide triết lý cốt lõi: lựa chọn dựa trên động cơ lâm sàng thắng tự động hóa mù quáng.\nĐiểm dạy chính: một mô hình đã định trước có thể bảo vệ trước người phản biện và có thể tái lập.\nSai lầm thường gặp: để máy tính chọn biến, rồi kể một câu chuyện lâm sàng quanh bất cứ cái gì còn sót lại.\nDiễn giải lâm sàng: trong một nghiên cứu giải thích, chúng ta giữ các yếu tố nhiễu đã biết ngay cả khi không có ý nghĩa thống kê.\nCâu hỏi cho học viên: có nên bỏ một biến chỉ vì p > 0.05? Trả lời mong đợi: không, không nếu nó là một yếu tố nhiễu đã biết; bỏ nó có thể đưa lại nhiễu."},

    {"type": "two_column", "title": "Nhiễu: Một Ví Dụ Lâm Sàng",
     "left": {"header": "Nhiễu là gì", "lines": [
        "Một biến thứ ba làm méo mối liên hệ thô giữa phơi nhiễm và biến kết cục.",
        "Ví dụ: cư dân thành thị trẻ hơn và có bảo hiểm tốt hơn.",
        "Những yếu tố đó cũng làm tăng tiếp nhận - nên nơi cư trú thô trông quá mạnh.",
        "Hiệu chỉnh cho chúng sẽ tách được hiệu ứng thật của nơi cư trú."], "bullets": True},
     "right": {"header": "Cách chúng ta phát hiện nó", "lines": [
        "So sánh OR thô với OR hiệu chỉnh của nơi cư trú.",
        "Nếu ước lượng dịch chuyển đáng kể (quy tắc kinh nghiệm >10%), có nhiễu.",
        "Luôn báo cáo và diễn giải tỷ số chênh ĐÃ HIỆU CHỈNH.",
        "OR thành thị đã hiệu chỉnh trong mô hình của chúng ta là 1.87 (1.41-2.49)."], "bullets": True},
     "notes": "Nhiễu là khái niệm mô hình hóa quan trọng nhất đối với bác sĩ lâm sàng.\nĐiểm dạy chính: hiệu chỉnh là cách các nghiên cứu quan sát xấp xỉ một so sánh công bằng.\nSai lầm thường gặp: báo cáo và diễn giải OR thô.\nDiễn giải lâm sàng: hiệu ứng thành thị thô một phần được giải thích bởi tuổi và bảo hiểm; sau khi hiệu chỉnh, một lợi thế thành thị còn lại thực sự khoảng 1.87 vẫn tồn tại.\nMẹo trình diễn: trong slide tiếp theo chúng ta cho thấy các con số thô vs hiệu chỉnh từ R."},

    {"type": "code", "title": "Demo: OR Thô vs Hiệu Chỉnh Cho Nơi Cư Trú",
     "intro": "Khớp một mô hình thô, rồi so sánh với mô hình đầy đủ.",
     "code": "crude <- glm(treatment_uptake ~ residence,\n             data = dx, family = binomial)\nfull <- glm(treatment_uptake ~ age + sex + education +\n             residence + diabetes + family_history_htn +\n             health_insurance + knowledge_score +\n             distance_to_facility_km,\n             data = dx, family = binomial)\nexp(coef(crude))[\"residenceUrban\"]\nexp(coef(full))[\"residenceUrban\"]",
     "output": "residenceUrban\n     2.34\nresidenceUrban\n     1.87",
     "note": "OR co lại từ 2.34 (thô) xuống 1.87 (hiệu chỉnh): tuổi và bảo hiểm đã gây nhiễu cho nó.",
     "notes": "Demo trực tiếp từ day5_demo.R, phần 2-3.\nĐiểm dạy chính: exp() biến log số chênh thành một tỷ số chênh.\nSai lầm thường gặp: quên rằng glm cần family = binomial cho một mô hình logistic.\nDiễn giải lâm sàng: mức giảm >10% xác nhận có nhiễu; con số 1.87 đã hiệu chỉnh là cái chúng ta báo cáo.\nCâu hỏi cho học viên: tại sao hiệu ứng thành thị co lại? Trả lời mong đợi: vì cư dân thành thị khác nhau về tuổi và bảo hiểm, những yếu tố này làm tăng tiếp nhận một cách độc lập."},

    {"type": "code", "title": "Demo: Mô Hình Cuối Cùng và Các OR Đã Được Sắp Gọn",
     "intro": "Khớp một lần, rồi biến các hệ số thành tỷ số chênh với KTC.",
     "code": "model_final <- full\nlibrary(broom)\nor_table <- tidy(model_final,\n                 exponentiate = TRUE,\n                 conf.int = TRUE)\nprint(or_table, n = Inf)",
     "output": "term            estimate conf.low conf.high\ndiabetesYes        3.56     1.46      9.61\nhealth_insuranceYes 2.05    1.54      2.74\nresidenceUrban     1.87     1.41      2.49\nage                1.03     1.02      1.04",
     "note": "exponentiate = TRUE cho các OR; conf.int = TRUE thêm KTC 95% - chính xác bảng mà người đọc của bạn cần.",
     "notes": "Demo trực tiếp từ day5_demo.R, phần 7.\nĐiểm dạy chính: broom::tidy() biến một đối tượng mô hình thành một data frame sạch, sẵn sàng để vẽ hoặc xuất.\nSai lầm thường gặp: chép tay các con số từ summary() vào một bảng Word - dễ sai và không thể tái lập.\nDiễn giải lâm sàng: mọi KTC được hiển thị đều không chứa 1, nên tất cả đều có ý nghĩa thống kê; đái tháo đường có OR lớn nhất nhưng KTC rộng nhất.\nCâu hỏi cho học viên: tại sao KTC của đái tháo đường lại rộng như vậy? Trả lời mong đợi: người đái tháo đường là một phân nhóm nhỏ hơn, nên ước lượng kém chính xác hơn."},

    {"type": "table", "title": "Mô Hình Đa Biến Cuối Cùng: Các OR Đã Hiệu Chỉnh",
     "headers": ["Yếu tố dự báo", "aOR", "KTC 95%", "p"],
     "rows": [["Tuổi (mỗi năm)", "1.03", "1.02-1.04", "<0.001"],
              ["Giới: Nam (so với Nữ)", "0.74", "0.56-0.97", "0.031"],
              ["Học vấn (xu hướng tuyến tính)", "1.96", "1.39-2.77", "<0.001"],
              ["Nơi cư trú: Thành thị (so với Nông thôn)", "1.87", "1.41-2.49", "<0.001"],
              ["Đái tháo đường: Có", "3.56", "1.46-9.61", "0.007"],
              ["Bảo hiểm y tế: Có", "2.05", "1.54-2.74", "<0.001"],
              ["Khoảng cách tới cơ sở (mỗi km)", "0.98", "0.96-1.01", "0.128"]],
     "caption": "Hồi quy logistic; n = 992 trường hợp đầy đủ; AUC = 0.71. Tiền sử gia đình aOR 1.91 (1.44-2.54); kiến thức 1.10 (1.06-1.14) mỗi điểm.",
     "notes": "Đây là các con số chuẩn từ key_findings.md - trích dẫn chúng chính xác.\nĐiểm dạy chính: đây là bảng kết quả chính của bản thảo.\nSai lầm thường gặp: bỏ sót KTC hoặc n; người phản biện luôn hỏi.\nDiễn giải lâm sàng: khoảng cách theo hướng bảo vệ-chống-lại-tiếp nhận như kỳ vọng (OR 0.98) nhưng không có ý nghĩa thống kê - báo cáo đúng như vậy, đừng gọi nó là không có hiệu ứng.\nCâu hỏi cho học viên: yếu tố dự báo nào quan trọng nhất? Trả lời mong đợi: đái tháo đường có OR lớn nhất (3.56), nhưng thận trọng - KTC của nó rộng nhất, nên độ chính xác thấp hơn.\nMẹo trình diễn: tiền sử gia đình và kiến thức được đưa vào chú thích để giữ bảng trong giới hạn số dòng."},

    {"type": "image", "title": "Trực Quan Hóa Các OR Đã Hiệu Chỉnh",
     "image": "forest_plot_or.png", "aspect": 0.78,
     "side_header": "Cách đọc nó",
     "side_notes": ["Mỗi điểm là một tỷ số chênh đã hiệu chỉnh.",
                    "Các râu là khoảng tin cậy 95%.",
                    "Đường đứt nét tại 1 = không có hiệu ứng.",
                    "Bên phải của 1 tăng tiếp nhận; bên trái giảm nó.",
                    "Đái tháo đường nằm xa nhất về bên phải - hiệu ứng lớn nhất.",
                    "Khoảng cách vượt qua 1 - không có ý nghĩa thống kê."],
     "notes": "Điểm dạy chính: một biểu đồ forest truyền đạt toàn bộ mô hình trong một cái nhìn.\nTrục x ở thang log nên các KTC trông đối xứng quanh mỗi điểm.\nSai lầm thường gặp: đặt trục OR ở thang tuyến tính, làm bẹp các OR nhỏ.\nDiễn giải lâm sàng: bất kỳ râu KTC nào vượt qua đường đứt nét tại 1 đều không có ý nghĩa thống kê - ở đây chỉ có khoảng cách.\nCâu hỏi cho học viên: tại sao khoảng cách trông khác các yếu tố khác? Trả lời mong đợi: khoảng của nó nằm vắt qua 1, nên chúng ta không thể loại trừ việc không có hiệu ứng."},

    {"type": "code", "title": "Demo: Bảng và Biểu Đồ Forest Sẵn Sàng Xuất Bản",
     "intro": "Dựng một bảng kiểu tạp chí, rồi lưu hình.",
     "code": "library(gtsummary)\ntbl <- tbl_regression(model_final,\n                      exponentiate = TRUE) |>\n  bold_p()\ntbl\n# save the forest plot built from or_table\nggsave(\"Resources/forest_plot_or.png\",\n       plot = forest, width = 8, height = 5, dpi = 300)",
     "note": "tbl_regression đọc mô hình trực tiếp - không chép tay - và ggsave xuất hình cho bản thảo.",
     "notes": "Demo trực tiếp từ day5_demo.R, phần 8-9.\nĐiểm dạy chính: bảng và hình nên được sinh ra từ code, không bao giờ gõ lại.\nSai lầm thường gặp: sửa các con số bằng tay trong Word, làm hỏng khả năng tái lập và gây ra lỗi sao chép.\nDiễn giải lâm sàng: file PNG đã lưu là chính xác hình trên slide trước.\nMẹo trình diễn: hiển thị as_gt(tbl) |> gtsave(\"Resources/regression_table.html\") để xuất bảng nữa; đề cập một phương án dự phòng write_csv nếu không có gtsummary."},

    {"type": "content", "title": "Xuất Kết Quả Cho Bản Thảo",
     "blocks": [
        {"header": "Lưu bảng", "lines": [
            "gtsummary: as_gt(tbl) rồi gtsave() ghi HTML, PNG hoặc Word.",
            "Phương án dự phòng: write_csv(or_table, \"Resources/regression_table.csv\")."]},
        {"header": "Lưu hình", "lines": [
            "ggsave() ghi biểu đồ forest ở kích thước và độ phân giải cố định.",
            "Dùng dpi = 300 cho các hình chất lượng in trong tạp chí."]},
        {"header": "Tại sao xuất từ code", "lines": [
            "Báo cáo có thể được dựng lại từ dữ liệu thô mà không cần bước thủ công nào.",
            "Không sao chép nghĩa là không có lỗi sao chép."]},
        {"callout": "tip", "header": "Giữ một thư mục Resources/",
         "lines": ["Gửi mọi bảng và hình vào đó để các kết quả nằm cùng một chỗ."]},
     ],
     "notes": "Điểm dạy chính: kết quả là sản phẩm của code, không phải file dựng bằng tay.\nSai lầm thường gặp: chụp màn hình một đồ thị từ trình xem RStudio thay vì dùng ggsave - độ phân giải thấp và không tái lập được.\nDiễn giải lâm sàng: một người phản biện yêu cầu chỉnh sửa sẽ nhận được nó bằng cách sửa một dòng và chạy lại.\nCâu hỏi cho học viên: dpi bao nhiêu cho một hình in? Trả lời mong đợi: 300.\nMẹo trình diễn: chạy ggsave và gtsave trực tiếp, rồi mở thư mục Resources/ để cho thấy các file xuất hiện."},

    {"type": "two_column", "title": "Từ Tỷ Số Chênh Đến Câu Văn",
     "left": {"header": "Các con số", "lines": [
        "Đái tháo đường: aOR 3.56 (1.46-9.61).",
        "Bảo hiểm: aOR 2.05 (1.54-2.74).",
        "Thành thị: aOR 1.87 (1.41-2.49).",
        "Xu hướng học vấn: aOR 1.96 (1.39-2.77).",
        "Giới nam: aOR 0.74 (0.56-0.97).",
        "Khoảng cách: aOR 0.98 (0.96-1.01), KYN."], "bullets": True},
     "right": {"header": "Biến mỗi OR thành một câu", "lines": [
        "Nêu hướng, độ lớn, nhóm so sánh và KTC.",
        "OR>1: 'gấp X lần số chênh tiếp nhận'.",
        "OR<1: 'số chênh thấp hơn' - ở đây nam so với nữ.",
        "Liên tục: 'trên mỗi 1 đơn vị tăng'.",
        "Nêu rõ nhóm tham chiếu một cách tường minh.",
        "Báo cáo các phát hiện KYN một cách trung thực, kèm KTC."], "bullets": True},
     "notes": "Điểm dạy chính: một phần Kết quả là sự chuyển ngữ có cấu trúc, không phải bịa đặt.\nMỗi OR trở thành một mệnh đề rõ ràng: hướng, độ lớn, nhóm so sánh, độ chính xác.\nSai lầm thường gặp: viết 'X gây ra Y' từ một OR quan sát - hãy dùng 'có liên quan với'.\nDiễn giải lâm sàng: một OR 0.74 cho giới nam nghĩa là nam có số chênh thấp hơn nữ khoảng 26%.\nCâu hỏi cho học viên: làm sao diễn đạt một phát hiện không có ý nghĩa thống kê? Trả lời mong đợi: báo cáo ước lượng và KTC và nêu rằng nó không có ý nghĩa thống kê - đừng khẳng định 'không có hiệu ứng'."},

    {"type": "content", "title": "Ví Dụ Thực Hành: Một Đoạn Kết Quả",
     "blocks": [
        {"header": "Đoạn kết quả mô hình", "lines": [
            "Trong 992 người tăng huyết áp đã được chẩn đoán, tiếp nhận điều trị liên quan độc lập",
            "với đái tháo đường (aOR 3.56, KTC 95% 1.46-9.61), bảo hiểm y tế",
            "(2.05, 1.54-2.74), nơi cư trú thành thị (1.87, 1.41-2.49) và học vấn cao hơn",
            "(1.96, 1.39-2.77). Tuổi cao hơn (1.03 mỗi năm) và kiến thức nhiều hơn (1.10",
            "mỗi điểm) cũng làm tăng số chênh, trong khi nam giới có số chênh thấp hơn nữ giới",
            "(0.74, 0.56-0.97). Khoảng cách tới cơ sở không có ý nghĩa thống kê (0.98,",
            "0.96-1.01). Mô hình phân biệt ở mức chấp nhận được (AUC 0.71)."]},
        {"callout": "tip", "header": "Luôn kết thúc bằng khả năng phân biệt",
         "lines": ["Báo cáo AUC cho người đọc biết mô hình phân tách tiếp nhận với không tiếp nhận tốt đến đâu."]},
     ],
     "notes": "Đây là một câu trả lời mẫu mà lớp có thể chỉnh sửa cho bài tập.\nĐiểm dạy chính: mở đầu bằng n phân tích, liệt kê các yếu tố quyết định có ý nghĩa thống kê với OR và KTC, rồi báo cáo cái không có ý nghĩa thống kê và độ khớp tổng thể.\nSai lầm thường gặp: ngôn ngữ nhân quả ('đái tháo đường làm tăng tiếp nhận') từ một nghiên cứu cắt ngang.\nDiễn giải lâm sàng: đoạn văn phản ánh chính xác các hướng trong key_findings.md.\nCâu hỏi cho học viên: điều gì thuộc về câu đầu tiên? Trả lời mong đợi: cỡ mẫu và biến kết cục, để người đọc biết cơ sở của mọi con số theo sau."},

    {"type": "content", "title": "Khả Năng Tái Lập: Thông Điệp Tổng Kết",
     "blocks": [
        {"header": "Làm cho công việc của bạn ai cũng chạy lại được", "lines": [
            "Script hơn menu bấm chuột: code là hồ sơ vĩnh viễn.",
            "set.seed() làm cho mọi tính ngẫu nhiên (bootstrap, chia mẫu) có thể lặp lại.",
            "Dùng RStudio Projects và đường dẫn tương đối - không bao giờ C:/Users/yourname/...",
            "Lưu mọi bảng và hình vào đĩa để báo cáo dựng lại được từ code."]},
        {"header": "Ghi lại và chia sẻ môi trường của bạn", "lines": [
            "sessionInfo() ghi lại đúng phiên bản R và các gói của bạn.",
            "R Markdown / Quarto kết code, văn bản và hình thành một báo cáo."]},
        {"callout": "tip", "header": "Thực hành tốt nhất",
         "lines": ["Một cú nhấp chuột nên dựng lại toàn bộ báo cáo từ dữ liệu thô đến PDF."]},
     ],
     "notes": "Điểm dạy chính: một kết quả bạn không thể tái lập là một kết quả bạn không thể bảo vệ.\nCác phân tích bằng menu bấm chuột không để lại dấu vết; script thì có.\nSai lầm thường gặp: gán cứng một đường dẫn tuyệt đối chỉ chạy trên laptop của bạn - nó hỏng với mọi cộng tác viên.\nDiễn giải lâm sàng: khả năng tái lập là một phần của liêm chính nghiên cứu, không phải một thứ tùy chọn.\nCâu hỏi cho học viên: tại sao đặt seed nếu hồi quy logistic là tất định? Trả lời mong đợi: để toàn bộ script - bao gồm bất kỳ lấy mẫu lại hay mô phỏng nào - tái lập giống hệt từ đầu đến cuối.\nMẹo trình diễn: hiển thị cấu trúc thư mục Data/ Scripts/ Solutions/ Resources/ References/."},

    {"type": "code", "title": "Demo: Một Đoạn Mã Về Khả Năng Tái Lập",
     "intro": "Seed, đường dẫn tương đối, và một môi trường được ghi lại.",
     "code": "set.seed(2025)\nanalysis_data <- readRDS(\"Data/analysis_data.rds\")\ndx <- filter(analysis_data, htn_diagnosed == \"Yes\")\n# record the exact software environment\nwriteLines(capture.output(sessionInfo()),\n           \"References/session_info.txt\")",
     "output": "R version 4.4.1 (2024-06-14)\nattached: dplyr_1.1.4 broom_1.0.6 gtsummary_2.0\n... (full environment written to References/session_info.txt)",
     "note": "Đường dẫn tương đối cộng với một sessionInfo() đã lưu cho phép bất kỳ đồng nghiệp nào chạy lại cái này trên bất kỳ máy nào.",
     "notes": "Demo trực tiếp từ day5_demo.R, phần 0-1 và 10.\nĐiểm dạy chính: ba thói quen này - seed, đường dẫn tương đối, môi trường được ghi lại - bao phủ hầu hết các thất bại về khả năng tái lập.\nSai lầm thường gặp: làm sạch lại dữ liệu bên trong script phân tích; làm sạch nên thuộc về script riêng của nó (tách biệt trách nhiệm).\nDiễn giải lâm sàng: readRDS nạp dữ liệu đã được làm sạch, sẵn sàng phân tích.\nMẹo trình diễn: mở References/session_info.txt sau khi chạy để cho thấy những gì đã được ghi lại."},

    {"type": "content", "title": "Bài Tập Ngày 5: Hoàn Thành Phân Tích & Viết Một Phần Kết Quả",
     "blocks": [
        {"header": "Nhiệm vụ của bạn", "lines": [
            "Khớp mô hình đa biến đã định trước trên tập con đã chẩn đoán.",
            "Tạo một bảng OR đã sắp gọn (exponentiate = TRUE, conf.int = TRUE).",
            "Chạy các chẩn đoán: VIF, kiểm tra tính tuyến tính, khoảng cách Cook, AUC.",
            "Dựng một bảng gtsummary và một biểu đồ forest, và lưu cả hai vào Resources/.",
            "Viết một phần Kết quả 4-6 câu từ các OR của chính bạn."]},
        {"callout": "note", "header": "Sản phẩm bàn giao",
         "lines": ["Một script có thể tái lập cộng với một đoạn Kết quả ngắn trích dẫn các aOR, KTC 95% và AUC."]},
     ],
     "notes": "Điểm dạy chính: bài tập này tích hợp cả tuần thành một sản phẩm bàn giao.\nSai lầm thường gặp: quên giới hạn ở htn_diagnosed == 'Yes', hoặc báo cáo OR thô thay vì OR đã hiệu chỉnh.\nDiễn giải lâm sàng: bảng chấm điểm (key_findings.md) thưởng cho phương pháp và diễn giải đúng, không phải khớp đến số thập phân thứ 2.\nCâu hỏi cho học viên: đoạn Kết quả nên dài bao nhiêu? Trả lời mong đợi: gọn 4-6 câu - n và biến kết cục, các yếu tố quyết định có ý nghĩa thống kê với OR và KTC, cái không có ý nghĩa thống kê, rồi AUC.\nMẹo trình diễn: chỉ họ tới day5_demo.R như một khung sườn và đi vòng quanh trong lúc họ làm."},

    {"type": "bullets", "title": "Tổng Kết Khóa Học: Những Gì Bạn Giờ Đã Làm Được",
     "intro": "Năm ngày, một bộ dữ liệu thực, một quy trình phân tích đầy đủ.",
     "items": [
        "Nhập dữ liệu lâm sàng lộn xộn vào R và hiểu cấu trúc của nó.",
        "Làm sạch nó: sửa các giá trị bất khả thi, chuẩn hóa các danh mục, xử lý dữ liệu khuyết.",
        "Tóm tắt và trực quan hóa: Bảng 1, histogram, boxplot, biểu đồ cột.",
        "Khớp và diễn giải hồi quy logistic với các tỷ số chênh đã hiệu chỉnh.",
        "Xây dựng mô hình từ lập luận lâm sàng và kiểm tra các giả định của chúng.",
        "Tạo các bảng và hình sẵn sàng xuất bản, và một phần Kết quả.",
        "Làm việc một cách có thể tái lập với script, project, seed và báo cáo Quarto."],
     "notes": "Điểm dạy chính: chúc mừng chặng đường đã đi - họ bắt đầu mà không có nền tảng lập trình.\nTrấn an họ rằng sự thành thạo đến cùng với luyện tập trên dữ liệu của chính họ.\nDiễn giải lâm sàng: giờ họ sở hữu một quy trình có thể bảo vệ, có thể tái lập mà họ có thể mang tới các nghiên cứu của chính mình.\nCâu hỏi cho học viên: thói quen giá trị nhất cần giữ là gì? Trả lời mong đợi: làm mọi thứ trong một script để nó có thể tái lập.\nMẹo trình diễn: mời một hoặc hai học viên chia sẻ điều gì khiến họ bất ngờ nhất."},

    {"type": "content", "title": "Giai Đoạn II Có Thể Bao Gồm Những Gì",
     "blocks": [
        {"header": "Mô hình hóa sâu hơn", "lines": [
            "Nhiễu, tương tác và biến đổi hiệu ứng một cách chuyên sâu.",
            "Chẩn đoán mô hình: đa cộng tuyến, độ khớp và khả năng phân biệt (AUC).",
            "Lựa chọn biến và cách xây dựng một mô hình có trách nhiệm."]},
        {"header": "Phương pháp và kỹ năng mới", "lines": [
            "Phân tích sống còn: Kaplan-Meier và mô hình Cox cho dữ liệu thời gian-đến-biến cố.",
            "Mô hình hiệu ứng hỗn hợp: bệnh nhân được phân cụm trong các cơ sở.",
            "Dữ liệu khuyết (đa quy nạp) và báo cáo Quarto tự động."]},
        {"callout": "tip", "header": "Tiếp tục luyện tập",
         "lines": ["Mang bộ dữ liệu của chính bạn tới Giai đoạn II và phân tích nó từ đầu đến cuối."]},
     ],
     "notes": "Điểm dạy chính: mô hình logistic hôm nay là nền tảng; Giai đoạn II tổng quát hóa nó.\nDiễn giải lâm sàng: nghiên cứu 6 cơ sở của họ tự nhiên được phân cụm, điều này thúc đẩy các mô hình hỗn hợp trong Giai đoạn II.\nHiểu lầm thường gặp: rằng phân tích sống còn và hồi quy logistic không liên quan - cả hai đều là hồi quy, chỉ khác loại biến kết cục.\nCâu hỏi cho học viên: chủ đề Giai đoạn II nào phù hợp với một nghiên cứu theo dõi bệnh nhân theo thời gian? Trả lời mong đợi: phân tích sống còn, vì biến kết cục là thời gian-đến-biến cố.\nMẹo trình diễn: cảm ơn lớp học, chỉ tới References/ để đọc thêm, và kết thúc bằng #ClearDataClearImpact."},
]
