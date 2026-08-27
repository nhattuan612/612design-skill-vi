---
name: cai-dat-skill-tu-dong
description: Cài skill Codex từ link repo, hỏi phạm vi và key, Việt hoá tên và mô tả, kiểm tra kết quả, rồi lưu nguồn để cập nhật hoặc reset về sau.
---

# Cài skill từ repo

Kích hoạt khi người dùng gửi link repo và yêu cầu cài, thêm, import hoặc cập nhật skill. Không kích hoạt chỉ vì người dùng gửi một link GitHub mà chưa có ý định cài.

## Quy trình

1. Đọc cấu trúc repo, README, marketplace/plugin manifest nếu có; xác định các thư mục chứa `SKILL.md` và đọc frontmatter của từng skill. Không chạy script lạ trong repo chỉ để khảo sát.
2. Nếu người dùng chưa nói rõ phạm vi, hỏi ngắn gọn muốn cài skill nào hay toàn bộ. Nếu đã nói `all`, `toàn bộ` hoặc nêu danh sách, không hỏi lại.
3. Hỏi key hoặc prefix muốn ghi nhớ cho bộ skill. Đề xuất mặc định là tên repo dạng slug, ví dụ `taste-skill-`. Nếu người dùng đã chọn key, dùng đúng key đó.
4. Cài đúng các thư mục đã chọn vào thư mục skill Codex. Ưu tiên helper có sẵn tại `/Users/trannhattuan/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py`; không ghi đè skill đang có nếu chưa được người dùng yêu cầu update hoặc reset.
5. Sau khi cài, đổi trường `name` trong YAML frontmatter thành tên có key/prefix. Dùng chữ thường, số và dấu gạch ngang, tối đa 63 ký tự. Không dùng dấu tiếng Việt hoặc khoảng trắng để tránh lỗi nhận diện.
6. Dịch trường `description` sang tiếng Việt, giữ nguyên khả năng, phạm vi, điều kiện kích hoạt và các giới hạn của skill. Không tự dịch hoặc sửa phần nội dung hướng dẫn bên dưới nếu người dùng chỉ yêu cầu Việt hoá tên và mô tả.
7. Kiểm tra không trùng tên, đủ số lượng skill, frontmatter hợp lệ và mỗi skill có `SKILL.md`. Nếu có xung đột tên hoặc repo không có skill hợp lệ, dừng phần đó và báo rõ thay vì tự xoá hoặc ghi đè.
8. Ghi vào sổ nguồn `${CODEX_HOME:-$HOME/.codex}/skill-sources.md`: link repo, nhánh hoặc ref, ngày cài, danh sách path, key/prefix, số lượng, vị trí cài và các tuỳ biến Việt hoá. Tạo sổ nếu chưa có; cập nhật mục repo nếu đã tồn tại.
9. Báo cáo ngắn: đã cài bao nhiêu, key nào, vị trí nào, kiểm tra nào đạt và skill sẽ khả dụng từ lượt chat tiếp theo.

## Cập nhật và reset

- Khi người dùng yêu cầu cập nhật, đọc sổ nguồn để lấy đúng repo, ref, path và key; kiểm tra thay đổi trước khi thay thế.
- Khi người dùng yêu cầu reset, xác nhận phạm vi reset nếu chưa rõ; chỉ xoá hoặc thay thế đúng thư mục skill thuộc repo đó, không đụng skill khác.
- Sao lưu hoặc ghi nhận các tuỳ biến local trước khi update/reset, đặc biệt là tên và mô tả Việt hoá; sau đó áp dụng lại key, tên và mô tả.
- Không coi việc tải bản mới là hoàn tất. Luôn kiểm tra lại số lượng, tên, mô tả và YAML rồi mới báo thành công.

## Nguyên tắc tương tác

- Luôn hỏi lựa chọn cài cụ thể hay toàn bộ khi người dùng chưa nêu.
- Luôn hỏi key/prefix khi chưa có; đề xuất tên repo làm mặc định nhưng không tự chọn im lặng.
- Nếu yêu cầu đã đủ rõ, làm ngay và không hỏi lại câu đã được trả lời.
- Không cài dependency mới chỉ để dịch hoặc kiểm tra đơn giản; ưu tiên công cụ sẵn có.
