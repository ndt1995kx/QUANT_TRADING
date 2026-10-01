# 01 — Quant trading là gì, giao dịch ở đâu, lợi nhuận tính thế nào

> Cập nhật: 2026-10-01 · Tài liệu giáo dục, **không phải tư vấn đầu tư**. Số trong tài liệu dùng dấu chấm thập phân (như MT5/Python).
> Mọi ví dụ bằng số là **minh họa** và đã được tính lại bằng chương trình; không phải kết quả của một chiến lược thật.

## 1. Quant trading là gì?

### 1.1 Định nghĩa

**Quant trading (giao dịch định lượng)** là ra quyết định mua/bán dựa trên **mô hình toán học – thống kê được kiểm chứng bằng dữ liệu**, và thực hiện **theo quy tắc xác định trước** (thường tự động hóa bằng máy tính), thay vì dựa vào phán đoán chủ quan ở từng lệnh.

Ba đặc trưng phân biệt:

1. **Giả thuyết kiểm chứng được** — quy tắc/mô hình viết ra được thành công thức hoặc mã.
2. **Bằng chứng từ dữ liệu** — backtest, kiểm định thống kê, forward-test; không dựa vào cảm giác.
3. **Thực thi có kỷ luật** — lệnh sinh ra từ quy tắc; rủi ro bị chặn bởi giới hạn định lượng.

### 1.2 Phân biệt các khái niệm hay bị nhầm

| Thuật ngữ | Ý nghĩa | Quan hệ với quant |
|---|---|---|
| Giao dịch phán đoán (discretionary) | Con người quyết định từng lệnh dựa trên phân tích và kinh nghiệm | Đối lập: không có quy tắc hình thức |
| Giao dịch hệ thống (systematic) | Quy tắc rõ ràng, mô phỏng ngược được (kể cả đơn giản, vài chỉ báo) | Quant thường nằm trong nhóm này, nhưng nhấn mạnh mô hình thống kê/toán và cách xây danh mục |
| Giao dịch thuật toán (algorithmic) | Dùng thuật toán để **đặt lệnh/thực thi** (VWAP, TWAP…) | Có thể là bước thực thi của quant; "có thuật toán" **không** đồng nghĩa "có lợi thế" |
| Tần suất cao (HFT) | Giữ vị thế rất ngắn, cạnh tranh về độ trễ và hạ tầng | Một nhánh của quant; không phải quant nào cũng là HFT |
| Đầu tư theo nhân tố (factor investing) | Danh mục theo nhân tố (value, momentum, quality…), tần suất thấp | Nhánh của quant, nắm giữ lâu hơn |
| Bot / EA (Expert Advisor) | Chương trình tự động giao dịch, ví dụ trên MetaTrader 5 | Công cụ triển khai; chất lượng "quant" nằm ở quy trình nghiên cứu phía sau |

### 1.3 Ai làm quant

- **Quỹ định lượng và quỹ phòng hộ** — ví dụ Renaissance Technologies, Two Sigma, D. E. Shaw, AQR, Man AHL.
- **Công ty giao dịch tự doanh / market maker** — ví dụ Jane Street, Optiver, Hudson River Trading, Citadel Securities.
- **Ngân hàng đầu tư và nhà quản lý tài sản** — bàn quant, quỹ cổ phiếu hệ thống.
- **Nhà giao dịch cá nhân** — bot/EA trên MetaTrader, hoặc Python qua API broker/sàn.

### 1.4 Các họ chiến lược chính

