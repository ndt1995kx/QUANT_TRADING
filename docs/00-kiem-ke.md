# 00 — Kiểm kê tài sản QUANT

> Cập nhật: 2026-10-01 · Phạm vi: máy chạy phiên Claude Code này (container đám mây) và các thành phần đồng bộ từ tài khoản Claude của chủ repo.

## 1. Kết luận nhanh

- Máy mà phiên này truy cập được là **container đám mây tạm thời**, khởi tạo mới cho phiên làm việc. Nó **không phải** máy cá nhân của chủ repo.
- Trên container **không có** mã giao dịch, dữ liệu thị trường, kết quả backtest, notebook hay thư viện quant nào.
- Tài sản liên quan quant duy nhất tìm thấy: **01 skill mô tả quy trình dựng bot giao dịch tự động**, đồng bộ từ tài khoản Claude của chủ repo. Nội dung skill này **chưa được đưa lên repo** — repo đang ở chế độ **công khai** nên việc công bố cần chủ repo xác nhận trước.
- Phần "kiến thức quant" trong repo (tài liệu 01–05) là **kiến thức tổng quát đã tra cứu và kiểm chứng**, không phải dữ liệu lấy từ máy cá nhân.

## 2. Đã quét những gì, thấy gì

| Phạm vi | Cách quét | Kết quả |
|---|---|---|
| Kho Git `QUANT_TRADING` | `git log`, liệt kê tệp | 1 commit ("Initial commit"); chỉ có `README.md` (1 dòng) |
| Toàn bộ hệ tệp (trừ thư mục hệ thống, cache, `node_modules`, `.git`) | tìm theo tên: `*quant*`, `*backtest*`, `*trading*`, `*strategy*`, `*.mq5`, `*.mq4`, `*.mqh`, `*.ex5`, `*obsidian*` | không có gì của người dùng ngoài kho này và skill nêu trên |
| Dữ liệu và notebook | `*.ipynb`, `*.csv`, `*.parquet` ngoài thư mục hệ thống | 0 tệp |
| Thư viện Python quant | thử `import` pandas, numpy, scipy, statsmodels, scikit-learn, backtrader, vectorbt, ccxt, TA-Lib, yfinance, MetaTrader5 | **không có** thư viện nào được cài |
| Thành phần đồng bộ từ tài khoản | duyệt thư mục skill đồng bộ | 19 skill; **1** liên quan quant (nêu trên); 18 còn lại là công cụ tài liệu/thiết kế/marketing, không thuộc phạm vi quant nên không đưa vào kiểm kê |
| Đường dẫn cá nhân mà skill nhắc tới | kiểm tra sự tồn tại trên container | **không tồn tại** — thư mục đó nằm trên máy cá nhân của chủ repo |

## 3. Những gì không có trên container (nằm trên máy cá nhân)

Container không có quyền truy cập vào máy cá nhân của chủ repo, nên các thứ sau **chưa được thống kê**:

- Thư mục ghi chép/vault: phiên bản bot, ghi chú chiến lược, bài học rút ra.
- Mã nguồn bot (MQL5/Python), tệp đã biên dịch (`.ex5`), cấu hình.
- Dữ liệu lịch sử, kết quả backtest / forward-test / demo, log telemetry.
- Terminal MetaTrader 5 và các thiết lập đi kèm.

## 4. Cách hoàn tất kiểm kê trên máy cá nhân

**Cách A (khuyến nghị).** Mở Claude Code ngay trong thư mục dự án quant trên máy cá nhân và yêu cầu thống kê theo khung ở [04 — Kiến trúc tham chiếu](04-kien-truc-tham-chieu.md), rồi đẩy kết quả lên một nhánh riêng. Cách này dùng đúng quyền truy cập của bạn và bạn thấy từng thao tác được duyệt.

**Cách B.** Chạy các lệnh chỉ-đọc dưới đây (macOS/Linux) và dán kết quả lại vào phiên làm việc để tích hợp:

```bash
cd /đường/dẫn/tới/thư-mục-quant          # đổi thành thư mục dự án của bạn

# 1) Cấu trúc thư mục (3 cấp)
find . -maxdepth 3 -type d -not -path '*/.git*' | sort

# 2) Số tệp theo đuôi tệp
find . -type f -not -path '*/.git/*' | sed 's/.*\.//' | sort | uniq -c | sort -rn | head -30

# 3) Số tệp mã giao dịch và tài liệu
find . -type f \( -name '*.mq5' -o -name '*.mqh' -o -name '*.ex5' -o -name '*.py' -o -name '*.ipynb' \) -not -path '*/.git/*' | wc -l
find . -type f -name '*.md' -not -path '*/.git/*' | wc -l
```

> Các lệnh trên chỉ liệt kê **tên và số lượng**, không in nội dung tệp.

## 5. Quyền riêng tư và trạng thái repo

- Repo `ndt1995kx/QUANT_TRADING` hiện **công khai**: mọi nhánh và toàn bộ lịch sử commit đều xem được.
- Tài liệu 01–05 chỉ chứa kiến thức tổng quát. **Chưa đưa lên:** nội dung skill, đường dẫn trên máy cá nhân, thông tin tài khoản, tham số hoặc mã nguồn chiến lược.
- Trước khi đẩy bất cứ thứ gì thuộc chiến lược thật lên đây, hãy rà soát: tham số chiến lược, API key, thông tin tài khoản giao dịch, đường dẫn chứa tên người dùng. Nếu cần lưu bản sao riêng tư, hãy đặt repo ở chế độ `private` (Settings của repo → Danger Zone → Change visibility) hoặc dùng một repo riêng.

## 6. Nhật ký

| Ngày | Thay đổi |
|---|---|
| 2026-10-01 | Kiểm kê lần đầu; thêm tài liệu 01–05 |

---
[Mục lục](../README.md)
