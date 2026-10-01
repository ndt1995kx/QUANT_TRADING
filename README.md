# QUANT_TRADING

Kho tri thức tiếng Việt về **quant trading (giao dịch định lượng)**: là gì, giao dịch ở đâu, lợi nhuận tính thế nào, học ở đâu, các yếu tố cốt lõi và kiến trúc hệ thống.

> Cập nhật **2026-10-01** · Tài liệu giáo dục, **không phải tư vấn đầu tư hay pháp lý**.
> ⚠ Repo này **công khai** — đừng đưa vào đây tham số chiến lược thật, API key hay thông tin tài khoản.

## Trả lời nhanh

### 1. Quant trading là gì? Giao dịch ở đâu? Lợi nhuận tính thế nào?

- **Là gì:** ra quyết định mua/bán bằng **mô hình toán học – thống kê được kiểm chứng bằng dữ liệu**, thực hiện **theo quy tắc xác định trước** (thường tự động hóa), thay vì phán đoán chủ quan từng lệnh. Chiến lược chỉ có ý nghĩa khi có **lý do kinh tế** cho lợi thế (edge) và bằng chứng sau chi phí. → [01 §1](docs/01-quant-trading-la-gi.md#1-quant-trading-là-gì)
- **Ở đâu:** sàn tập trung (cổ phiếu, hợp đồng tương lai/quyền chọn), thị trường OTC (ngoại hối, trái phiếu — không có sàn trung tâm), sàn tiền mã hóa (24/7, gồm hợp đồng vĩnh cửu), CFD qua broker. Cá nhân tiếp cận qua broker, API hoặc MetaTrader. Việt Nam: cổ phiếu HOSE/HNX/UPCoM và phái sinh VN30. → [01 §2](docs/01-quant-trading-la-gi.md#2-giao-dịch-ở-đâu), [05](docs/05-thi-truong-viet-nam.md)
- **Lợi nhuận:** `lãi ròng = lãi/lỗ giá − chi phí` (spread, phí, trượt giá, swap/funding, thuế). Đánh giá bằng lợi suất **đã điều chỉnh rủi ro** (Sharpe, max drawdown, profit factor, recovery factor…) và tách **alpha** khỏi **beta**. Lãi trong backtest thường lớn hơn lãi thật (overfitting, chi phí, sức chứa). Có ví dụ bằng số đã tính lại. → [01 §3](docs/01-quant-trading-la-gi.md#3-lợi-nhuận-được-tính-như-thế-nào)

### 2. Các kênh học thuật

Kho preprint (**arXiv q-fin**, **SSRN**, NBER), tạp chí bình duyệt (*Journal of Finance*, *Journal of Financial Economics*, *Review of Financial Studies*, *Quantitative Finance*, *Journal of Portfolio Management*…), hội nghị (QuantMinds, Bachelier Finance Society, ACM ICAIF, AFA/WFA/EFA…), thạc sĩ (Baruch, CMU, Columbia, NYU, Oxford, Imperial, ETH–UZH, WorldQuant University — miễn học phí…), chứng chỉ (CQF, FRM, CFA, PRM, CAIA…), khóa học mở (MIT OCW, Coursera…), sách kinh điển, thư viện mã nguồn mở, cộng đồng. Mỗi mục có nhãn mức độ đối chiếu. → [02](docs/02-kenh-hoc-thuat.md)

### 3. Các yếu tố cốt lõi

**Edge** (giả thuyết có lý do kinh tế) → **dữ liệu** → **backtest & kiểm định** → **chi phí & thực thi** → **định cỡ vị thế & danh mục** → **quản trị rủi ro** → **hạ tầng** → **giám sát & phản hồi** → **quy trình & kỷ luật**, trên nền **toán–thống kê–tài chính–lập trình**. Mắt xích yếu nhất quyết định kết quả; kèm checklist 12 mục trước khi chuyển từ demo sang tiền thật. → [03](docs/03-yeu-to-cot-loi.md)

## Mục lục

| Tài liệu | Nội dung |
|---|---|
| [00 — Kiểm kê](docs/00-kiem-ke.md) | Đã quét gì, thấy gì, chưa có gì; cách hoàn tất kiểm kê trên máy cá nhân; lưu ý riêng tư |
| [01 — Quant trading là gì](docs/01-quant-trading-la-gi.md) | Định nghĩa, các họ chiến lược, nơi giao dịch, cách tính lợi nhuận kèm ví dụ số |
| [02 — Kênh học thuật](docs/02-kenh-hoc-thuat.md) | Nghiên cứu, hội nghị, thạc sĩ, chứng chỉ, khóa học, sách, thư viện, cộng đồng; lộ trình học |
| [03 — Yếu tố cốt lõi](docs/03-yeu-to-cot-loi.md) | 10 yếu tố, sai lầm điển hình, checklist trước khi chạy tiền thật |
| [04 — Kiến trúc tham chiếu](docs/04-kien-truc-tham-chieu.md) | Bảy lớp của một hệ thống quant, ba cấu hình theo quy mô, tám nguyên tắc thiết kế |
| [05 — Thị trường Việt Nam](docs/05-thi-truong-viet-nam.md) | Cổ phiếu, phái sinh, API, tiền mã hóa, forex/CFD, thuế — kèm nhãn đối chiếu |

## Trạng thái và giới hạn

- **Kiểm kê máy:** máy chạy phiên soạn thảo là container đám mây mới, **không chứa** mã, dữ liệu hay vault của chủ repo; nội dung nằm trên máy cá nhân chưa được thống kê. Chi tiết và cách hoàn tất: [00](docs/00-kiem-ke.md).
- **Độ tin cậy số liệu:** các dữ kiện cập nhật theo thời gian (giá, ngày, quy định, số hiệu văn bản) được đối chiếu **qua kết quả tìm kiếm** — môi trường soạn thảo không mở trực tiếp được trang gốc. Mỗi tài liệu có nhãn ✔ / ? / ⚠ cho từng mục; mục nào quan trọng với quyết định của bạn, hãy mở liên kết nguồn để xác nhận.
- Công thức và khái niệm chuẩn (Sharpe, drawdown, Kelly, CAPM…) là kiến thức giáo trình; ví dụ bằng số được tính lại bằng chương trình.
