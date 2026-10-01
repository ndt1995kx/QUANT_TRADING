# 03 — Các yếu tố cốt lõi của quant trading

> Cập nhật: 2026-10-01 · Khung tổng hợp từ kiến thức chuẩn ngành (sách và bài báo gốc ở [02](02-kenh-hoc-thuat.md)).
> Đây là tài liệu giáo dục, **không phải tư vấn đầu tư**. Con số "quy ước thực hành" chỉ là điểm xuất phát để cân nhắc, không phải chuẩn bắt buộc.

## 1. Bức tranh một dòng

Quant trading là một **chuỗi mắt xích**; mắt xích yếu nhất quyết định kết quả:

```
Edge (giả thuyết có lý do kinh tế)
  → Dữ liệu → Backtest & kiểm định → Danh mục & định cỡ vị thế
  → Quản trị rủi ro → Thực thi → Giám sát & phản hồi ──┐
        ▲                                               │
        └──────────── bài học quay lại giả thuyết ◄─────┘
Nền móng chạy xuyên suốt: toán–thống kê–tài chính · lập trình · hạ tầng · kỷ luật quy trình
```

Khung 4 khối phổ biến trong các giáo trình nhập môn là: **tìm chiến lược → backtest → thực thi → quản trị rủi ro**. Tài liệu này mở rộng thành **10 yếu tố** để thấy cả phần nền móng và vòng phản hồi.

## 2. Mười yếu tố

### 1. Edge — giả thuyết có lý do kinh tế
- **Câu hỏi cốt lõi:** Chiến lược kiếm tiền *từ đâu*, ai là người ở phía bên kia giao dịch, và vì sao lợi thế này chưa bị triệt tiêu?
- **Nguồn edge thường gặp:**
  (a) *phần thưởng rủi ro* (risk premia: value, momentum, carry, quality, low-volatility);
  (b) *thiên lệch hành vi* (phản ứng chậm hoặc quá mức với tin tức);
  (c) *ràng buộc cấu trúc* (quỹ buộc phải mua/bán, tái cân bằng chỉ số, margin call);
  (d) *cung cấp thanh khoản* (market making — thu chênh lệch giá mua/bán);
  (e) *quan hệ giá* (arbitrage giữa spot–futures, ETF–rổ, cùng tài sản trên hai sàn);
  (f) *thông tin / tốc độ xử lý* (dữ liệu thay thế, NLP, độ trễ thấp);
  (g) *thực thi tốt hơn* (giảm tác động giá).
- **Sai lầm điển hình:** "đào dữ liệu" tìm mẫu hình không có lý do → thường biến mất ngoài mẫu. Chiến lược kiểu *grid/martingale* trông thắng đều nhưng thực chất **bán bảo hiểm đuôi**: nhiều lần lãi nhỏ, thỉnh thoảng một lần lỗ rất lớn.
- **Ở quy mô cá nhân:** bắt đầu bằng chiến lược ít tham số; viết ra 3 dòng *"Tôi kiếm tiền từ …; người thua là …; edge biến mất khi …"* trước khi viết dòng code đầu tiên.

### 2. Dữ liệu
- **Câu hỏi cốt lõi:** Dữ liệu có phản ánh đúng những gì mình *biết được và giao dịch được* tại thời điểm đó không?
- **Khái niệm chính:** tick / bar OHLCV / order book (L2, L3) / cơ bản / dữ liệu thay thế; **point-in-time** (chỉ dùng thông tin đã công bố tại thời điểm đó); điều chỉnh sự kiện doanh nghiệp (chia tách, cổ tức); **survivorship bias** (thiếu mã đã hủy niêm yết); **look-ahead bias** (dùng tương lai); múi giờ, DST, dấu thời gian; hợp đồng tương lai cần *roll* sang kỳ hạn mới; FX không có sàn trung tâm nên dữ liệu **khác nhau giữa các broker** (spread, giờ máy chủ).
- **Sai lầm điển hình:** kiểm định bằng giá mid trong khi thực tế mua giá ask, bán giá bid; dùng dữ liệu broker A để kết luận cho broker B; bỏ qua khoảng trống (gap) và điểm giá bất thường.
- **Ở quy mô cá nhân:** ghi lại nguồn + phiên bản dữ liệu; đối chiếu hai nguồn; kiểm tra gap/spike trước khi tin bất kỳ kết quả nào.

