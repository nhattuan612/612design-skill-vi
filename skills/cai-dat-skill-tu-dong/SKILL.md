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
4. Đọc tuỳ chọn icon đã lưu trong sổ nguồn trước. Nếu repo hoặc người dùng đã có chế độ `luôn tự chọn`, `luôn không dùng` hoặc icon cụ thể, áp dụng đúng lựa chọn đó và không hỏi lại. Nếu chưa có, hỏi người dùng có muốn thêm icon vào tên hiển thị không; nếu có, hỏi chọn icon cụ thể hay để hệ thống tự chọn theo nhóm chức năng.
5. Nếu chọn tự động, phân loại từng skill theo chức năng và chọn icon nhất quán. Gợi ý mặc định: UI/design `🎨`, cài đặt `📦`, quản lý `⚙️`, cập nhật `🔄`, bảo mật `🛡️`, test `🧪`, tài liệu `📚`, hiệu năng `⚡`, debug `🐞`, API `🔌`, Git `🌿`, kế hoạch `🧭`, automation `🤖`, dữ liệu `🗄️`, tổng quát `🧩`. Nếu một skill thuộc nhiều nhóm, chọn nhóm chính theo mô tả.
6. Cài đúng các thư mục đã chọn vào thư mục skill Codex. Xác định thư mục Codex từ `CODEX_HOME`, mặc định là `~/.codex`; ưu tiên helper `skills/.system/skill-installer/scripts/install-skill-from-github.py` trong thư mục Codex đó. Không ghi đè skill đang có nếu chưa được người dùng yêu cầu update hoặc reset.
7. Trước khi ghi tuỳ biến, hiển thị preview ngắn cho từng skill gồm tên mã, tên Việt hoá, icon dự kiến và mô tả một dòng. Nếu người dùng đã chọn chế độ tự động, chỉ hỏi lại khi icon suy ra không rõ hoặc có xung đột.
8. Sau khi cài, đổi trường `name` trong YAML frontmatter thành tên có key/prefix. Dùng chữ thường, số và dấu gạch ngang, tối đa 63 ký tự. Không dùng icon, dấu tiếng Việt hoặc khoảng trắng trong `name` để tránh lỗi nhận diện.
9. Nếu dùng icon, sửa `agents/openai.yaml` ở `interface.display_name` thành `ICON + tên tiếng Việt`; không nhét icon vào frontmatter `name`. Nếu skill chưa có `agents/openai.yaml`, tạo file này với `display_name`, `short_description` tiếng Việt và `default_prompt` tiếng Việt. Nếu không dùng icon, giữ display name không icon. Không tạo icon riêng cho từng skill nếu người dùng yêu cầu một icon chung cho cả repo.
10. Dịch trường `description` sang tiếng Việt, giữ nguyên khả năng, phạm vi, điều kiện kích hoạt và các giới hạn của skill. Không tự dịch hoặc sửa phần nội dung hướng dẫn bên dưới nếu người dùng chỉ yêu cầu Việt hoá tên và mô tả.
11. Kiểm tra không trùng tên, đủ số lượng skill, frontmatter hợp lệ, metadata icon nhất quán và mỗi skill có `SKILL.md`. Nếu có xung đột tên hoặc repo không có skill hợp lệ, dừng phần đó và báo rõ thay vì tự xoá hoặc ghi đè.
12. Ghi vào sổ nguồn `${CODEX_HOME:-$HOME/.codex}/skill-sources.md`: link repo, nhánh hoặc ref, ngày cài, danh sách path, key/prefix, số lượng, vị trí cài, chính sách icon `ask|auto|off|custom`, mapping icon theo skill và các tuỳ biến Việt hoá. Tạo sổ nếu chưa có; cập nhật mục repo nếu đã tồn tại.
13. Báo cáo ngắn: đã cài bao nhiêu, key nào, icon nào, vị trí nào, kiểm tra nào đạt và skill sẽ khả dụng từ lượt chat tiếp theo.

## Cập nhật và reset

- Khi người dùng yêu cầu cập nhật, đọc sổ nguồn để lấy đúng repo, ref, path và key; kiểm tra thay đổi trước khi thay thế.
- Khi người dùng yêu cầu reset, xác nhận phạm vi reset nếu chưa rõ; chỉ xoá hoặc thay thế đúng thư mục skill thuộc repo đó, không đụng skill khác.
- Sao lưu hoặc ghi nhận các tuỳ biến local trước khi update/reset, đặc biệt là tên và mô tả Việt hoá; sau đó áp dụng lại key, tên và mô tả.
- Giữ icon và mapping icon đã lưu trong `agents/openai.yaml` khi update/reset. Chỉ đổi icon khi người dùng yêu cầu hoặc chọn lại chế độ tự động.
- Không coi việc tải bản mới là hoàn tất. Luôn kiểm tra lại số lượng, tên, mô tả và YAML rồi mới báo thành công.

## Nguyên tắc tương tác

- Luôn hỏi lựa chọn cài cụ thể hay toàn bộ khi người dùng chưa nêu.
- Luôn hỏi key/prefix khi chưa có; đề xuất tên repo làm mặc định nhưng không tự chọn im lặng.
- Khi chưa có chính sách icon, hỏi có dùng icon không; nếu có thì hỏi icon cụ thể hay tự chọn theo nhóm chức năng. Nếu người dùng chọn, lưu thành `ask`, `auto`, `off` hoặc `custom` để lần sau không hỏi lặp.
- Nếu yêu cầu đã đủ rõ, làm ngay và không hỏi lại câu đã được trả lời.
- Không cài dependency mới chỉ để dịch hoặc kiểm tra đơn giản; ưu tiên công cụ sẵn có.
