# Document check and review — Kiểm tra và thẩm định hồ sơ

Synthetic example. Ví dụ tự đặt: hệ thống kiểm tra hình thức hồ sơ. Không hợp lệ thì ghi lý do và kết thúc. Hợp lệ thì người thẩm định dùng ứng dụng chọn duyệt hoặc từ chối; hệ thống ghi kết quả tương ứng. Hợp lệ hình thức không đồng nghĩa chắc chắn được duyệt.

| Variant | Editable source | Images |
|---|---|---|
| Normal | [document-review.drawio](document-review.drawio) | [document-review.png](normal/document-review.png) · [document-review.svg](normal/document-review.svg) |
| Colour | [document-review-color.drawio](document-review-color.drawio) | [document-review.png](color/document-review.png) · [document-review.svg](color/document-review.svg) |

![Colour variant: one pool, two lanes, three outcomes; every end is red](color/document-review.png)

**Walkthrough / Đi thử:** S → T1 → G1 [Không] → TI → EI; hoặc G1 [Có] → T2 → G2 [Có] → TA → EA; hoặc G2 [Không] → TR → ER. T1 tạo kết quả kiểm tra, T2 tạo quyết định; hai gateway chỉ đọc dữ liệu đã có, không tự thẩm định.
