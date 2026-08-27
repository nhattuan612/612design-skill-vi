# Skill for Skill VN

Bộ 3 skill tiếng Việt giúp Codex quản lý chính các skill của nó: chọn đúng skill, cài đúng repo, rồi kiểm tra và cập nhật an toàn về sau.

Không cần nhớ lệnh dài. Mô tả việc bạn muốn làm bằng tiếng Việt; skill sẽ hỏi phần còn thiếu, giải thích lựa chọn và chỉ thay đổi khi bạn xác nhận.

## Ba skill trong bộ này

| Icon | Skill | Dùng khi |
| --- | --- | --- |
| 📦 | `cai-dat-skill-tu-dong` | Bạn có link repo và muốn cài skill vào Codex. |
| 🔄 | `kiem-tra-cap-nhat-skill` | Bạn muốn kiểm tra, cập nhật, reset hoặc rollback skill đã cài. |
| 🧭 | `so-sanh-va-chon-skill` | Bạn có nhiều repo hoặc một task nhưng chưa biết nên dùng skill nào. |

## Hình dung bằng tình huống thật

### 1. Thấy một repo nhiều skill nhưng chưa biết cài cái nào

Bạn gửi link repo và nói: “Cài skill trong repo này.”

Gọi `@cai-dat-skill-tu-dong`.

Skill sẽ đọc README và toàn bộ `SKILL.md`, sau đó hỏi bạn muốn cài một skill hay toàn bộ. Nó hỏi key/prefix để dễ nhận ra nguồn, hỏi có dùng icon không, cho xem preview tên tiếng Việt trước khi sửa rồi mới cài. Link repo, branch, danh sách skill, key và icon được lưu để lần sau cập nhật không phải tìm lại từ đầu.

Ví dụ:

```text
@cai-dat-skill-tu-dong
https://github.com/example/team-skills
Cài toàn bộ. Key là team-skills-. Tự chọn icon theo chức năng.
```

Kết quả có thể dễ nhìn như `🎨 Team skills giao diện`, `🛡️ Team skills bảo mật`, `🧪 Team skills kiểm thử`. Icon chỉ nằm ở tên hiển thị; mã skill luôn giữ slug không dấu để Codex gọi ổn định.

### 2. Có hai repo, không muốn cài thử từng repo để so sánh

Bạn đang cân nhắc một repo mạnh về UI và một repo mạnh về quy trình kỹ thuật. Thay vì cài cả hai rồi tự đọc hàng chục file, gửi cả hai link và nhu cầu của bạn.

Gọi `@so-sanh-va-chon-skill`.

Skill sẽ so sánh số lượng và chất lượng skill, phần trùng, phần riêng, dependencies, references, license, tín hiệu bảo trì và khả năng chạy trong Codex. Báo cáo luôn bằng tiếng Việt, có khuyến nghị rõ: chọn repo A, chọn repo B, hay lấy vài skill tốt nhất từ mỗi repo. Skill này chỉ đề xuất; sau khi bạn chốt, nó bàn giao sang skill 📦 để cài.

Ví dụ:

```text
@so-sanh-va-chon-skill
So sánh hai repo này. Tôi cần làm landing page cao cấp nhưng cũng cần test kỹ.
https://github.com/org-a/design-skills
https://github.com/org-b/engineering-skills
```

### 3. Có task nhưng không nhớ đã cài skill nào

Bạn nói: “Tôi sắp sửa API thanh toán, cần làm an toàn và có test, nên dùng skill nào?”

Gọi `@so-sanh-va-chon-skill`.

Skill quét các skill đang cài, chọn tối đa ba skill phù hợp, phân biệt skill chính với skill bổ trợ và giải thích lý do. Nó không đề xuất một danh sách dài cho có; nếu một skill là đủ, nó sẽ nói rõ.

Ví dụ kết quả:

```text
Chính: skill bảo mật — vì có input, session và dữ liệu nhạy cảm.
Bổ trợ: skill kiểm thử — để chứng minh luồng thanh toán vẫn đúng.
Không cần: skill UI — task chưa đụng giao diện.
```

### 4. Một tháng sau muốn biết repo có bản mới không

Bạn nói: “Kiểm tra các skill của team-skills có update không.”

Gọi `@kiem-tra-cap-nhat-skill`.

Skill mặc định chỉ kiểm tra, không tự ghi đè. Nó đọc registry đã lưu, so sánh repo remote với bản local, chỉ ra skill mới, sửa, bị xoá hoặc xung đột với tuỳ biến tiếng Việt/icon. Nếu bạn muốn cập nhật, nó backup đúng phạm vi trước, giữ key, tên tiếng Việt, mô tả và icon rồi kiểm tra lại YAML. Nếu có lỗi, nó giữ hoặc phục hồi bản cũ thay vì báo thành công nửa chừng.

Ví dụ:

```text
@kiem-tra-cap-nhat-skill
Kiểm tra repo team-skills. Chỉ báo cáo, chưa cập nhật.
```

## Luồng sử dụng ngắn gọn

```text
Chưa biết chọn repo/skill?
        ↓
🧭 So sánh và chọn skill
        ↓
Đã chốt repo/skill?
        ↓
📦 Cài skill từ repo
        ↓
Muốn kiểm tra, cập nhật hoặc reset?
        ↓
🔄 Kiểm tra và cập nhật skill
```

## Icon và tiếng Việt

Khi cài, bạn chọn một trong ba cách:

- Không dùng icon.
- Dùng một icon chung cho cả repo.
- Để hệ thống tự chọn theo nhóm chức năng, ví dụ UI `🎨`, quản lý `⚙️`, bảo mật `🛡️`, kiểm thử `🧪`, tài liệu `📚`, hiệu năng `⚡`, debug `🐞`.

Lựa chọn được lưu lại. Lần sau cài hoặc cập nhật cùng repo, Codex không hỏi lặp nếu bạn đã chọn chế độ mặc định.

Mọi câu hỏi, preview, bảng so sánh và báo cáo dùng tiếng Việt. Icon chỉ dùng trong `display_name`; tên kỹ thuật của skill không có dấu và không có emoji để luôn tương thích Codex.

## Cài bộ skill

Trong Codex, bạn có thể gửi link repo này và yêu cầu cài. Nếu đã có công cụ cài skill, cài toàn bộ thư mục `skills/` để giữ đủ ba skill và metadata hiển thị.

```text
https://github.com/nhattuan612/skill-for-skill-vn
Cài toàn bộ skill trong repo này.
```

Repo đang ở chế độ private. Người cài cần có quyền truy cập GitHub tương ứng.

## Nguyên tắc an toàn

- Không tự cài, cập nhật, reset hoặc xoá khi bạn mới yêu cầu kiểm tra.
- Không chạy script lạ từ repo chỉ để khảo sát.
- Luôn preview tên/icon khi cần thay đổi hiển thị.
- Luôn backup đúng skill trước update hoặc rollback.
- Không đưa registry cá nhân, token hay đường dẫn nhạy cảm vào repository.