### 3. Backtest & kiểm định
- **Câu hỏi cốt lõi:** Nếu chạy chiến lược này trong quá khứ, có lãi **sau chi phí** không — và bằng chứng này đáng tin đến mức nào?
- **Kỹ thuật chính:**
  - *Vector hóa* (nhanh, dễ nghiên cứu) vs *event-driven* (sát thực tế khớp lệnh).
  - Mô hình hóa spread, phí, slippage, swap/funding, độ trễ.
  - Tách **in-sample / out-of-sample**; **walk-forward**.
  - Cross-validation cho chuỗi thời gian: *purged k-fold* + *embargo*, *combinatorial purged CV* (López de Prado).
  - Độ nhạy tham số: kết quả tốt phải nằm trên **vùng bình nguyên**, không phải một đỉnh nhọn.
  - Hiệu chỉnh nhiều lần thử: **Deflated Sharpe Ratio** và **Probability of Backtest Overfitting** (Bailey, López de Prado và cộng sự).
  - Stress theo giai đoạn khủng hoảng; Monte Carlo trên chuỗi lệnh.
- **Sai lầm điển hình:** *overfitting* (tối ưu quá nhiều tham số); thử hàng trăm biến thể rồi chọn cái đẹp nhất mà không hiệu chỉnh; dùng cùng một đoạn dữ liệu để tối ưu **và** để đánh giá; bỏ qua chi phí; backtest bằng dữ liệu bar không mô phỏng được biến động trong nến.
- **Ở quy mô cá nhân:** ghi nhật ký **số lần đã thử**; dành một đoạn out-of-sample chỉ nhìn **một lần**; thử lại với chi phí cao hơn 1.5–2 lần (quy ước thực hành) để xem edge còn sống không.

### 4. Chi phí & thực thi
- **Câu hỏi cốt lõi:** Từ tín hiệu đến vị thế thật, mất bao nhiêu (spread, phí, slippage, tác động giá, độ trễ)?
- **Khái niệm chính:** loại lệnh (market, limit, stop, IOC/FOK…); thuật toán thực thi (TWAP, VWAP, POV, implementation shortfall); **market impact** (thực nghiệm thường tăng xấp xỉ theo căn bậc hai của khối lượng so với thanh khoản thị trường — "square-root law"); vòng đời lệnh (từ chối, requote, khớp một phần); độ tin cậy kết nối.
- **Sai lầm điển hình:** giả định khớp ngay tại giá tín hiệu; không tính spread nới rộng lúc tin tức hoặc giờ rollover; không đo slippage thật rồi so với mô hình.
- **Ở quy mô cá nhân:** ghi giá tín hiệu vs giá khớp cho **từng lệnh**; đặt bộ lọc spread; tránh giờ thanh khoản mỏng nếu chiến lược nhạy với chi phí.

### 5. Định cỡ vị thế & danh mục
- **Câu hỏi cốt lõi:** Mỗi cơ hội nên đặt bao nhiêu vốn, và các vị thế phối hợp với nhau ra sao?
- **Khái niệm chính:**
  - **Kelly**: với xác suất thắng *p* và tỷ lệ lãi/lỗ *b*, tỷ lệ vốn tối ưu về lý thuyết là `f* = p − (1 − p) / b`. Ước lượng *p, b* luôn nhiễu nên thực hành hay dùng một **phần** Kelly (ví dụ 1/4–1/2).
  - **Volatility targeting** (cỡ vị thế tỷ lệ nghịch với biến động); **risk parity**; **mean-variance** (Markowitz) và điểm yếu: rất nhạy với sai số ước lượng → dùng shrinkage, Black–Litterman, HRP.
  - Ràng buộc về đòn bẩy, tập trung, thanh khoản; **tương quan giữa các chiến lược** (đa dạng hóa thật vs ảo).
