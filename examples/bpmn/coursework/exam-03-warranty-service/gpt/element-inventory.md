# Phụ lục toàn bộ phần tử và đường nối

Nguồn: `diagram.drawio`. SHA-256: `4a3c3ef0e367fd3bc444274eb99100dced17a8cd9e12cc2d9ac88192c876070b`.

## Phần tử

| ID | Loại | Nhãn | Pool/lane hoặc parent |
|---|---|---|---|
| KH | participant | KHÁCH HÀNG | 1 |
| DN | participant | DOANH NGHIỆP BẢO HÀNH | 1 |
| CS | lane | CHĂM SÓC / KHÁCH HÀNG | DN |
| HT | lane | HỆ THỐNG | DN |
| TP | lane | TRƯỞNG BỘ PHẬN / KỸ THUẬT | DN |
| KT | lane | BỘ PHẬN KỸ THUẬT | DN |
| S | startEvent | Nhận được yêu cầu / bảo hành | CS |
| C1 | task | Tiếp nhận và kiểm tra / thông tin yêu cầu | CS |
| GI | exclusiveGateway | Thông tin / đầy đủ? | CS |
| C2 | sendTask | Yêu cầu khách hàng / bổ sung thông tin | CS |
| C3 | receiveTask | Nhận thông tin / khách hàng bổ sung | CS |
| SYS | serviceTask | Kiểm tra thời hạn / bảo hành sản phẩm | HT |
| GW | exclusiveGateway | Còn hạn / bảo hành? | HT |
| C4 | sendTask | Thông báo từ chối / bảo hành miễn phí / (hết hạn) | CS |
| E_EXP | endEvent | Từ chối miễn phí: / hết hạn | CS |
| T1 | task | Xem xét và quyết định / phê duyệt tiếp nhận | TP |
| GA | exclusiveGateway | Phê duyệt / tiếp nhận? | TP |
| E_APP | endEvent | Từ chối: / không phê duyệt | TP |
| AND_S | parallelGateway |  | KT |
| K1 | task | Kiểm tra tình trạng / thiết bị | KT |
| K2 | task | Kiểm tra nguyên nhân / gây lỗi | KT |
| AND_J | parallelGateway |  | KT |
| K3 | task | Đối chiếu lỗi với / phạm vi bảo hành | KT |
| GS | exclusiveGateway | Thuộc phạm vi / bảo hành? | KT |
| C5 | sendTask | Thông báo từ chối / bảo hành miễn phí / (ngoài phạm vi) | CS |
| E_SCOPE | endEvent | Từ chối miễn phí: / ngoài phạm vi | CS |
| K4 | task | Yêu cầu bàn giao / và ghi nhận thời điểm / khách nhận yêu cầu | KT |
| WAIT | task | Chờ và tiếp nhận / thiết bị bàn giao | KT |
| B48 | boundaryEvent | Hết hạn: / t₀ + 48 giờ | WAIT |
| CLOSE | task | Đóng yêu cầu bảo hành / quá hạn bàn giao | KT |
| E_TIME | endEvent | Đã đóng yêu cầu: / quá hạn bàn giao | KT |
| REPAIR | manualTask | Sửa chữa / thiết bị | KT |
| QA | manualTask | Kiểm tra chất lượng / thiết bị | KT |
| GQ | exclusiveGateway | Thiết bị đạt / yêu cầu? | KT |
| FIN | task | Hoàn tất xử lý / kỹ thuật | KT |
| C6 | sendTask | Thông báo khách hàng / nhận lại thiết bị | CS |
| C7 | task | Cập nhật bảo hành: / HOÀN THÀNH | CS |
| E_OK | endEvent | Bảo hành / hoàn thành | CS |

## Sequence — nét liền, mũi tên đặc

| ID | Nguồn | Đích | Nhãn | Điều kiện |
|---|---|---|---|---|
| F01 | S | C1 |  |  |
| F02 | C1 | GI |  |  |
| F03 | GI | C2 | Chưa đầy đủ | not information_complete |
| F04 | C2 | C3 |  |  |
| F05 | C3 | C1 |  |  |
| F06 | GI | SYS | Đầy đủ | information_complete |
| F07 | SYS | GW |  |  |
| F08 | GW | C4 | Hết hạn | not warranty_active |
| F09 | C4 | E_EXP |  |  |
| F10 | GW | T1 | Còn hạn | warranty_active |
| F11 | T1 | GA |  |  |
| F12 | GA | E_APP | Không | not approved |
| F13 | GA | AND_S | Có | approved |
| F14 | AND_S | K1 |  |  |
| F15 | AND_S | K2 |  |  |
| F16 | K1 | AND_J |  |  |
| F17 | K2 | AND_J |  |  |
| F18 | AND_J | K3 |  |  |
| F19 | K3 | GS |  |  |
| F20 | GS | C5 | Không | not covered_fault |
| F21 | C5 | E_SCOPE |  |  |
| F22 | GS | K4 | Có | covered_fault |
| F23 | K4 | WAIT |  |  |
| F24 | B48 | CLOSE |  |  |
| F25 | CLOSE | E_TIME |  |  |
| F26 | WAIT | REPAIR | Đã nhận thiết bị / đúng hạn |  |
| F27 | REPAIR | QA |  |  |
| F28 | QA | GQ |  |  |
| F29 | GQ | REPAIR | Chưa đạt — sửa và kiểm tra lại | not quality_ok |
| F30 | GQ | FIN | Đạt | quality_ok |
| F31 | FIN | C6 |  |  |
| F32 | C6 | C7 |  |  |
| F33 | C7 | E_OK |  |  |

## Message — nét đứt, vòng tròn gửi rỗng và mũi tên nhận rỗng

| ID | Nguồn | Đích | Nhãn | Điều kiện |
|---|---|---|---|---|
| M01 | KH | S | Yêu cầu bảo hành / Thông tin sản phẩm / và mô tả lỗi |  |
| M02 | C2 | KH | Yêu cầu bổ sung / thông tin |  |
| M03 | KH | C3 | Thông tin / bổ sung |  |
| M04 | C4 | KH | Thông báo từ chối / (hết hạn) |  |
| M05 | C5 | KH | Thông báo từ chối / (lỗi ngoài phạm vi) |  |
| M06 | K4 | KH | Yêu cầu bàn giao / thiết bị |  |
| M07 | C6 | KH | Thông báo / nhận lại thiết bị |  |

## Timer và bàn giao

- `K4` là Task thường: gửi yêu cầu và ghi nhận mốc khách nhận thực tế; chỉ hoàn tất khi `t_customer_received_request` đã có.
- Không dùng Send Task cho K4 vì Send Task hoàn tất khi gửi, không xác nhận việc nhận. Dữ liệu nhận do kênh giao tiếp cung cấp, không tự thêm một yêu cầu KH chấp thuận.
- `B48` gắn `WAIT`, `cancelActivity=true`, hai vòng nét liền.
- Quy tắc hạn tuyệt đối: `t_customer_received_request + PT48H`.
- `WAIT` chỉ hoàn thành với bàn giao thực tế trong hạn; không có message flow nào biểu diễn vật phẩm được vận chuyển.
- Thuộc tính trong draw.io là metadata mô tả, không phải BPMN 2.0 XML triển khai engine.
