# Examples

Every example has a normal and a colour `.drawio` (same model, colour only), PNG/SVG renderings and a written explanation (Vietnamese). Notation reference: [OMG BPMN 2.0.2](https://www.omg.org/spec/BPMN/2.0.2/PDF), cited by name only.

Mỗi ví dụ có hai bản `.drawio` (chỉ khác màu), ảnh PNG/SVG và tài liệu giải thích tiếng Việt.

## Synthetic examples — Ví dụ tự đặt

| Example | Covers |
|---|---|
| [Interlibrary loan — Mượn sách liên thư viện](bpmn/interlibrary-loan/README.md) | Three pools, event-based gateway, Link events, interrupting and non-interrupting boundary timers, long Vietnamese labels |
| [Shared equipment reservation — Đặt trước thiết bị dùng chung](bpmn/equipment-reservation/README.md) | Small demo produced by `create_demo.py`: two pools, two lanes, one XOR |
| [Document check and review — Kiểm tra và thẩm định hồ sơ](bpmn/document-review/README.md) | One diagram, two lanes; each decision is produced by a task before the gateway |
| [Ten advanced patterns — Mười mẫu nâng cao](bpmn/advanced-patterns/README.md) | XOR/AND/inclusive, event race, boundary events, event subprocess, transaction/compensation, multi-instance, terminate |

## Coursework solutions — Lời giải bài tập học phần

Reference solutions for exercises of a Software Business Analysis course (Phân tích nghiệp vụ phần mềm). The exercises are cited by name only and not included. These are **not** official answers and were not reviewed by the lecturer; student name, ID and submissions were removed. Exam 03 has three independent solutions for comparison.

| Example | Covers |
|---|---|
| [Exam 01 — Internal equipment purchasing (Đề 01 — Mua sắm thiết bị nội bộ)](bpmn/coursework/exam-01-equipment-purchasing/README.md) | Collaboration: three lanes and a black-box supplier, AND, 48-hour timer |
| [Exam 03 — Electronic device warranty, Claude solution (Đề 03 — Bảo hành thiết bị điện tử)](bpmn/coursework/exam-03-warranty-service/claude/README.md) | One of three independent solutions to the same exercise |
| [Exam 03 — Electronic device warranty, GPT solution (Đề 03 — Bảo hành thiết bị điện tử)](bpmn/coursework/exam-03-warranty-service/gpt/README.md) | One of three independent solutions to the same exercise |
| [Exam 03 — Electronic device warranty, Gemini solution (Đề 03 — Bảo hành thiết bị điện tử)](bpmn/coursework/exam-03-warranty-service/gemini/README.md) | One of three independent solutions; includes zoomed detail crops |
| [Practice — Food ordering app (Thực hành — Ứng dụng gọi đồ ăn)](bpmn/coursework/practice-food-delivery/README.md) | Three pages: overview; driver search, expiry and refund; preparation and delivery |