- **Sai lầm điển hình:** cỡ lệnh cố định mặc kệ biến động; tăng cỡ sau chuỗi thắng hoặc gấp đôi cỡ lệnh sau chuỗi thua (martingale); chạy nhiều bot tương quan cao rồi tưởng đã phân tán rủi ro.
- **Ở quy mô cá nhân:** đặt trần rủi ro mỗi lệnh và mỗi ngày bằng một tỷ lệ nhỏ **cố định** của vốn, tính theo biến động hiện tại.

### 6. Quản trị rủi ro
- **Câu hỏi cốt lõi:** Điều tồi tệ nhất có thể xảy ra là gì, và hệ thống có **sống sót** qua nó không?
- **Khái niệm chính:** giới hạn vị thế / đòn bẩy / lỗ trong ngày / drawdown; **VaR** và **Expected Shortfall (CVaR)** cùng hạn chế khi đuôi phân phối dày; stress test và kịch bản; **kill switch**; kiểm tra margin trước khi vào lệnh; rủi ro mô hình, rủi ro vận hành (lỗi mạng, lỗi mã, lệnh lặp), rủi ro đối tác (broker/sàn); *risk of ruin*.
- **Sai lầm điển hình:** tin VaR chuẩn hóa theo phân phối chuẩn; để giới hạn rủi ro nằm **trong** logic chiến lược (chiến lược lỗi thì giới hạn lỗi theo); quên gap qua đêm/cuối tuần.
- **Ở quy mô cá nhân:** mỗi bot cần một "cầu dao tổng" độc lập: trần lỗ ngày, số vị thế tối đa, lọc spread, kiểm tra margin; có ngưỡng drawdown **định sẵn** để dừng bot.
- **Toán học của drawdown:** lỗ càng sâu càng khó hồi — lỗ 10% cần +11.1% để hòa vốn, 20% cần +25%, 50% cần +100%, 70% cần +233% (`cần = 1/(1−d) − 1`).

### 7. Hạ tầng & công nghệ
- **Câu hỏi cốt lõi:** Hệ thống chạy đúng, đủ nhanh, và phục hồi được khi lỗi không?
- **Khái niệm chính:** tách lớp (dữ liệu / tín hiệu / rủi ro / thực thi); kiểm thử tự động; quản lý cấu hình và bí mật (API key); VPS gần máy chủ broker/sàn; đồng bộ giờ; xử lý lệnh *idempotent* (gửi lặp không tạo vị thế lặp); **đối chiếu vị thế** giữa hệ thống và broker; với HFT: co-location, phần cứng chuyên dụng.
- **Sai lầm điển hình:** hai bộ logic khác nhau cho backtest và live; API key nằm trong mã nguồn; bot chết mà không ai biết.
- **Ở quy mô cá nhân:** cùng một mã chạy backtest và live; VPS; heartbeat/cảnh báo khi bot ngừng.

### 8. Giám sát, telemetry & vòng phản hồi
- **Câu hỏi cốt lõi:** Chiến lược đang hành xử đúng như lúc kiểm định không? Khi nào thì dừng?
- **Khái niệm chính:** ghi log **mọi quyết định** (tín hiệu, lý do vào/ra, rule nào kích hoạt, rule nào chặn lệnh); so sánh live với backtest (lãi/lỗ, slippage, tần suất lệnh, phân phối kết quả); theo dõi **alpha decay**; ngưỡng dừng định trước; post-mortem.
- **Sai lầm điển hình:** chỉ nhìn P&L; không ghi lý do vào/ra; can thiệp bằng cảm tính khi gặp chuỗi thua.
- **Ở quy mô cá nhân:** nhật ký có cấu trúc (CSV/JSON) cho mỗi lệnh *và* mỗi lần guard chặn lệnh; rà soát định kỳ.

