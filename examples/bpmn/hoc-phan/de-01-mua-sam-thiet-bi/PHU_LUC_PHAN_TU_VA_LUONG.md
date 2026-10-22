# Phụ lục phần tử và luồng — Đề 01

Danh mục trích từ `BPMN_De_01.drawio`. SHA-256: `ee2d277ef0c674a175a6e019007a95c42da3c753ecb0d3c8359bffdc077a681b`.

## Phần tử

| ID | Loại BPMN | Nhãn | Parent |
|---|---|---|---|
| DN | participant | DOANH NGHIỆP | 1 |
| NV | lane | NHÂN VIÊN | DN |
| TP | lane | TRƯỞNG PHÒNG | DN |
| HC | lane | HÀNH CHÍNH | DN |
| NCC | participant | NHÀ CUNG CẤP — participant bên ngoài (black box) | 1 |
| S | startEvent | Phát sinh nhu cầu | NV |
| N1 | task | Lập và gửi yêu cầu mua sắm / Tên thiết bị, SL, mục đích, / chi phí dự kiến | NV |
| N2 | task | Bổ sung thông tin / yêu cầu mua sắm | NV |
| H1 | task | Tiếp nhận và kiểm tra / tính đầy đủ thông tin | HC |
| G1 | exclusiveGateway | Thông tin đầy đủ? | HC |
| H2 | task | Kiểm tra ngân sách / còn lại của phòng ban | HC |
| G2 | exclusiveGateway | Ngân sách đủ? | HC |
| R1 | task | Từ chối yêu cầu và / thông báo nhân viên | HC |
| ER1 | endEvent | Từ chối: thiếu ngân sách | HC |
| T1 | task | Xem xét và quyết định / phê duyệt yêu cầu | TP |
| G3 | exclusiveGateway | Phê duyệt? | TP |
| ER2 | endEvent | Từ chối: không phê duyệt | TP |
| AND_S | parallelGateway | Thực hiện đồng thời | HC |
| H3 | task | Tìm kiếm / nhà cung cấp | HC |
| H4 | task | Chuẩn bị hồ sơ / đặt mua | HC |
| AND_J | parallelGateway | Chờ CẢ HAI hoàn tất | HC |
| H5 | sendTask | Gửi đơn đặt mua / cho nhà cung cấp | HC |
| H6 | receiveTask | Chờ xác nhận / đơn đặt mua | HC |
| B48 | boundaryEvent | Hạn: t₀ + 48 giờ | H6 |
| CANCEL | task | Hủy đơn mua và / thông báo nhân viên | HC |
| EC | endEvent | Đơn mua đã hủy / quá hạn xác nhận | HC |
| H7 | receiveTask | Nhận thông tin bàn giao / thiết bị / thiết bị thay thế | HC |
| H8 | manualTask | Tiếp nhận và / kiểm tra thiết bị | HC |
| G4 | exclusiveGateway | Thiết bị đạt yêu cầu? | HC |
| H9 | task | Gửi trả thiết bị / và yêu cầu thay thế | HC |
| H10 | manualTask | Bàn giao thiết bị / cho nhân viên | HC |
| N3 | task | Xác nhận đã / nhận thiết bị | NV |
| H11 | task | Cập nhật yêu cầu: / HOÀN THÀNH | HC |
| E | endEvent | Yêu cầu hoàn thành | HC |

## Sequence — nét liền, mũi tên đặc

| ID | Nguồn | Đích | Nhãn | Điều kiện |
|---|---|---|---|---|
| F01 | S | N1 |  |  |
| F02 | N1 | H1 |  |  |
| F03 | H1 | G1 |  |  |
| F04 | G1 | N2 | Chưa đầy đủ | not information_complete |
| F05 | N2 | H1 |  |  |
| F06 | G1 | H2 | Đầy đủ | information_complete |
| F07 | H2 | G2 |  |  |
| F08 | G2 | R1 | Không đủ | not budget_sufficient |
| F09 | R1 | ER1 |  |  |
| F10 | G2 | T1 | Đủ ngân sách | budget_sufficient |
| F11 | T1 | G3 |  |  |
| F12 | G3 | ER2 | Không | not approved |
| F13 | G3 | AND_S | Có | approved |
| F14 | AND_S | H3 |  |  |
| F15 | AND_S | H4 |  |  |
| F16 | H3 | AND_J |  |  |
| F17 | H4 | AND_J |  |  |
| F18 | AND_J | H5 |  |  |
| F19 | H5 | H6 |  |  |
| F20 | B48 | CANCEL |  |  |
| F21 | CANCEL | EC |  |  |
| F22 | H6 | H7 | Đã xác nhận đúng hạn |  |
| F23 | H7 | H8 |  |  |
| F24 | H8 | G4 |  |  |
| F25 | G4 | H9 | Không đạt | not equipment_ok |
| F26 | H9 | H7 | Chờ thiết bị thay thế |  |
| F27 | G4 | H10 | Đạt | equipment_ok |
| F28 | H10 | N3 |  |  |
| F29 | N3 | H11 |  |  |
| F30 | H11 | E |  |  |

## Message — nét đứt, tròn rỗng, mũi tên rỗng

| ID | Nguồn | Đích | Nhãn | Điều kiện |
|---|---|---|---|---|
| M01 | H5 | NCC | Đơn đặt mua |  |
| M02 | NCC | H6 | Xác nhận đơn |  |
| M03 | NCC | H7 | Thông tin bàn giao / giao thay thế |  |
| M04 | H9 | NCC | Yêu cầu thay thế + kết quả kiểm tra |  |

## Thuộc tính boundary timer

- Gắn vào `H6`; `cancelActivity=true`.
- Hạn được diễn đạt: `t_ncc_nhan + PT48H`.
- Đây là metadata của sơ đồ draw.io, không phải một BPMN executable timeDate đã liên kết với đồng hồ hoặc kênh nhận đơn.
