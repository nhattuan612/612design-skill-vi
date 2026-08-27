---
name: kiem-tra-cap-nhat-skill
description: Kiểm tra chuyên sâu nguồn, phiên bản, thay đổi và độ lệch của các skill Codex đã cài; báo cáo trước, cập nhật có xác nhận, bảo toàn tuỳ biến Việt hoá và hỗ trợ rollback an toàn.
---

# Kiểm tra và cập nhật skill

Kích hoạt khi người dùng yêu cầu kiểm tra, audit, đối chiếu, cập nhật, đồng bộ hoặc rollback skill đã cài. Skill này tập trung vào các skill có nguồn repo được ghi trong `${CODEX_HOME:-$HOME/.codex}/skill-sources.md` và các skill local có thể truy ra nguồn.

## Chế độ làm việc

- **Chỉ kiểm tra** là mặc định nếu người dùng nói kiểm tra, audit, xem có bản mới hoặc báo cáo. Không sửa file, không xoá và không cập nhật.
- **Cập nhật** chỉ chạy khi người dùng nói rõ cập nhật, đồng bộ, nâng cấp hoặc xác nhận kết quả kiểm tra. Nếu báo cáo phát hiện thay đổi nhưng chưa có xác nhận, dừng ở báo cáo.
- **🩺 Kiểm tra sức khoẻ skill** chạy chỉ đọc khi người dùng hỏi skill nào hỏng, kho skill có ổn không hoặc muốn audit sức khoẻ.
- **🧩 Hợp nhất skill an toàn** chỉ chạy khi người dùng nói rõ muốn gộp các skill cụ thể hoặc chấp nhận một đề xuất gộp.

## 🩺 Kiểm tra sức khoẻ skill

1. Chạy `scripts/skill_audit.py` với thư mục skill Codex và ngưỡng trùng lặp `80`. Script chỉ đọc, kiểm tra frontmatter, slug, mô tả, nội dung trống, TODO, metadata UI và reference Markdown tương đối.
2. Phân loại kết quả bằng tiếng Việt: `🟢 Khỏe`, `🟡 Cảnh báo`, `🔴 Hỏng`. Skill hỏng là lỗi cản trở Codex tải hoặc dùng skill; cảnh báo là thiếu metadata, reference, TODO hoặc vấn đề cần review.
3. Với lỗi semantic mà script không thể biết, đọc `SKILL.md` và kiểm tra: phạm vi kích hoạt có rõ không, hướng dẫn có mâu thuẫn không, dependency/tool có còn tồn tại không và prompt mặc định có phù hợp không.
4. Báo cặp trùng lặp từ `80%` trở lên nhưng không gọi chúng là “trùng hoàn toàn” chỉ dựa vào phần trăm. Xem phần nội dung riêng trước khi đề xuất gộp.
5. Chế độ này không tự sửa, cài lại hoặc gộp skill. Chỉ nêu phương án sửa, cập nhật hoặc chuyển sang 🧩 sau khi người dùng chọn.

## 🧩 Hợp nhất skill an toàn

Chỉ đề xuất gộp khi hai skill có độ trùng lặp từ `80%` trở lên hoặc người dùng chỉ rõ chúng trùng vai trò.

1. Hiển thị cảnh báo rủi ro: có thể mất điều kiện kích hoạt riêng, xung đột hướng dẫn, làm skill quá rộng hoặc làm hỏng link/resource. Nêu phần trùng và phần riêng của từng skill.
2. Hỏi xác nhận rõ phạm vi: hai skill nguồn, tên skill mới, icon, mô tả và việc giữ hay archive bản cũ. Không tự chọn tên hay xoá bản cũ.
3. Tạo backup phục hồi được cho **cả hai** skill, gồm `SKILL.md`, metadata UI và resources. Ghi đường dẫn backup, thời gian và nguồn vào sổ nguồn trước khi tạo bản hợp nhất.
4. Tạo skill hợp nhất trong **thư mục mới**, không ghi đè hai skill gốc. Chỉ giữ các hướng dẫn chung một lần, giữ các phần riêng dưới điều kiện kích hoạt rõ ràng và không tự kết hợp các rule mâu thuẫn.
5. Thêm ghi nhận nguồn trong sổ nguồn: hai skill cha, tỷ lệ trùng lặp, phần giữ lại, phần bỏ, backup và lý do gộp. Không cần sao chép toàn bộ nội dung cũ vào skill mới.
6. Chạy lại 🩺 Kiểm tra sức khoẻ skill, kiểm tra YAML, slug, metadata, reference, prompt mặc định và đọc review phần merge. Nếu bất kỳ kiểm tra nào fail, giữ hai skill gốc và phục hồi hoặc bỏ bản hợp nhất.
7. Sau khi người dùng xác nhận bản hợp nhất chạy đúng, chỉ **archive** hai skill gốc trong registry. Không xoá chúng trừ khi có lệnh xoá riêng.

