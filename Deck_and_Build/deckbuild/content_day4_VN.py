# -*- coding: utf-8 -*-
"""Day 4 slides - Common Medical Statistical Tests: choosing and running the right test."""

SLIDES_DAY4 = [

    {"type": "divider", "title": "Ngày 4: Các Kiểm Định Thống Kê Y Học Thường Gặp",
     "agenda": ["Kiến thức cơ bản về kiểm định giả thuyết",
                "So sánh hai nhóm: kiểm định t và kiểm định Wilcoxon",
                "Nhiều hơn hai nhóm: ANOVA",
                "Liên quan giữa các biến phân loại: kiểm định chi bình phương và Fisher",
                "Tương quan và chọn kiểm định phù hợp"],
     "notes": "Chào mừng đến với Ngày 4. Hôm qua chúng ta MÔ TẢ dữ liệu; hôm nay chúng ta ĐẶT CÂU HỎI về dữ liệu bằng các kiểm định thống kê.\nÝ chính: mỗi kiểm định trả lời một câu hỏi - hai nhóm có khác nhau không? hai biến có liên quan không?\nTrấn an các bác sĩ lâm sàng: R tự động lo phần tính toán; nhiệm vụ của bạn là chọn đúng kiểm định và diễn giải nó.\nCầu nối: hôm nay là các kiểm định; tuần sau (Ngày 5) chúng ta giới thiệu hồi quy để mô hình hóa nhiều yếu tố dự báo cùng lúc.\nMẹo demo: mở sẵn script day4_demo.R và chạy trực tiếp từng khối khi đến mỗi slide."},

    {"type": "bullets", "title": "Những Gì Chúng Ta Sẽ Học Hôm Nay",
     "intro": "Chọn và chạy các kiểm định thường dùng trong nghiên cứu lâm sàng.",
     "items": ["Kiểm định giả thuyết: giả thuyết không, giả thuyết đối, giá trị p và ý nghĩa thống kê",
               "Kiểm tra tính chuẩn trước khi chọn kiểm định",
               "So sánh hai nhóm: kiểm định t và kiểm định Wilcoxon",
               "So sánh nhiều hơn hai nhóm: ANOVA và Tukey",
               "Liên quan giữa các biến phân loại: kiểm định chi bình phương và kiểm định chính xác Fisher",
               "Tương quan: Pearson và Spearman",
               "Khung ra quyết định: khớp câu hỏi với kiểm định"],
     "notes": "Lộ trình cho cả ngày: các kiểm định thống kê y học thường gặp, và cách chọn giữa chúng.\nNhấn mạnh mạch logic: loại biến kết cục + số nhóm + bắt cặp vs độc lập -> đúng kiểm định.\nCầu nối: các kiểm định này so sánh từng cặp nhóm; Ngày 5 giới thiệu hồi quy để nghiên cứu nhiều yếu tố dự báo cùng nhau.\nCâu hỏi cho học viên: điều gì quyết định kiểm định nào chúng ta dùng? Trả lời: loại biến kết cục và số nhóm cần so sánh."},

    {"type": "content", "title": "Câu Hỏi Phân Tích",
     "blocks": [
        {"header": "Câu hỏi nghiên cứu của chúng ta", "lines": [
            "Bệnh nhân đang điều trị có khác với những người không điều trị không?",
            "Những đặc điểm nào (tuổi, giới, bệnh đồng mắc) khác nhau giữa hai nhóm?"]},
        {"header": "Định nghĩa quần thể phân tích TRƯỚC TIÊN", "lines": [
            "Tiếp nhận điều trị chỉ có ý nghĩa với những người đã được chẩn đoán.",
            "Chúng ta giới hạn ở htn_diagnosed == \"Yes\" (khoảng 1,089 bệnh nhân).",
            "Khoảng 47% bệnh nhân được chẩn đoán đã tiếp nhận điều trị."]},
        {"callout": "mistake", "header": "Đừng phân tích cả 1,500 người",
         "lines": ["Bao gồm cả người chưa chẩn đoán, những người có biến kết cục không xác định, sẽ làm sai lệch mọi kết quả."]},
     ],
     "notes": "Điểm dạy chính: định nghĩa quần thể phân tích một cách rõ ràng và một lần duy nhất, trước mọi kiểm định.\nLogic lâm sàng: bạn không thể tiếp nhận điều trị cho một bệnh mà bạn chưa được chẩn đoán.\nSai lầm thường gặp: chạy phân tích trên toàn bộ 1,500 người - nó trộn lẫn các biến kết cục không xác định và làm sai lệch ước lượng.\nMẹo demo: hiển thị dx <- filter(analysis_data, htn_diagnosed == \"Yes\") rồi nrow(dx) và table(dx$treatment_uptake)."},

    {"type": "content", "title": "Kiểm Định Giả Thuyết Bằng Ngôn Ngữ Đơn Giản",
     "blocks": [
        {"header": "Hai giả thuyết", "lines": [
            "Giả thuyết không (H0): KHÔNG có khác biệt / KHÔNG có liên quan.",
            "Giả thuyết đối (H1): CÓ khác biệt / liên quan."]},
        {"header": "Giá trị p thực sự là gì", "lines": [
            "Xác suất quan sát được dữ liệu cực đoan như thế này NẾU giả thuyết không đúng.",
            "Giá trị p nhỏ (< 0.05) là bằng chứng CHỐNG LẠI giả thuyết không.",
            "Nó KHÔNG PHẢI là xác suất giả thuyết không là đúng."]},
        {"callout": "interpretation", "header": "Mức ý nghĩa",
         "lines": ["Chúng ta ấn định trước alpha = 0.05 làm ngưỡng để gọi một kết quả là có ý nghĩa thống kê."]},
     ],
     "notes": "Điểm dạy chính: giá trị p trả lời 'dữ liệu của tôi bất ngờ đến mức nào nếu không có gì xảy ra?'\nHiểu sai thường gặp: p KHÔNG PHẢI là khả năng giả thuyết không đúng, và (1 - p) KHÔNG PHẢI là khả năng H1 đúng.\nDiễn giải lâm sàng: ý nghĩa thống kê là về bằng chứng chống lại H0, không phải về tầm quan trọng hay độ lớn hiệu ứng.\nCâu hỏi cho học viên: p = 0.04 có chứng minh hiệu ứng là thật không? Trả lời: không - đó chỉ là một mảnh bằng chứng, cần xét cùng độ lớn hiệu ứng và bối cảnh."},

    {"type": "content", "title": "p < 0.05 Không Phải Toàn Bộ Câu Chuyện",
     "blocks": [
        {"header": "Ý nghĩa thống kê vs ý nghĩa lâm sàng", "lines": [
            "Một khác biệt nhỏ, vô nghĩa vẫn có thể 'có ý nghĩa thống kê' trong mẫu lớn.",
            "Một khác biệt lớn, quan trọng vẫn có thể 'không có ý nghĩa thống kê' nếu mẫu nhỏ.",
            "Luôn báo cáo độ lớn hiệu ứng và khoảng tin cậy của nó, không chỉ giá trị p."]},
        {"callout": "warning", "header": "Cẩn thận với việc sùng bái giá trị p",
         "lines": ["Đừng chạy theo p < 0.05 hay coi 0.049 và 0.051 là hai điều trái ngược.",
                   "Một khoảng tin cậy cho bạn biết cả độ lớn LẪN độ bất định."]},
     ],
     "notes": "Điểm dạy chính: giá trị p là cần thiết nhưng chưa đủ - nó bỏ qua độ lớn hiệu ứng.\nSai lầm thường gặp: phân đôi tại 0.05 như thể 0.049 và 0.051 khác nhau về bản chất.\nDiễn giải lâm sàng: một KTC thể hiện cả độ lớn lẫn độ chính xác; hãy ưu tiên nó hơn một giá trị p trần trụi.\nCâu hỏi cho học viên: cái nào hữu ích hơn, 'p = 0.03' hay 'OR 3.6 (KTC 95% 1.5 đến 9.6)'? Trả lời: cái thứ hai - nó cho thấy hướng, độ lớn và độ bất định."},

    {"type": "two_column", "title": "Biến Có Chuẩn Không? Nhìn Trước, Rồi Kiểm Định",
     "left": {"header": "Nhìn trước (luôn luôn)", "lines": [
        "Histogram cho thấy hình dạng của phân phối.",
        "Biểu đồ Q-Q: các điểm nằm trên đường thẳng nghĩa là gần chuẩn.",
        "Các điểm cong đi ở hai đầu nghĩa là lệch hoặc đuôi nặng."], "bullets": True},
     "right": {"header": "Rồi mới kiểm định", "lines": [
        "Kiểm định Shapiro-Wilk: H0 là dữ liệu CÓ phân phối chuẩn.",
        "Giá trị p nhỏ (< 0.05) nghĩa là chúng ta bác bỏ tính chuẩn.",
        "Đối xứng và hình chuông nghĩa là kiểm định tham số là ổn.",
        "Rõ ràng bị lệch nghĩa là dùng kiểm định phi tham số."], "bullets": True},
     "notes": "Điểm dạy chính: vẽ đồ thị trước khi kiểm định - mắt bắt được những gì một giá trị p đơn lẻ che giấu.\nSai lầm thường gặp: chỉ tin vào Shapiro-Wilk trong mẫu lớn; với ~1,089 dòng nó gắn cờ những sai lệch không đáng kể là có ý nghĩa thống kê.\nDiễn giải lâm sàng: một biểu đồ Q-Q gần thẳng và một histogram đối xứng quan trọng hơn giá trị p Shapiro ở đây.\nMẹo demo: chạy hist(dx$age), qqnorm/qqline, rồi shapiro.test(dx$age) và đối chiếu các kết luận."},

    {"type": "content", "title": "Shapiro-Wilk: Dùng Thận Trọng Trong Mẫu Lớn",
     "blocks": [
        {"header": "Tại sao kiểm định gây hiểu lầm ở đây", "lines": [
            "Shapiro-Wilk càng mạnh khi cỡ mẫu càng lớn.",
            "Trong ~1,089 dòng nó phát hiện những sai lệch nhỏ, không liên quan về mặt lâm sàng.",
            "Nó gần như luôn trả về p < 0.05 - kể cả với dữ liệu dùng được."]},
        {"callout": "tip", "header": "Quy tắc kinh nghiệm cho khóa học này",
         "lines": ["Mẫu lớn + histogram đối xứng + Q-Q thẳng nghĩa là kiểm định tham số là ổn.",
                   "Hãy để đồ thị, chứ không phải giá trị p Shapiro, dẫn dắt quyết định."]},
     ],
     "notes": "Điểm dạy chính: sức mạnh thống kê là con dao hai lưỡi - với n lớn kiểm định tính chuẩn gắn cờ quá mức.\nSai lầm thường gặp: chuyển sang kiểm định phi tham số chỉ vì Shapiro trả về p < 0.05.\nDiễn giải lâm sàng: đánh giá tính chuẩn qua hình dạng và độ thẳng của Q-Q; dành các kiểm định phi tham số cho trường hợp lệch rõ hoặc n nhỏ.\nCâu hỏi cho học viên: Shapiro nói p < 0.001 nhưng Q-Q thẳng - bạn làm gì? Trả lời: tin vào đồ thị và dùng kiểm định tham số."},

    {"type": "two_column", "title": "So Sánh Hai Nhóm: Biến Kết Cục Liên Tục",
     "left": {"header": "Kiểm định t (tham số)", "lines": [
        "So sánh TRUNG BÌNH của hai nhóm.",
        "Kiểm định t Welch là lựa chọn mặc định an toàn (phương sai không bằng nhau).",
        "Dùng khi dữ liệu gần đối xứng.",
        "Công thức: age ~ treatment_uptake."], "bullets": True},
     "right": {"header": "Wilcoxon (phi tham số)", "lines": [
        "So sánh HẠNG, không phải trung bình.",
        "Bền vững với giá trị ngoại lai và độ lệch.",
        "Dùng khi dữ liệu rõ ràng không chuẩn.",
        "Báo cáo trung vị thay vì trung bình."], "bullets": True},
     "notes": "Điểm dạy chính: câu hỏi vẫn như nhau (hai nhóm có khác nhau không?); kiểm định phụ thuộc vào hình dạng dữ liệu.\nVí dụ diễn giải lâm sàng: tuổi trung bình cao hơn ở nhóm đang điều trị, phù hợp với việc bệnh nhân lớn tuổi tiếp nhận điều trị nhiều hơn.\nSai lầm thường gặp: mặc định dùng kiểm định t Student cổ điển - Welch an toàn hơn vì nó không giả định phương sai bằng nhau.\nMẹo demo: chạy cả t.test và wilcox.test trên age ~ treatment_uptake; lưu ý chúng thường nhất quán với dữ liệu lớn, đối xứng."},

    {"type": "code", "title": "Demo: Kiểm Định t Cho Tuổi Theo Tiếp Nhận Điều Trị",
     "intro": "Tuổi trung bình có khác nhau giữa những người đã tiếp nhận điều trị và những người không?",
     "code": "t.test(age ~ treatment_uptake, data = dx)",
     "output": "Welch Two Sample t-test\nt = -8.9, df = 1011, p-value < 2.2e-16\n95 percent CI: -6.4 to -4.1\nmean in No  mean in Yes\n   50.1        55.3",
     "note": "Bệnh nhân đang điều trị lớn hơn khoảng 5 tuổi trung bình; KTC không chứa 0, nên p < 0.05.",
     "notes": "Điểm dạy chính: đọc ba thứ - hai trung bình nhóm, KTC 95% cho khác biệt của chúng, và giá trị p.\nDiễn giải lâm sàng: chênh lệch tuổi trung bình ~5 năm, với KTC không chứa số không, ủng hộ việc bệnh nhân lớn tuổi tiếp nhận nhiều hơn.\nSai lầm thường gặp: chỉ báo cáo giá trị p và bỏ qua các trung bình và KTC cho khác biệt.\nMẹo demo: chạy wilcox.test(age ~ treatment_uptake, data = dx) song song và cho thấy chúng nhất quán."},

    {"type": "content", "title": "Khi Dữ Liệu Không Chuẩn: Kiểm Định Phi Tham Số",
     "blocks": [
        {"header": "Các lựa chọn thay thế dựa trên hạng", "lines": [
            "Kiểm định tổng hạng Wilcoxon (Mann-Whitney): so sánh hai nhóm mà không giả định tính chuẩn.",
            "Kiểm định chính xác Fisher: cho bảng 2x2 khi tần số kỳ vọng nhỏ (< 5).",
            "Chúng dùng hạng và tần số chính xác thay vì trung bình và đường cong chuẩn."]},
        {"header": "Cách chạy chúng", "lines": [
            "wilcox.test(sbp_mmhg ~ treatment_uptake, data = dx)",
            "fisher.test(table(dx$treatment_uptake, dx$diabetes))"]},
        {"callout": "tip", "header": "Quy tắc kinh nghiệm",
         "lines": ["Dữ liệu lệch hoặc nhỏ -> dùng kiểm định phi tham số; đó là lựa chọn an toàn khi còn nghi ngờ."]}],
     "notes": ("Điểm dạy chính: khi các giả định về tính chuẩn hay cỡ mẫu của kiểm định t hoặc "
               "chi bình phương không thỏa, kiểm định Wilcoxon dựa trên hạng và kiểm định chính xác Fisher cho câu trả lời hợp lệ.\n"
               "Diễn giải lâm sàng: các giá trị xét nghiệm và chi phí thường bị lệch - kiểm định Wilcoxon trên "
               "trung vị thường là lựa chọn trung thực.\n"
               "Sai lầm thường gặp: ép dùng kiểm định t trên dữ liệu lệch rõ, hoặc dùng chi bình phương khi một ô "
               "có tần số kỳ vọng dưới 5.\n"
               "Câu hỏi cho học viên: khi nào bạn ưu tiên kiểm định chính xác Fisher hơn chi bình phương? Trả lời mong đợi: "
               "mẫu nhỏ hoặc bảng thưa với tần số kỳ vọng thấp.\n"
               "Mẹo demo: cho thấy Wilcoxon và kiểm định t nhất quán ở đây (mẫu lớn, gần đối xứng), "
               "rồi dựng một bảng nhỏ để làm động lực cho kiểm định chính xác Fisher.")},

    {"type": "content", "title": "So Sánh Nhiều Hơn Hai Nhóm: ANOVA",
     "blocks": [
        {"header": "Tại sao không dùng nhiều kiểm định t?", "lines": [
            "Mỗi kiểm định t từng cặp mang theo nguy cơ dương tính giả 5% riêng của nó.",
            "Thực hiện nhiều lần làm tăng tỷ lệ sai số tổng thể.",
            "ANOVA kiểm định tất cả các nhóm cùng lúc với một giá trị p trung thực."]},
        {"header": "Sau một ANOVA có ý nghĩa thống kê", "lines": [
            "Giá trị p nhỏ cho bạn biết MỘT SỐ nhóm khác nhau, chứ không phải nhóm nào.",
            "TukeyHSD so sánh mọi cặp và hiệu chỉnh cho tính đa so sánh.",
            "Ví dụ: tuổi có khác nhau giữa các trình độ học vấn không?"]},
        {"callout": "note", "header": "Nếu các giả định không thỏa",
         "lines": ["Dùng kruskal.test() phi tham số thay cho aov()."]},
     ],
     "notes": "Điểm dạy chính: ANOVA là kiểm định t đa nhóm; nó kiểm soát sai số toàn cục mà một chồng kiểm định t sẽ không kiểm soát được.\nSai lầm thường gặp: chạy mọi kiểm định t từng cặp - làm tăng dương tính giả. Chạy ANOVA, rồi hậu kiểm chỉ khi nó có ý nghĩa thống kê.\nDiễn giải lâm sàng: một bảng Tukey cho thấy những cặp trình độ học vấn cụ thể nào khác nhau về tuổi trung bình.\nCâu hỏi cho học viên: p của ANOVA có ý nghĩa thống kê - có phải tất cả các nhóm đều khác nhau không? Trả lời: không, ít nhất một cặp khác nhau; Tukey cho biết cặp nào."},

    {"type": "content", "title": "Liên Quan Giữa Hai Biến Phân Loại",
     "blocks": [
        {"header": "Kiểm định chi bình phương về tính độc lập", "lines": [
            "Câu hỏi: tiếp nhận điều trị có liên quan với đái tháo đường không?",
            "Dựng một bảng dự phòng, rồi kiểm định nó.",
            "H0: hai biến độc lập (không có liên quan)."]},
        {"header": "Khi tần số kỳ vọng nhỏ", "lines": [
            "Chi bình phương cần mọi tần số kỳ vọng của ô >= 5.",
            "Kiểm tra với chisq.test(tab)$expected.",
            "Nếu có ô quá nhỏ, dùng kiểm định chính xác Fisher thay thế."]},
        {"callout": "interpretation", "header": "Bảng cho biết hướng",
         "lines": ["Kiểm định cho một giá trị p; bảng cho thấy AI có tỷ lệ tiếp nhận cao hơn."]},
     ],
     "notes": "Điểm dạy chính: chi bình phương hỏi liệu hai biến phân loại có biến động cùng nhau không; bảng cho thấy hướng.\nSai lầm thường gặp: áp dụng chi bình phương khi tần số kỳ vọng dưới 5 - chuyển sang kiểm định chính xác Fisher trong trường hợp đó.\nDiễn giải lâm sàng: tỷ lệ người đái tháo đường đang điều trị cao hơn gợi ý một liên quan dương, được định lượng sau bằng OR.\nMẹo demo: hiển thị table(dx$treatment_uptake, dx$diabetes), rồi chisq.test, $expected của nó, và fisher.test."},

    {"type": "two_column", "title": "Tương Quan: Hai Con Số Có Biến Động Cùng Nhau Không?",
     "left": {"header": "Pearson", "lines": [
        "Đo lường liên quan TUYẾN TÍNH.",
        "Giả định dữ liệu gần chuẩn.",
        "Nhạy với giá trị ngoại lai.",
        "Ví dụ: sbp_mmhg vs bmi."], "bullets": True},
     "right": {"header": "Spearman", "lines": [
        "Dựa trên HẠNG.",
        "Bền vững với giá trị ngoại lai và tính phi tuyến.",
        "Dùng khi dữ liệu bị lệch.",
        "Báo cáo một hệ số tương quan hạng."], "bullets": True},
     "notes": "Điểm dạy chính: r nằm trong khoảng -1 đến +1; ~0-0.3 yếu, 0.3-0.7 trung bình, 0.7-1.0 mạnh; dấu cho biết hướng.\nSai lầm thường gặp: nhầm một giá trị p có ý nghĩa thống kê với một mối liên hệ mạnh - trong mẫu lớn một r nhỏ (0.08) vẫn có ý nghĩa thống kê nhưng không đáng kể.\nDiễn giải lâm sàng: luôn báo cáo và đánh giá r, không chỉ giá trị p; nhớ rằng tương quan không phải là nhân quả.\nCâu hỏi cho học viên: r = 0.1, p < 0.001 - mối liên hệ mạnh? Trả lời: không, phát hiện được về mặt thống kê nhưng không đáng kể về mặt lâm sàng."},

    {"type": "code", "title": "Demo: Tương Quan Giữa SBP và BMI",
     "intro": "Huyết áp tâm thu và BMI có biến động cùng nhau không?",
     "code": "cor.test(dx$sbp_mmhg, dx$bmi, method = \"pearson\")",
     "output": "Pearson's product-moment correlation\nt = 6.1, df = 1087, p-value = 1.4e-09\n95 percent CI: 0.12 to 0.24\ncor = 0.18",
     "note": "r = 0.18 là một mối liên hệ dương yếu: rất có ý nghĩa thống kê, nhưng khiêm tốn về mặt lâm sàng.",
     "notes": "Điểm dạy chính: giá trị p xác nhận mối liên hệ là thật; r cho bạn biết nó yếu.\nDiễn giải lâm sàng: SBP và BMI tăng cùng nhau một chút, nhưng BMI giải thích rất ít biến thiên của SBP.\nSai lầm thường gặp: giật tít 'tương quan có ý nghĩa thống kê' trong khi che giấu rằng r chỉ là 0.18.\nMẹo demo: chạy lại với method = \"spearman\" và lưu ý hệ số tương quan hạng tương tự, xác nhận tính bền vững."},

    {"type": "table", "title": "Chọn Kiểm Định Phù Hợp",
     "headers": ["Biến kết cục", "Yếu tố dự báo / biến thứ 2", "Kiểm định"],
     "rows": [["Liên tục", "Hai nhóm", "Kiểm định t (Wilcoxon nếu lệch)"],
              ["Liên tục", "Nhiều hơn hai nhóm", "ANOVA (Kruskal-Wallis nếu lệch)"],
              ["Phân loại", "Phân loại", "Chi bình phương (Fisher nếu thưa)"],
              ["Liên tục", "Liên tục", "Tương quan (Pearson / Spearman)"],
              ["Nhị phân", "Một hoặc nhiều yếu tố dự báo", "Hồi quy logistic - Ngày 5"]],
     "caption": "Khớp CÂU HỎI và các loại dữ liệu với kiểm định; một biến kết cục nhị phân với các yếu tố dự báo dẫn tới hồi quy (Ngày 5).",
     "notes": "Điểm dạy chính: kiểm định được quyết định bởi loại biến kết cục và loại yếu tố dự báo - không phải bởi thói quen.\nMẹo demo: giữ bảng này trên màn hình như một công cụ hỗ trợ quyết định cho bài tập.\nDiễn giải lâm sàng: khi biến kết cục là nhị phân và chúng ta muốn xét nhiều yếu tố dự báo cùng lúc, chúng ta chuyển sang hồi quy logistic - đó là Ngày 5.\nCâu hỏi cho học viên: biến kết cục là Có/Không và chúng ta muốn hiệu chỉnh cho nhiều yếu tố - dùng phương pháp nào? Trả lời: hồi quy logistic, buổi tiếp theo."},

    {"type": "content", "title": "Bài Tập Ngày 4: Chọn và Chạy Kiểm Định Phù Hợp",
     "blocks": [
        {"header": "Nhiệm vụ của bạn", "lines": [
            "So sánh tuổi giữa các nhóm tiếp nhận điều trị bằng kiểm định t.",
            "Kiểm định liên quan giữa giới và tiếp nhận điều trị (chi bình phương).",
            "Kiểm định tương quan giữa SBP và BMI (Pearson hoặc Spearman).",
            "Với mỗi kiểm định, nêu câu hỏi, kiểm định, và kết quả bằng ngôn ngữ đơn giản."]},
        {"header": "Kết quả mong đợi", "lines": [
            "Một kết quả kiểm định cho mỗi câu hỏi, mỗi cái có một giá trị p.",
            "Với kiểm định t và tương quan, ước lượng và KTC 95% của nó.",
            "Một câu diễn giải mỗi kết quả về mặt lâm sàng."]},
        {"callout": "tip", "header": "Hãy để loại dữ liệu chọn kiểm định",
         "lines": ["Kiểm tra loại biến kết cục và số nhóm trước khi bạn chọn kiểm định."]},
     ],
     "notes": "Điểm dạy chính: sản phẩm bàn giao là lập luận - câu hỏi -> loại biến -> kiểm định -> diễn giải.\nSai lầm thường gặp: dùng kiểm định t theo thói quen mà không kiểm tra loại biến kết cục hay phân phối.\nDiễn giải lâm sàng: kỳ vọng tương quan SBP-BMI yếu nhưng có ý nghĩa thống kê; liên quan giới-tiếp nhận có thể khiêm tốn.\nMẹo demo: đi vòng quanh và kiểm tra rằng học viên báo cáo ước lượng và KTC, không chỉ giá trị p."},

    {"type": "content", "title": "Tóm Tắt và Cầu Nối Sang Ngày 5",
     "blocks": [
        {"header": "Những gì bạn giờ đã làm được", "lines": [
            "Khớp một câu hỏi với kiểm định đúng bằng các loại dữ liệu.",
            "Chạy và diễn giải kiểm định t, Wilcoxon, ANOVA, chi bình phương và tương quan.",
            "Đọc một giá trị p cùng với độ lớn hiệu ứng và khoảng tin cậy của nó.",
            "Phân biệt ý nghĩa thống kê với tầm quan trọng lâm sàng."]},
        {"header": "Ngày 5 đi xa hơn", "lines": [
            "Giới thiệu về hồi quy: tuyến tính (con số) và logistic (Có/Không).",
            "Tỷ số chênh, hiệu chỉnh và nhiễu.",
            "Biến kết quả mô hình thành phần Kết quả, một cách có thể tái lập."]},
        {"callout": "note", "header": "Mang theo",
         "lines": ["Giữ bảng khung ra quyết định của bạn - buổi tiếp theo chúng ta mô hình hóa nhiều yếu tố dự báo cùng lúc."]},
     ],
     "notes": "Điểm dạy chính: hôm nay là về chọn và diễn giải từng kiểm định đơn lẻ; Ngày 5 giới thiệu hồi quy để xử lý nhiều yếu tố dự báo cùng nhau.\nDiễn giải lâm sàng: các kiểm định so sánh hai thứ mỗi lần; hồi quy hiệu chỉnh cho nhiều yếu tố đồng thời.\nSai lầm thường gặp: dừng lại ở giá trị p; buổi tiếp theo chúng ta tập trung vào độ lớn hiệu ứng và báo cáo rõ ràng.\nCâu hỏi cho học viên: nếu chúng ta muốn nghiên cứu nhiều yếu tố dự báo của một biến kết cục Có/Không cùng lúc thì sao? Trả lời: hồi quy logistic - đó là Ngày 5."},
]
