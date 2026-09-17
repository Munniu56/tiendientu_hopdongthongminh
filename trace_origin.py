import json
import urllib.request

url = "https://eth.drpc.org"
payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "debug_traceTransaction",
    "params": [
        "0xb61413c495fdad6114a7aa863a00b2e3c28945979a10885b12b30316ea9f072c",
        {"tracer": "callTracer"}
    ]
}

req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode("utf-8"),
    headers={"content-type": "application/json", "User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(req) as resp:
    res = json.loads(resp.read().decode("utf-8"))

def print_tree(call, indent=0):
    val_hex = call.get("value", "0x0")
    val_int = int(val_hex, 16) if val_hex.startswith("0x") else int(val_hex)
    t = call.get("type")
    f = call.get("from")
    to = call.get("to")
    inp = call.get("input", "")[:10]
    print("  " * indent + f"{t} | from: {f} | to: {to} | val: {val_int/1e18} ETH | input: {inp}")
    for sub in call.get("calls", []):
        print_tree(sub, indent + 1)

print("Call Tree of 0xb61413c495fdad6114a7aa863a00b2e3c28945979a10885b12b30316ea9f072c:")
print_tree(res.get("result", {}))
