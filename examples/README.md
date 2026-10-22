# Ví dụ

Tất cả ví dụ đều có bản `.drawio` thường và có màu (chỉ khác màu), ảnh PNG/SVG và tài liệu giải thích. Chuẩn tham chiếu: [OMG BPMN 2.0.2](https://www.omg.org/spec/BPMN/2.0.2/PDF) — trích theo tên, không đính kèm.

## Ví dụ tự đặt

| Ví dụ | Nội dung |
|---|---|
| [Mượn sách liên thư viện](bpmn/muon-sach-lien-thu-vien/README.md) | Ba pool, event-based gateway, Link, boundary timer ngắt/không ngắt, nhãn tiếng Việt dài |
| [Đặt trước thiết bị dùng chung](bpmn/dat-truoc-thiet-bi/README.md) | Ví dụ nhỏ do `create_demo.py` sinh: hai pool, hai lane, một XOR |
| [Kiểm tra và thẩm định hồ sơ](bpmn/ho-so-hai-lane/README.md) | Một biểu đồ, hai lane, hai quyết định do task tạo trước gateway |
| [Mười mẫu nâng cao](bpmn/10-mau-nang-cao/README.md) | XOR/AND/Inclusive, event race, boundary, event subprocess, transaction/compensation, multi-instance, terminate |

## Lời giải bài tập học phần

Lời giải tham khảo cho đề của học phần Phân tích nghiệp vụ phần mềm. Đề gốc chỉ được trích tên, không đính kèm. Không phải đáp án chính thức và chưa được giảng viên xác nhận; tên, mã sinh viên và bài nộp đã được lược bỏ. Đề 03 có ba lời giải độc lập để so sánh cách mô hình hóa.

| Ví dụ | Nội dung |
|---|---|
| [Đề 01 — Quy trình mua sắm thiết bị nội bộ](bpmn/hoc-phan/de-01-mua-sam-thiet-bi/README.md) | Collaboration ba lane + nhà cung cấp black box, AND, timer 48 giờ |
| [Đề 03 — Bảo hành thiết bị điện tử (bản Claude)](bpmn/hoc-phan/de-03-bao-hanh-thiet-bi/ban-claude/README.md) | Một trong ba lời giải độc lập của cùng đề |
| [Đề 03 — Bảo hành thiết bị điện tử (bản GPT)](bpmn/hoc-phan/de-03-bao-hanh-thiet-bi/ban-gpt/README.md) | Một trong ba lời giải độc lập của cùng đề |
| [Đề 03 — Bảo hành thiết bị điện tử (bản Gemini)](bpmn/hoc-phan/de-03-bao-hanh-thiet-bi/ban-gemini/README.md) | Một trong ba lời giải độc lập của cùng đề; có ảnh phóng to từng cụm |
| [Thực hành — Ứng dụng gọi đồ ăn](bpmn/hoc-phan/thuc-hanh-goi-do-an/README.md) | Ba trang: tổng thể, tìm tài xế/hết hạn/hoàn tiền, chuẩn bị và giao món |
