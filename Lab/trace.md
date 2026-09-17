# Lab 3B — Follow the Money — Ngo Thi Thuy Van — 23K4300023

# Trạm 1 — Giao dịch gốc
| Trường | Giá trị |
| -| -|
| Status | `Success` |
| Block | `21895251` |
| Timestamp (UTC) | `Feb-21-2025 02:16:11 PM +UTC` (14:16:11 UTC) |
| From | `0x0fa09C3A328792253f8dee7116848723b72a6d2e` (Bybit Exploiter) |
| To | `0x1Db92e2EeBC8E0c075a02BeA49a2935BcD2dFCF4` (Bybit: Cold Wallet 1) |
| Value | `0 ETH` |
| Transaction Fee | `0.000378762248769534 ETH` |
| Ví nhận 401.346 ETH (Hop 0) | `0x47666Fab8bd0Ac7003bce3f5C3585383F09486E2` (Bybit Exploiter 1) |

Vì sao Value = 0 mà tiền vẫn đi: Đây là giao dịch tương tác gọi hàm với Hợp đồng thông minh (`sweepETH(address to)`). Trường `Value` ở cấp giao dịch gốc bằng 0 ETH vì ví gửi (`From`) không đính kèm ETH cá nhân khi khởi tạo lệnh. Tuy nhiên, mã lệnh trong hợp đồng thông minh ví lạnh Bybit (`To`) khi được kích hoạt đã thực thi lệnh rút toàn bộ số dư 401.346,77 ETH đang lưu trữ trong hợp đồng và chuyển tiếp sang ví nhận của kẻ tấn công (`Hop 0`) thông qua một **Giao dịch nội bộ (Internal Transaction)**.

# Trạm 2 — Hop 1
| Chỉ số | Giá trị | Bằng chứng |
| -| -| -|
| Giao dịch ra đầu tiên (> 0 ETH) | `1 ETH` (lúc `14:29:47 UTC` ngày 21/02/2025 đến `0xa4b2fd68593b6f34e51cb9edb66e71c1b4ab449e`) | `0xdd5cd734d4d67ff5af7e53cdd72c26d4d7d28d08c8f0ff32d12ab3e2a277e4bc` |
| Số giao dịch đúng 10.000 ETH | `40` giao dịch (Tổng cộng `400.000 ETH` chuyển đến 40 ví nhận mới) | Blockscout API trả về đúng 40 giao dịch có `value = 10000000000000000000000 wei` |
| Giao dịch 10.000 ETH sớm nhất | `14:56:11 UTC` ngày 21/02/2025 (đến `0x36ed3c0213565530c35115d93a80f9c04d94e4cb`) | `0x0359814b48479156b804c8330878214943204c597d88affcb164d04907fa2b25` |
| Giao dịch 10.000 ETH muộn nhất | `15:54:23 UTC` ngày 21/02/2025 (đến `0xbca02b395747d62626a65016f2e64a20bd254a39`) | `0x0edac66a8fa637fa26807071d8a5ce8906c7d7a22c075ae25acf90ff774c7641` |
| Khoảng thời gian thực hiện nhóm 10.000 ETH | `3.492 giây` (~ 58 phút 12 giây, từ 14:56:11 đến 15:54:23 UTC) | Hiệu số timestamp giữa giao dịch 10.000 ETH đầu tiên và cuối cùng |
| Số dư ETH hiện tại của ví | `0.206896893854386779 ETH` (`206.896.893.854.386.779 Wei`) | Blockscout API (`module=account&action=balance`) |

Trả lời 3 câu thảo luận:
1. **Ý nghĩa của giao dịch 1 ETH đầu tiên:** Đây là giao dịch thử nghiệm (*test transaction*) nhằm kiểm tra tính thông suốt của đường dẫn ví và bảo đảm cấu hình mạng không gặp lỗi trước khi chuyển số tài sản khổng lồ.
2. **Lý do chia nhỏ thành các gói đúng 10.000 ETH:** Kẻ tấn công sử dụng chiến thuật phân tán dòng tiền (*smurfing / peeling chain*) để phân tán rủi ro, tránh bị phong tỏa toàn bộ tài sản cùng lúc và làm tăng độ phức tạp cho các cơ quan điều tra khi phải theo dõi đồng thời 40 luồng giao dịch độc lập.
3. **Dấu hiệu thực hiện tự động bằng Script/Bot:** Các giao dịch được kích hoạt liên tục với tốc độ rất nhanh, nhiều giao dịch diễn ra trong cùng một giây (ví dụ: 15:48:23 có 7 giao dịch, 15:49:35 có 5 giao dịch) hoặc cách nhau đúng chu kỳ 12 giây (khoảng thời gian tạo khối của mạng Ethereum), khẳng định có sự can thiệp của mã kịch bản/bot tự động hóa.