## Quy trình kiểm tra chuyên sâu

1. Đọc sổ nguồn skill. Với mỗi repo, lấy link chính xác, branch/ref, danh sách path, key/prefix, chính sách icon, vị trí cài và các tuỳ biến đã ghi. Không suy đoán repo từ tên thư mục nếu sổ nguồn có dữ liệu khác.
2. Kiểm tra trạng thái local trước khi chạm vào file: thư mục tồn tại, `SKILL.md`, `agents/openai.yaml`, resources, ngày sửa và các thay đổi local. Ghi nhận tên/mô tả Việt hoá khác upstream là tuỳ biến có chủ đích.
3. Khảo sát nguồn từ remote bằng GitHub API, helper cài skill hoặc git sparse checkout. Đọc README, manifest và `SKILL.md`; không chạy script build/install của repo chỉ để kiểm tra.
4. Đối chiếu theo từng path, không chỉ theo tên thư mục. Phân loại `mới`, `đã xoá`, `đã sửa`, `không đổi`, `local-only` và `nguồn không truy cập được`.
5. So sánh frontmatter riêng với nội dung hướng dẫn. Báo rõ thay đổi ở `name`, `description`, policy, dependencies, references, scripts và assets. Phân biệt thay đổi upstream với thay đổi local.
6. Kiểm tra drift của bản cài: source link, branch/ref, số skill, tên skill, key/prefix, tên Việt hoá, mô tả Việt hoá, icon và `display_name`, nội dung body, resource files và metadata UI.
7. Đánh giá rủi ro cập nhật. Đánh dấu xung đột tên, path biến mất, thay đổi phạm vi kích hoạt, thay đổi policy, dependency mới, script mới, file bị xoá và thay đổi lớn trong hướng dẫn. Không tự kết luận “an toàn” chỉ vì file vẫn parse được.
8. Xuất báo cáo gọn nhưng đủ bằng chứng: repo, ref local/remote, trạng thái truy cập, số lượng, bảng thay đổi theo skill, rủi ro, tuỳ biến cần giữ, hành động đề xuất và câu hỏi cần người dùng quyết định.

## Quy trình cập nhật an toàn

Chỉ thực hiện sau khi người dùng xác nhận phạm vi cập nhật.

1. Chốt phạm vi theo repo hoặc skill cụ thể. Nếu người dùng nói “cập nhật hết”, chỉ cập nhật các repo đã có trong sổ nguồn, không tự tìm và cài repo mới.
2. Tải bản nguồn mới vào thư mục tạm riêng. Không ghi đè trực tiếp bản đang dùng và không xoá trước khi có bản thay thế đã kiểm tra.
3. Tạo bản sao lưu phục hồi được của đúng các thư mục sắp thay đổi. Ghi đường dẫn backup và timestamp vào báo cáo; không dùng lệnh xoá đệ quy trên thư mục rộng.
4. So sánh thay đổi lần cuối. Nếu có sửa local trong body, script, reference hoặc asset, không âm thầm ghi đè; báo xung đột và hỏi giữ local, nhận upstream hay chuyển sang 🧩 Hợp nhất skill an toàn.
5. Cài hoặc thay thế bản upstream tối thiểu. Giữ key/prefix, chính sách icon và mapping icon đã lưu, sau đó áp dụng lại tên Việt hoá, icon và mô tả Việt hoá. Nếu upstream chưa có `agents/openai.yaml`, tạo metadata hiển thị theo tuỳ biến đã lưu. Không đổi nội dung body chỉ để “đồng bộ tên”.
6. Cập nhật sổ nguồn với ref mới, ngày cập nhật, path, số lượng, fingerprint hoặc commit nếu có, tên/mô tả tuỳ biến và backup gần nhất.
7. Xác minh sau cập nhật: mọi path đã chọn tồn tại, mỗi skill có `SKILL.md`, frontmatter YAML hợp lệ, tên hợp lệ và không trùng, mô tả còn đúng, resources tham chiếu tồn tại, policy không bị đổi ngoài ý muốn.
8. Nếu bất kỳ kiểm tra bắt buộc nào thất bại, không báo thành công. Khôi phục từ backup hoặc giữ nguyên bản cũ, báo lỗi cụ thể và đường dẫn backup.

