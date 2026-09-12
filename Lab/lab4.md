# BÁO CÁO LAB 4 — NHẬN DIỆN HỢP ĐỒNG CÓ RỦI RO

## Bảng kết luận thẩm định 3 hợp đồng mẫu

| Hợp đồng | Kết luận | Tên hàm | Số dòng | Rủi ro cho người nắm giữ |
| :---: | :--- | :--- | :---: | :--- |
| **A** | **An toàn** | Không có | N/A | Không có vấn đề. Hợp đồng tuân thủ chuẩn ERC-20, không chứa quyền đặc biệt gây bất lợi cho người dùng. |
| **B** | **Rủi ro cao** | `mint(address to, uint256 amount)` | Dòng 13 - 15 | Chủ sở hữu (Owner) có quyền đúc thêm token vô hạn không giới hạn số lượng, dẫn đến nguy cơ lạm phát cực cao (Dilution Risk) và xả tháo hàng (Rug Pull) làm mất sạch giá trị token. |
| **C** | **Rủi ro cực cao** | `setBlacklist(address _user, bool _status)` | Dòng 15 - 17 | Chủ sở hữu có thể đưa ví người dùng vào danh sách đen bất kỳ lúc nào, khóa vĩnh viễn tài sản (Asset Freezing) và tạo bẫy thanh khoản chỉ cho mua không cho bán (Selective Honeypot). |