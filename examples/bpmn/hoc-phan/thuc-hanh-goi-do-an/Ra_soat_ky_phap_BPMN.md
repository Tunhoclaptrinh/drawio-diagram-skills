# Rà soát màu sắc, đường nối và sự kiện BPMN

Đã xem sáu ảnh PNG của hai phiên bản hiện tại, kiểm tra hình SVG thực tế và đối chiếu **đặc tả OMG BPMN 2.0.2** trong [OMG BPMN 2.0.2](https://www.omg.org/spec/BPMN/2.0.2/PDF). Các nhóm kiểm tra bên dưới đạt sau khi sửa màu và tách task vật lý D02a/D03a. Báo cáo toàn diện ghi đầy đủ phát hiện, đối chiếu đề, từng bước nghiệp vụ, giả định và giới hạn; tài liệu này là bản tra nhanh ký pháp.

**Bổ sung theo yêu cầu:** có thêm [bản có màu](BPMN_Goi_do_an_Co_mau.drawio). Đã xem ba ảnh màu và chạy cùng các kiểm tra; bản màu đạt và được xác nhận chỉ khác thuộc tính màu, giữ nguyên nhãn, hình học, ký hiệu và kết nối. Xem Kiem_tra_Co_mau.json.

## 1. Màu sắc

**Không bắt buộc thêm màu để đúng chuẩn.** Mục 7.5 cho phép dùng màu tô và màu nét, nhưng không bắt buộc bộ màu xanh/vàng/đỏ cho start/gateway/end. Theo lựa chọn của người học, bộ kết quả nay có cả bản bình thường và bản màu. Bảng dưới đây mô tả bản bình thường; bảng màu của phiên bản mới nằm trong [README](README.md).

- Task thường và event: nền trắng.
- SP1 và B03: xanh nhạt để dễ nhận ra phần điều phối.
- Các bước hủy/hoàn tiền/thông báo hủy: hồng nhạt.
- Gateway và kiểm tra chính sách: vàng/cam rất nhạt.
- Pool: xám xanh nhạt.

Màu này là quy ước trình bày của bài, **không phải quy định màu của OMG**. Giữ sự khác biệt tô tối/không tô của các marker gửi và nhận; không đổi đường nét liền thành nét đứt vì muốn đổi giao diện.

**Bản có màu hiện tại:** start xanh, mọi end đỏ, gateway/timer vàng, activity xanh dương. End thành công cũng đỏ; đọc nhãn để biết kết quả. Đã bỏ quy tắc cũ chọn màu theo chữ “hủy”, vốn khiến end “từ chối” bị xanh. Mục 12.1.1, trang in 367/PDF 397, xác nhận màu thay thế không có tính quy phạm và có thể được hiểu khác giữa các công cụ/người dùng.

Nguồn: mục 7.5, trang in **39–40**, tương ứng [OMG BPMN 2.0.2](https://www.omg.org/spec/BPMN/2.0.2/PDF).

## 2. Kết quả kiểm tra từng nhóm ký pháp

| Nhóm | Chuẩn cần đáp ứng | Kết quả trên ba trang |
|---|---|---|
| Sequence flow | Một đường nét liền, mũi tên tô đặc; không vượt pool hoặc ranh giới scope subprocess | **47/47 đạt** |
| Message flow | Một đường nét đứt, vòng tròn rỗng ở đầu gửi, đầu mũi tên không tô; hai đầu thuộc hai pool khác nhau | **19/19 đạt** |
| Start event | Một vòng tròn mảnh; không có sequence flow đi vào | **4/4 đạt** |
| Message start | Phong bì không tô; thông điệp đi vào, không đi ra | **A00, C00, D00 đạt** |
| Start của SP1 | None start, không có marker; được kích hoạt từ subprocess cha | **B00 đạt** |
| None end event | Một vòng tròn đậm; không có marker; không có sequence flow đi ra | **7/7 đạt** |
| Interrupting boundary timer | Hai vòng mảnh nét liền và đồng hồ; gắn vào tác vụ chờ, có nhánh đi ra; ngắt tác vụ khi kích hoạt | **AT1 trên A03 và BT1 trên B02 đạt** |
| XOR | Hình thoi có dấu X; không nối message flow vào gateway | **6/6 đạt** |
| Send/receive task | Phong bì gửi tô tối, phong bì nhận không tô | **19/19 marker đạt** |

Mũi tên message đang dùng là **tam giác không tô**, giống hình 9.11 trong đặc tả. Không nhầm nó với mũi tên tam giác **tô đặc** của sequence flow. Các đoạn gấp khúc vẫn là cùng một đường nối, không tạo thêm gateway hoặc event.

## 3. Kiểm tra chi tiết điểm bắt đầu và kết thúc

| Trang | Điểm bắt đầu | Điểm kết thúc | Giải thích |
|---|---|---|---|
| 01 | A00: Message start | AE1, AE2, AE3: None end | Nhận đơn khởi tạo quy trình; kết quả là hoàn tất hoặc hủy theo từng nhánh |
| 02 | B00: None start bên trong SP1 | BE1, BE2: None end bên trong SP1 | SP1 được quy trình cha gọi; end nội bộ hoàn thành SP1, cha đọc kết quả ở AG3 |
| 03, nhà hàng | C00: Message start | CE1: None end | Yêu cầu chuẩn bị khởi tạo phần quy trình được hiển thị; kết thúc sau bàn giao |
| 03, tài xế | D00: Message start | DE1: None end | Xác nhận phân công khởi tạo quy trình chuyến; kết thúc sau báo giao hoàn tất |

Trên SVG, viền start rộng **1,5** đơn vị; viền end rộng **4,5** đơn vị. Hai vòng ngoài của timer đều rộng **1,5** và không có dash. OMG yêu cầu phân biệt mảnh/đậm; các trị số này là cách trình dựng draw.io thể hiện, không phải trị số bắt buộc của chuẩn.

**End có nhãn “Hủy” không bắt buộc có dấu X.** Cancel End Event có dấu X dành cho Transaction Sub-Process; bài này không dùng transaction. None end sau các task hủy/hoàn tiền là phù hợp. Vòng tròn đen đặc bên trong end là Terminate marker, không phải cách tô màu để báo kết thúc thông thường.

## 4. Các điểm đối chiếu trong đặc tả

Các số sau là số **trang in bên dưới trang tài liệu**, khác số thứ tự trang của trình đọc PDF:

| Nội dung | Mục | Trang in | Trang PDF |
|---|---|---|---|
| Màu sắc, độ lớn và kiểu nét | 7.5 | 39–40 | 69–70 |
| Giới hạn sequence/message flow theo pool và scope | 7.6 | 40–42 | 70–72 |
| Sequence flow, mũi tên đặc | 8.4.13, hình 8.32 | 95 | 125 |
| Message flow, vòng tròn và mũi tên không tô | 9.4, hình 9.11 | 119 | 149 |
| Send/receive task: marker phong bì | 10.3.3 | 158–159 | 188–189 |
| Start một vòng mảnh | 10.5.2 | 237 | 267 |
| None start cho subprocess thông thường | 10.5.2 | 241 | 271 |
| End một vòng đậm, hướng nối, None/Cancel/Terminate | 10.5.3 | 245–248 | 275–278 |
| Intermediate event hai vòng mảnh | 10.5.4 | 248–249 | 278–279 |
| Boundary event ngắt tác vụ khi kích hoạt | 10.5.6 | 276 | 306 |

Đã sửa tham chiếu chương trong tài liệu giải thích: **Events là mục 10.5**; mục 10.4 là Items and Data.

## 5. Cách kiểm chứng và phạm vi kết luận

`kiem_tra.py` gọi auditor chung, đọc style `.drawio`, dữ liệu hình học và SVG thực tế. Nó kiểm tra các ràng buộc được hỗ trợ về nét, mũi tên/vòng tròn, viền event, marker phong bì, hướng nối, chồng hình và đường xuyên hình. Ảnh có hash nguồn và commit draw.io; bằng chứng nằm trong `kiem-chung/`, kết quả ở Kiem_tra.json. Bản màu kiểm tra thêm profile trình bày và sự tương đương với bản thường.

Cảnh báo thủ công về khung `SP1_EXP` không có sequence bên ngoài đã được xem: trang 02 là góc nhìn nội dung SP1, còn kết nối của hoạt động cha ở trang 01. Không dùng cảnh báo này để suy diễn mô hình thực thi hoàn chỉnh; xem phân tích phạm vi trong báo cáo toàn diện.

Phần rà soát này xác nhận ký pháp được dùng trong phạm vi bài thực hành, kết hợp xem ảnh và đọc đặc tả; không thay thế kiểm thử chạy trên BPMN engine. Những lựa chọn nghiệp vụ bổ sung vẫn được ghi rõ trong tài liệu giải thích, gồm thời gian tìm tài xế **5 phút** và chính sách **đúng hạn thì hủy**.
