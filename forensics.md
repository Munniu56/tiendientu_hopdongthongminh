# BÁO CÁO LAB 3 — ĐỌC GIAO DỊCH VÀ HỢP ĐỒNG TRÊN ETHERSCAN

## 1. Phân tích giao dịch thực tế của sinh viên (Sepolia Testnet)

- **Transaction Hash:** `0xf1b9c7586f805b0cb6573d7e21518b6305a1103d457ccfb166e2f3170c1131d`

| Trường | Giá trị thực tế trên Etherscan | Ý nghĩa & Lý do nghiệp vụ cần |
| :--- | :--- | :--- |
| **Status** | `Success` | Giao dịch đã thực thi thành công. *Nếu thất bại vẫn mất phí Gas, ảnh hưởng hạch toán.* |
| **Block** | `11673318` | Số thứ tự khối chứa giao dịch, xác định thời điểm ghi nhận vào sổ cái Blockchain. |
| **Timestamp** | `Sep-10-2026 06:54:24 AM +UTC` | Thời gian đào khối — mốc thời gian pháp lý để ghi nhận doanh thu / chi phí. |
| **From** | `0x82d022a704706B2f144863D619D7418F8a0f19A7` | Địa chỉ ví gửi (Ví của bạn). |
| **To** | `0x36Fd4887e9d1ecA4Ae5062A745cc2c6182B77060` | Địa chỉ ví nhận. |
| **Value** | `2 ETH` (Sepolia ETH) | Giá trị nguyên giá của tài sản được chuyển đi trong giao dịch. |
| **Transaction Fee** | `0.000052218178047 ETH` | Chi phí giao dịch phát sinh, cần hạch toán riêng vào chi phí vận hành. |
| **Gas Price** | `2.486579907 Gwei` | Đơn giá phí cho mỗi đơn vị Gas tại thời điểm thực hiện giao dịch. |

---

## 2. Phân tích hợp đồng thông minh USDT (Tether USD)

- **Địa chỉ hợp đồng phân tích:** `0xdAC17F958D2ee523a2206206994597C13D831ec7` (Tether USD trên Ethereum Mainnet)

### **Trả lời các câu hỏi thu hoạch:**

1. **Hợp đồng bạn xem có công bố mã nguồn đã xác thực không?**
   - **Có.** Hợp đồng USDT trên Etherscan đã được xác thực mã nguồn (**Source Code Verified** với dấu tích xanh). Việc này giúp công khai toàn bộ logic hoạt động, tạo niềm tin cho người dùng so với mã máy bytecode thô.

2. **Tổng cung của đồng đó là bao nhiêu? Đọc ra từ hàm nào?**
   - **Đọc từ hàm:** `totalSupply()` trong tab **Read Contract**.
   - **Giải thích:** Hàm này trả về tổng số lượng token USDT đang lưu hành trên toàn mạng lưới.

3. **Trong tab Write Contract, có hàm nào cho phép một địa chỉ đặc biệt đóng băng tài khoản người khác không? Nếu có, tên hàm là gì?**
   - **Có.** 
   - **Tên hàm:** `addBlackList(address _evilUser)` (được gọi bởi địa chỉ Owner/Quản trị).
   - **Ý nghĩa nghiệp vụ:** Hàm này cho phép nhà phát hành (Tether) cho một địa chỉ ví vào danh sách đen, chặn mọi thao tác chuyển tiền của ví đó. Điều này chứng minh các đồng Stablecoin phổ biến hiện nay vẫn mang tính **tập trung nhất định (centralized)** để phục vụ công tác tuân thủ pháp lý khi có yêu cầu từ cơ quan chức năng.