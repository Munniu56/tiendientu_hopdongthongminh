# SPEC – [Tên bài Lab]

## 1. Mục đích
[Mô tả ngắn gọn trong 1 câu: Hệ thống này giải quyết vấn đề gì cho ai].

## 2. Đầu vào
- `[Tên tham số 1]`: [Kiểu dữ liệu], do [Người dùng / Admin / Hệ thống] cung cấp.
- `[Tên tham số 2]`: [Kiểu dữ liệu], do [Người dùng / Admin / Hệ thống] cung cấp.

## 3. Quy tắc nghiệp vụ
- R1 (Chính): [Ví dụ: Chỉ chủ sở hữu (Owner) mới có quyền thực thi hàm này].
- R2 (Chính): [Ví dụ: Dữ liệu đầu vào không được để rỗng hoặc bằng 0].
- R3 (Bổ sung nâng cao 1): [Ví dụ: Không cho phép thực hiện lại thao tác nếu trạng thái đã hoàn thành].
- R4 (Bổ sung nâng cao 2): [Ví dụ: Bắt buộc phải phát ra Event khi thay đổi trạng thái hệ thống].

## 4. Đầu ra
- [Kết quả trả về hoặc sự thay đổi trạng thái, hiển thị ở đâu].

## 5. Trường hợp ngoại lệ (Security & Error Handling)
- Kịch bản 1 (Unauthorized): Nếu tài khoản không có quyền gọi hàm, hệ thống dừng giao dịch và revert lỗi `Unauthorized()`.
- Kịch bản 2 (Invalid Input): Nếu truyền tham số vi phạm điều kiện R2, hệ thống revert lỗi `InvalidInput()`.
- Kịch bản 3 (State Lock): Nếu hệ thống đang trong trạng thái tạm khóa (Pausable), giao dịch phải bị hủy ngay lập tức.

## 6. Ngoài phạm vi
- [Ghi rõ những gì bài lab này KHÔNG làm để giới hạn phạm vi công việc].