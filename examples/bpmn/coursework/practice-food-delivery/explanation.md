# BPMN — Ứng dụng gọi đồ ăn

Bộ lời giải cho bài thực hành và bài mở rộng trong *BPMN — Ứng dụng gọi đồ ăn* (đề thực hành của học phần, không đính kèm). Phần ký pháp đối chiếu với [OMG BPMN 2.0.2](https://www.omg.org/spec/BPMN/2.0.2/PDF).

Lần rà soát mới nhất có báo cáo toàn diện và phụ lục toàn bộ phần tử/đường nối. Báo cáo tách dữ kiện đề, giả định, nghiệp vụ, ký pháp, màu và các giới hạn kiểm tra.

## 1. Mở kết quả

- **File chỉnh sửa:** [diagram.drawio](diagram.drawio). Vào draw.io → **File → Open From → Device** rồi chọn file. Chuyển trang bằng các tab phía dưới.
- **Phiên bản có màu:** [diagram-color.drawio](diagram-color.drawio), cùng logic và bố cục. Xem [README](README.md) để mở ảnh từng trang và đọc bảng màu.
- **Trang 01 — Quy trình tổng thể:** [PNG](page-01-overview.png) · [SVG](page-01-overview.svg).
- **Trang 02 — Không tìm được tài xế:** [PNG](page-02-no-driver-found.png) · [SVG](page-02-no-driver-found.svg).
- **Trang 03 — Chuẩn bị và giao món:** [PNG](page-03-preparation-and-delivery.png) · [SVG](page-03-preparation-and-delivery.svg).

Các phần tử trong `.drawio` là hình, chữ và đường nối riêng biệt, có thể kéo và sửa. SVG phù hợp để phóng to mà chữ vẫn nét. `.drawio` là định dạng sơ đồ của draw.io, không phải file mô hình thực thi BPMN 2.0 XML `.bpmn`.

Ba trang là các góc nhìn của cùng bài toán. **Không nối sequence flow từ trang này sang trang khác.** Trang 02 mô tả nội dung của SP1; trang 03 phóng to tương tác chuẩn bị–giao ở nhánh thành công.

## 2. Đọc đề và chốt phạm vi

| Nội dung | Vị trí trong đề | Áp dụng trong lời giải |
|---|---|---|
| Một đơn thuộc một nhà hàng; online, không COD; nhà hàng đồng ý rồi mới thu tiền | Trang PDF 11 | A03 → AG1 → A04 |
| Bốn bên độc lập: khách hàng, nền tảng, nhà hàng, tài xế | Trang PDF 12 | Bốn pool ở mỗi trang |
| Nhận và kiểm tra đơn; xác nhận; thu tiền; chuẩn bị; phân công; báo giao xong | Trang PDF 13–15 | Luồng chính trang 01 |
| Nhà hàng từ chối, thanh toán thất bại | Trang PDF 16 | AG1/AG2 → nhánh hủy trước thu tiền |
| Chuẩn bị món, báo sẵn sàng, lấy món và giao | Trang PDF 17 | Trang 03 |
| Chờ nhà hàng quá 2 phút; timer ngắt tác vụ đang chờ | Trang PDF 18 | AT1 gắn trên A03 |
| Đã thanh toán nhưng không tìm được tài xế; hủy, thông báo, hoàn tiền; tranh chấp với hết hạn | Trang PDF 20 | SP1 và toàn bộ trang 02 |

Điểm bắt đầu của quy trình nền tảng là **nhận đơn mới**. Điểm kết thúc là **giao hoàn tất**, **hủy khi chưa thu tiền**, hoặc **hủy sau khi đã hoàn tiền**.

### Những giả định cần nói rõ khi trình bày bài

1. **Thông tin đầu vào hợp lệ.** A01 kiểm tra thông tin; bài này không tự thêm tình huống sai địa chỉ, giá thay đổi, món hết hàng ngoài phản hồi nhà hàng. Nếu giảng viên yêu cầu xử lý dữ liệu không hợp lệ, bổ sung XOR sau A01.
2. **Tìm tài xế tối đa 5 phút.** Đây là giả định của lời giải; đề chỉ quy định **2 phút chờ nhà hàng**, chưa quy định thời gian tìm tài xế. Có thể đổi 5 phút thành tham số `T`.
3. **Thanh toán thất bại nghĩa là chưa thu tiền.** Không bao gồm tình huống cổng thanh toán đã trừ tiền nhưng phản hồi bị thất lạc. Tình huống đó cần đối soát riêng, không được kết luận ngay “chưa thu tiền”.
4. **Chính sách bài thực hành cho phép hủy khi nhà hàng quá 2 phút.** A09 vẫn thể hiện bước kiểm tra chính sách theo đề. Trong phạm vi đã chọn, kết quả của A09 dẫn đến hủy; chưa mở rộng nhánh được phép chờ tiếp.
5. **Yêu cầu chuẩn bị được gửi trước khi tìm tài xế.** Vì vậy khi không tìm được tài xế, phải thông báo hủy/dừng chuẩn bị cho nhà hàng. Chính sách bồi hoàn món đã chế biến chưa được đề quy định, nên không tự thêm số tiền bồi hoàn.
6. **Nhận chuyến ban đầu là một đề nghị.** Tài xế chỉ được coi là đã nhận chuyến sau khi nền tảng chốt và gửi M05. Đề nghị đến đúng hạn hoặc sau hạn không tự tạo phân công.
7. **Thông điệp được gắn mã đơn và lưu khi bên nhận chưa chờ.** Ví dụ món sẵn sàng trước khi có tài xế: lưu M14 theo `order_id`, chuyển cho đúng tài xế khi bắt đầu chờ. Điều này tránh mất thông điệp khi hai bên chạy độc lập.
8. **B06 chỉ kết thúc khi hoàn tiền đã được xác nhận.** Nếu hoàn tiền lỗi hoặc còn chờ xử lý thủ công, subprocess vẫn chưa hoàn thành; không đi đến end “đã hoàn tiền”. Chi tiết tích hợp cổng thanh toán và xử lý lỗi hoàn tiền nằm dưới mức phân rã của bài này.

## 3. Vì sao dùng bốn pool?

**Pool biểu diễn participant; lane phân chia vai trò bên trong một participant.** Đề đã chọn bốn bên độc lập, nên vẽ bốn pool: khách hàng, nền tảng, nhà hàng, tài xế. Không thay bằng bốn lane của một pool vì sẽ làm sai ranh giới trao đổi thông điệp đã được đề xác định.

Trang 01 hiển thị chi tiết nền tảng. Ba pool còn lại là **black box**: để trống phần bên trong nhưng vẫn nối message flow vào ranh giới. Đây chính là cách đề gợi ý ở trang PDF 15. Không cần thêm lane “Hỗ trợ” vì bài chưa mô hình hóa quy trình hỗ trợ.

Trang 02 tiếp tục hiển thị nền tảng; SP1 được mở ra bên trong pool này. Trang 03 hiển thị chi tiết nhà hàng và tài xế; nền tảng và khách hàng trở thành black box. Không có yêu cầu mọi participant đều phải mở chi tiết trong cùng một hình.

## 4. Trang 01 — Quy trình tổng thể

### 4.1. Luồng thành công

**A00 → A01 → A02 → A03 → AG1 [Có] → A04 → AG2 [Có] → A05 → SP1 → AG3 [Có] → A06 → A07 → A08 → AE1.**

| Mã | Phần tử BPMN | Nghiệp vụ và lý do chọn |
|---|---|---|
| A00 | Message start event | Đơn mới từ khách hàng khởi tạo một instance của quy trình nền tảng |
| A01 | Service task | Kiểm tra thông tin đơn theo phạm vi đầu vào hợp lệ |
| A02 | Send task | Gửi yêu cầu xác nhận đến nhà hàng qua M02 |
| A03 | Receive task | Chờ M03; tác vụ gửi A02 hoàn thành không có nghĩa là nhà hàng đã trả lời |
| AG1 | Exclusive gateway | Kiểm tra nội dung phản hồi: nhà hàng đồng ý hay từ chối |
| A04 | Service task | Thu tiền và chỉ hoàn thành khi đã có kết quả thanh toán |
| AG2 | Exclusive gateway | Tách nhánh thanh toán thành công/thất bại theo kết quả A04 |
| A05 | Send task | Yêu cầu nhà hàng chuẩn bị món qua M04 |
| SP1 | Collapsed subprocess | Tìm/chốt tài xế hoặc xử lý hủy và hoàn tiền; mở rộng ở trang 02 |
| AG3 | Exclusive gateway | Đọc kết quả SP1: đã gán hoặc đã hủy và hoàn tiền |
| A06 | Send task | Gửi M05 xác nhận phân công cho tài xế đã được chốt |
| A07 | Receive task | Chờ M06 báo giao hoàn tất, không tự đi tiếp ngay sau phân công |
| A08 | Send task | Thông báo hoàn tất cho khách qua M07 |
| AE1 | None end event | Kết thúc quy trình nền tảng ở kết quả giao thành công |

**AG1/AG2/AG3 là nơi quyết định, không phải nơi thực hiện công việc.** Thu tiền nằm ở A04; gateway chỉ đọc kết quả.

### 4.2. Nhà hàng từ chối

**A03 → AG1 [Không] → AG4 → A10 → A11 → AE2.**

Nhà hàng có phản hồi, nhưng nội dung là từ chối. Hệ thống hủy đơn, lưu lý do và thông báo cho khách. A04 chưa chạy nên **không có bước hoàn tiền** trên nhánh này.

### 4.3. Thanh toán thất bại

**A04 → AG2 [Không] → AG4 → A10 → A11 → AE2.**

Nhà hàng đã đồng ý nhưng thu tiền thất bại theo giả định ở mục 2. Chưa gửi yêu cầu chuẩn bị A05, chưa phân công A06. Nhánh này dùng cùng phần hủy/thông báo với nhánh từ chối, nhưng lưu lý do “thanh toán thất bại”. Việc thông báo nhà hàng hủy giữ chỗ sơ bộ chưa được đề yêu cầu; quy trình chi tiết phản hồi xác nhận của nhà hàng nằm ngoài góc nhìn trang 01.

### 4.4. Nhà hàng không phản hồi trong 2 phút

**AT1 → A09 → AG4 → A10 → A11 → AE2.**

AT1 là **interrupting boundary timer** gắn lên A03. Bộ đếm bắt đầu khi A03 được kích hoạt. Khi hết thời gian, A03 bị ngắt và token đi theo nhánh timeout. Không cần nhận được phản hồi rồi mới kiểm tra “đã quá 2 phút chưa”.

Nếu A03 hoàn thành trước, timer bị gỡ khỏi tác vụ. Phản hồi nhà hàng đến muộn phải được đối chiếu trạng thái đơn, không được làm sống lại đơn đã hủy.

**AG4 chỉ nhập các nhánh loại trừ nhau.** Nó không đợi đủ cả từ chối, lỗi thanh toán và timeout. Dùng AND tại đây sẽ gây chờ những nhánh không bao giờ chạy.

### 4.5. Không tìm được tài xế sau thanh toán

SP1 tự xử lý nhánh hủy, yêu cầu dừng chuẩn bị, thu hồi lời mời, hoàn tiền và thông báo. Khi SP1 trả về “đã hủy và hoàn tiền”, **AG3 [Không] → AE3**. Không chạy A06, A07 hoặc A08 và không hoàn tiền lần thứ hai ở quy trình cha.

## 5. Trang 02 — Lời giải ba câu hỏi bài mở rộng

### Câu 1: Tác vụ nào chờ, hết thời gian khi nào?

**B02 — Chờ đề nghị nhận chuyến hợp lệ** là receive task đang chờ. **BT1** là timer ngắt gắn vào biên dưới của B02, với thời lượng giả định `T = 5 phút` tính từ lúc B02 bắt đầu. B01 chỉ gửi lời mời; gửi xong chưa có nghĩa là đã có tài xế.

Hai lối ra của việc chờ:

- Nhận M10: B02 hoàn thành → BG0.
- Hết thời gian: BT1 ngắt B02 → BG0.

**BG0 là XOR nhập nhánh**. Nó không chọn ai thắng và không đợi đồng bộ; cơ chế receive task + interrupting timer đã loại trừ hai hướng thực thi trong cùng instance. Sau đó B03 kiểm tra/chốt kết quả nghiệp vụ.

### Câu 2: Hủy, thông báo các bên và hoàn tiền nằm ở đâu?

| Mã | Hành động |
|---|---|
| B03 | Chốt kết quả dưới khóa/giao dịch nguyên tử theo mã đơn: ĐÃ GÁN hoặc ĐÃ HỦY |
| BG1 [Không] | Đi tiếp theo trạng thái ĐÃ HỦY đã được chốt |
| B04 | Gửi M11 yêu cầu nhà hàng hủy/dừng chuẩn bị món |
| B05 | Gửi M12 thu hồi lời mời đến các tài xế đang được mời |
| B06 | Thực hiện hoàn tiền, chờ và xác nhận kết quả |
| B07 | Gửi M13 thông báo đơn hủy và kết quả hoàn tiền cho khách |
| BE2 | Kết thúc SP1, trả về ĐÃ HỦY VÀ HOÀN TIỀN |

B04/B05 là tác vụ **gửi**, chưa bao gồm chờ xác nhận nhà hàng/tài xế đã thực hiện xong. Kết thúc quy trình nền tảng không tự chứng minh mọi quy trình bên ngoài đều kết thúc. Nếu yêu cầu giảng viên đòi xác nhận dừng món, cần bổ sung receive task/timeout tương ứng.

B06 là một subprocess thu gọn. Nội dung tối thiểu khi cần phân rã thêm: tạo yêu cầu hoàn tiền theo giao dịch gốc → chờ kết quả → nếu thành công thì kết thúc; nếu lỗi thì thử lại hoặc chuyển xử lý thủ công và tiếp tục chờ kết quả. Yêu cầu lặp lại phải dùng cùng khóa nghiệp vụ để không hoàn trùng. Bài hiện tại không thể hiện chi tiết này thành trang riêng.

### Câu 3: Nếu tài xế nhận đúng lúc hết hạn?

**BPMN cần đi kèm quy tắc chốt trạng thái của nghiệp vụ.** Vẽ một XOR sau hai đường chạy song song không tự bảo đảm chống tranh chấp.

Quy tắc chọn cho bài này:

1. B03 đọc và cập nhật trạng thái đơn trong **một thao tác nguyên tử** theo `order_id`.
2. Chỉ gán tài xế nếu trạng thái còn `SEARCHING`, đề nghị đúng đơn/đúng tài xế đủ điều kiện, chưa có tài xế được gán, và **thời điểm chốt nhỏ hơn hạn chót**.
3. Nếu thời điểm chốt **bằng hoặc lớn hơn hạn chót**, chốt `CANCELLED`. Đây là chính sách xử lý hòa do lời giải bổ sung, không phải quy tắc bắt buộc của BPMN.
4. Nếu đã có kết quả cuối của lần xử lý trước, trả lại kết quả đó. Không chuyển `ASSIGNED` sang `CANCELLED` hoặc chuyển `CANCELLED` sang `ASSIGNED` bằng một callback đến muộn.
5. Chỉ gửi M05 khi trạng thái cuối là `ASSIGNED`. Chỉ hoàn tiền khi trạng thái cuối là `CANCELLED` và có giao dịch thu tiền cần hoàn.

| Tình huống | Kết quả |
|---|---|
| Nhận đề nghị và chốt trước hạn | ĐÃ GÁN → BE1 → về trang 01 → A06 |
| Không có đề nghị, BT1 hết hạn | ĐÃ HỦY → B04–B07 → BE2 |
| Đề nghị đến trước hạn nhưng việc chốt diễn ra sau hạn | ĐÃ HỦY, theo chính sách dùng thời điểm chốt |
| Đề nghị và hết hạn trùng thời điểm | ĐÃ HỦY, vì điều kiện gán là `< hạn chót` |
| Đề nghị đến sau khi đơn đã hủy | Bị coi là hết hiệu lực; không phát M05, không mở lại đơn |
| Callback/timeout được giao lặp | Đọc lại kết quả đã chốt; không phân công hoặc hoàn tiền trùng |

Trong một instance BPMN, timer ngắt và receive task cho ra một nhánh đang hoạt động. Khi triển khai bằng nhiều worker, vẫn phải bảo vệ thao tác chốt và các tác dụng phụ; ký pháp của sơ đồ không thay thế khóa/giao dịch/idempotency của hệ thống.

## 6. Trang 03 — Nhà hàng và tài xế phối hợp

Trang này chỉ mô tả **nhánh giao thành công**, không phải quy trình đầy đủ của nhà hàng khi bị hủy.

**Nhà hàng:** C00 nhận yêu cầu chuẩn bị M04 → C01 chuẩn bị món → C02 gửi M14 báo món sẵn sàng → C03 chờ M15 tài xế đến → C04 bàn giao món → C05 gửi M16 xác nhận bàn giao → CE1.

**Tài xế:** D00 nhận xác nhận phân công M05 → D01 chờ M14 → D02a di chuyển tới nhà hàng → D02 gửi M15 báo đã đến → D03a nhận món tại quầy → D03 chờ/nhận M16 xác nhận bàn giao → D04 giao cho khách → D05 gửi M06 báo giao hoàn tất cho nền tảng → DE1.

Món ăn vật lý được xử lý trong C04/D03a/D04; việc di chuyển ở D02a. D02/D03 chỉ gửi/nhận thông tin. M17 của bản trước đã được bỏ để tránh mở rộng thông điệp không cần thiết và gây nhầm thông tin với việc giao món. Thông báo hoàn tất tới khách là M07 do nền tảng gửi ở trang 01. Các thông điệp sớm, bao gồm M14/M15/M16, được giả định lưu và tương quan theo mã đơn; hạ tầng lưu/relay chưa được vẽ chi tiết.

Tại sao trang 01 không có AND giữa chuẩn bị món và tìm tài xế? Sau A05, nhà hàng bắt đầu quy trình riêng qua M04. Nền tảng tiếp tục SP1. Hai participant hoạt động độc lập, nên không bắt buộc thêm AND trong nền tảng chỉ để diễn tả sự đồng thời này. Tài xế chỉ lấy món sau khi có tín hiệu món sẵn sàng.

## 7. Danh mục thông điệp

| Mã | Bên gửi → bên nhận | Nội dung |
|---|---|---|
| M01 | Khách → nền tảng | Đơn mới |
| M02 | Nền tảng → nhà hàng | Yêu cầu xác nhận đơn |
| M03 | Nhà hàng → nền tảng | Đồng ý hoặc từ chối |
| M04 | Nền tảng → nhà hàng | Yêu cầu chuẩn bị món |
| M05 | Nền tảng → tài xế | Xác nhận chuyến đã được phân công |
| M06 | Tài xế → nền tảng | Báo giao hoàn tất |
| M07 | Nền tảng → khách | Thông báo hoàn tất |
| M08 | Nền tảng → khách | Thông báo hủy trước khi thu tiền và lý do |
| M09 | Nền tảng → các tài xế được mời | Lời mời nhận chuyến |
| M10 | Tài xế → nền tảng | Đề nghị nhận chuyến, chưa phải xác nhận đã gán |
| M11 | Nền tảng → nhà hàng | Yêu cầu hủy/dừng chuẩn bị |
| M12 | Nền tảng → các tài xế được mời | Thu hồi lời mời |
| M13 | Nền tảng → khách | Thông báo hủy sau thanh toán và kết quả hoàn tiền |
| M14 | Nhà hàng → tài xế | Món sẵn sàng |
| M15 | Tài xế → nhà hàng | Tài xế đã đến lấy món |
| M16 | Nhà hàng → tài xế | Xác nhận bàn giao |

M04/M05/M06 xuất hiện lại ở trang 03 vì đang phóng to cùng tương tác. Không phải hệ thống gửi lại chúng thêm một lần. Thông điệp thực tế cần gắn mã đơn; những lời mời nhận chuyến có thêm mã tài xế/phiên tìm kiếm để loại phản hồi cũ.

## 8. Cách tự vẽ lại trong draw.io

1. **Bật thư viện:** More Shapes → BPMN → Apply. Tìm task, event, gateway trong thư viện BPMN thay vì thay bằng các hình flowchart gần giống.
2. **Dựng pool trước:** bố trí khách ở trên, nền tảng ở giữa. Trang 01 đặt nhà hàng và tài xế cạnh nhau phía dưới để đường thông điệp không chạy xuyên qua một pool không liên quan. Không cần mọi pool có cùng chiều rộng.
3. **Vẽ luồng chính:** tạo A00 → A01–A08 cùng ba gateway và SP1. Canh tâm các phần tử theo một đường ngang, đặt nhãn gateway phía trên.
4. **Nối sequence flow:** nét liền, mũi tên đặc; chỉ nối các phần tử cùng quy trình/pool. Dùng các điểm gấp khúc vuông góc và giữ nhãn rời khỏi hình.
5. **Bổ sung nhánh hủy:** kéo nhánh Không của AG1/AG2 xuống AG4, rồi A10/A11/AE2. Ghi nhãn Có/Không và lý do; không đặt công việc vào hình thoi.
6. **Gắn timer lên biên:** chọn boundary timer hai vòng nét liền, gắn vào A03. Không đặt đồng hồ đứng rời giữa luồng rồi gọi đó là boundary event. Nối AT1 → A09 → AG4.
7. **Vẽ message flow:** nét đứt, đầu gửi là vòng tròn rỗng, đầu nhận là mũi tên rỗng. Chọn kiểu đường trong bảng Style, không dùng sequence flow rồi chỉ đổi sang nét đứt mà quên đầu mũi tên. Nối đúng hai pool.
8. **Mở rộng SP1 thành trang 02:** subprocess thu gọn ở trang 01 có dấu `+`; trang 02 thể hiện khung subprocess và các start/end bên trong. B02 có timer BT1, B03 chốt kết quả, BG1 tách gán/hủy.
9. **Dựng trang 03:** mở chi tiết nhà hàng và tài xế. Nối tác vụ cùng pool bằng sequence flow; nối các lần gửi/nhận tương ứng bằng message flow.
10. **Căn chỉnh và xuất:** dùng Arrange → Align/Distribute khi cần. Task thường cùng kích thước; subprocess có thể rộng hơn để chứa nhãn. Xuất SVG hoặc PNG, xem ở 100% và phóng to vùng gateway/timer để kiểm tra. Nếu in, chọn giấy đủ rộng hoặc chia theo trang; tránh ép toàn bộ hình ngang vào A4 làm chữ quá nhỏ.

**Mẹo khi làm bài có giới hạn thời gian:** chốt pool, luồng thành công và các XOR trước; thêm từ chối/thanh toán lỗi; sau đó thêm hai timer cùng hoàn tiền. Màu nền chỉ giúp đọc, không quyết định ý nghĩa BPMN. Nếu giảng viên yêu cầu đen trắng, có thể bỏ màu mà giữ nguyên ký pháp.

### Màu sắc có bắt buộc không?

**Không.** OMG BPMN 2.0.2 mục 7.5, trang in 39–40, cho phép sử dụng màu tô và màu đường khác để phục vụ cách trình bày. Không có yêu cầu start phải xanh, end phải đỏ hoặc gateway phải vàng. Bản bình thường dùng bảng màu nhẹ dưới đây; phiên bản `_Co_mau` dùng bảng màu rõ hơn được giải thích trong [README](README.md).

| Màu đang dùng | Mục đích trình bày |
|---|---|
| Trắng | Task thông thường, start/end và phần nội dung chính |
| Xanh nhạt | SP1, bước chốt trạng thái B03, giúp nhận ra phần phân rã/điều phối |
| Hồng nhạt | Các bước xử lý hủy, hoàn tiền và thông báo hủy |
| Vàng/cam rất nhạt | Gateway và bước kiểm tra chính sách hủy |
| Xám xanh rất nhạt | Tiêu đề pool và pool ngoài dạng black box |

Đọc sơ đồ bằng loại hình, nét và nhãn; không suy ra một nhánh hủy chỉ từ nền màu hồng. Đặc biệt, giữ marker gửi/throwing có màu tối và marker nhận/catching không tô đặc. **Không đổi nét liền/đứt của đường nối hoặc viền event chỉ để trang trí.**

### Vì sao end “Hủy đơn” vẫn là một vòng đậm, bên trong trống?

“Hủy đơn” là kết quả nghiệp vụ được ghi bằng nhãn, không tự động là **Cancel End Event**. Cancel End có dấu X chỉ dùng trong Transaction Sub-Process theo quy tắc của BPMN. Bài này dùng subprocess thông thường, nên các end sau hủy vẫn là **None End Event**: một vòng tròn nét đậm, không có marker. Các task hủy/hoàn tiền/thông báo chạy trước khi token đi tới end.

Tương tự, không tô đặc toàn bộ hình tròn end: vòng tròn đen đặc bên trong là marker của **Terminate End Event**, mang ý nghĩa khác. Bài này không cần dùng terminate.

## 9. Các lỗi cần chủ động tránh

| Lỗi | Cách bài này xử lý |
|---|---|
| Nét liền đi từ nền tảng sang nhà hàng/tài xế | Chỉ dùng message flow giữa các pool |
| Message flow nằm trong một pool | Các bước nội bộ dùng sequence flow |
| Dùng AND cho đồng ý/từ chối | AG1 và AG2 là XOR |
| AND nhập nhánh từ chối, lỗi thanh toán, timeout | AG4 là XOR nhập nhánh, không chờ đủ ba token |
| Bước “Nhận…” đi tiếp mà không chờ | A03, A07, B02, C03, D01, D03 là receive task |
| Dùng timer không ngắt khiến vừa hủy vừa tiếp tục | AT1/BT1 là boundary timer ngắt, viền nét liền |
| Timeout sau thanh toán kết thúc mà bỏ tiền đã thu | Nhánh hủy đi qua B06 trước end đã hoàn tiền |
| Tài xế nhận muộn làm sống lại đơn | B03 chốt trạng thái; chỉ phát M05 với kết quả đã gán |
| Nối sequence flow xuyên ranh giới subprocess | Trang 01 dùng SP1 làm một hoạt động; start/end nội bộ nằm ở trang 02 |
| Coi end event của nền tảng là dừng tất cả bên ngoài | End chỉ kết thúc scope của nó; các bên khác nhận thông điệp hủy/thông báo |

## 10. Kiểm tra kết quả và giới hạn xác nhận

File được tạo bằng các ký hiệu BPMN của draw.io, giải mã lại và xuất SVG bằng **trình xem/bộ dựng chính thức `viewer-static.min.js`**, chạy trong Chrome headless. PNG được xuất từ chính các SVG này. Các ảnh đã được xem để sửa đường đi xuyên qua điểm kết thúc và các ghi chú đè lên đường thông điệp.

Kiểm tra cấu trúc gồm: tham chiếu phần tử tồn tại; sequence flow không vượt pool hoặc scope subprocess; message flow nối hai pool khác nhau; start/end có hướng nối phù hợp; boundary timer có tác vụ chủ; send/receive có thông điệp tương ứng trong góc nhìn đang hiển thị; hình và các đoạn đường không xuyên qua phần tử không liên quan. Xem Kiem_tra.json để biết kết quả máy kiểm tra.

Lần rà soát mới kiểm tra style XML và hình SVG thực tế: **47 sequence flow nét liền/mũi tên đặc, 19 message flow nét đứt/vòng tròn rỗng/mũi tên không tô, 4 start một vòng mảnh, 7 end một vòng đậm, 2 timer ngắt với hai vòng nét liền, 6 XOR và 19 marker send/receive**. Có thêm hai Manual Task D02a/D03a, tổng 5 Manual Task. Đối chiếu cùng số trang đặc tả nằm trong [notation-review.md](notation-review.md); mô tả mọi giả định và giới hạn ở báo cáo toàn diện.

Hai phiên bản hiện đều đã qua các kiểm tra này. Kiem_tra_Co_mau.json xác nhận bản màu giữ nguyên nội dung, hình học, ký hiệu và kết nối của bản bình thường; chỉ thay các thuộc tính màu. Đã xem lại cả ba ảnh màu sau khi xuất.

Kiểm tra nghiệp vụ dựa trên việc đi từng kịch bản: thành công, nhà hàng từ chối, thanh toán thất bại, timeout nhà hàng, timeout tài xế và tài xế nhận sát/đúng hạn. Đây là rà soát mô hình và bố cục; không phải chứng nhận OMG, không phải mô phỏng thực thi BPMN engine, và không chứng minh các tích hợp thanh toán đã hoạt động thực tế.

Nguồn ký hiệu/trình dựng: [jgraph/drawio](https://github.com/jgraph/drawio), phần `Sidebar-BPMN.js`, `mxBpmnShape2.js` và `viewer-static.min.js`. Nguồn quy tắc: OMG BPMN 2.0.2, mục 7.5 **Use of Text, Color, Size, and Lines in a Diagram**, 8.4.13 **Sequence Flow**, 9.4 **Message Flow**, 10.3 **Activities**, 10.5 **Events** và 10.6 **Gateways**. Quy tắc boundary event ngắt được mô tả ở trang in 276 của đặc tả; quy tắc message flow nối hai pool ở trang in 119.
