---
name: kiem-tra-suc-khoe-skill
description: Kiểm tra sức khoẻ cấu trúc và khả năng dùng của kho skill Codex, phát hiện skill hỏng hoặc cảnh báo; chỉ báo cáo bằng tiếng Việt, không tự sửa.
---

# Kiểm tra sức khoẻ skill

Kích hoạt khi người dùng hỏi skill nào hỏng, kho skill có ổn không, hoặc muốn audit sức khoẻ. Đây là skill **chỉ kiểm tra**; không cập nhật, reset, gộp, cài lại hoặc xoá.

## Cách chạy

1. Xác định kho skill từ `CODEX_HOME`, mặc định `~/.codex/skills`.
2. Chạy `python3 scripts/skill_audit.py --health-only`.
3. Đọc thêm `SKILL.md` khi kết quả cấu trúc chưa đủ để kết luận: phạm vi kích hoạt, hướng dẫn mâu thuẫn, dependency/tool không tồn tại hoặc prompt mặc định không phù hợp.

## Kết quả

- `🟢 Khỏe`: đủ frontmatter, name, mô tả, nội dung và reference cơ bản.
- `🟡 Cảnh báo`: vẫn dùng được nhưng có TODO, metadata hoặc reference cần xem.
- `🔴 Hỏng`: thiếu phần bắt buộc có thể cản Codex tải hoặc dùng skill.

Trả kết luận ngắn, danh sách lỗi/cảnh báo, ảnh hưởng và bước kế tiếp. Nếu cần sửa, cập nhật hoặc rollback, bàn giao sang `🔄 Kiểm tra skill`; không tự chạm file trong lượt audit.