| Họ chiến lược | Ý tưởng | Nguồn lợi nhuận (vì sao có) | Rủi ro điển hình |
|---|---|---|---|
| Trend following / momentum | Đi theo xu hướng giá | Phản ứng chậm với thông tin, hành vi bầy đàn, phần thưởng rủi ro | Tín hiệu giả khi thị trường đi ngang (*whipsaw*); chuỗi lỗ dài |
| Mean reversion / stat arb / pairs | Giá lệch khỏi giá trị tương đối sẽ quay về | Phản ứng quá mức ngắn hạn; quan hệ giá giữa tài sản tương tự | Quan hệ gãy (*regime break*) → lỗ lớn |
| Carry | Nắm tài sản lợi suất cao, tài trợ bằng tài sản lợi suất thấp | Phần bù rủi ro | Sụp đổ đột ngột khi khủng hoảng |
| Market making | Báo giá mua/bán hai phía, thu chênh lệch | Cung cấp thanh khoản | Rủi ro tồn kho; bị khớp bởi bên biết nhiều hơn (*adverse selection*) |
| Arbitrage | Khai thác chênh lệch giá của tài sản giống/tương đương (spot–futures, ETF–rổ, giữa các sàn) | Giá phải hội tụ | Cạnh tranh tốc độ; chi phí; rủi ro thực thi |
| Biến động (volatility) | Giao dịch biến động ngụ ý vs thực tế | Phần bù bảo hiểm | Bán bảo hiểm: lãi nhỏ đều, lỗ lớn hiếm gặp (rủi ro đuôi) |
| Nhân tố / smart beta | Danh mục theo nhân tố | Phần thưởng rủi ro dài hạn | Nhân tố có thể "đói" nhiều năm; đông đúc (*crowding*) |
| Sự kiện / tin tức / NLP | Phản ứng với công bố lợi nhuận, tin tức | Xử lý thông tin nhanh hơn | Độ trễ, chất lượng dữ liệu, tin sai |
| Machine learning | Mô hình học từ dữ liệu để dự báo | Phát hiện quan hệ phi tuyến | Overfitting; dữ liệu tài chính nhiễu và ít mẫu |

> **Lưu ý về grid/martingale:** các chiến lược "chia lưới" hoặc "gấp đôi khi thua" thuộc họ *bán bảo hiểm đuôi* — đường vốn rất đẹp cho đến lúc một biến động lớn xóa sạch nhiều tháng lãi. Cần giới hạn cứng độc lập (xem [03](03-yeu-to-cot-loi.md), yếu tố 6).

## 2. Giao dịch ở đâu?

> **Về độ tin cậy của số liệu:** các dữ kiện dưới đây được đối chiếu qua kết quả tìm kiếm trỏ tới trang chính thức (10/2026); môi trường soạn thảo **không mở trực tiếp được trang gốc**. Giờ giao dịch, quy định và con số thay đổi theo thời gian — hãy bấm vào liên kết nguồn để xác nhận trước khi dựa vào chúng.

### 2.1 Bản đồ thị trường theo loại tài sản

| Loại tài sản | Nơi giao dịch tiêu biểu | Cách vận hành | Giờ giao dịch (tham khảo) | Cá nhân tiếp cận qua |
|---|---|---|---|---|
| **Cổ phiếu** | NYSE, Nasdaq (Mỹ); các sở châu Âu/châu Á; HOSE, HNX, UPCoM (Việt Nam, xem [05](05-thi-truong-viet-nam.md)). Ngoài sàn: ATS / "dark pool" (Mỹ), MTF (châu Âu) | Khớp lệnh liên tục, cộng phiên đấu giá mở/đóng cửa | Mỹ (Nasdaq): trước giờ 4:00–9:30, chính 9:30–16:00, sau giờ 16:00–20:00 (giờ ET) | Công ty chứng khoán / broker |
| **Hợp đồng tương lai và quyền chọn niêm yết** | CME Group (nền tảng Globex), ICE, Eurex, Cboe | Sàn tập trung, có bù trừ trung tâm; ký quỹ + ghi nhận lãi/lỗ hằng ngày | CME Globex gần 24 giờ, Chủ nhật–Thứ sáu (nghỉ khoảng 60 phút/ngày); ICE Brent 01:00–23:00 (giờ London); Eurex Bund/Euro STOXX 50 01:10–22:00 (giờ CET) | Broker phái sinh |
| **Ngoại hối (FX)** | **Không có sàn trung tâm**: mạng lưới ngân hàng, dealer và nền tảng điện tử | OTC, phi tập trung | Gần 24 giờ, 5 ngày/tuần | Broker FX/CFD (MetaTrader…) |
| **Tiền mã hóa** | Sàn tập trung (Binance, Coinbase, Kraken, OKX…); sàn phi tập trung/AMM (Uniswap…) | Spot + hợp đồng vĩnh cửu (*perpetual*); AMM định giá bằng công thức | Thường liên tục 24/7 | Tài khoản sàn (API); ví on-chain cho DEX |
| **Trái phiếu, tín dụng** | Chủ yếu OTC giữa dealer; nền tảng điện tử như MarketAxess, Tradeweb | Thương lượng song phương hoặc báo giá điện tử | Theo giờ của dealer/nền tảng | Chủ yếu tổ chức; cá nhân bị hạn chế |
| **CFD** | Sản phẩm OTC do broker cung cấp | Hợp đồng chênh lệch, đòn bẩy cao; quy định khác nhau theo nước | Theo tài sản gốc | Broker CFD |

