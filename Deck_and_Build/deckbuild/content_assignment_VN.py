# -*- coding: utf-8 -*-
"""Final assignment, marking rubric, resources, and closing."""

SLIDES_ASSIGN = [
    {"type": "divider", "title": "Bài tập lớn Cuối khóa",
     "plan_title": "Tổng quan",
     "agenda": ["Một bài phân tích độc lập, làm tại nhà",
                "Một tuần để hoàn thành",
                "Sử dụng cùng bộ dữ liệu nghiên cứu",
                "Chấm trên thang 100%"],
     "notes": ("Giới thiệu bài đánh giá tổng kết.\n"
               "Điểm giảng dạy chính: bài này củng cố toàn bộ năm ngày thành một phân tích độc lập.\n"
               "Diễn giải lâm sàng: nó phản ánh việc viết phần phân tích cho một bài báo thực tế.\n"
               "Câu hỏi cho học viên: nên dành bao nhiêu thời gian? Dự kiến: một vài buổi tập trung trải trong tuần.\n"
               "Mẹo demo: khuyến khích bắt đầu từ script làm sạch đã lưu ở Buổi 2.")},

    {"type": "content", "title": "Bài tập lớn Cuối khóa - Cần Làm Gì",
     "blocks": [
        {"header": "Nhiệm vụ", "lines": [
            "Làm việc độc lập, phân tích bộ dữ liệu nghiên cứu và xác định các yếu tố quyết định việc tiếp nhận điều trị."]},
        {"header": "Bài nộp của bạn phải", "lines": [
            "Nhập dữ liệu thô và làm sạch/kiểm định nó.",
            "Tạo thống kê mô tả và một Bảng 1 sẵn sàng công bố.",
            "Tạo ít nhất hai hình chất lượng công bố.",
            "Thực hiện các kiểm định thống kê phù hợp.",
            "Khớp các mô hình hồi quy logistic đơn biến và đa biến.",
            "Diễn giải kết quả và viết một mục Kết quả ngắn.",
            "Có khả năng tái lập hoàn toàn (một script duy nhất chạy từ đầu đến cuối)."], "bullets": True},
     ],
     "notes": ("Nêu rõ chính xác cần nộp những gì.\n"
               "Điểm giảng dạy chính: khả năng tái lập được chấm điểm - script phải chạy được trên một máy sạch.\n"
               "Lỗi phổ biến: chỉ nộp kết quả mà không có script, hoặc script với đường dẫn tuyệt đối cứng.\n"
               "Diễn giải lâm sàng: mục Kết quả nên đọc như một bài nộp tạp chí.\n"
               "Câu hỏi cho học viên: điều gì khiến một script có khả năng tái lập? Dự kiến: đường dẫn tương đối, các lệnh library(), set.seed, không có bước thủ công.\n"
               "Mẹo demo: chỉ họ tới bản nháp kết quả Buổi 5 như một mẫu.")},

    {"type": "content", "title": "Bài tập lớn Cuối khóa - Sản phẩm & Nộp bài",
     "blocks": [
        {"header": "Nộp", "lines": [
            "1. Một script R (.R) có chú thích, hoặc một tệp R Markdown/Quarto.",
            "2. Bảng 1 và các hình đã xuất.",
            "3. Một mục Kết quả một trang (khoảng 250-400 từ)."]},
        {"header": "Định dạng", "lines": [
            "Dùng một RStudio Project với đường dẫn tương đối.",
            "Đặt tên tệp rõ ràng: Surname_Phase1_Assignment.R"]},
        {"callout": "warning", "header": "Liêm chính học thuật",
         "lines": ["Làm việc độc lập. Bạn có thể dùng các script và ghi chú của khóa học, nhưng phần phân tích và viết phải là của riêng bạn."]},
     ],
     "notes": ("Làm rõ cơ chế nộp bài.\n"
               "Điểm giảng dạy chính: code rõ ràng, có chú thích là một phần của điểm số, không phải chuyện phụ.\n"
               "Lỗi phổ biến: hình lưu ở độ phân giải màn hình - yêu cầu 300 dpi qua ggsave.\n"
               "Diễn giải lâm sàng: một bài nộp gọn gàng phản ánh một nhà phân tích gọn gàng.\n"
               "Câu hỏi cho học viên: script R hay Quarto? Dự kiến: cái nào cũng được - Quarto dễ đạt điểm khả năng tái lập.\n"
               "Mẹo demo: cho xem cấu trúc thư mục bạn kỳ vọng.")},

    {"type": "table", "title": "Bảng Chấm điểm (trên thang 100%)",
     "headers": ["Thành phần", "Được đánh giá điều gì", "Điểm"],
     "rows": [
        ["Nhập & làm sạch dữ liệu", "Nhập đúng, mã khuyết, kiểm định, mã hóa lại", "20"],
        ["Thống kê mô tả", "Tóm tắt phù hợp và một Bảng 1 chính xác", "15"],
        ["Hình", "Hai hình rõ ràng, gán nhãn đúng, chất lượng công bố", "10"],
        ["Kiểm định thống kê", "Chọn đúng kiểm định và áp dụng chính xác", "15"],
        ["Mô hình hồi quy", "Mô hình logistic đơn biến & đa biến vững chắc", "20"],
        ["Diễn giải & Kết quả", "OR/KTC chính xác và văn phong lâm sàng rõ ràng", "15"],
        ["Khả năng tái lập & chất lượng code", "Chạy từ đầu đến cuối; sạch, có chú thích, đường dẫn tương đối", "5"]],
     "caption": "Tổng = 100%. Một hướng dẫn chấm điểm chi tiết được cung cấp cho giảng viên.",
     "notes": ("Làm cho việc chấm điểm minh bạch.\n"
               "Điểm giảng dạy chính: làm sạch và hồi quy chiếm trọng số cao nhất (mỗi phần 20) - hãy dành thời gian cho chúng.\n"
               "Diễn giải lâm sàng: diễn giải được khen thưởng một cách rõ ràng, không chỉ tính toán.\n"
               "Lỗi phổ biến: code hoàn hảo, diễn giải sai - bạn mất 15 điểm diễn giải.\n"
               "Câu hỏi cho học viên: bạn sẽ tập trung nỗ lực ở đâu? Dự kiến: làm sạch + mô hình hóa - chính xác.\n"
               "Mẹo demo: hướng dẫn chấm điểm đầy đủ với tiêu chí từng điểm nằm trong gói tài liệu giảng viên.")},

    {"type": "two_column", "title": "Hướng dẫn Chấm điểm - Điều gì Đạt Điểm Tối đa",
     "left": {"header": "Bài nộp xuất sắc", "lines": [
        "Xử lý mọi sự lộn xộn (bản trùng, giá trị canh gác, giá trị bất khả thi).",
        "Bảng 1 phân tầng theo tiếp nhận điều trị với các kiểm định hợp lý.",
        "Tỷ số chênh hiệu chỉnh (aOR) kèm khoảng tin cậy 95% (KTC 95%) và mức tham chiếu đúng.",
        "Đoạn văn Kết quả khớp với con số và được đóng khung lâm sàng.",
        "Một script chạy trơn tru từ dữ liệu thô đến kết quả."], "bullets": True},
     "right": {"header": "Những chỗ thường mất điểm", "lines": [
        "Để nguyên 999 / -99 như số thực.",
        "Phân tích cả 1,500 thay vì chỉ bệnh nhân đã được chẩn đoán.",
        "Báo cáo log-odds thay vì tỷ số chênh (OR).",
        "Diễn giải một kết quả không có ý nghĩa thống kê là 'không có tác động'.",
        "Đường dẫn tuyệt đối hỏng trên máy tính khác."], "bullets": True},
     "notes": ("Cho học viên một hình dung cụ thể về bài xuất sắc so với bài yếu.\n"
               "Điểm giảng dạy chính: đa số điểm bị mất do các lỗi làm sạch và diễn giải có thể tránh được.\n"
               "Diễn giải lâm sàng: 'không có ý nghĩa thống kê' nghĩa là 'chưa đủ bằng chứng', không phải 'không có tác động'.\n"
               "Lỗi phổ biến: quên giới hạn ở htn_diagnosed == Yes cho phân tích tiếp nhận điều trị.\n"
               "Câu hỏi cho học viên: vì sao chỉ phân tích bệnh nhân đã được chẩn đoán? Dự kiến: tiếp nhận điều trị chỉ được xác định sau khi đã chẩn đoán.\n"
               "Mẹo demo: phát slide này như một bảng tự kiểm trước khi nộp.")},

    {"type": "content", "title": "Tài nguyên & Đọc thêm",
     "blocks": [
        {"header": "Trong gói tài liệu khóa học", "lines": [
            "Bảng tra cứu lệnh R và hướng dẫn cài đặt gói.",
            "Tất cả script demo và lời giải mẫu.",
            "Bộ dữ liệu, từ điển dữ liệu và bộ slide này."]},
        {"header": "Để đi xa hơn", "lines": [
            "R for Data Science (Wickham & Grolemund) - miễn phí trực tuyến.",
            "Regression Modeling Strategies (Harrell).",
            "Các trang tài liệu gtsummary và ggplot2."]},
        {"callout": "tip", "header": "Tiếp tục luyện tập",
         "lines": ["Chạy lại các script của tuần trên dữ liệu của chính bạn - đó là nơi kỹ năng trở nên bền vững."]},
     ],
     "notes": ("Chỉ ra mọi thứ họ có thể mang về và nơi để phát triển tiếp.\n"
               "Điểm giảng dạy chính: bảng tra cứu trả lời 80% câu hỏi hằng ngày.\n"
               "Diễn giải lâm sàng: áp dụng R vào dữ liệu của CHÍNH họ là bài kiểm tra thực sự của việc học.\n"
               "Câu hỏi cho học viên: sau khóa học bạn sẽ phân tích gì đầu tiên? Dự kiến: một cuộc kiểm toán hoặc một dự án đang dang dở.\n"
               "Mẹo demo: nhắc đến Giai đoạn II (phân tích sống còn, mô hình hỗn hợp) như bước tiếp theo.")},

    {"type": "divider", "title": "Cảm ơn & Hỏi đáp",
     "plan_title": "Giữ liên lạc",
     "agenda": ["Bạn giờ đã có thể nhập, làm sạch, phân tích và báo cáo dữ liệu lâm sàng bằng R",
                "Luyện tập trên các bộ dữ liệu của riêng bạn",
                "Giai đoạn II: phân tích sống còn, mô hình hỗn hợp và dự báo",
                "Liên hệ: Neudata  -  #ClearDataClearImpact"],
     "notes": ("Kết thúc ấm áp và mở lời cho thảo luận.\n"
               "Điểm giảng dạy chính: chúc mừng rằng mọi người đã đi từ số không đến một phân tích hoàn chỉnh trong năm ngày.\n"
               "Diễn giải lâm sàng: khuyến khích họ đưa phân tích có khả năng tái lập vào nhóm của mình.\n"
               "Câu hỏi cho học viên: điều bạn thu nhận lớn nhất là gì? Dự kiến: khác nhau - khẳng định mỗi ý.\n"
               "Mẹo demo: thu thập phản hồi và chia sẻ thông tin liên hệ để theo dõi tiếp.")},

    {"type": "closing", "notes": ("COPYRIGHT / CLOSING SLIDE.\n"
               "Bản quyền chuẩn của Neudata. Cảm ơn học viên và đơn vị đăng cai.")},
]
