# Đặt trước thiết bị dùng chung

Tạo lại bằng `python3 skills/bpmn-drawio/scripts/create_demo.py --output-dir THƯ_MỤC`.

| Bản | Nguồn chỉnh sửa | Ảnh |
|---|---|---|
| Thường (`monochrome`) | [Demo.drawio](Demo.drawio) | [01-dat-truoc-thiet-bi-dung-chung.png](normal/01-dat-truoc-thiet-bi-dung-chung.png) · [01-dat-truoc-thiet-bi-dung-chung.svg](normal/01-dat-truoc-thiet-bi-dung-chung.svg) · [01-dat-truoc-thiet-bi-dung-chung.pdf](normal/01-dat-truoc-thiet-bi-dung-chung.pdf) |
| Màu (`bizagi-inspired`) | [Demo_Co_mau.drawio](Demo_Co_mau.drawio) | [01-dat-truoc-thiet-bi-dung-chung.png](color/01-dat-truoc-thiet-bi-dung-chung.png) · [01-dat-truoc-thiet-bi-dung-chung.svg](color/01-dat-truoc-thiet-bi-dung-chung.svg) · [01-dat-truoc-thiet-bi-dung-chung.pdf](color/01-dat-truoc-thiet-bi-dung-chung.pdf) |

![Bản màu](color/01-dat-truoc-thiet-bi-dung-chung.png)


Ví dụ tổng hợp, không sử dụng đề thi hoặc dữ liệu khách hàng.

| Yêu cầu | Phần tử | Kịch bản |
|---|---|---|
| Nhận yêu cầu từ bên ngoài | CUSTOMER, M, S | Một thông điệp tạo một lần xử lý |
| Kiểm tra tồn khả dụng trước quyết định | CHECK, G | available và requested là số nguyên không âm đã được kiểm tra |
| Đủ thiết bị thì ghi nhận và giữ số lượng | F5, RESERVE, E_OK | Không thực hiện nhánh từ chối |
| Thiếu thiết bị thì thông báo | F3, REJECT, E_NO | Không giữ thiết bị |

Một pool đơn vị quản lý, hai lane phân vai; khách là pool black-box. Sequence đi qua lane trong cùng pool. Message M có nét đứt, vòng gửi và đầu mũi tên rỗng; không truyền token qua pool.

CHECK tạo kết quả tồn khả dụng; G chỉ đọc điều kiện. RESERVE hoàn tất khi đặt trước và giữ thiết bị đã được ghi nhận. REJECT là tác vụ tổng quát vì đề tự đặt chưa xác định kênh thông báo.

Giả định: yêu cầu đã có định danh và số lượng hợp lệ; kiểm tra và giữ thiết bị không có cạnh tranh từ yêu cầu khác trong phạm vi minh họa. Dùng thật cần xác định cơ chế giữ chỗ nguyên tử và xử lý đồng thời; biểu đồ này không chứng minh điều đó. Pool black-box không mô tả việc khách làm sau khi nhận phản hồi.

Walkthrough: available=3/requested=2 → S,CHECK,G,RESERVE,E_OK; available=1/requested=2 → S,CHECK,G,REJECT,E_NO; available=2/requested=2 → nhánh đủ. Mỗi lần chỉ có một kết thúc, không có AND join.

Vẽ lại: đặt hai pool, hai lane trong pool đơn vị; đặt trigger/kiểm tra/gateway trên lane tiếp nhận; nhánh thiếu đi thẳng, nhánh đủ đi xuống lane kho; nối sequence và đặt predicate; tạo bản màu bằng theme, giữ nguyên hình học.

## Chú giải màu

| Role | Fill |
|---|---|
| start | `#bbf7d0` |
| end | `#fecaca` |
| intermediate | `#fde68a` |
| gateway | `#fef08a` |
| activity | `#dbeafe` |
| frame | `#eff6ff` |
| header | `#e2e8f0` |
| body | `#ffffff` |
