# NHẬT KÝ LÀM VIỆC VỚI AI - [Tên bài tập của bạn]

## Lần 1
**Prompt:** [Dán nguyên văn câu hỏi bạn vừa gửi cho AI]
**AI trả về:** [Tóm tắt ngắn gọn câu trả lời hoặc code AI tạo ra]
**Đánh giá:** [Đạt / Lưu ý / Không đạt]
**Chỗ sai:** [Mô tả chi tiết chỗ sai nếu có]
**Cách sửa:** [Bạn đã sửa như thế nào]
**Ai phát hiện:** [Sinh viên phát hiện / AI tự nhận]

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