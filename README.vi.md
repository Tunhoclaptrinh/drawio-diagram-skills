# drawio-diagram-skills

[![Skills CI](https://github.com/Tunhoclaptrinh/drawio-diagram-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/Tunhoclaptrinh/drawio-diagram-skills/actions/workflows/ci.yml)
[![Tài liệu trực quan](https://img.shields.io/badge/tài_liệu-GitHub_Pages-blue.svg)](https://tunhoclaptrinh.github.io/drawio-diagram-skills/)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

[English](README.md) · **Tiếng Việt**

Bộ skill giúp AI agent (Claude Code và các agent đọc định dạng `SKILL.md`) **phân tích nghiệp vụ, vẽ và rà soát sơ đồ trong draw.io**: file `.drawio` chỉnh sửa được, ảnh PNG/SVG/PDF dựng bằng renderer thật của draw.io, và tài liệu giải thích. Thứ tự ưu tiên: đúng nghiệp vụ → đúng ký pháp → bố cục dễ đọc → màu sắc.

## Các skill

| Skill | Loại sơ đồ | Phiên bản | Trạng thái |
|---|---|---|---|
| [bpmn-drawio](skills/bpmn-drawio/README.md) | BPMN 2.0.2 Process / Collaboration | `1.0.0-rc.2` | Pre-release để dùng thử và góp ý |

Mỗi skill nằm trong `skills/<tên>/`, có phiên bản, test và gói ZIP riêng. Các loại sơ đồ khác (ví dụ UML, ERD, C4) là **hướng mở rộng chưa triển khai**; khi thêm sẽ theo cùng cấu trúc `skills/<loai>-drawio/`.

## Tài liệu

| Tài liệu | Nội dung |
|---|---|
| [Tài liệu trực quan (Web)](https://tunhoclaptrinh.github.io/drawio-diagram-skills/) | Cổng tài liệu trực quan trên GitHub Pages: tra cứu quy tắc OMG, chẩn đoán bố cục có ảnh, bảng màu và bộ demo |
| [Hướng dẫn sử dụng](docs/user-guide.md) | Cài đặt, câu lệnh mẫu cho agent, tự chạy công cụ, đọc báo cáo kiểm tra, lỗi bố cục có ảnh, theme, sự cố thường gặp |
| [Ví dụ](examples/README.md) | 9 bộ ví dụ: sơ đồ `.drawio` hai bản, ảnh PNG/SVG và giải thích nghiệp vụ |
| [README skill bpmn-drawio](skills/bpmn-drawio/README.md) · [SKILL.md](skills/bpmn-drawio/SKILL.md) | Nguyên tắc thiết kế, thành phần, nguồn tham khảo; điểm vào cho agent |
| [Quy tắc BPMN](skills/bpmn-drawio/references/bpmn-rules.md) · [Phạm vi hỗ trợ](skills/bpmn-drawio/references/coverage.md) | Ma trận event theo vị trí, kết nối; những gì được kiểm tự động và phải rà tay |
| [Đóng góp](CONTRIBUTING.md) · [Phát hành](RELEASING.md) · [CHANGELOG](CHANGELOG.md) | Báo lỗi, thêm luật, thêm skill cho loại sơ đồ khác; quy trình phát hành; lịch sử phiên bản (tiếng Anh) |

Chuẩn BPMN được trích theo tên và liên kết tới bản công bố chính thức [OMG BPMN 2.0.2](https://www.omg.org/spec/BPMN/2.0.2/PDF); repo không đính kèm PDF của OMG.

![Ví dụ BPMN mượn sách liên thư viện, bản màu](examples/bpmn/interlibrary-loan/color/interlibrary-loan.png)

## Cài đặt

1. Tải `bpmn-drawio-<phiên bản>-candidate.zip` ở mục **Releases**, đối chiếu SHA-256, giải nén giữ nguyên thư mục `bpmn-drawio/`.
2. Đặt thư mục vào nơi agent đọc skill, ví dụ với Claude Code: `~/.claude/skills/bpmn-drawio/` (dùng cho mọi dự án) hoặc `.claude/skills/bpmn-drawio/` trong một dự án.
3. Kiểm tra gói ngay từ bản vừa tải:

```bash
python3 -B bpmn-drawio/scripts/smoke_package.py bpmn-drawio-1.0.0-rc.2-candidate.zip --report smoke.json
```

Hoặc clone repo và sao chép `skills/bpmn-drawio/`.

## Yêu cầu

- Python 3.10+ (chỉ thư viện chuẩn cho phần lõi).
- Chrome/Chromium để dựng ảnh và PDF.
- Mã nguồn draw.io do bạn tự cung cấp (không đóng kèm). Phiên bản đã thử: commit `17b367b91dbab91804f852645788d7ffb46dcb79` (draw.io 32.5.5):

```bash
git clone --filter=blob:none https://github.com/jgraph/drawio.git
git -C drawio checkout 17b367b91dbab91804f852645788d7ffb46dcb79
python3 skills/bpmn-drawio/scripts/doctor.py --drawio-root drawio --output-dir output
```

Đã thử trên Linux. Windows/macOS chưa được kiểm chứng.

## Kiểm thử

```bash
python3 -B skills/bpmn-drawio/scripts/run_checks.py
python3 -B skills/bpmn-drawio/scripts/run_checks.py --render --drawio-root drawio --output-dir output/render --report output/render/checks.json
```

CI ([workflow](.github/workflows/ci.yml)) chạy test nhanh trên Python 3.10/3.12/3.14, đóng gói và smoke test từ ZIP; job dựng ảnh chạy thủ công.

## Giới hạn

Đây là bộ kiểm tra chọn lọc, không phải trình kiểm định toàn bộ chuẩn, BPMN engine hay chứng nhận OMG. Kết quả kiểm tra công cụ không thay xác nhận nghiệp vụ của người có chuyên môn. Xem [phạm vi hỗ trợ](skills/bpmn-drawio/references/coverage.md).

Không liên kết hoặc được bảo trợ bởi OMG, JGraph (draw.io) hay Bizagi. Tên profile màu `bizagi-inspired` chỉ là tham chiếu phong cách trình bày, không phải bảng màu chính thức.

## Giấy phép

[Apache-2.0](LICENSE). Copyright 2026 Tunhoclaptrinh — xem [NOTICE](NOTICE). Khi phân phối lại cần giữ LICENSE và NOTICE.
