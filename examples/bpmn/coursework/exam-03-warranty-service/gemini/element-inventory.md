# Phụ lục phần tử và luồng — Đề 02 (Đề thi giữa kỳ Đề 03)

Danh mục trích từ `diagram.drawio`. SHA-256: `d8f4d055d06fe367aa18efbd14f913d499a7304fd00a3bd686e53058436bc649`.

## Phần tử

| ID | Loại BPMN | Nhãn | Parent |
|---|---|---|---|
| KH | participant | KHÁCH HÀNG — participant bên ngoài (black box) | 1 |
| DN | participant | DOANH NGHIỆP | 1 |
| CSKH | lane | BỘ PHẬN CHĂM SÓC KHÁCH HÀNG | DN |
| HT | lane | HỆ THỐNG QUẢN LÝ BẢO HÀNH | DN |
| TP | lane | TRƯỞNG BỘ PHẬN KỸ THUẬT | DN |
| KT | lane | BỘ PHẬN KỸ THUẬT | DN |
| S | startEvent | Tiếp nhận / yêu cầu bảo hành | CSKH |
| GM1 | exclusiveGateway |  | CSKH |
| C1 | userTask | Tiếp nhận và kiểm tra / tính đầy đủ thông tin | CSKH |
| G1 | exclusiveGateway | Thông tin đầy đủ? | CSKH |
| C2 | sendTask | Yêu cầu khách hàng / bổ sung thông tin | CSKH |
| C3 | receiveTask | Tiếp nhận thông tin / bổ sung từ khách hàng | CSKH |
| C4 | sendTask | Thông báo từ chối bảo hành: / Hết hạn bảo hành | CSKH |
| E_EXPIRED | endEvent | Từ chối: / Hết hạn bảo hành | CSKH |
| C5 | sendTask | Thông báo từ chối bảo hành: / Không được phê duyệt | CSKH |
| E_REJECT_TP | endEvent | Từ chối: / Không được phê duyệt | CSKH |
| C6 | sendTask | Thông báo từ chối bảo hành: / Ngoài phạm vi bảo hành | CSKH |
| E_OUT_OF_SCOPE | endEvent | Từ chối: / Ngoài phạm vi bảo hành | CSKH |
| C7 | sendTask | Thông báo cho khách hàng / nhận lại thiết bị | CSKH |
| S1 | serviceTask | Kiểm tra thời hạn bảo hành / của sản phẩm trên hệ thống | HT |
| G2 | exclusiveGateway | Còn thời hạn / bảo hành? | HT |
| S2 | serviceTask | Cập nhật trạng thái bảo hành: / HOÀN THÀNH | HT |
| E_COMPLETE | endEvent | Quy trình bảo hành / hoàn thành | HT |
| T1 | userTask | Xem xét yêu cầu và / phê duyệt tiếp nhận | TP |
| G3 | exclusiveGateway | Phê duyệt / tiếp nhận? | TP |
| AND_S | parallelGateway | Thực hiện đồng thời | KT |
| K1 | manualTask | Kiểm tra tình trạng / thiết bị thực tế | KT |
| K2 | manualTask | Kiểm tra nguyên nhân / gây lỗi sản phẩm | KT |
| AND_J | parallelGateway | Chờ CẢ HAI / hoàn tất | KT |
| G4 | exclusiveGateway | Lỗi thuộc phạm vi / bảo hành? | KT |
| K3 | sendTask | Gửi yêu cầu khách hàng / bàn giao thiết bị | KT |
| K4 | receiveTask | Chờ tiếp nhận / thiết bị bàn giao | KT |
| B48 | boundaryEvent | Hạn: t₀ + 48 giờ / (Quá hạn bàn giao) | K4 |
| K5 | task | Đóng yêu cầu bảo hành / do quá thời hạn bàn giao | KT |
| E_TIMEOUT | endEvent | Đóng yêu cầu: / Quá hạn 48 giờ | KT |
| GM2 | exclusiveGateway |  | KT |
| K6 | manualTask | Tiến hành sửa chữa / thiết bị | KT |
| K7 | manualTask | Kiểm tra chất lượng / sau sửa chữa | KT |
| G5 | exclusiveGateway | Thiết bị đạt / yêu cầu? | KT |
| K8 | task | Hoàn tất xử lý kỹ thuật / và lập biên bản bàn giao | KT |

