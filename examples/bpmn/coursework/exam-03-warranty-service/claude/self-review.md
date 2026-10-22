# Tự rà soát lần 2 — Đề 03 bảo hành thiết bị điện tử

Rà lại bài đã làm theo ba nguồn: **chuẩn OMG BPMN 2.0.2** ([OMG BPMN 2.0.2](https://www.omg.org/spec/BPMN/2.0.2/PDF), trang in = trang PDF − 30), **mã nguồn draw.io** trong `vendor/drawio` (commit `17b367b91dbab91804f852645788d7ffb46dcb79`) và **từng câu của *Đề thi giữa kỳ PTNVPM* (tài liệu của học phần, không đính kèm)**. **Bản final (mục 1d)** bổ sung bước đối chiếu phạm vi, ghi nhận mốc t₀ trước khi chờ và PDF vector. Kết quả các lượt trước: mô hình nghiệp vụ không có lỗi; có **3 điểm** chưa theo khuyến nghị/quy ước đặt tên của chuẩn (mục 1), **5 điểm trình bày** phát hiện khi soi hình (mục 1b), tất cả đã sửa; sau khi so sánh với bài GPT và Gemini, áp dụng thêm **3 cải tiến** (mục 1c). Sau khi sửa, toàn bộ ảnh, kiểm tra, bản nộp và ZIP đã được tạo lại.

## 1. Điểm đã sửa

| # | Trước | Căn cứ | Sau |
|---|---|---|---|
| R1 | Timer B48 gắn ở **cạnh trên** KT4, luồng quá hạn đi lên; vòng sửa chữa ở hàng dưới | OMG §10.5.4, tr.249: boundary được gắn ở bất kỳ đâu, nhưng **khuyến nghị** sơ đồ ngang gắn ở **cạnh dưới**, luồng đi xuống rồi sang phải | B48 ở cạnh dưới KT4; quá hạn đi xuống rồi sang phải tới KT5 → E4 ở hàng dưới. Vòng sửa chữa chuyển lên hàng trên, đường “Chưa đạt” đi vòng phía trên; KT4 → GM2 đi lên |
| R2 | Tên pool “KHÁCH HÀNG — participant bên ngoài (black box)” | Tên participant là tên bên tham gia (OMG §9.3); lời giải thích kỹ thuật không thuộc tên | Tên pool “KHÁCH HÀNG”; câu “Pool Khách hàng để rỗng (black box)” chuyển xuống chú thích chân sơ đồ |
| R3 | Start “Nhận yêu cầu bảo hành”; timer “48 giờ kể từ khi KH nhận yêu cầu bàn giao” | Event mô tả **sự kiện/điều kiện xảy ra**, khác task mô tả hành động | Start “Nhận được yêu cầu bảo hành”; timer “Hết 48 giờ kể từ khi KH nhận yêu cầu bàn giao” |

Ba sửa đổi không đổi logic: cùng ID, cùng 34 sequence flow (nguồn → đích), 7 message flow, cùng điều kiện gateway. Toàn bộ 22 kiểm tra kịch bản chạy lại đạt.

## 1b. Rà hình lần cuối (độ phân giải 2×, cả bản thường và bản màu)

Cắt ảnh 5942×2838 thành lưới 3×2 có chồng mép, soi từng vùng; sau đó đo bằng máy mọi dòng chữ trong SVG.

| # | Phát hiện | Sửa |
|---|---|---|
| R4 | Luồng “Không thuộc phạm vi” đi vào task thông báo từ chối lệch về phía phải đáy, trong khi message ra ở giữa | Đặt task thẳng hàng trên gateway G4; luồng vào và message ra cùng trục |
| R5 | “Thông báo khách hàng nhận lại thiết bị” có dòng chữ gần chạm viền task | Ngắt thành 3 dòng |
| R6 | Nhãn “Chưa đạt” nằm đè lên đường, khác kiểu các nhãn còn lại | Đưa lên trên đường vòng lặp |
| R7 | Nhãn end “Từ chối: lỗi ngoài phạm vi bảo hành” bắt đầu sát mép task bên cạnh | Dời end sang phải 16 px; vẫn cách đường message bàn giao ~30 px |
| R8 | Nhãn của hình được draw.io xuất thành HTML trong `foreignObject` (do `whiteSpace=wrap`), kèm dòng dự phòng “Text is not SVG”; trình xem SVG không hỗ trợ `foreignObject` phải dùng bản dự phòng | Mọi nhãn đã ngắt dòng thủ công nên đặt `whiteSpace=nowrap`: SVG giờ là chữ thuần, 0 `foreignObject`. Kiểm chứng bằng bộ nhập SVG độc lập của LibreOffice: hiển thị đủ chữ |

Bộ kiểm tra va chạm nhãn đo khung chữ bằng metric font Arial cho từng dòng `<text>/<tspan>`, có tính phép xoay của nhãn pool/lane: **0 lỗi** trên 102 dòng chữ (56 phần tử có nhãn, 33 hình, 41 đường) ở cả hai bản. Ba đối chứng cố ý sai — nhãn đè lên task, chữ tràn viền task, nhãn của phần tử khác đè lên đường — **đều bị bắt**. Nhãn nằm trên chính đường của nó được chấp nhận (cách draw.io vẫn làm), nên không dùng làm đối chứng.

## 1c. Cải tiến sau khi so sánh với bài GPT và Gemini

So sánh cùng tiêu chí (chỉ đọc, không sửa hai bài kia). Những gì bài khác làm tốt hơn và thật sự giúp bài này đúng/rõ hơn đã được áp dụng:

| # | Học từ | Thay đổi | Lý do |
|---|---|---|---|
| R9 | GPT, Gemini | Đặt tên hai gateway song song: “Thực hiện đồng thời”, “Chờ cả hai hoàn tất”; nới khối bên phải 50 px để tên nằm ở chỗ trống, không đường nào đi qua | Người chấm thấy ngay ý nghĩa tách/đồng bộ; tên “Chờ cả hai hoàn tất” ngay trước gateway phạm vi cũng chỉ ra căn cứ của quyết định |
| R10 | GPT | Kiểm thử dữ liệu thời hạn: áp đúng `timeDate` trong file lên 4 dòng thời gian, so với quy tắc của đề; 2 đối chứng (tính từ lúc gửi; đếm lại khi bắt đầu chờ) đều bị bắt; không tự gắn quy tắc hòa | Chứng minh định nghĩa trong file, không chỉ nhãn, khớp chữ “kể từ khi nhận được yêu cầu” |
| R11 | GPT | Thêm kịch bản: bổ sung rồi ngoài phạm vi; bổ sung rồi không được duyệt; nhánh quá hạn chỉ dẫn tới đóng yêu cầu | Phủ các tổ hợp còn thiếu và trường hợp thiết bị tới muộn |

Đã cân nhắc nhưng **không** áp dụng ở lượt này (hai dòng đầu được đổi ở bản final):

| Ý tưởng | Lý do giữ nguyên |
|---|---|
| Thêm task “Đối chiếu lỗi với phạm vi bảo hành” (GPT) | **Đã đổi quyết định ở bản final (R12, mục 1d).** Lý do ban đầu: Đề không nêu bước này; dữ liệu cho quyết định do hai kiểm tra tạo ra và tên “Chờ cả hai hoàn tất” đã thể hiện căn cứ. Thêm task làm sơ đồ rộng khoảng 200 px mà không thêm nghĩa nghiệp vụ |
| Đổi “Gửi yêu cầu bàn giao” thành task “gửi và ghi nhận mốc t₀” (GPT) | **Đã đổi quyết định ở bản final (R13, mục 1d).** Lý do ban đầu: Timer đã ghi “kể từ khi KH nhận yêu cầu”, định nghĩa trong file tính từ mốc nhận và có kiểm thử (R10). Cách doanh nghiệp biết mốc nhận là giả định triển khai đã công khai ở mục 6 tài liệu giải thích; giữ Send Task đúng bản chất gửi thông tin |
| Thông báo cho khách khi không được duyệt (Gemini) | Ngoài chữ đề (mục 6 của đề không nêu thông báo); tài liệu giải thích chỉ cách thêm nếu giảng viên yêu cầu |
| Receive Task + message “biên nhận” cho việc bàn giao (Gemini) | Mang thiết bị đến là việc vật lý; giữ Manual Task |
| Ghi chú BPMN (text annotation) gắn vào gateway phạm vi và timer | Vùng quanh hai phần tử đã có nhãn; đường liên kết sẽ đi qua chữ hiện có. Nội dung đã nằm trong nhãn timer, tên gateway song song và chú thích chân sơ đồ |

## 1d. Bản final — hoàn thiện bằng ưu điểm của bài GPT

Sau khi đánh giá lại công bằng, hai điểm bài GPT chặt hơn về nghiệp vụ và một điểm về bản nộp được đưa vào. Hai ý ở bảng “không áp dụng” của mục 1c được **đổi quyết định** vì lý do dưới đây; mọi thế mạnh sẵn có (gateway gộp tường minh cho hai vòng lặp, timer cạnh dưới, bố cục gọn, chữ SVG thuần, các bộ kiểm tra) được giữ.

| # | Thay đổi | Vì sao đúng hơn |
|---|---|---|
| R12 | Thêm task **KTP “Đối chiếu kết quả với phạm vi bảo hành”** giữa AND_J và G4; điều kiện ở G4 chỉ đọc biến `loi_thuoc_pham_vi` do KTP tạo | Gateway không tự “kiểm tra”; quyết định phải đọc dữ liệu do một việc trước đó tạo ra. Bước này suy ra từ mục 8 của đề, không thêm thẩm quyền mới |
| R13 | Bước gửi yêu cầu bàn giao thành **Task thường KT3 “Gửi yêu cầu bàn giao, ghi nhận lúc khách nhận yêu cầu (t₀)”**, có `outputData = t_kh_nhan_yeu_cau_ban_giao` — đúng biến timer dùng | Send Task kết thúc ngay khi gửi (OMG §10.3.3, tr.157). Hạn tính từ lúc khách **nhận**, nên phải có t₀ trước khi KT4 bắt đầu chờ thì timer mới xác định được hạn |
| R14 | PDF theo mẫu nhúng sơ đồ **vector** (bản tạm của DOCX thay ảnh bằng SVG chữ thuần, LibreOffice xuất PDF); DOCX giao kèm giữ PNG 2× | Phóng to không vỡ, tìm được chữ; kiểm tra bản nộp xác nhận 0 ảnh raster và có chữ thật của sơ đồ |
| R15 | Kiểm thử thêm: bất biến “chưa đối chiếu thì không xét phạm vi”, đối chứng bỏ qua bước đối chiếu, ràng buộc t₀ có trước khi chờ, ràng buộc gateway chỉ đọc kết luận đối chiếu | Bảo vệ hai thay đổi trên khỏi bị hồi quy |
| R16 | Chuẩn bị nộp bản màu: chú thích dưới biểu đồ viết lại ngắn gọn cho người chấm (t₀ và quy tắc đóng yêu cầu; ý nghĩa nét liền/nét đứt; vì sao bàn giao thiết bị không vẽ thành thông điệp), bỏ thuật ngữ công cụ và dòng “bản có màu” ở bản A3; tạo thư mục `nop-bai-final/` chỉ gồm bản màu và file giải thích riêng | Người chấm đọc hiểu ngay; gói nộp gọn, không lẫn bản thường |

Mô hình final: 35 sequence flow, 7 message flow, 10 task thường, 4 Send, 1 Receive, 1 Service, 2 Manual, 7 XOR, 2 AND, 1 Message Start, 5 None End, 1 timer biên ngắt.

## 2. Đối chiếu ký pháp với OMG

| Phần tử trong bài | Quy tắc OMG kiểm tra | Trang in | Kết quả |
|---|---|---|---|
| Pool KH rỗng, message gắn viền pool | Pool có thể là black box; message nối viền pool hoặc phần tử trong pool | 110–111, 119 | Đạt |
| 4 lane trong pool DN, có lane Hệ thống | Lane dùng cho vai trò, phòng ban, **hệ thống** | 305 | Đạt |
| 35 sequence flow | Nét liền, mũi tên đặc; chỉ trong một pool; được qua lane | 39–42, 95 | Đạt (audit dựng ảnh) |
| 7 message flow | Nối hai pool khác nhau; nét đứt, tròn rỗng đầu gửi, mũi tên rỗng đầu nhận; không nối gateway | 119 | Đạt |
| Message Start S | Marker phong bì; được là đích của message flow; không có sequence vào | 239–241 | Đạt |
| 5 None End | Một vòng đậm; có sequence vào, không có sequence ra; không nhận message | 246–248 | Đạt |
| Boundary timer B48 | Trigger Timer được phép gắn biên; không có sequence vào; phải có sequence ra; ngắt = `cancelActivity=true`, hai vòng nét liền | 249, 257, 276 | Đạt |
| Send ×4, Receive ×1, Service ×1, Manual ×2, Task thường có message ra (KT3) | Send kết thúc khi gửi; Receive chờ message; Service dùng ứng dụng/dịch vụ; Manual làm không qua ứng dụng; activity thường được làm nguồn message | 156–161 | Đạt: mỗi Send có message ra, Receive có message vào; KT3 không dùng Send vì còn chờ ghi nhận t₀ |
| 7 XOR (5 tách, 2 gộp), 2 AND | Gateway phải tách hoặc gộp; AND không mang điều kiện; XOR gộp không đồng bộ | 287–293 | Đạt: không có gateway vừa tách vừa gộp |
| Không activity nào có >1 luồng vào/ra | Nhiều luồng vào activity là *uncontrolled flow*; nhiều luồng ra tạo song song ngầm | 151 | Đạt: vòng lặp đi qua XOR gộp GM1, GM2 |
| Màu bản có màu | Màu không mang nghĩa chuẩn, không được đổi nét/marker | 39–40 | Đạt: audit `only_color_differs = true` |

## 3. Đối chiếu với cách draw.io hiện thực

| Kiểm tra | Căn cứ trong mã nguồn draw.io | Kết quả |
|---|---|---|
| Event dùng shape native | `Sidebar-BPMN.js`: Message Start = `outline=standard;symbol=message`; Timer biên ngắt = `outline=boundInt;symbol=timer` | Khớp |
| Gateway native | `gwType=exclusive` (có dấu X), `gwType=parallel` | Khớp |
| Task native | `shape=mxgraph.bpmn.task2;rectStyle=rounded;container=1;taskMarker=…` | Khớp (send, receive, service, manual, abstract) |
| End event | Mẫu “End” của palette là `symbol=terminate2` (Terminate) | Bài **cố ý** dùng `symbol=general` (None End) — đúng nghĩa đề |
| Message flow | Mẫu “Message Flow” trơn (dòng 88) có `endFill=1` — mũi tên **đặc**, không đúng OMG | Bài dùng `endFill=0`, `startArrow=oval;startFill=0`, `dashed=1` — đúng OMG; đã ghi lưu ý trong tài liệu giải thích |
| Gắn boundary | Task native có `container=1` để nhận event con | B48 là con của KT4 (`parent=KT4`), đi theo khi kéo task; ảnh dựng cho thấy timer cắt viền dưới |
| Hai vòng ngắt/không ngắt | `mxBpmnShape2.js`: `boundInt` vẽ hai vòng liền, `boundNonint` vẽ nét đứt | Audit đọc SVG: hai vòng không có dash |
| Mở được bằng draw.io | Viewer chính thức giải mã → dựng → mã hóa lại (roundtrip) | Không có shape lạ; số cell khớp; file roundtrip lưu trong `kiem-chung/` |
| Đường nối | `edgeStyle=none` + waypoint vuông góc (kiểu “Straight” của draw.io) | Giữ cố định tuyến đã rà; khi sửa tay có thể đổi sang *Orthogonal* nhưng cần xem lại tuyến |

## 4. Rà lại nghiệp vụ theo từng câu của đề

| Mục | Câu chữ cần giữ | Kết luận |
|---|---|---|
| 1 | Yêu cầu gồm thông tin sản phẩm **và** mô tả lỗi | M01 ghi đủ hai thành phần |
| 2 | Chưa đầy đủ → yêu cầu bổ sung → **kiểm tra lại** | Vòng quay về trước CS1 (qua GM1), không về Start, không bỏ qua kiểm tra lại (có đối chứng) |
| 3 | **Hệ thống** kiểm tra thời hạn, chỉ khi thông tin hợp lệ | HT1 là Service Task trong lane Hệ thống, sau nhánh “Đầy đủ” |
| 4 | Hết hạn: từ chối **và** thông báo khách | CS4 gửi M04 trước E1 |
| 5–6 | Trưởng BPKT **xem xét** rồi mới phê duyệt/không | TP1 tạo quyết định; G3 chỉ định tuyến |
| 7–8 | Hai việc **đồng thời**; **khi cả hai hoàn tất** mới xét phạm vi; **CSKH** thông báo | AND_S/AND_J; G4 sau AND_J; CS5 ở lane CSKH |
| 9 | **Bộ phận kỹ thuật** gửi yêu cầu bàn giao | KT3 ở lane Kỹ thuật gửi M06 và ghi nhận t₀ |
| 10 | 48 giờ **kể từ khi khách nhận** yêu cầu; quá hạn → **đóng** | Hạn tuyệt đối t₀ + 48 giờ; timer ngắt; KT5 → E4 |
| 11 | Sửa **và** kiểm tra chất lượng; chưa đạt thì **sửa tiếp và kiểm tra lại**; đạt thì **hoàn tất** | KT6 → KT7 → G5, vòng về trước KT6; KT8 |
| 12 | Thông báo nhận lại → cập nhật **hoàn thành** → kết thúc | CS6 → CS7 → E5 theo đúng thứ tự |
| Yêu cầu chung | Đối tượng tham gia, điều kiện phê duyệt, song song, vòng lặp, thời hạn | Đủ cả năm (xem bảng mục 3 của tài liệu giải thích) |

### Điểm đã cân nhắc và giữ nguyên

| Điểm | Lý do giữ |
|---|---|
| Không thông báo khách khi trưởng bộ phận không duyệt (E2) và khi đóng do quá hạn (E4) | Mục 4 và 8 nói rõ “thông báo”, mục 6 và 10 thì không. Vẽ đúng chữ của đề, không tự thêm chính sách; tài liệu giải thích chỉ cách thêm nếu giảng viên yêu cầu |
| KT1/KT2 diễn ra trước khi khách bàn giao thiết bị | Đúng thứ tự mục 7–9; diễn giải là đánh giá dựa trên thông tin đã có. Đảo thứ tự sẽ thay đổi quy trình đề cho |
| Bàn giao thiết bị không vẽ thành message | Message là thông tin giữa participant (§9.4); việc mang thiết bị đến là việc vật lý ở Manual Task KT4 — theo hướng dẫn của workspace để không hiểu message là hàng hóa |
| Không có hạn/giới hạn cho vòng bổ sung và vòng sửa chữa | Đề không nêu; thêm timer hoặc bộ đếm là tự đặt chính sách |
| Không dùng Terminate End | Tại mọi End chỉ còn một token (AND đã đồng bộ, timer là loại ngắt) |
| Không thêm Data Object/Data Store | Đề không yêu cầu; skill khuyến cáo không thêm artifact để trang trí |
| Không đặt nhánh default ở các XOR | Mỗi XOR có hai điều kiện bổ sung lẫn nhau, phủ hết trường hợp |

## 5. Chạy lại sau khi sửa

| Bước | Kết quả |
|---|---|
| Dựng hai bản bằng viewer draw.io chính thức | Thành công, không có shape lạ |
| Audit bản thường | 0 lỗi |
| Audit bản màu + palette + so sánh | 0 lỗi; palette đạt; chỉ khác màu |
| 32 kiểm tra riêng (14 kịch bản, 5 đối chứng mô hình, 6 ràng buộc mô hình, 1 nhánh quá hạn, 4 kiểm tra định nghĩa thời hạn, 2 hình học) | Đạt 32/32 |
| Phụ lục phần tử, bản nộp DOCX/PDF Letter, PDF A3 vector | Tạo lại từ sơ đồ mới; kiểm tra bản nộp đạt 6/6 |
| Kiểm tra va chạm nhãn trên SVG cả hai bản | 0 lỗi trên 109 dòng chữ, 0 `foreignObject`, 3/3 đối chứng bị bắt — Kiem_tra_nhan.json |
| Rà trực quan ảnh mới và bốn trang PDF | Không chồng chéo, không đường cắt nhau, nhãn không bị đè — ghi theo hash trong Ra_soat_truc_quan.json |

**Giới hạn vẫn giữ nguyên:** kiểm tra kịch bản tự khai báo lựa chọn ở XOR và kết quả cuộc đua timer/bàn giao, không chạy đồng hồ thật hay BPMN engine; file `.drawio` là sơ đồ chỉnh sửa được, không phải BPMN 2.0 XML thực thi; audit không phủ mọi điều khoản của OMG.
