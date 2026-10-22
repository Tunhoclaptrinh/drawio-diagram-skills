# Mượn sách liên thư viện — ví dụ forward-test

Đề tự đặt để thử skill trên một nghiệp vụ mới: không lấy từ bài thi, bộ 10 mẫu hay demo dùng xây checker. Đây là mô hình minh họa; **chưa được thủ thư hoặc chủ quy trình xác nhận**.

| Bản | Nguồn chỉnh sửa | Ảnh | PDF |
|---|---|---|---|
| Thường (`monochrome`) | [interlibrary-loan.drawio](interlibrary-loan.drawio) | [PNG](normal/interlibrary-loan.png) · [SVG](normal/interlibrary-loan.svg) | PDF |
| Màu (`bizagi-inspired`) | [interlibrary-loan-color.drawio](interlibrary-loan-color.drawio) | [PNG](color/interlibrary-loan.png) · [SVG](color/interlibrary-loan.svg) | PDF |

![Bản màu](color/interlibrary-loan.png)

## Đề tự đặt

Bạn đọc gửi phiếu đề nghị mượn một tài liệu thư viện trường không có. Quầy lưu thông kiểm tra thẻ, hạn mức và tài liệu yêu cầu; không đủ điều kiện thì báo từ chối kèm lý do. Đủ điều kiện thì bộ phận liên thư viện gửi yêu cầu cho thư viện đối tác và chờ: đối tác xác nhận đã gửi sách, báo không cho mượn, hoặc quá 10 ngày làm việc không phản hồi (khi đó gửi hủy yêu cầu). Khi nhận sách, thư viện dán nhãn, mời bạn đọc đến nhận; sau 3 ngày chưa đến thì nhắc một lần nhưng vẫn giữ sách; sau 7 ngày chưa nhận thì dừng chờ và gửi trả sách cho đối tác.

## Yêu cầu → phần tử

| Yêu cầu (F = dữ kiện đề, A = giả định) | Phần tử | Ghi chú |
|---|---|---|
| F: Bạn đọc gửi phiếu | Pool `Bạn đọc` (black-box), message M1 → Message Start `S` | Một phiếu tạo một lần xử lý |
| F: Kiểm tra thẻ, hạn mức, tài liệu | User task `T1`, data store `CSDL bạn đọc` | T1 tạo kết quả đủ/không đủ; XOR `G1` chỉ đọc kết quả |
| F: Không đủ → báo từ chối kèm lý do | `G1` nhánh mặc định `Không` → send `T_REJ` → M2 → End `Đề nghị bị từ chối` | Slash mặc định; nhánh `Có` mang điều kiện |
| F: Gửi yêu cầu cho đối tác | Lane `BỘ PHẬN LIÊN THƯ VIỆN`, send `T2`, M3 | Sequence đi qua lane trong cùng pool |
| F: Chờ một trong ba khả năng | Event-based gateway `EG` → catch Message `C1`, catch Message `C2`, catch Timer `C3` | Sự kiện đến trước thắng; không có điều kiện trên nhánh |
| F: Quá hạn thì hủy yêu cầu | `C3` → send `T9` → M6 | A: 10 ngày làm việc tính từ khi gửi yêu cầu (T2 hoàn tất) |
| F: Từ chối hoặc hết hạn đều báo bạn đọc | XOR gộp `GM` → Link throw `A · Báo không mượn được` → Link catch cùng tên → send `T8` → M9 → End | Cặp Link tránh đường nối dài quay ngược về lane quầy |
| F: Nhận sách, dán nhãn, mời đến nhận | Manual `T3` (việc vật lý) → send `T4` → M7 | Nhận sách vật lý tách khỏi xác nhận thông tin C1 |
| F: Giao sách | User `T5` → End `Đã giao sách` | A: ghi mượn trên phần mềm thư viện |
| F: 3 ngày chưa đến thì nhắc, vẫn giữ sách | Boundary timer **không ngắt** `B1` (vòng đứt) → send `T6` → M8 → End `Đã nhắc` | T5 vẫn tiếp tục chờ |
| F: 7 ngày chưa nhận thì trả sách | Boundary timer **ngắt** `B2` (vòng liền) → manual `T7` → End | Gửi trả là việc vật lý, không vẽ thành message flow |