## Sequence — nét liền, mũi tên đặc

| ID | Nguồn | Đích | Nhãn | Điều kiện |
|---|---|---|---|---|
| F01 | S | GM1 |  |  |
| F02 | GM1 | C1 |  |  |
| F03 | C1 | G1 |  |  |
| F04 | G1 | C2 | Chưa đầy đủ | not info_complete |
| F05 | C2 | C3 |  |  |
| F06 | C3 | GM1 |  |  |
| F07 | G1 | S1 | Đầy đủ | info_complete |
| F08 | S1 | G2 |  |  |
| F09 | G2 | C4 | Hết hạn | not valid_warranty |
| F10 | C4 | E_EXPIRED |  |  |
| F11 | G2 | T1 | Còn hạn | valid_warranty |
| F12 | T1 | G3 |  |  |
| F13 | G3 | C5 | Không duyệt | not approved |
| F14 | C5 | E_REJECT_TP |  |  |
| F15 | G3 | AND_S | Phê duyệt | approved |
| F16 | AND_S | K1 |  |  |
| F17 | AND_S | K2 |  |  |
| F18 | K1 | AND_J |  |  |
| F19 | K2 | AND_J |  |  |
| F20 | AND_J | G4 |  |  |
| F21 | G4 | C6 | Ngoài phạm vi | not warranty_coverage |
| F22 | C6 | E_OUT_OF_SCOPE |  |  |
| F23 | G4 | K3 | Thuộc phạm vi | warranty_coverage |
| F24 | K3 | K4 |  |  |
| F25 | B48 | K5 | Quá 48 giờ |  |
| F26 | K5 | E_TIMEOUT |  |  |
| F27 | K4 | GM2 | Đã bàn giao đúng hạn |  |
| F28 | GM2 | K6 |  |  |
| F29 | K6 | K7 |  |  |
| F30 | K7 | G5 |  |  |
| F31 | G5 | GM2 | Chưa đạt | not quality_ok |
| F32 | G5 | K8 | Đạt yêu cầu | quality_ok |
| F33 | K8 | C7 |  |  |
| F34 | C7 | S2 |  |  |
| F35 | S2 | E_COMPLETE |  |  |

## Message — nét đứt, tròn rỗng, mũi tên rỗng

| ID | Nguồn | Đích | Nhãn | Điều kiện |
|---|---|---|---|---|
| M01 | KH | S | Yêu cầu bảo hành / (Thông tin SP / & mô tả lỗi) |  |
| M02 | C2 | KH | Yêu cầu bổ sung thông tin |  |
| M03 | KH | C3 | Thông tin bổ sung |  |
| M04 | C4 | KH | Thông báo từ chối: / Hết hạn bảo hành |  |
| M05 | C5 | KH | Thông báo từ chối: / Không được phê duyệt |  |
| M06 | C6 | KH | Thông báo từ chối: / Ngoài phạm vi bảo hành |  |
| M07 | K3 | KH | Yêu cầu bàn giao thiết bị / để sửa chữa |  |
| M08 | KH | K4 | Thông tin / Biên nhận / bàn giao thiết bị |  |
| M09 | C7 | KH | Thông báo nhận lại / thiết bị hoàn thành |  |

## Thuộc tính boundary timer

- Gắn vào `K4`; `cancelActivity=true`.
- Hạn được diễn đạt: `t_yeu_cau + PT48H`.
- Đây là metadata của sơ đồ draw.io, thể hiện quy tắc hạn bàn giao 48 giờ từ khi khách hàng nhận được yêu cầu.
