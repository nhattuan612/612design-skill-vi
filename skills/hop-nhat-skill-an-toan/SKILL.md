---
name: hop-nhat-skill-an-toan
description: Đề xuất và thực hiện hợp nhất hai skill theo quy trình backup, tạo bản xem trước và kiểm tra lại; chỉ archive hoặc xoá bản cũ sau xác nhận rõ ràng của người dùng.
---

# Hợp nhất skill an toàn

Kích hoạt khi người dùng muốn gộp hai skill cụ thể hoặc đã chấp nhận một cặp từ `🧬 Quét skill trùng lặp từ 80%`. Không gộp chỉ vì tên giống nhau.

## Điều kiện trước khi thực hiện

- Xác định đúng hai skill nguồn, tỷ lệ/phần trùng, phần riêng và mục tiêu skill mới.
- Hiển thị rủi ro: mất điều kiện kích hoạt riêng, xung đột hướng dẫn, skill quá rộng hoặc link/resource hỏng.
- Hỏi xác nhận rõ tên skill mới, icon, mô tả và việc giữ hay archive bản cũ. Nếu chưa có xác nhận, chỉ dừng ở đề xuất.

## Quy trình an toàn sau xác nhận

1. Backup phục hồi được cho cả hai skill: `SKILL.md`, metadata UI và resources; ghi đường dẫn, thời gian và nguồn vào sổ nguồn.
2. Tạo skill hợp nhất ở **thư mục mới**, không ghi đè hai skill gốc. Giữ hướng dẫn chung một lần, nêu điều kiện kích hoạt riêng và không tự trộn rule mâu thuẫn.
3. Ghi nguồn gốc: hai skill cha, tỷ lệ trùng, phần giữ/bỏ, backup và lý do gộp.
4. Chạy `🩺 Kiểm tra sức khoẻ skill` cho bản mới. Nếu fail, giữ hai bản gốc và phục hồi hoặc bỏ bản mới.
5. Chỉ sau khi người dùng xác nhận bản mới hoạt động mới archive hai bản gốc trong registry. Không xoá chúng nếu không có lệnh xoá riêng.