### 2.2 Một số dữ kiện đã đối chiếu

- **Ngoại hối là thị trường lớn nhất:** khảo sát ba năm một lần của BIS (kỳ tháng 4/2025) cho doanh số bình quân khoảng **9.5 nghìn tỷ USD/ngày** (số cuối, BIS Quarterly Review 12/2025; số sơ bộ công bố 30/9/2025 là 9.6 nghìn tỷ), tăng khoảng 27% so với 7.5 nghìn tỷ của tháng 4/2022. Nguồn: [BIS press release](https://www.bis.org/press/p250930.htm), [BIS Quarterly Review](https://www.bis.org/publ/qtrpdf/r_qt2512_foreword.htm).
- **Hợp đồng vĩnh cửu (perpetual) trên sàn tiền mã hóa:** không có ngày đáo hạn; để giá hợp đồng bám giá chỉ số/spot, hai phía định kỳ **trả funding cho nhau** — khi funding dương thì bên mua trả bên bán. Phí = `giá trị danh nghĩa của vị thế × funding rate`. Chu kỳ tính phụ thuộc sàn (ví dụ Binance, OKX: 8 giờ; Kraken, Coinbase: mỗi giờ) và có thể khác theo từng cặp. Nguồn: tài liệu hỗ trợ của [Binance](https://www.binance.com/en/support/faq/what-are-perpetual-futures-and-quarterly-futures-d2a1afd5f829455c9ded23f0ca561a40), [OKX](https://www.okx.com/en-us/help/i-perpetual-swaps), [Kraken](https://www.kraken.com/learn/trading/perpetual-futures-contracts), [Coinbase](https://help.coinbase.com/en/derivatives/perpetual-style-futures/funding-rate).
- **Sàn phi tập trung kiểu AMM:** hợp đồng thông minh giữ quỹ dự trữ trên blockchain, giá do công thức quyết định; Uniswap dùng tích số không đổi `x · y = k`. Nguồn: [Uniswap](https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/glossary).
- **Trái phiếu doanh nghiệp tại Mỹ** giao dịch OTC nhưng phải báo cáo vào hệ thống TRACE của FINRA trong vòng 15 phút (quy tắc hiện hành tại thời điểm tra cứu). Nguồn: [FINRA](https://www.finra.org/filing-reporting/trade-reporting-and-compliance-engine-trace/trace-reporting-timeframes).
- **CFD bán lẻ — quy định khác nhau rất nhiều theo nước:**
  - *Liên minh châu Âu (ESMA, 2018):* đòn bẩy tối đa cho khách bán lẻ 30:1 (cặp FX chính), 20:1 (cặp FX phụ, vàng, chỉ số lớn), 10:1 (hàng hóa khác, chỉ số phụ), 5:1 (cổ phiếu riêng lẻ), 2:1 (tiền mã hóa); đóng bắt buộc khi ký quỹ xuống 50%; bảo vệ số dư âm. Nguồn: [ESMA](https://www.esma.europa.eu/press-news/esma-news/esma-agrees-prohibit-binary-options-and-restrict-cfds-protect-retail-investors). Anh (FCA) có biện pháp tương tự: [PS19/18](https://www.fca.org.uk/publications/policy-statements/ps19-18-restricting-contract-difference-products).
  - *Mỹ:* không có điều khoản ghi thẳng "cấm CFD", nhưng quy định về swap đối với người không đủ tư cách ECP khiến CFD OTC bán lẻ **thực tế không được cung cấp** (đây là cách diễn giải từ luật, cần đối chiếu nguồn pháp lý nếu quan trọng). Ngoại hối bán lẻ ở Mỹ có mức ký quỹ tối thiểu 2% (đòn bẩy 50:1) cho cặp chính và 5% (20:1) cho cặp khác (hiệu lực 10/2010, nguồn: [CFTC](https://www.cftc.gov/PressRoom/PressReleases/5883-10)).

### 2.3 Cách tiếp cận thị trường

| Khái niệm | Ý nghĩa |
|---|---|
| **Broker / API broker** | Cá nhân gửi lệnh qua công ty môi giới (giao diện, nền tảng MetaTrader hoặc API). Phổ biến nhất ở quy mô cá nhân |
| **DMA (direct market access)** | Gửi lệnh điện tử thẳng tới nơi giao dịch bằng hạ tầng của thành viên, không qua thao tác tay của broker. Theo MiFID II (Điều 4) còn có *sponsored access* — dùng mã của thành viên nhưng không qua hạ tầng của họ. Nguồn: [ESMA](https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/mifid-ii/article-4-definitions) |
| **Co-location** | Đặt máy chủ trong trung tâm dữ liệu của chính sàn để giảm độ trễ (ví dụ trung tâm của Nasdaq ở Carteret, New Jersey; của CME ở Aurora, Illinois). Quan trọng với HFT, ít ý nghĩa với chiến lược tần suất thấp. Nguồn: [Nasdaq](https://www.nasdaqtrader.com/Trader.aspx?id=colo), [CME](https://www.cmegroup.com/solutions/co-location.html) |
| **Prime broker** | Ngân hàng/broker cung cấp trọn gói thanh toán, lưu ký, cho vay chứng khoán và tài trợ đòn bẩy cho quỹ và tổ chức (kiến thức chung, chưa đối chiếu nguồn) |

### 2.4 Ở Việt Nam

Thị trường cổ phiếu (HOSE, HNX, UPCoM), phái sinh (hợp đồng tương lai chỉ số VN30) và khung pháp lý hiện hành được trình bày riêng trong [05 — Thị trường Việt Nam](05-thi-truong-viet-nam.md), kèm mức độ đã/chưa đối chiếu của từng thông tin.

### 2.5 Tiêu chí chọn nơi giao dịch cho một chiến lược quant

1. **Chi phí tổng** (spread + phí + swap/funding + thuế) so với biên lợi nhuận của chiến lược.
2. **Thanh khoản và độ sâu**: lệnh của bạn có thể vào/ra mà không tự đẩy giá không.
3. **API, độ ổn định và độ trễ**: có kết nối lập trình được không; giới hạn tốc độ gửi lệnh.
4. **Quy định và rủi ro đối tác**: tài sản có được bảo vệ không; nếu broker/sàn gặp sự cố thì sao.
5. **Chất lượng dữ liệu lịch sử** để kiểm định: có đủ sâu và có khớp với giá thực tế bạn sẽ giao dịch không.

## 3. Lợi nhuận được tính như thế nào?

### 3.1 Từ biến động giá đến lãi/lỗ (P&L)

- **Lãi/lỗ đã chốt (realized):** từ vị thế đã đóng. **Chưa chốt (unrealized / floating):** từ vị thế đang mở, tính theo giá thị trường hiện tại.
- **Công thức theo loại tài sản** (vị thế *mua*; vị thế *bán khống* đảo dấu):

| Loại | Lãi/lỗ gộp (gross) |
|---|---|
| Cổ phiếu | `(giá bán − giá mua) × số lượng` |
| Hợp đồng tương lai | `(giá đóng − giá mở) × hệ số nhân × số hợp đồng` — ghi nhận theo ngày (*mark-to-market*); ký quỹ chỉ là tiền đặt cọc, **không phải** chi phí |
| Ngoại hối / CFD | `(giá đóng − giá mở) × khối lượng` (khối lượng = lot × kích thước hợp đồng), quy đổi về tiền tệ của tài khoản |

- **Lãi/lỗ ròng (net)** = lãi/lỗ gộp **− chi phí giao dịch** (mục 3.2).

### 3.2 Chi phí — thứ làm biến mất nhiều chiến lược

| Chi phí | Giải thích |
|---|---|
| Spread | Chênh lệch giá mua (ask) – giá bán (bid); vào lệnh mua ở ask, bán ở bid |
| Phí/hoa hồng | Phí môi giới, phí sàn, phí thanh toán bù trừ |
| Trượt giá (slippage) | Chênh lệch giữa giá kỳ vọng và giá khớp thực tế |
| Tác động giá (market impact) | Lệnh lớn tự đẩy giá bất lợi cho chính nó |
| Swap / funding / phí vay | Phí qua đêm của ngoại hối/CFD; funding của hợp đồng vĩnh cửu tiền mã hóa; phí vay cổ phiếu để bán khống |
| Thuế | Tùy thị trường và quốc gia (xem [05](05-thi-truong-viet-nam.md) cho Việt Nam) |
| Hạ tầng | Dữ liệu, VPS, phần mềm — chi phí cố định cần tính vào hiệu quả tổng |

### 3.3 Lợi suất và năm hóa

- Lợi suất đơn: `r = P_t / P_{t−1} − 1`. Lợi suất log: `ln(P_t / P_{t−1})` — **cộng được theo thời gian**, nên tiện cho phân tích.
- Lãi kép: `CAGR = (V_cuối / V_đầu)^(1/số năm) − 1`.
- **Năm hóa:** lợi suất trung bình nhân với `N`, độ lệch chuẩn nhân với `√N`; `N = 252` (số ngày giao dịch/năm của cổ phiếu, hợp đồng tương lai) hoặc `365` cho thị trường giao dịch cả tuần như tiền mã hóa. Đây là **quy ước** — luôn ghi rõ bạn dùng `N` nào.

### 3.4 Điều chỉnh theo rủi ro — vì "lãi bao nhiêu" chưa đủ

| Chỉ số | Công thức | Ý nghĩa |
|---|---|---|
| **Sharpe ratio** | `(E[R] − R_f) / σ` (năm hóa: nhân `√N` nếu tính từ lợi suất vượt trội theo kỳ) | Lãi vượt lãi suất phi rủi ro trên mỗi đơn vị biến động |
| **Sortino ratio** | `(E[R] − MAR) / độ lệch giảm` | Như Sharpe nhưng chỉ phạt biến động **xuống** |
| **Max drawdown** | `max_t (đỉnh_t − V_t) / đỉnh_t` | Mức sụt sâu nhất từ đỉnh vốn |
| **Calmar ratio** | `CAGR / abs(max drawdown)` | Lãi so với nỗi đau tệ nhất |
| **Information ratio** | `E[R_p − R_b] / σ(R_p − R_b)` | Lãi vượt chuẩn so sánh trên mỗi đơn vị sai lệch so với chuẩn |

### 3.5 Chỉ số theo lệnh / theo bot (kiểu báo cáo MetaTrader 5)

Công thức dưới đây tóm tắt từ tài liệu MetaTrader 5 / MQL5 ([ENUM_SYMBOL_CALC_MODE](https://www.mql5.com/en/docs/constants/environment_state/marketinfoconstants), [Testing Report](https://www.metatrader5.com/en/terminal/help/algotrading/testing_report), [Testing Statistics](https://www.mql5.com/en/docs/constants/environment_state/statistics)). Các trang này không mở trực tiếp được khi soạn tài liệu, nên nguyên văn có thể khác đôi chút — hãy đối chiếu lại.

**Lãi/lỗ của một lệnh theo cách MT5 tính** (cho lệnh mua; lệnh bán đảo dấu):

| Loại symbol | Công thức |
|---|---|
| Forex, CFD, cổ phiếu sàn | `(giá đóng − giá mở) × Contract Size × Lots` |
| Futures | `(giá đóng − giá mở) × TickPrice / TickSize × Lots` |
| Trái phiếu sàn | `Lots × ContractSize × (giá đóng × mệnh giá + lãi tích lũy)` |

Ngoài lãi/lỗ giá còn có **commission, swap, fee** — MT5 ghi chúng thành các thuộc tính riêng của mỗi giao dịch; kết quả ròng = lãi/lỗ − commission − fee − swap (theo quy ước dấu của báo cáo). Swap có nhiều chế độ tính (theo điểm, theo tiền tệ, theo %/năm…) và thường nhân ba vào một ngày trong tuần để bù cuối tuần.

**Các chỉ số trong báo cáo Strategy Tester:**

| Chỉ số | Cách tính | Cách hiểu |
|---|---|---|
| Profit Factor | Tổng lãi gộp / tổng lỗ gộp (lấy giá trị tuyệt đối) | > 1: tổng lãi lớn hơn tổng lỗ. Không nói gì về drawdown |
| Expected Payoff | Lãi ròng / số giao dịch | Kỳ vọng lãi/lỗ mỗi lệnh |
| Recovery Factor | Lãi ròng / drawdown tối đa (MQL5 dùng drawdown theo **balance**) | Lãi so với lần sụt tệ nhất |
| Drawdown | *Absolute* = vốn đầu − balance thấp nhất; *Maximal* = sụt lớn nhất từ một đỉnh cục bộ (tiền); *Relative* = sụt lớn nhất tính theo % của đỉnh. Có cả bản theo **Balance** và theo **Equity** | Hai mức "Maximal" và "Relative" có thể thuộc hai đợt sụt khác nhau |
| Sharpe Ratio | `(Return − Rf) / Std(Return)`, trong tester coi `Rf = 0`. Thuật toán mới: tính log-return của equity theo từng bar rồi quy về năm bằng căn bậc hai của tỷ lệ thời gian (ví dụ dữ liệu ngày × √252) | **Không giống hệt** Sharpe trong sách giáo khoa; đừng so trực tiếp với số liệu từ nguồn khác |
| Profit Trades (% of total) | Số lệnh lãi / tổng số lệnh | MT5 không có chỉ số tên "win rate"; đây là chỉ số tương ứng |
| LR Correlation / LR Standard Error | Tương quan và sai số chuẩn giữa đường balance với đường hồi quy tuyến tính | Đường vốn càng "thẳng" thì tương quan càng gần 1 và sai số càng nhỏ; sai số chỉ so sánh được giữa hệ thống cùng vốn đầu |
| Z-Score | Kiểm định mức tương quan giữa các lệnh lãi/lỗ liên tiếp (theo độ lệch chuẩn) | Đo "chuỗi" thắng/thua, **không** phải điểm chất lượng |

**Sai lầm hay gặp khi tính lợi nhuận bot** (có cơ sở từ tài liệu trên):

1. **Dùng công thức forex cho mọi symbol** — futures tính theo `TickPrice / TickSize`, trái phiếu có lãi tích lũy; cần đọc chế độ tính của symbol (hoặc dùng hàm `OrderCalcProfit` của MQL5).
2. **Bỏ qua swap, commission, fee** — chúng được tách riêng nên rất dễ quên khi tự cộng lãi/lỗ.
3. **Lẫn balance với equity** — Recovery Factor của MQL5 dựa trên drawdown balance (không thấy lỗ chưa chốt); báo cáo có sẵn cả hai loại, hãy xem cả hai.
4. **Đọc Sharpe của MT5 như Sharpe sách giáo khoa** — khác cách tính (log-return equity theo bar, `Rf = 0`, quy về năm); backtest ngắn thì chênh lệch rõ hơn.
5. **Hiểu sai chỉ số thống kê** — Z-Score không đo chất lượng; LR Standard Error chỉ so sánh được khi cùng vốn đầu; Profit Factor đẹp vẫn có thể đi kèm drawdown rất sâu.

### 3.6 Ví dụ có số (đã tính lại bằng chương trình)

**A. Cổ phiếu — một chu kỳ mua rồi bán.** Mua 1,000 cổ phiếu giá 50.00; bán giá 52.00; phí 0.1% mỗi chiều.
- Lãi gộp = (52.00 − 50.00) × 1,000 = **2,000**
- Phí = 0.001 × (50,000 + 52,000) = **102**
- Lãi ròng = **1,898** → trên vốn 50,000 là **3.796%**

**B. Ngoại hối — kiểu MetaTrader.** Mua EURUSD 0.10 lot (10,000 đơn vị tiền cơ sở), vào 1.08000, thoát 1.08500.
- Biến động = +0.00500 = **+50 pip**
- Lãi gộp = (1.08500 − 1.08000) × 0.10 × 100,000 = **50.00 USD** (tiền báo giá là USD nên đã ở đơn vị USD)
- Giả sử hoa hồng minh họa 7 USD/lot/chiều → 1.40 USD; swap −0.30 USD
- Lãi ròng = 50.00 − 1.40 − 0.30 = **48.30 USD**

**C. Từ danh sách lệnh đến chỉ số của bot.** 10 lệnh (USD): +120, −60, +80, −50, +200, −70, +40, −90, +150, −30; vốn đầu 10,000.

| Chỉ số | Kết quả |
|---|---|
| Lãi gộp / Lỗ gộp | 590 / 300 |
| Lãi ròng | **290** (2.9% vốn) |
| Profit factor | 590 / 300 = **1.97** |
| Tỷ lệ thắng | 5/10 = **50%** |
| Lãi TB / Lỗ TB (payoff ratio) | 118 / 60 = **1.97** |
| Kỳ vọng mỗi lệnh | 0.5 × 118 − 0.5 × 60 = **29.00** |
| Max drawdown | **120** (1.17%): từ đỉnh 10,290 xuống 10,170 |
| Recovery factor | 290 / 120 = **2.42** |

Chỉ mới 10 lệnh nên các tỷ lệ này **nhiễu rất nhiều**; với số lệnh ít, đừng kết luận gì từ chúng. (Công thức Kelly của [03](03-yeu-to-cot-loi.md) cho `f* = 0.5 − 0.5/1.97 ≈ 24.6%` — một con số lý thuyết hay bị ước lượng quá lạc quan, nên thực hành dùng một phần nhỏ của nó.)

**D. Năm hóa Sharpe.** Lợi suất ngày trung bình 0.05%, độ lệch chuẩn ngày 0.8%, lãi suất phi rủi ro ≈ 0:
- Sharpe ngày = 0.0005 / 0.008 = 0.0625 → năm hóa × √252 ≈ **0.99**.
- Cùng dữ liệu nhưng dùng lịch 365 ngày: × √365 ≈ **1.19** — chênh vì **quy ước**, không phải vì chiến lược tốt hơn.

**E. Chi phí ăn mòn lãi.** Một chiến lược giao dịch khối lượng gấp 10 lần vốn mỗi năm (*turnover* 1000%), chi phí khứ hồi 10 bps (0.10%) cho mỗi lần: chi phí = 10 × 0.10% = **1.0%/năm**. Lãi gộp 12%/năm → lãi ròng **11%**. Nếu turnover gấp 10 lần nữa thì chi phí thành 10%/năm — **gần như xóa sạch** lãi gộp.

**F. Lỗ sâu khó gỡ.** Số % cần lãi để hòa vốn sau khi lỗ `d`: `1/(1−d) − 1`.

| Lỗ | 10% | 20% | 33% | 50% | 70% |
|---|---|---|---|---|---|
| Cần lãi để hòa vốn | 11.1% | 25.0% | 49.3% | 100% | 233% |

**G. Lợi suất đơn vs log.** +10% rồi −10%: đơn = (1.10 × 0.90) − 1 = **−1.00%**; log = ln 1.10 + ln 0.90 = **−1.005%** (≈ cùng một thứ, nhưng log cộng được).

### 3.7 Alpha và beta — lãi *thực sự* của chiến lược

Hồi quy lợi suất vượt trội của chiến lược theo lợi suất vượt trội của thị trường (CAPM):

`R_p − R_f = α + β × (R_m − R_f) + ε`

- **β** là phần lãi/lỗ chỉ đơn giản đi theo thị trường (có thể mua rẻ bằng quỹ chỉ số).
- **α** là phần **vượt** sau khi trừ β — đây mới là thứ mà "quant" muốn tạo ra. Một chiến lược lãi 15% nhưng β = 1 trong năm thị trường tăng 15% **không có alpha**.

### 3.8 Kinh tế của một quỹ — lãi của chiến lược khác lãi của nhà đầu tư

Quỹ phòng hộ thường thu hai loại phí: **phí quản lý** (tính theo % tài sản, hằng năm) và **phí thưởng hiệu suất** (tính theo % lợi nhuận, thường chỉ thu khi quỹ vượt đỉnh vốn cũ — *high-water mark* — và có thể kèm ngưỡng *hurdle*). Cấu trúc kinh điển là **"2 và 20"** (2% + 20%).

Ví dụ minh họa (quy ước: phí thưởng tính trên lãi **sau** phí quản lý; không có hurdle; hợp đồng thực tế khác nhau): quỹ lãi gộp **10%** →
- trừ phí quản lý 2% → 8%;
- phí thưởng 20% × 8% = 1.6%;
- nhà đầu tư nhận **6.4%**, tức 64% lãi gộp.

Mức phí bình quân thực tế của ngành do các khảo sát (HFR, Preqin…) công bố; số liệu mới nhất **chưa được đối chiếu** khi soạn tài liệu này — hãy xem khảo sát gần nhất trước khi trích dẫn.

### 3.9 Vì sao lãi trong backtest thường lớn hơn lãi thật

| Nguyên nhân | Giải thích ngắn |
|---|---|
| Overfitting / chọn lọc | Thử nhiều biến thể rồi chọn biến thể đẹp nhất: nó đẹp một phần nhờ may mắn |
| Look-ahead & survivorship bias | Vô tình dùng thông tin tương lai; bỏ sót mã đã hủy niêm yết |
| Chi phí bị đánh giá thấp | Spread, slippage, swap, phí thực tế cao hơn giả định |
| Sức chứa (capacity) | Vốn tăng → tác động giá tăng → lãi giảm |
| Thay đổi chế độ thị trường | Quan hệ trong quá khứ không còn nữa (*alpha decay*) |

Có các phương pháp thống kê để hiệu chỉnh: **Deflated Sharpe Ratio** (điều chỉnh Sharpe theo số lần thử và độ lệch/độ nhọn của lợi suất) và **Probability of Backtest Overfitting** (xác suất chiến lược tốt nhất trong mẫu lại kém ngoài mẫu) — chi tiết ở [03](03-yeu-to-cot-loi.md), yếu tố 3.

## 4. Kỳ vọng thực tế

- Quant **không** đảm bảo lợi nhuận. Nhiều chiến lược tự xây ở quy mô cá nhân **không có lợi thế bền vững sau chi phí**: trông tốt trong backtest rồi thua khi chạy thật (xem mục 3.9).
- Thua lỗ có thể vượt số vốn ký quỹ đối với một số sản phẩm đòn bẩy (kiểm tra điều khoản của broker/sàn).
- Thứ tự an toàn: **học → mô phỏng → forward-test → vốn nhỏ → tăng dần theo bằng chứng**, với giới hạn rủi ro đặt sẵn.
- Tài liệu này không khuyến nghị mua/bán bất kỳ tài sản hay sản phẩm nào.

---
Tiếp: [02 — Kênh học thuật](02-kenh-hoc-thuat.md) · [03 — Yếu tố cốt lõi](03-yeu-to-cot-loi.md) · [05 — Thị trường Việt Nam](05-thi-truong-viet-nam.md) · [Mục lục](../README.md)
