# 06 — Dựng "bộ não" Obsidian cho dự án trên máy cá nhân

> Cập nhật: 2026-10-01 · Hướng dẫn chạy **trên máy cá nhân** (macOS/Linux). Môi trường đám mây dùng để soạn tài liệu không truy cập được ổ đĩa và các vault của bạn.

## 1. Ý tưởng

Thư mục dự án `QUANT_TRADING` chính là một **vault Obsidian**:

- Các tài liệu `docs/00`–`05` đã dùng liên kết tương đối, bảng và sơ đồ Mermaid — Obsidian hiển thị được ngay.
- Ghi chú quant trích từ các vault khác (BRAIN, Assistant…) được gom vào `_extracted/` — thư mục này **bị git bỏ qua**, nên ghi chú riêng tư không lên repo công khai.
- Khi đã rà soát, bạn tự chuyển ghi chú đáng giữ từ `_extracted/` sang một thư mục có tổ chức (ví dụ `notes/`) và quyết định cái nào được phép công khai.

## 2. Lấy repo về máy

```bash
mkdir -p ~/AI && cd ~/AI
git clone -b claude/jolly-carson-hayqwk https://github.com/ndt1995kx/QUANT_TRADING.git QUANT_TRADING
```

Nếu thư mục đã có sẵn: `cd ~/AI/QUANT_TRADING && git fetch origin && git checkout claude/jolly-carson-hayqwk && git pull`.

Trong Obsidian: *Open folder as vault* → chọn `~/AI/QUANT_TRADING`.

## 3. Trích ghi chú quant từ BRAIN / Assistant

```bash
cd ~/AI/QUANT_TRADING

# Bước 1 — xem trước, chưa ghi gì (đổi đường dẫn vault cho đúng máy bạn)
python3 tools/extract_quant_notes.py --source ~/AI/BRAIN --source ~/AI/Assistant

# Bước 2 — hài lòng thì sao chép vào _extracted/
python3 tools/extract_quant_notes.py --source ~/AI/BRAIN --source ~/AI/Assistant --apply
```

Cách script hoạt động:

| Điểm | Hành vi |
|---|---|
| Phạm vi | Chỉ tệp `.md`; bỏ qua `.obsidian`, `.git`, `.trash`; bỏ tệp > 2 MB và liên kết tượng trưng |
| Chọn lọc | Chấm điểm theo từ khóa quant (tiếng Anh và tiếng Việt) trong tên đường dẫn và nội dung; chỉnh bằng `--keyword` và `--min-score` |
| An toàn | Mặc định xem trước; `--apply` chỉ **sao chép**, không sửa/xóa nguồn; từ chối đích lồng trong nguồn |
| Riêng tư | Đích mặc định `_extracted/` đã nằm trong `.gitignore`; `_manifest.md` chỉ ghi đường dẫn, không chép nội dung; gắn cờ ghi chú có mẫu giống khóa/mật khẩu |

**Giới hạn cần biết:** tệp đính kèm (ảnh, PDF) không được sao chép; liên kết `[[...]]` tới ghi chú không được chọn sẽ thành liên kết "chưa tồn tại" trong bản sao. Điểm số là heuristic — hãy đọc `_manifest.md` và bản xem trước trước khi tin.

## 4. Sau khi trích

1. Mở `_extracted/_manifest.md`, rà các dòng có cờ "Nhạy cảm?" và xóa/che khóa trong **bản sao**.
2. Chuyển ghi chú đáng giữ sang `notes/` (hoặc cấu trúc bạn muốn) và nối vào các tài liệu `docs/` bằng liên kết `[[ ]]` hoặc liên kết tương đối.
3. Chỉ commit những gì bạn chấp nhận công khai — repo này đang **công khai**. Nếu muốn commit cả ghi chú riêng tư, hãy đặt repo sang `private` trước (Settings → Danger Zone → Change visibility) rồi sửa `.gitignore`.
4. Không dùng `git add -f` cho `_extracted/` hoặc `private/`.

---
[Mục lục](../README.md) · [00 — Kiểm kê](00-kiem-ke.md)
