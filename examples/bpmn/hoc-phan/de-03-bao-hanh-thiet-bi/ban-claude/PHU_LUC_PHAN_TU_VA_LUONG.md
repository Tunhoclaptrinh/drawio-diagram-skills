# Phụ lục phần tử và luồng — Đề 03 bảo hành thiết bị

Danh mục trích từ `BPMN_Bao_hanh_thiet_bi.drawio`. SHA-256: `f9044c5249e40b08a58a1590c677893b0bbd8ab76ed9f7f9ec5e8538e66721b7`.
Bản có màu dùng cùng ID, nhãn, tọa độ và đường nối; chỉ khác thuộc tính màu.

## Phần tử

| ID | Loại BPMN | Nhãn | Lane / pool |
|---|---|---|---|
| KH | participant | KHÁCH HÀNG | — |
| DN | participant | DOANH NGHIỆP KINH DOANH THIẾT BỊ ĐIỆN TỬ | — |
| CSKH | lane | BỘ PHẬN CHĂM SÓC KHÁCH HÀNG | DN |
| HT | lane | HỆ THỐNG QUẢN LÝ BẢO HÀNH | DN |
| TP | lane | TRƯỞNG BỘ PHẬN KỸ THUẬT | DN |
| KT | lane | BỘ PHẬN KỸ THUẬT | DN |
| S | startEvent | Nhận được yêu cầu bảo hành | BỘ PHẬN CHĂM SÓC KHÁCH HÀNG |
| GM1 | exclusiveGateway |  | BỘ PHẬN CHĂM SÓC KHÁCH HÀNG |
| CS1 | task | Tiếp nhận yêu cầu, kiểm tra tính đầy đủ thông tin | BỘ PHẬN CHĂM SÓC KHÁCH HÀNG |
| G1 | exclusiveGateway | Thông tin đầy đủ? | BỘ PHẬN CHĂM SÓC KHÁCH HÀNG |
| CS2 | sendTask | Yêu cầu khách hàng bổ sung thông tin | BỘ PHẬN CHĂM SÓC KHÁCH HÀNG |
| CS3 | receiveTask | Nhận thông tin bổ sung | BỘ PHẬN CHĂM SÓC KHÁCH HÀNG |
| HT1 | serviceTask | Kiểm tra thời hạn bảo hành | HỆ THỐNG QUẢN LÝ BẢO HÀNH |
| G2 | exclusiveGateway | Còn hạn bảo hành? | HỆ THỐNG QUẢN LÝ BẢO HÀNH |
| CS4 | sendTask | Thông báo từ chối bảo hành miễn phí (hết hạn bảo hành) | BỘ PHẬN CHĂM SÓC KHÁCH HÀNG |
| E1 | endEvent | Từ chối: sản phẩm hết hạn bảo hành | BỘ PHẬN CHĂM SÓC KHÁCH HÀNG |
| TP1 | task | Xem xét yêu cầu, quyết định phê duyệt tiếp nhận | TRƯỞNG BỘ PHẬN KỸ THUẬT |
| G3 | exclusiveGateway | Phê duyệt tiếp nhận? | TRƯỞNG BỘ PHẬN KỸ THUẬT |
| E2 | endEvent | Từ chối: không phê duyệt tiếp nhận | TRƯỞNG BỘ PHẬN KỸ THUẬT |
| AND_S | parallelGateway | Thực hiện đồng thời | BỘ PHẬN KỸ THUẬT |
| KT1 | task | Kiểm tra tình trạng thiết bị | BỘ PHẬN KỸ THUẬT |
| KT2 | task | Kiểm tra nguyên nhân gây lỗi | BỘ PHẬN KỸ THUẬT |
| AND_J | parallelGateway | Chờ cả hai hoàn tất | BỘ PHẬN KỸ THUẬT |
| KTP | task | Đối chiếu kết quả với phạm vi bảo hành | BỘ PHẬN KỸ THUẬT |
| G4 | exclusiveGateway | Lỗi thuộc phạm vi bảo hành? | BỘ PHẬN KỸ THUẬT |
| CS5 | sendTask | Thông báo từ chối bảo hành miễn phí (lỗi ngoài phạm vi) | BỘ PHẬN CHĂM SÓC KHÁCH HÀNG |
| E3 | endEvent | Từ chối: lỗi ngoài phạm vi bảo hành | BỘ PHẬN CHĂM SÓC KHÁCH HÀNG |
| KT3 | task | Gửi yêu cầu bàn giao, ghi nhận lúc khách nhận yêu cầu (t₀) | BỘ PHẬN KỸ THUẬT |
| KT4 | manualTask | Tiếp nhận thiết bị khách hàng bàn giao | BỘ PHẬN KỸ THUẬT |
| B48 | boundaryEvent | Hết hạn t₀ + 48 giờ (t₀: lúc KH nhận yêu cầu) | BỘ PHẬN KỸ THUẬT |
| KT5 | task | Đóng yêu cầu bảo hành | BỘ PHẬN KỸ THUẬT |
| E4 | endEvent | Yêu cầu bị đóng: quá hạn bàn giao | BỘ PHẬN KỸ THUẬT |
| GM2 | exclusiveGateway |  | BỘ PHẬN KỸ THUẬT |
| KT6 | manualTask | Sửa chữa thiết bị | BỘ PHẬN KỸ THUẬT |
| KT7 | task | Kiểm tra chất lượng thiết bị | BỘ PHẬN KỸ THUẬT |
| G5 | exclusiveGateway | Thiết bị đạt yêu cầu? | BỘ PHẬN KỸ THUẬT |
| KT8 | task | Hoàn tất xử lý kỹ thuật | BỘ PHẬN KỸ THUẬT |
| CS6 | sendTask | Thông báo khách hàng nhận lại thiết bị | BỘ PHẬN CHĂM SÓC KHÁCH HÀNG |
| CS7 | task | Cập nhật trạng thái bảo hành: HOÀN THÀNH | BỘ PHẬN CHĂM SÓC KHÁCH HÀNG |
| E5 | endEvent | Bảo hành hoàn thành | BỘ PHẬN CHĂM SÓC KHÁCH HÀNG |

