# Đóng góp

Cảm ơn bạn quan tâm. Repo nhận báo lỗi, ví dụ mới, cải tiến bộ kiểm tra và skill cho loại sơ đồ khác.

## Báo lỗi

Mở issue kèm:

- file `.drawio` **tối giản** tái hiện lỗi (không gửi tài liệu nội bộ, bài thi hay dữ liệu cá nhân);
- lệnh đã chạy và báo cáo JSON (`audit_drawio.py`, `doctor.py`);
- phiên bản skill (`VERSION`), commit draw.io, phiên bản Chrome, hệ điều hành;
- kết quả mong đợi và căn cứ (mục/trang trong chuẩn OMG nếu là lỗi ký pháp).

Phân biệt rõ: checker **báo nhầm** một sơ đồ đúng, checker **bỏ sót** một lỗi, hay lỗi hiển thị/bố cục.

## Sửa hoặc thêm luật kiểm tra

- Căn cứ vào chuẩn chính thức (OMG BPMN 2.0.2 cho BPMN), ghi mục/bảng/trang trong mã hoặc tài liệu. Hành vi của draw.io lấy từ mã nguồn tại commit đã khóa.
- Mỗi luật mới cần ít nhất một ca **đúng phải được chấp nhận** và một ca **sai phải bị bắt** trong `tests/`.
- Không đổi nghiệp vụ hay ký pháp của ví dụ để làm checker đạt. Khi một luật báo nhầm, sửa luật và thêm test.
- Phần không tự kiểm được thì đưa vào `manual_review`, không im lặng coi là đạt. Cập nhật `references/coverage.md`.
- Lõi chỉ dùng thư viện chuẩn Python 3.10+.

## Thêm skill cho loại sơ đồ khác

Đặt trong `skills/<loai>-drawio/`, ví dụ `skills/uml-drawio/`:

```text
skills/<loai>-drawio/
├── SKILL.md          # frontmatter: name, description, license
├── README.md         # mục tiêu, cách dùng, phạm vi, nguồn tham khảo
├── VERSION
├── LICENSE, NOTICE
├── references/       # quy tắc chuẩn, quy trình, phạm vi hỗ trợ
├── scripts/          # công cụ; có run_checks.py, package_skill.py
├── assets/           # ví dụ tổng hợp, theme
└── tests/
```

Giữ `SKILL.md` ngắn và trỏ tới `references/` để agent chỉ đọc khi cần. Thêm skill vào bảng trong [README](README.md) và job CI.

## Trước khi gửi pull request

```bash
python3 -B skills/<skill>/scripts/run_checks.py
python3 -B skills/<skill>/scripts/run_checks.py --render --drawio-root DRAWIO --output-dir output/render --report output/render/checks.json
python3 -B skills/<skill>/scripts/package_skill.py --output-dir output/candidate
python3 -B skills/<skill>/scripts/smoke_package.py output/candidate/<skill>-<phiên bản>-candidate.zip --drawio-root DRAWIO --report output/smoke.json
```

Mở và xem lại ảnh dựng của phần bạn thay đổi. Không commit thư mục `output/`, `dist/`, cache hay mã nguồn draw.io. Không đưa dữ liệu cá nhân, tài liệu khách hàng hoặc tài liệu có bản quyền của bên thứ ba vào repo.

## Phiên bản và phát hành

Mỗi skill có `VERSION` riêng theo SemVer; `-rc.N` là bản ứng viên (pre-release). Tag Git dạng `<skill>-v<phiên bản>`, ví dụ `bpmn-drawio-v1.0.0-rc.2`. Ghi thay đổi vào [CHANGELOG.md](CHANGELOG.md). Release đính kèm ZIP do `package_skill.py` tạo cùng file SHA-256.

## Giấy phép

Đóng góp được phát hành theo [Apache-2.0](LICENSE) như phần còn lại của repo.