## Luồng và kết thúc

- **Chính:** S → T1 → G1 (Có) → T2 → EG → C1 → T3 → T4 → T5 → `Đã giao sách`.
- **Không đủ điều kiện:** S → T1 → G1 (Không) → T_REJ → `Đề nghị bị từ chối`.
- **Đối tác từ chối:** … → EG → C2 → GM → Link → T8 → `Không mượn được`.
- **Đối tác im lặng 10 ngày:** … → EG → C3 → T9 (gửi hủy) → GM → Link → T8 → `Không mượn được`.
- **Bạn đọc đến muộn hơn 3 ngày nhưng trong 7 ngày:** B1 tạo thêm token → T6 → `Đã nhắc`; token chính vẫn ở T5 và kết thúc `Đã giao sách`. Hai End được đạt trong cùng một lần xử lý.
- **Quá 7 ngày:** B2 ngắt T5 → T7 → `Đã trả sách do quá hạn nhận`. Nếu nhắc đã chạy trước đó, token nhắc kết thúc độc lập.

Màu đỏ ở mọi End chỉ có nghĩa “kết thúc”, kể cả `Đã giao sách`.

## Giả định và câu hỏi mở

- Không mô tả việc bạn đọc làm sau khi nhận thông báo (pool black-box).
- Phản hồi của đối tác đến sau khi đã gửi hủy không được mô hình hóa; cần quy tắc tương quan/huỷ ở hệ thống thật.
- Không có phí, đặt cọc, gia hạn hay trả sách sau khi mượn — ngoài phạm vi đề tự đặt.
- Thời hạn 3/7/10 ngày là dữ kiện của đề tự đặt, không phải mặc định cho đề khác.

## Ký pháp đã chọn

Message start (envelope rỗng), send task (envelope đặc), catch message (rỗng) và Link throw (đặc)/catch (rỗng) theo Bảng 10.89; boundary timer ngắt vòng liền, không ngắt vòng đứt (Bảng 10.90); event-based gateway có ≥2 catch, không có điều kiện (§10.6.5); gateway gộp `GM` có hai nhánh vào (§10.6). Message flow nét đứt, vòng hở ở bên gửi, đầu mũi tên rỗng.

## Kiểm tra đã làm

- Audit thường và màu: 0 lỗi cấu trúc/palette, `--strict-layout` và `--require-supported` đạt, so sánh chỉ khác màu đạt (audit-normal.json, audit-color.json). Hai manual note còn lại: association dữ liệu D1 và event-based gateway.
- Đã đọc ảnh toàn trang cả hai bản và phóng to vùng EG/C1–C3, boundary B1/B2: marker catch/throw, vòng liền/đứt, chữ tiếng Việt hiển thị đúng.
- PDF: 0 ảnh raster, trích được chữ tiếng Việt.
- **Bản nháp đầu bị checker rc.2 từ chối 5 lỗi bố cục có thật** (nhãn S lấn header lane, nhãn link chạm T8, nhãn message M5 đè chữ T9, F9 cắt nhãn M4, nhãn M1 vắt biên lane); ảnh xác nhận từng lỗi, sau đó mới sửa bố cục. Lỗi M1 được phát hiện khi đọc ảnh, dẫn tới luật “nhãn vắt biên container”.

## Vẽ lại

Tạo ba pool ngang (bạn đọc, thư viện trường với hai lane, đối tác). Đặt luồng chính trái→phải trong lane quầy, nhánh liên thư viện ở lane dưới; ba catch xếp dọc sau EG; message của đối tác đi vào từ dưới với nhãn đặt ở khe giữa hai pool. Tạo bản màu bằng `colorize_drawio.py --theme bizagi-inspired` từ bản thường, không sửa hình học. Script tạo lại: `python3 -B build_diagram.py ĐƯỜNG_DẪN_SKILL .`