## Sequence — nét liền, mũi tên đặc

| ID | Nguồn | Đích | Nhãn | Điều kiện |
|---|---|---|---|---|
| F01 | S | GM1 |  |  |
| F02 | GM1 | CS1 |  |  |
| F03 | CS1 | G1 |  |  |
| F04 | G1 | CS2 | Chưa đầy đủ | not thong_tin_day_du |
| F05 | CS2 | CS3 |  |  |
| F06 | CS3 | GM1 |  |  |
| F07 | G1 | HT1 | Đầy đủ | thong_tin_day_du |
| F08 | HT1 | G2 |  |  |
| F09 | G2 | CS4 | Hết hạn | not con_han_bao_hanh |
| F10 | CS4 | E1 |  |  |
| F11 | G2 | TP1 | Còn hạn | con_han_bao_hanh |
| F12 | TP1 | G3 |  |  |
| F13 | G3 | E2 | Không | not phe_duyet |
| F14 | G3 | AND_S | Có | phe_duyet |
| F15 | AND_S | KT1 |  |  |
| F16 | AND_S | KT2 |  |  |
| F17 | KT1 | AND_J |  |  |
| F18 | KT2 | AND_J |  |  |
| F19 | AND_J | KTP |  |  |
| F19b | KTP | G4 |  |  |
| F20 | G4 | CS5 | Không thuộc phạm vi | not loi_thuoc_pham_vi |
| F21 | CS5 | E3 |  |  |
| F22 | G4 | KT3 | Thuộc phạm vi | loi_thuoc_pham_vi |
| F23 | KT3 | KT4 |  |  |
| F24 | KT4 | GM2 |  |  |
| F25 | B48 | KT5 | Quá hạn |  |
| F26 | KT5 | E4 |  |  |
| F27 | GM2 | KT6 |  |  |
| F28 | KT6 | KT7 |  |  |
| F29 | KT7 | G5 |  |  |
| F30 | G5 | GM2 | Chưa đạt | not dat_chat_luong |
| F31 | G5 | KT8 | Đạt | dat_chat_luong |
| F32 | KT8 | CS6 |  |  |
| F33 | CS6 | CS7 |  |  |
| F34 | CS7 | E5 |  |  |

## Message — nét đứt, tròn rỗng đầu gửi, mũi tên rỗng đầu nhận

| ID | Nguồn | Đích | Nhãn | Điều kiện |
|---|---|---|---|---|
| M01 | KH | S | Yêu cầu bảo hành (thông tin sản phẩm, mô tả lỗi) |  |
| M02 | CS2 | KH | Yêu cầu bổ sung thông tin |  |
| M03 | KH | CS3 | Thông tin bổ sung |  |
| M04 | CS4 | KH | Thông báo từ chối (hết hạn bảo hành) |  |
| M05 | CS5 | KH | Thông báo từ chối (lỗi ngoài phạm vi) |  |
| M06 | KT3 | KH | Yêu cầu bàn giao thiết bị (hạn 48 giờ) |  |
| M07 | CS6 | KH | Thông báo nhận lại thiết bị |  |

## Thuộc tính boundary timer

- Gắn vào `KT4`; `cancelActivity=true` (interrupting, hai vòng nét liền).
- Hạn được diễn đạt: `t_kh_nhan_yeu_cau_ban_giao + PT48H`.
- Đây là metadata của sơ đồ draw.io diễn đạt quy tắc nghiệp vụ, không phải biểu thức timeDate thực thi đã nối với đồng hồ hoặc kênh thông báo.
