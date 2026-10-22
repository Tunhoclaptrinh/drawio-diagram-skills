# Changelog

Mỗi skill có phiên bản riêng. Tag Git theo dạng `<skill>-v<phiên bản>`, ví dụ `bpmn-drawio-v1.0.0-rc.2`.

## bpmn-drawio 1.0.0-rc.2 — 2026-10-22 (pre-release)

Bản phát hành công khai đầu tiên, dùng thử và góp ý.

- Ma trận trigger/result theo vị trí event (OMG BPMN 2.0.2, Bảng 10.84–10.93): start cấp cao, start subprocess, start event-subprocess ngắt/không ngắt, catch, throw, boundary ngắt/không ngắt, end.
- Message flow theo catch/throw; boundary phải có sequence ra; event trung gian phải có vào và ra; Link theo cặp cùng tên trong cùng cấp process; gateway phải tách hoặc gộp.
- Nhận diện Call Activity và lane native; event symbol renderer không vẽ được báo unsupported.
- Bản màu không được ẩn nét/chữ; marker phải đủ tương phản để phân biệt catch/throw.
- Kiểm tra bố cục trên số đo render: nhãn tràn hình, nhãn ra ngoài lane/pool, nhãn vắt biên, connector cắt nhãn, connector chạy chồng.
- Báo cáo ghi phiên bản và digest công cụ; `smoke_package.py` kiểm tra gói từ ZIP giải nén.
- Giấy phép Apache-2.0.
- Kiểm thử: 75 test nhanh; 28 trang dựng bằng viewer draw.io; 41 ca ký pháp mới (bản trước đúng 15, bản này đúng 41).

Giới hạn đã biết: chưa thử Windows/macOS; SVG chế độ `preserve` có id ngẫu nhiên nên hash đổi giữa các lần dựng; Choreography, Conversation, BPMN XML thực thi và tự layout chưa hỗ trợ.

## bpmn-drawio 1.0.0-rc.1

Ứng viên nội bộ, không phát hành công khai.
