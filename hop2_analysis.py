import json
import sys
import time
import urllib.request
from datetime import datetime, timezone
from decimal import Decimal

# Dam bao in ra Unicode chuan tren console Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ADDR_HOP2 = "0x36ed3c0213565530c35115d93a80f9c04d94e4cb".lower()
URL_TXLIST = f"https://eth.blockscout.com/api?module=account&action=txlist&address={ADDR_HOP2}&sort=asc"
TX_HASH_MSG = "0xf0f7c2a84e29300089fc1049982675c68efcfc8a18557193f113f9881d014f55"
URL_TX_MSG = f"https://eth.blockscout.com/api/v2/transactions/{TX_HASH_MSG}"

def fetch_data(url, max_retries=3):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    req = urllib.request.Request(url, headers=headers)
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < max_retries - 1:
                time.sleep(3 * (attempt + 1))
            else:
                raise e

def decode_hex_to_utf8(hex_str):
    # Ham giai ma chuoi hex sang van ban UTF-8
    clean_hex = hex_str[2:] if hex_str.startswith("0x") else hex_str
    try:
        raw_bytes = bytes.fromhex(clean_hex)
        return raw_bytes.decode("utf-8")
    except Exception as e:
        return f"Loi giai ma: {e}"

def main():
    print("=== BAT DAU XU LY HO SO TRACE LAB 3B (TRAM 3) ===")
    
    # 1. Truy van danh sach giao dich cua vi Hop 2
    print("\n[1] Goi Blockscout API truy van danh sach giao dich vi Hop 2...")
    try:
        data_txlist = fetch_data(URL_TXLIST)
        txs = data_txlist.get("result", [])
    except Exception as e:
        print(f"Loi goi API txlist: {e}")
        return

    # Tram 3a:
    # Tim giao dich nhan (To = ADDR_HOP2) co so tien 10.000 ETH dau tien
    in_10k = [t for t in txs if t.get("to", "").lower() == ADDR_HOP2 and int(t.get("value", 0)) == 10000 * 10**18]
    first_in = in_10k[0]
    ts_in = int(first_in["timeStamp"])
    dt_in = datetime.fromtimestamp(ts_in, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    hash_in = first_in["hash"]

    # Tim giao dich gui di (From = ADDR_HOP2) dau tien co value > 0 ETH
    out_gt0 = [t for t in txs if t.get("from", "").lower() == ADDR_HOP2 and int(t.get("value", 0)) > 0]
    first_out = out_gt0[0]
    ts_out = int(first_out["timeStamp"])
    dt_out = datetime.fromtimestamp(ts_out, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    val_out = Decimal(int(first_out["value"])) / Decimal(10**18)
    to_out = first_out.get("to", "")
    hash_out = first_out["hash"]

    # Tinh thoi gian tien nam yen
    diff_sec = ts_out - ts_in
    hours = diff_sec // 3600
    mins = (diff_sec % 3600) // 60
    secs = diff_sec % 60
    idle_time_str = f"{diff_sec:,} giây (~ {hours} giờ {mins} phút {secs} giây)"

    print(f"   + Nhan 10.000 ETH luc : {dt_in} | Tx: {hash_in}")
    print(f"   + Giao dich ra dau    : {val_out} ETH luc {dt_out} | To: {to_out} | Tx: {hash_out}")
    print(f"   + Thoi gian nam yen   : {idle_time_str}")

    # Tram 3b:
    print("\n[2] Giai ma chuoi Hex va truy van tin nhan tren chuoi...")
    # Truong hop 0xf0f7c2a8... la Tx Hash chua tin nhan
    time.sleep(2)
    try:
        tx_msg_data = fetch_data(URL_TX_MSG)
        raw_input_hex = tx_msg_data.get("raw_input", "")
        decoded_message = decode_hex_to_utf8(raw_input_hex).strip()
    except Exception as e:
        print(f"Loi goi API tx message: {e}")
        raw_input_hex = "0x54686973206973204642492e20596f7520636f756c642062652061727265737465642e20576520617265206d6f6e69746f72696e6720617420796f75206f766572206b69746368656e2077696e646f772e203130302045544820746f2074686973206164647265737320616e642077652061726520676f696e6720617761792e20"
        decoded_message = decode_hex_to_utf8(raw_input_hex).strip()

    print(f"   + Tx Hash tin nhan    : {TX_HASH_MSG}")
    print(f"   + Input Data (Hex)    : {raw_input_hex}")
    print(f"   + Ket qua giai ma     : \"{decoded_message}\"")

    # 3. Cap nhat truc tiep vao file trace.md
    print("\n[3] Dang cap nhat truc tiep vao file Lab/trace.md...")
    trace_path = r"d:\Antigravity IDE\tiendientu\Lab\trace.md"
    with open(trace_path, "r", encoding="utf-8") as f:
        content = f.read()

    target_block = """# Trạm 3 — Hop 2 & tin nhắn
| Câu hỏi | Trả lời | Bằng chứng |
| -| -| -|
| . | | |

Nội dung tin nhắn giải mã: " ."

Anonymous vs pseudonymous: ."""

    replacement_block = f"""# Trạm 3 — Hop 2 & tin nhắn

### Bảng Trạm 3a — Dòng tiền tại Hop 2 (`{ADDR_HOP2}`)
| Chỉ số | Giá trị | Bằng chứng |
| -| -| -|
| Ví nhận 10.000 ETH lúc nào | `{dt_in}` | Tx: `{hash_in}` |
| Giao dịch ra đầu tiên (> 0 ETH) | `{val_out} ETH` (đến ví `{to_out}`) lúc `{dt_out}` | Tx: `{hash_out}` |
| Thời gian tiền nằm yên | `{idle_time_str}` | Hiệu số timestamp giữa giao dịch nạp 10.000 ETH và giao dịch rút đầu tiên |

### Trạm 3b — Giải mã Hex & Thảo luận

- **Mã giao dịch (Tx Hash) chứa tin nhắn:** `{TX_HASH_MSG}`
- **Chuỗi Hex Input Data:** `{raw_input_hex}`
- **Nội dung tin nhắn giải mã:**
  > *"{decoded_message}"*
  *(Tạm dịch: "Đây là FBI. Bạn có thể bị bắt giữ. Chúng tôi đang theo dõi bạn qua cửa sổ nhà bếp. Hãy gửi 100 ETH đến địa chỉ này và chúng tôi sẽ rời đi.")*

#### Thảo luận:
1. **Giải thích vì sao không thể biết chính xác người gửi tin nhắn:**
   Trên mạng lưới Ethereum, bất kỳ cá nhân nào sở hữu một địa chỉ ví đều có thể khởi tạo một giao dịch (chỉ cần trả một lượng nhỏ phí Gas) gửi đến ví của hacker và đính kèm văn bản tùy ý vào trường **Input Data (Payload)**. Trường Input Data hoàn toàn mở và không có cơ chế xác thực danh tính thực tế (real-world identity) của người gửi. Vì vậy, bất kỳ ai cũng có thể mạo danh các tổ chức thực thi pháp luật (như FBI), chuyên gia an ninh mạng hoặc người dùng khác để gửi tin nhắn hăm dọa, tống tiền hoặc chọc ghẹo mà không thể xác minh danh tính thực chỉ qua dữ liệu on-chain.

2. **Phân biệt tính chất Pseudonymous (Bí danh) vs Anonymous (Ẩn danh):**
   Trường hợp này minh chứng rõ nét cho tính chất **Pseudonymous (Bí danh)** của Blockchain thay vì **Anonymous (Ẩn danh)**:
   - **Pseudonymous (Bí danh):** Mọi giao dịch, giá trị chuyển giao, mốc thời gian và luồng dịch chuyển từ Bybit -> Hop 0 -> Hop 1 -> Hop 2 đều được công khai, minh bạch và lưu trữ vĩnh viễn trên sổ cái chuỗi khối dưới danh nghĩa các địa chỉ ví mã hóa (`0x36ed...`, `0x4766...`). Bất kỳ ai cũng có thể truy vết toàn bộ hành trình của dòng tiền. Danh tính chỉ tạm thời mang tính bí danh cho đến khi địa chỉ ví bị liên kết với thông tin định danh (KYC) tại các sàn CEX hoặc thông qua điều tra off-chain.
   - **Anonymous (Ẩn danh):** Là khi thông tin về người gửi, người nhận và số lượng tiền giao dịch bị ẩn giấu hoàn toàn, không thể xem hoặc liên kết trên sổ cái công khai (ví dụ: công nghệ Zero-Knowledge của Monero, hoặc sau khi dòng tiền đã bị xáo trộn qua Tornado Cash)."""

    if target_block in content:
        new_content = content.replace(target_block, replacement_block, 1)
        with open(trace_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(new_content)
        print("-> DA CAP NHAT THANH CONG VAO FILE Lab/trace.md!")
    else:
        print("Khong tim thay target_block, kiem tra lai noi dung trace.md!")

if __name__ == "__main__":
    main()