## Quy trình rollback

- Chỉ rollback repo hoặc skill được người dùng chỉ định.
- Đọc backup gần nhất trong sổ nguồn, xác nhận đúng path trước khi phục hồi.
- Phục hồi cả `SKILL.md`, metadata và resources liên quan; không phục hồi sang skill khác có tên gần giống.
- Kiểm tra lại YAML, tên, mô tả, số lượng và trạng thái sau rollback.
- Ghi lịch sử rollback vào sổ nguồn, không xoá backup cũ nếu chưa được yêu cầu.

## Quy tắc Việt hoá và tương thích

- Giữ key/prefix của repo trong mọi lần cập nhật, trừ khi người dùng yêu cầu đổi.
- Tên skill dùng chữ thường, số và dấu gạch ngang, tối đa 63 ký tự; tên hiển thị có dạng `ICON + tên tiếng Việt` hoặc `key-mo-ta-ngan` khi không dùng icon.
- Icon chỉ nằm trong `agents/openai.yaml` ở `interface.display_name`, không nằm trong frontmatter `name`. Kiểm tra icon theo mapping đã lưu và phát hiện display name thiếu hoặc sai icon.
- Mô tả phải bằng tiếng Việt, ngắn, phân biệt được skill và giữ nguyên khả năng, phạm vi, giới hạn, điều kiện kích hoạt.
- Không dịch tên file, path, code, frontmatter key, tên dependency hoặc lệnh kỹ thuật.
- Không sửa body upstream chỉ vì khác tiếng Việt. Nếu cần Việt hoá toàn bộ nội dung, đó là yêu cầu riêng và phải ghi nhận như một tuỳ biến local.

## Xử lý lỗi và tình huống đặc biệt

- Repo không có `SKILL.md`: báo đây không phải nguồn skill hợp lệ, không tạo skill giả.
- Repo private hoặc remote lỗi: báo lỗi truy cập, không xoá bản local và không thay bằng bản chưa xác thực.
- Ref không tồn tại: giữ bản local, báo ref lỗi và hỏi có dùng ref khác không.
- Tên mới trùng skill khác: dừng skill bị xung đột, đề xuất key khác hoặc hậu tố phiên bản.
- Sổ nguồn thiếu hoặc cũ: không đoán im lặng; truy ra bằng link/path nếu có, rồi cập nhật sổ sau khi người dùng xác nhận.
- Skill local có repo nguồn riêng nhưng registry chỉ có path local: đánh dấu `nguồn chưa liên kết`, yêu cầu hoặc đề xuất thêm URL, branch/ref và danh sách path trước khi update/reset.
- Upstream xoá skill: không tự xoá bản local; chỉ đánh dấu `đã xoá upstream` và hỏi người dùng có muốn gỡ không.
- Độ trùng lặp từ `80%` trở lên: báo `🧬 Trùng lặp cao`, kèm phần riêng và đề xuất 🧩 Hợp nhất skill an toàn; không tự merge.

## Báo cáo đầu ra

Luôn báo theo thứ tự:

1. Kết luận ngắn: 🟢 khỏe, 🟡 cảnh báo, 🔴 hỏng, có cập nhật, 🧬 trùng lặp cao hoặc cần quyết định.
2. Phạm vi: repo, ref, skill và file bị ảnh hưởng.
3. Thay đổi/rủi ro quan trọng nhất.
4. Tuỳ biến local được giữ hoặc conflict cần xử lý.
5. Kiểm tra đã chạy và kết quả.
6. Backup, sổ nguồn và hành động tiếp theo.

Không nói “đã cập nhật” nếu mới chỉ tải hoặc so sánh. Không tự tạo lịch chạy định kỳ; chỉ thiết lập automation khi người dùng yêu cầu riêng.
