#!/usr/bin/env python3
"""Trích ghi chú liên quan quant từ các vault Obsidian khác (BRAIN, Assistant...) vào vault này.

CHẠY TRÊN MÁY CÁ NHÂN (nơi có các vault). Chỉ dùng thư viện chuẩn, không kết nối mạng.

An toàn:
  * Mặc định chỉ XEM TRƯỚC (dry-run): liệt kê ghi chú sẽ được chọn, không ghi gì.
  * Với --apply: SAO CHÉP (không di chuyển, không sửa nguồn) tệp .md vào <dest>/<tên-vault>/...
  * Đích mặc định là thư mục `_extracted/` — đã nằm trong .gitignore để ghi chú riêng tư
    KHÔNG bị đưa lên repo công khai. Đừng dùng `git add -f` với thư mục này.
  * Tệp manifest chỉ ghi đường dẫn, điểm, kích thước; không chép nội dung ghi chú.
  * Cờ "nhạy cảm" chỉ báo có mẫu giống khóa/mật khẩu trong ghi chú; hãy tự kiểm tra bản sao.

Ví dụ:
  python3 tools/extract_quant_notes.py --source ~/AI/BRAIN --source ~/AI/Assistant
  python3 tools/extract_quant_notes.py --source ~/AI/BRAIN --source ~/AI/Assistant --apply
"""
import argparse
import datetime as dt
import re
import shutil
import sys
from pathlib import Path

SKIP_DIRS = {".git", ".obsidian", ".trash", "node_modules", "__pycache__", "_extracted"}
DEFAULT_KEYWORDS = [
    "quant", "backtest", "forward test", "forward-test", "mql5", "mql4", "metatrader", "mt5",
    "expert advisor", "trading", "trader", "alpha", "sharpe", "drawdown", "slippage", "spread",
    "stat arb", "mean reversion", "momentum", "volatility", "portfolio", "hedge fund",
    "giao dịch", "định lượng", "chiến lược", "lợi nhuận", "rủi ro", "sàn", "ký quỹ",
]
SECRET_RE = re.compile(
    r"(api[_-]?key|secret|passwd|password|token|private[_-]?key)\s*[:=]\s*\S{8,}|"
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----", re.I)
MAX_BYTES = 2 * 1024 * 1024


def score_note(path: Path, rel: Path, kws):
    try:
        if path.stat().st_size > MAX_BYTES:
            return 0, False
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return 0, False
    low, name = text.lower(), (str(rel.parent) + "/" + rel.stem).lower()
    score = 0
    for k in kws:
        score += 3 * name.count(k) + min(low.count(k), 5)
    return score, bool(SECRET_RE.search(text))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", action="append", required=True, type=Path,
                    help="Thư mục vault nguồn (lặp lại cho nhiều vault)")
    ap.add_argument("--dest", type=Path, default=Path(__file__).resolve().parent.parent / "_extracted",
                    help="Thư mục đích (mặc định: <repo>/_extracted, đã bị git bỏ qua)")
    ap.add_argument("--keyword", action="append", help="Thêm từ khóa (có thể lặp lại)")
    ap.add_argument("--min-score", type=int, default=6, help="Điểm tối thiểu để chọn (mặc định 6)")
    ap.add_argument("--apply", action="store_true", help="Thực sự sao chép (mặc định chỉ xem trước)")
    a = ap.parse_args()

    kws = [k.lower() for k in DEFAULT_KEYWORDS + (a.keyword or [])]
    dest = a.dest.expanduser().resolve()
    rows = []
    for src in a.source:
        src = src.expanduser().resolve()
        if not src.is_dir():
            sys.exit(f"Không thấy thư mục nguồn: {src}")
        if dest == src or src in dest.parents or dest in src.parents:
            sys.exit(f"Đích và nguồn không được lồng nhau: {src} / {dest}")
        for p in sorted(src.rglob("*.md")):
            rel = p.relative_to(src)
            if p.is_symlink() or any(part in SKIP_DIRS for part in rel.parts):
                continue
            s, flag = score_note(p, rel, kws)
            if s >= a.min_score:
                rows.append((src.name, rel, s, flag, p.stat().st_size,
                             dt.datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d"), p))

    rows.sort(key=lambda r: -r[2])
    print(f"Chọn được {len(rows)} ghi chú (điểm >= {a.min_score}). Đích: {dest}")
    for v, rel, s, flag, size, mt, _ in rows[:40]:
        print(f"  {s:4d}  {v}/{rel}" + ("   [NHẠY CẢM?]" if flag else ""))
    if len(rows) > 40:
        print(f"  ... và {len(rows) - 40} ghi chú nữa (xem manifest sau khi --apply)")
    if not a.apply:
        print("\nĐây là bản xem trước. Thêm --apply để sao chép.")
        return

    for v, rel, _, _, _, _, p in rows:
        out = dest / v / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, out)
    lines = ["# Manifest trích xuất", "",
             f"Tạo lúc {dt.datetime.now():%Y-%m-%d %H:%M}. Chỉ ghi đường dẫn, không chép nội dung.", "",
             "| Điểm | Vault | Ghi chú | Sửa lần cuối | KB | Nhạy cảm? |", "|---|---|---|---|---|---|"]
    for v, rel, s, flag, size, mt, _ in rows:
        lines.append(f"| {s} | {v} | [[{v}/{rel.with_suffix('').as_posix()}]] | {mt} | {size // 1024} | {'có' if flag else ''} |")
    (dest / "_manifest.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Đã sao chép {len(rows)} ghi chú vào {dest}; manifest: {dest / '_manifest.md'}")


if __name__ == "__main__":
    main()
