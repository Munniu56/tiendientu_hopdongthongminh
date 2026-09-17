import json
import urllib.request
from datetime import datetime, timezone
from decimal import Decimal

ADDR = "0x36ed3c0213565530c35115d93a80f9c04d94e4cb".lower()
URL = f"https://eth.blockscout.com/api?module=account&action=txlist&address={ADDR}&sort=asc"

req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode("utf-8"))

txs = data.get("result", [])
print(f"Total txs: {len(txs)}")

# 1. Giao dich nhan (To = ADDR) co 10.000 ETH dau tien
in_10k = [t for t in txs if t.get("to", "").lower() == ADDR and int(t.get("value", 0)) == 10000 * 10**18]
if in_10k:
    first_in = in_10k[0]
    ts_in = int(first_in["timeStamp"])
    dt_in = datetime.fromtimestamp(ts_in, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"Nhan 10k ETH luc: {dt_in} (ts={ts_in}), Hash: {first_in['hash']}")
else:
    print("Khong tim thay tx nhan 10k ETH")

# 2. Giao dich gui di (From = ADDR) dau tien co value > 0 ETH
out_gt0 = [t for t in txs if t.get("from", "").lower() == ADDR and int(t.get("value", 0)) > 0]
if out_gt0:
    first_out = out_gt0[0]
    ts_out = int(first_out["timeStamp"])
    dt_out = datetime.fromtimestamp(ts_out, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    val_out = Decimal(int(first_out["value"])) / Decimal(10**18)
    print(f"Giao dich ra dau tien: {val_out} ETH luc {dt_out} (ts={ts_out}), To: {first_out.get('to')}, Hash: {first_out['hash']}")
    
    # 3. Thoi gian tien nam yen
    diff = ts_out - ts_in
    hours = diff // 3600
    mins = (diff % 3600) // 60
    secs = diff % 60
    print(f"Thoi gian tien nam yen: {diff} giay ({hours} gio {mins} phut {secs} giay)")
else:
    print("Khong tim thay tx ra co value > 0")

# 4. Kiem tra cac tx co input data
print("\n--- Kiem tra input data cac tx ---")
for t in txs:
    inp = t.get("input", "")
    if inp and inp != "0x":
        print(f"Tx: {t['hash']} | from: {t['from']} | to: {t['to']} | val: {int(t['value'])/1e18} | input_len: {len(inp)}")
        print(f"Raw input: {inp[:80]}...")
        try:
            clean_hex = inp[2:] if inp.startswith("0x") else inp
            decoded = bytes.fromhex(clean_hex).decode("utf-8", errors="replace")
            print(f"Decoded: {decoded[:100]}")
        except Exception as e:
            print(f"Decode error: {e}")

# 5. Kiem tra chuoi hex user yeu cau: 0xf0f7c2a84e29300089fc1049982675c68efcfc8a18557193f113f9881d014f55
test_hex = "0xf0f7c2a84e29300089fc1049982675c68efcfc8a18557193f113f9881d014f55"
print("\n--- Test hex user dua ---")
print("User hex:", test_hex)
try:
    h = test_hex[2:] if test_hex.startswith("0x") else test_hex
    print("Decoded utf-8 (replace):", bytes.fromhex(h).decode("utf-8", errors="replace"))
    print("Decoded latin1:", bytes.fromhex(h).decode("latin1", errors="replace"))
except Exception as e:
    print("Error:", e)