# Trạm 3 — Hop 2 & tin nhắn

### Bảng Trạm 3a — Dòng tiền tại Hop 2 (`0x36ed3c0213565530c35115d93a80f9c04d94e4cb`)
| Chỉ số | Giá trị | Bằng chứng |
| -| -| -|
| Ví nhận 10.000 ETH lúc nào | `2025-02-21 14:56:11 UTC` | Tx: `0x0359814b48479156b804c8330878214943204c597d88affcb164d04907fa2b25` |
| Giao dịch ra đầu tiên (> 0 ETH) | `5000 ETH` (đến ví `0x4571bd67d14280e40bf3910bd39fbf60834f900a`) lúc `2025-02-22 06:28:23 UTC` | Tx: `0xbf80907830e46317da2c1708a13a9f016e242f8a6db6e6b0706ea5f2328cb001` |
| Thời gian tiền nằm yên | `55,932 giây (~ 15 giờ 32 phút 12 giây)` | Hiệu số timestamp giữa giao dịch nạp 10.000 ETH và giao dịch rút đầu tiên |

### Trạm 3b — Giải mã Hex & Thảo luận

- **Mã giao dịch (Tx Hash) chứa tin nhắn:** `0xf0f7c2a84e29300089fc1049982675c68efcfc8a18557193f113f9881d014f55`
- **Chuỗi Hex Input Data:** `0x54686973206973204642492e20596f7520636f756c642062652061727265737465642e20576520617265206d6f6e69746f72696e6720617420796f75206f766572206b69746368656e2077696e646f772e203130302045544820746f2074686973206164647265737320616e642077652061726520676f696e6720617761792e20`
- **Nội dung tin nhắn giải mã:**
  > *"This is FBI. You could be arrested. We are monitoring at you over kitchen window. 100 ETH to this address and we are going away."*
  *(Tạm dịch: "Đây là FBI. Bạn có thể bị bắt giữ. Chúng tôi đang theo dõi bạn qua cửa sổ nhà bếp. Hãy gửi 100 ETH đến địa chỉ này và chúng tôi sẽ rời đi.")*

#### Thảo luận:
1. **Giải thích vì sao không thể biết chính xác người gửi tin nhắn:**
   Trên mạng lưới Ethereum, bất kỳ cá nhân nào sở hữu một địa chỉ ví đều có thể khởi tạo một giao dịch (chỉ cần trả một lượng nhỏ phí Gas) gửi đến ví của hacker và đính kèm văn bản tùy ý vào trường **Input Data (Payload)**. Trường Input Data hoàn toàn mở và không có cơ chế xác thực danh tính thực tế (real-world identity) của người gửi. Vì vậy, bất kỳ ai cũng có thể mạo danh các tổ chức thực thi pháp luật (như FBI), chuyên gia an ninh mạng hoặc người dùng khác để gửi tin nhắn hăm dọa, tống tiền hoặc chọc ghẹo mà không thể xác minh danh tính thực chỉ qua dữ liệu on-chain.

2. **Phân biệt tính chất Pseudonymous (Bí danh) vs Anonymous (Ẩn danh):**
   Trường hợp này minh chứng rõ nét cho tính chất **Pseudonymous (Bí danh)** của Blockchain thay vì **Anonymous (Ẩn danh)**:
   - **Pseudonymous (Bí danh):** Mọi giao dịch, giá trị chuyển giao, mốc thời gian và luồng dịch chuyển từ Bybit -> Hop 0 -> Hop 1 -> Hop 2 đều được công khai, minh bạch và lưu trữ vĩnh viễn trên sổ cái chuỗi khối dưới danh nghĩa các địa chỉ ví mã hóa (`0x36ed...`, `0x4766...`). Bất kỳ ai cũng có thể truy vết toàn bộ hành trình của dòng tiền. Danh tính chỉ tạm thời mang tính bí danh cho đến khi địa chỉ ví bị liên kết với thông tin định danh (KYC) tại các sàn CEX hoặc thông qua điều tra off-chain.
   - **Anonymous (Ẩn danh):** Là khi thông tin về người gửi, người nhận và số lượng tiền giao dịch bị ẩn giấu hoàn toàn, không thể xem hoặc liên kết trên sổ cái công khai (ví dụ: công nghệ Zero-Knowledge của Monero, hoặc sau khi dòng tiền đã bị xáo trộn qua Tornado Cash).

