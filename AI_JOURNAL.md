# NHẬT KÝ LÀM VIỆC VỚI AI – [Tên bài Lab]

## Lần 1
**Prompt:** [Dán nguyên văn câu lệnh bạn đã gửi cho AI]
**AI trả về:** [Tóm tắt ngắn gọn đoạn mã hoặc câu trả lời AI sinh ra]
**Đánh giá:** ⚠️ Phải sửa
**Chỗ sai:** 
1. AI thiếu kiểm tra phân quyền (chưa có modifier/require)[cite: 12].
2. AI sử dụng kiểu dữ liệu chưa tối ưu tốn gas (ví dụ: dùng `string` thay vì `bytes32` hoặc dùng `transfer` thay vì `call`)[cite: 10, 12].
3. AI không phát ra Event khi cập nhật trạng thái (Vi phạm quy ước `AGENTS.md`)[cite: 12].
**Cách sửa:** 
- [Chỉ rõ bạn đã sửa dòng mã nào, thêm logic kiểm tra điều kiện gì hoặc yêu cầu AI sửa lại ra sao].
**Ai phát hiện:** Sinh viên phát hiện

---

## Nhật ký Lab 4 — So sánh Đọc thủ công vs AI

**1. Đọc thủ công tìm ra gì:**
- Đọc thủ công phát hiện Hợp đồng B có hàm `mint` ở dòng 13 và 14 kèm điều kiện `onlyOwner`.
- Đọc thủ công phát hiện Hợp đồng C có cấu trúc `isBlacklisted` tại hàm `setBlacklist` (dòng 15 và 16) và logic chặn giao dịch trong `_update` (dòng 19 - 22).

**2. AI tìm thêm được gì:**
- AI liệt kê chính xác 100% vị trí số dòng mã nguồn của các hàm độc hại trên cả 2 hợp đồng.
- AI phân tích chuyên sâu các thuật ngữ rủi ro tài sản số:
  + Hợp đồng B: Rủi ro lạm phát (*Dilution Risk*) và Nguy cơ xả tháo tài sản (*Rug Pull*).
  + Hợp đồng C: Rủi ro đóng băng tài sản (*Asset Freezing*) và Bẫy thanh khoản có chọn lọc (*Selective Honeypot / Censorship Risk*).

**3. AI có nói sai chỗ nào không:**
- AI trả lời hoàn toàn chuẩn xác, không bịa đặt (hallucination) nhờ câu lệnh prompt thiết lập vai trò thẩm định viên và ràng buộc *"Chỉ trả lời dựa trên mã nguồn tôi cung cấp"*.