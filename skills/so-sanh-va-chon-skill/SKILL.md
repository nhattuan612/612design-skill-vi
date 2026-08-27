---
name: so-sanh-va-chon-skill
description: So sánh nhiều repo skill hoặc phân tích task để đề xuất repo và skill phù hợp, giải thích lựa chọn bằng tiếng Việt và hỏi xác nhận trước khi cài hoặc kích hoạt.
---

# So sánh và chọn skill

Kích hoạt khi người dùng gửi từ hai link repo trở lên để so sánh, hỏi repo nào nên dùng, hoặc có task nhưng chưa biết skill nào phù hợp. Đây là skill phân tích và điều phối lựa chọn; không tự cài, xoá, reset hoặc kích hoạt skill khi chưa được xác nhận.

## Chế độ A — So sánh hai hoặc nhiều repo

1. Xác nhận mục tiêu và tiêu chí ưu tiên nếu người dùng chưa nêu. Ưu tiên mặc định là độ phù hợp nhu cầu, chất lượng hướng dẫn, tính đầy đủ, khả năng tương thích Codex, maintenance và rủi ro.
2. Khảo sát từng repo ở cùng một mức sâu: README, branch/ref, manifest/plugin, thư mục `skills/`, các `SKILL.md`, references, scripts, assets, dependency và license. Không chạy script lạ chỉ để khảo sát.
3. Lập bảng đối chiếu theo repo và skill: số lượng, phạm vi, skill trùng, skill riêng, version/commit, tài liệu dùng chung, dependency, yêu cầu công cụ, giới hạn và dấu hiệu repo còn được duy trì.
4. Phân loại kết quả thành `nên dùng`, `có thể dùng`, `không phù hợp` và nêu bằng chứng ngắn cho từng kết luận. Không chấm điểm giả với dữ liệu không kiểm chứng.
5. Đề xuất một repo chính, repo phụ hoặc phương án kết hợp từng skill từ nhiều repo. Nêu rõ conflict tên, nội dung trùng, reference bị thiếu, license khác nhau và chi phí bảo trì.
6. Liệt kê chính xác skill nên cài từ repo được chọn, key/prefix đề xuất và thứ tự cài.
7. Đề xuất icon theo nhóm chức năng cho từng skill và hỏi người dùng muốn không dùng icon, dùng một icon chung hay tự chọn icon theo nhóm. Không sửa repo ở chế độ đề xuất.
8. Dừng ở đề xuất và hỏi xác nhận. Sau khi người dùng chọn repo, skill và icon, chuyển sang `cai-dat-skill-tu-dong` để thực hiện cài.

## Chế độ B — Chọn skill theo task

1. Tóm tắt task thành mục tiêu, loại công việc, rủi ro, artifact cần tạo/sửa và tiêu chí hoàn tất. Nếu thiếu thông tin làm thay đổi lựa chọn, hỏi một câu ngắn bằng tiếng Việt.
2. Quét tên và mô tả của các skill trong thư mục skill Codex đang cấu hình, rồi đối chiếu với registry nếu cần. Không phụ thuộc vào path cá nhân của một máy cụ thể.
3. Xếp hạng tối đa 3 skill theo `phù hợp trực tiếp`, `bổ trợ`, `không cần thiết`. Không đề xuất skill chỉ vì tên có từ khoá giống task.
4. Với mỗi skill đề xuất, giải thích một câu về lý do kích hoạt, phạm vi áp dụng và điểm cần tránh. Nếu cần phối hợp, ghi rõ skill chính và skill bổ trợ.
5. Kiểm tra conflict giữa các skill, thứ tự áp dụng và skill nào có quyền quyết định cao hơn khi hướng dẫn mâu thuẫn.
6. Đề xuất prompt gọi skill bằng tên tiếng Việt, ví dụ `@agent-skills-ui-bao-mat-va-cung-co` hoặc tên skill local tương ứng. Giữ mã gọi không dấu, giao tiếp và lựa chọn hiển thị bằng tiếng Việt.
7. Đề xuất icon hiển thị phù hợp với nhóm chức năng nếu skill chưa có icon; tôn trọng chính sách icon `ask|auto|off|custom` đã lưu và không thay đổi icon đang được người dùng lưu nếu chưa được hỏi.
8. Hỏi người dùng xác nhận danh sách skill trước khi thực hiện task. Nếu người dùng đã chỉ rõ skill, chỉ kiểm tra tương thích và không ép chọn lại.

## Chế độ C — 🧬 Quét skill trùng lặp từ 80%

1. Khi người dùng hỏi skill nào trùng, chạy `../kiem-tra-cap-nhat-skill/scripts/skill_audit.py` trên thư mục skill Codex với ngưỡng `80`. Dùng phép đo theo nội dung hướng dẫn sau khi loại YAML frontmatter; không chỉ dựa vào tên hoặc mô tả.
2. Báo ba mức bằng tiếng Việt: `🧬 Trùng lặp cao từ 80%`, `🔎 Có thể trùng từ 60–79%`, `🟢 Khác biệt rõ dưới 60%`. Với mức cao, chỉ ra phần chung và phần riêng trước khi kết luận.
3. Loại trừ trường hợp chỉ cùng boilerplate, license, link hoặc câu hướng dẫn chung. Hai skill chỉ là ứng viên gộp khi phần workflow và điều kiện kích hoạt cũng trùng đáng kể.
4. Đề xuất một trong ba hướng: giữ cả hai vì phần riêng quan trọng, đổi tên/phạm vi để rõ vai trò hoặc chuyển sang 🧩 Hợp nhất skill an toàn. Không tự merge hay archive.
5. Mọi bảng, tỷ lệ, cảnh báo và lựa chọn dùng tiếng Việt; mã kỹ thuật chỉ xuất hiện khi người dùng cần gọi hoặc xác định đúng skill.

## Nguyên tắc quyết định

- Không chọn repo chỉ vì có nhiều skill hơn; độ phù hợp và chất lượng quan trọng hơn số lượng.
- Không cài trùng skill đã có nếu chưa so sánh nội dung và version.
- Không gộp hai skill có cùng vai trò nếu một skill đã đủ dùng; chỉ đề xuất gộp sau 🧬 Quét skill trùng lặp từ 80% và khi phần riêng không mâu thuẫn.
- Không xem mô tả upstream là bằng chứng chất lượng; đọc nội dung thực và references liên quan.
- Repo private, license không rõ, dependency mới hoặc script tự động đáng ngờ phải được đánh dấu rủi ro.
- Khi không đủ dữ liệu, nói rõ chưa kết luận được và đề xuất kiểm tra tiếp theo.

## Giao tiếp và giao diện

- Toàn bộ câu hỏi, lựa chọn, bảng so sánh và báo cáo dùng tiếng Việt.
- Tên hiển thị có thể dùng icon để dễ nhận biết; mã `name` và tên gọi kỹ thuật vẫn giữ slug không dấu để Codex nhận diện ổn định.
- Hiển thị tối đa ba lựa chọn chính, luôn có lý do và tác động thực tế.
- Không dùng popup giả bằng Markdown. Nếu môi trường có structured question trong Plan mode, ưu tiên cơ chế đó; nếu không, hỏi trực tiếp trong chat.

## Bàn giao

- Sau khi người dùng chọn, bàn giao repo/path/key cho `cai-dat-skill-tu-dong`.
- Sau khi đã cài, bàn giao cho `kiem-tra-cap-nhat-skill` khi cần audit, update hoặc reset.
- Không tự push GitHub, tạo automation hoặc thay đổi registry ngoài phạm vi người dùng đã xác nhận.
