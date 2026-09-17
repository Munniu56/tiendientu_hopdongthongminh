import json
import urllib.request
from datetime import datetime, timezone
from decimal import Decimal

# Dia chi vi hacker
HACKER_ADDRESS = "0x47666Fab8bd0Ac7003bce3f5C3585383F09486E2".lower()

# URL Blockscout API cong khai
URL = (
    "https://eth.blockscout.com/api"
    "?module=account&action=txlist"
    "&address=0x47666Fab8bd0Ac7003bce3f5C3585383F09486E2"
    "&sort=asc&page=1&offset=200"
)

def fetch_transactions():
    # Gui yeu cau toi API voi User-Agent tieu chuan
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return payload.get("result", [])

def main():
    transactions = fetch_transactions()

    outgoing_txs = []
    exact_10k_txs = []

    print("=" * 160)
    print(f"{'STT':<4} | {'Gio UTC':<20} | {'Dia chi nhan (to)':<44} | {'So ETH':<12} | {'Tx Hash'}")
    print("-" * 160)

    for tx in transactions:
        from_addr = tx.get("from", "").lower()
        val_wei = int(tx.get("value", "0"))

        # Loc giao dich di ra tu dia chi hacker va co value > 0
        if from_addr == HACKER_ADDRESS and val_wei > 0:
            ts = int(tx.get("timeStamp", "0"))
            dt_utc = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
            to_addr = tx.get("to", "")
            val_eth = Decimal(val_wei) / Decimal(10**18)
            tx_hash = tx.get("hash", "")

            tx_info = {
                "utc": dt_utc,
                "timestamp": ts,
                "to": to_addr,
                "val_eth": val_eth,
                "val_wei": val_wei,
                "hash": tx_hash
            }

            outgoing_txs.append(tx_info)
            idx = len(outgoing_txs)
            print(f"{idx:<4} | {dt_utc:<20} | {to_addr:<44} | {str(val_eth):<12} | {tx_hash}")

            # Kiem tra giao dich dung 10.000 ETH
            if val_wei == 10000 * 10**18:
                exact_10k_txs.append(tx_info)

    print("-" * 160)
    print(f"Tong so giao dich di ra (from = hacker, value > 0): {len(outgoing_txs)}")
    print(f"So giao dich dung 10.000 ETH: {len(exact_10k_txs)}")

    if exact_10k_txs:
        # Sap xep theo thoi gian de lay som nhat va muon nhat
        sorted_10k = sorted(exact_10k_txs, key=lambda x: x["timestamp"])
        earliest_tx = sorted_10k[0]
        latest_tx = sorted_10k[-1]

        print("\n" + "=" * 50 + " GIAO DICH 10.000 ETH SOM NHAT " + "=" * 50)
        print(f"Gio UTC      : {earliest_tx['utc']}")
        print(f"Dia chi nhan : {earliest_tx['to']}")
        print(f"So ETH       : {earliest_tx['val_eth']} ETH")
        print(f"Tx Hash      : {earliest_tx['hash']}")

        print("\n" + "=" * 50 + " GIAO DICH 10.000 ETH MUON NHAT " + "=" * 50)
        print(f"Gio UTC      : {latest_tx['utc']}")
        print(f"Dia chi nhan : {latest_tx['to']}")
        print(f"So ETH       : {latest_tx['val_eth']} ETH")
        print(f"Tx Hash      : {latest_tx['hash']}")
        print("=" * 128)

if __name__ == "__main__":
    main()