# Trạm 4 — Kết luận
1. **Sơ đồ luồng tiền tổng quát:**
   - **Gốc (14:16 UTC, 21/02/2025):** Ví lạnh Bybit (`0x1Db92e2EeBC8E0c075a02BeA49a2935BcD2dFCF4`) bị kích hoạt hàm `sweepETH`, rút **401.346,77 ETH** qua Internal Transaction sang ví hacker Hop 0 (`0x47666Fab8bd0Ac7003bce3f5C3585383F09486E2`).
   - **Hop 0 -> Hop 1 (14:29 & 14:56 - 15:54 UTC):**
     + 14:29 UTC: Gửi thử nghiệm **1 ETH** sang ví `0xa4b2fd68593b6f34e51cb9edb66e71c1b4ab449e`.
     + 14:56 - 15:54 UTC: Dùng script tự động phân tán **400.000 ETH** thành **40 giao dịch x 10.000 ETH** đến 40 ví nhận mới khác nhau.
   - **Hop 1 -> Hop 2 (Ví 0x36ed...):**
     + Nhận 10.000 ETH lúc 14:56:11 UTC (21/02/2025).
     + Tiền nằm yên khoảng **15 giờ 32 phút 12 giây** (55.932 giây).
     + Lúc 06:28:23 UTC ngày 22/02/2025: Thực hiện lệnh rút đầu tiên **5.000 ETH** chuyển tiếp sang ví Hop 2 (`0x4571bd67d14280e40bf3910bd39fbf60834f900a`).

2. **Chiến thuật rửa tiền và phân tán tài sản:**
   - Kẻ tấn công áp dụng kỹ thuật **Peeling Chain** và **Smurfing** (chia nhỏ tài sản thành từng phần 10.000 ETH, sau đó tiếp tục chia đôi thành 5.000 ETH ở Hop tiếp theo) kết hợp bot tự động hóa với tần suất cực cao (nhiều giao dịch cùng giây hoặc cách nhau đúng chu kỳ 12 giây tạo khối).
   - Mục đích nhằm phân tán rủi ro bị đóng băng tài sản tập trung và làm quá tải khả năng phân tích chuỗi của các đơn vị an ninh mạng.

3. **Bài học về an ninh Web3 & tính chất Blockchain:**
   - **Pseudonymous vs Anonymous:** Blockchain hoạt động theo cơ chế bí danh (Pseudonymous). Toàn bộ hành trình di chuyển của hơn 400.000 ETH đều phơi bày minh bạch và không thể chối cãi trên sổ cái chuỗi khối.
   - **Cảnh báo về Input Data:** Bất kỳ ai cũng có thể đính kèm văn bản tùy ý vào trường Input Data của giao dịch Ethereum chỉ với chi phí Gas nhỏ. Tin nhắn mạo danh FBI gửi đến ví hacker minh họa rõ ràng việc dữ liệu tin nhắn trên chuỗi không có cơ chế xác minh danh tính thực tế và dễ dàng bị giả mạo.

---

# AI_JOURNAL
- **Công cụ AI đã dùng:** Antigravity AI Assistant (Gemini 3.8 Flash), kết hợp các script Python tự động (`trace_tx.py`, `hop2_analysis.py`, `trace_origin.py`) tương tác trực tiếp với drpc RPC Node và Blockscout API.
- **Prompt hiệu quả nhất:** *"Dùng Blockscout API công khai ... Viết và chạy script Python: liệt kê các giao dịch đi ra ... Không suy đoán gì ngoài dữ liệu API trả về."* — Ràng buộc này buộc AI phải viết code thực thi và phân tích trên tập dữ liệu JSON thực tế thay vì trả lời dựa trên suy đoán hoặc ảo giác dữ liệu (hallucination).
- **Một chỗ AI nói sai / thừa / không kiểm chứng được:** Khi phân tích chuỗi hex `0xf0f7c2a84e29300089fc1049982675c68efcfc8a18557193f113f9881d014f55`, nếu nhìn lướt qua AI có thể hiểu nhầm đây là nội dung hex của tin nhắn (dẫn đến lỗi decode UTF-8 do độ dài đúng 32 bytes của Transaction Hash); thực tế cần truy vấn chi tiết giao dịch để lấy chuỗi hex nằm trong trường `raw_input` (`0x54686973206973...`) thì mới giải mã ra được thông điệp hoàn chỉnh.