### 9. Quy trình & kỷ luật (governance)
- **Câu hỏi cốt lõi:** Cái gì quyết định chiến lược được lên chạy tiền thật, dựa trên bằng chứng nào?
- **Khái niệm chính:** nhật ký giả thuyết; **version hóa** chiến lược và dữ liệu; các *cổng* chuyển giai đoạn (backtest → forward-test/paper → live quy mô nhỏ → live đầy đủ) với tiêu chí định lượng đặt **trước**; tiêu chí dừng; rà soát định kỳ; tuân thủ pháp lý.
- **Sai lầm điển hình:** chỉnh tham số liên tục theo kết quả gần nhất; ghi đè phiên bản cũ nên không so sánh được; bỏ qua forward-test vì "backtest đẹp quá".
- **Ở quy mô cá nhân:** mỗi thay đổi lớn là một phiên bản mới; ghi rõ lý do và kết quả; quy định trước số lệnh và thời gian tối thiểu của forward-test.

### 10. Nền tảng kiến thức
- **Toán – thống kê:** xác suất; suy luận thống kê và kiểm định giả thuyết (cẩn thận p-hacking); hồi quy; chuỗi thời gian (tính dừng, tự tương quan, đồng tích hợp, ARIMA/GARCH); đại số tuyến tính (PCA, ma trận hiệp phương sai); tối ưu hóa lồi; với phái sinh: giải tích ngẫu nhiên, Black–Scholes; với ML: regularization, cross-validation, rò rỉ dữ liệu.
- **Tài chính:** cấu trúc vi mô thị trường; định giá tài sản (CAPM, mô hình đa nhân tố); phái sinh; quản trị danh mục.
- **Lập trình:** Python (pandas/numpy), SQL, C++ (độ trễ thấp), MQL5 nếu giao dịch trên MetaTrader 5.
- **Tâm lý:** chấp nhận drawdown *đã nằm trong kế hoạch*; không phá quy tắc giữa chừng.

## 3. Nếu chỉ được chọn ba thứ

Nhiều thất bại của bot bán lẻ quy về ba nguồn quen thuộc — và ba yếu tố tương ứng bảo vệ bạn:

| Nguồn thất bại | Yếu tố cần siết chặt |
|---|---|
| Edge chỉ tồn tại trong backtest (overfitting) | **3. Backtest & kiểm định** trung thực |
| Chi phí ăn hết lợi nhuận | **4. Chi phí & thực thi**, đo thực tế |
| Một chuỗi sự kiện xấu xóa sạch vốn | **6. Quản trị rủi ro** bằng giới hạn cứng độc lập |

## 4. Checklist trước khi chuyển từ demo sang tiền thật

Mỗi mục nên trả lời "có" kèm bằng chứng (đường dẫn file, số liệu), không phải "chắc là có":

1. Viết được lý do kinh tế của edge trong 3 câu.
2. Dữ liệu có nguồn rõ ràng, đã kiểm tra gap/outlier, không look-ahead, không survivorship bias.
3. Chi phí thực (spread, phí, swap, slippage) đã mô hình hóa; kết quả còn dương khi tăng chi phí 1.5–2 lần.
4. Có đoạn out-of-sample hoặc walk-forward **chưa từng** dùng để tối ưu.
5. Kết quả bền khi dịch tham số ±20% (vùng bình nguyên, không phải đỉnh nhọn).
6. Số biến thể đã thử được ghi lại và có hiệu chỉnh nhiều lần thử.
7. Drawdown tối đa chấp nhận được đã định trước; cỡ vị thế tính theo đó.
8. Có giới hạn cứng độc lập: lỗ ngày, số vị thế, đòn bẩy, spread, margin.
9. Forward-test/paper đủ dài và đủ số lệnh; so sánh với backtest (lãi/lỗ, slippage, tần suất).
10. Có log + cảnh báo; biết chính xác cách dừng bot và xử lý vị thế đang mở.
11. Có kế hoạch khi broker, mạng hoặc VPS gián đoạn.
12. Bắt đầu với quy mô nhỏ và tăng dần theo bằng chứng.

> Các ngưỡng số (1.5–2 lần chi phí, ±20% tham số) là **quy ước thực hành** phổ biến, không phải định lý. Điều quan trọng là *đặt ngưỡng trước khi nhìn kết quả*.

---
Tiếp theo: [04 — Kiến trúc tham chiếu](04-kien-truc-tham-chieu.md) · [01 — Quant trading là gì](01-quant-trading-la-gi.md) · [Mục lục](../README.md)
