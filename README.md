# Quản Lý Skill VN

> **QLSVN (Quản Lý Skill VN)** giúp bạn quản lý và hệ thống hoá kho skill tốt hơn: chọn đúng skill, cài đúng repo, Việt hoá dễ dùng, rồi kiểm tra và nâng cấp an toàn về sau.

## QLSVN đứng ở đâu trong kho skill của bạn?

```text
Nhiều repo skill trên GitHub
        │
        │  so sánh, chọn lọc, kiểm tra rủi ro
        ▼
🧭 QLSVN — Trung tâm quyết định
        │
        │  cài, Việt hoá, đặt icon, lưu nguồn
        ▼
📦 Kho skill Codex của bạn
        │
        │  audit, update, reset, rollback
        ▼
🔄 Kho skill luôn rõ nguồn và dễ bảo trì
```

QLSVN không thay thế các skill chuyên môn như UI, security hay testing. Nó đứng **trước và sau** chúng để bạn biết nên dùng skill nào, skill đó đến từ đâu, hiển thị ra sao và cập nhật thế nào.

## Ba giá trị cốt lõi

| Ý chính | QLSVN làm gì | Ý phụ quan trọng |
| --- | --- | --- |
| **🇻🇳 Việt hoá an toàn** | Đổi tên hiển thị, thêm icon và dịch mô tả sang tiếng Việt. | Mã `name`, nội dung hướng dẫn, path, dependency và logic gốc vẫn được giữ đúng chuẩn để không làm hư skill. |
| **🧱 Ổn định khi nâng cấp** | Lưu repo nguồn, branch, skill path, key và icon. | Khi update/reset, QLSVN so sánh trước, backup đúng phạm vi, áp lại tuỳ biến tiếng Việt và chỉ báo hoàn tất sau khi kiểm tra YAML. |
| **🗂️ Hệ thống hoá kho skill** | Gom thông tin repo, phân loại chức năng và đề xuất skill phù hợp với từng task. | Bạn không cần nhớ repo nào có gì hay cài trùng nhiều bản cho cùng một việc. |

### Việt hoá có làm hư skill không?

Không. QLSVN tách phần **dễ nhìn cho người dùng** khỏi phần **kỹ thuật mà Codex cần**:

```text
Tên hiển thị:  🎨 agent-skills-ui- Giao diện người dùng
Mã kỹ thuật:   agent-skills-ui-giao-dien
Nội dung gốc:  giữ nguyên workflow và điều kiện kích hoạt
```

Icon chỉ nằm trong `display_name`, còn mã kỹ thuật luôn là slug không dấu. Vì vậy skill vẫn được Codex nhận diện ổn định, trong khi người dùng nhìn kho skill dễ hơn nhiều.

### Nâng cấp theo thời gian có bị mất tuỳ biến không?

QLSVN được thiết kế để nâng cấp ổn định theo thời gian: kiểm tra thay đổi trước, backup trước khi thay thế, sau đó áp lại tên tiếng Việt có dấu, mô tả, key và icon đã lưu. Mục tiêu là giữ **tính ổn định tuyệt đối cho phần tuỳ biến**, đồng thời vẫn nhận được cải tiến từ repo nguồn.

Không cần nhớ lệnh dài. Mô tả việc bạn muốn làm bằng tiếng Việt; skill sẽ hỏi phần còn thiếu, giải thích lựa chọn và chỉ thay đổi khi bạn xác nhận.

## Bảy skill trong bộ này

| Icon | Skill | Dùng khi |
| --- | --- | --- |
| 📦 | `cai-dat-skill-tu-dong` | Bạn có link repo và muốn cài skill vào Codex. |
| 🔄 | `kiem-tra-cap-nhat-skill` | Bạn muốn kiểm tra nguồn, cập nhật, reset hoặc rollback skill. |
| 🧭 | `so-sanh-va-chon-skill` | Bạn có nhiều repo hoặc một task chưa rõ skill phù hợp. |
| 📊 | `bang-quan-ly-kho-skill` | Bạn muốn nhìn toàn cảnh mọi skill đang có, nguồn nào rõ/chưa rõ và việc gì cần xử lý. |
| 🩺 | `QLSVN · Kiểm tra sức khoẻ skill` | Bạn muốn biết skill nào khoẻ, cảnh báo hoặc hỏng. |
| 🧬 | `QLSVN · Quét skill trùng lặp từ 80%` | Bạn muốn tìm các skill có workflow trùng từ 80% trở lên. |
| 🧩 | `QLSVN · Hợp nhất skill an toàn` | Bạn đã chọn hai skill cần gộp và muốn backup, bản xem trước, kiểm tra trước khi archive. |

## Hình dung bằng tình huống thật

### 1. Thấy một repo nhiều skill nhưng chưa biết cài cái nào

Bạn gửi link repo và nói: “Cài skill trong repo này.”

Gọi `@cai-dat-skill-tu-dong`.

Skill sẽ đọc README và toàn bộ `SKILL.md`, sau đó hỏi bạn muốn cài một skill hay toàn bộ. Nó hỏi dùng key `có`, `không` hay `tuỳ chọn`, hỏi có dùng icon không, cho xem preview tên tiếng Việt có dấu trước khi sửa rồi mới cài. Nếu có key, key luôn đứng trước tên để tìm kiếm nhanh. Link repo, branch, danh sách skill, key và icon được lưu để lần sau cập nhật không phải tìm lại từ đầu.

Ví dụ:

```text
@cai-dat-skill-tu-dong
https://github.com/example/team-skills
Cài toàn bộ. Key là team-skills-. Tự chọn icon theo chức năng.
```

Kết quả có thể dễ nhìn như `🎨 team-skills- Giao diện`, `🛡️ team-skills- Bảo mật`, `🧪 team-skills- Kiểm thử`. Icon chỉ nằm ở tên hiển thị; mã skill luôn giữ slug không dấu để Codex gọi ổn định.

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

### 5. Kho skill đã nhiều, muốn biết cái nào là của mình và cái nào đang có vấn đề

Bạn nói: “Lập bảng tất cả skill trong máy. Cho tôi biết skill nào từ repo ngoài, cái nào QLSVN đã Việt hoá, có cái nào hỏng, mất nguồn, lệch icon hay lâu chưa kiểm tra không.”

Gọi `@bang-quan-ly-kho-skill`.

Skill này tạo một bảng quản lý chỉ đọc: không tự sửa, cập nhật hay xoá. Nó tách rõ skill local, skill hệ thống, skill agent và skill plugin để số lượng không bị đánh đồng. Với mỗi skill local, QLSVN đối chiếu sổ nguồn đã lưu để hiển thị repo, tình trạng **nguyên gốc hay đã qua QLSVN**, sức khoẻ, key/icon và tín hiệu cần kiểm tra cập nhật.

Ví dụ bảng rút gọn:

| Skill | Nguồn | Cài đặt | Sức khoẻ | Brand | Cập nhật | Gợi ý |
| --- | --- | --- | --- | --- | --- | --- |
| `taste-skill-giao-dien-toi-gian` | `Leonxlnx/taste-skill` | 🟦 QLSVN đã chỉnh | 🟢 Khỏe | ✅ Đồng bộ | 🟢 3 ngày | Không cần |
| `team-review` | Chưa rõ | ⚪ Chưa rõ | 🟢 Khỏe | — | ⚪ Chưa ghi nguồn | Ghi nguồn bằng 📦 |
| `legacy-deploy` | `org/dev-skills` | ⚪ Nguyên gốc | 🔴 Hỏng | ✅ Đồng bộ | 🟡 Cần kiểm tra | Dùng 🔄 kiểm tra/sửa |

Sau bảng là thống kê tổng số và phần đề xuất. Ví dụ: “2 skill chưa có nguồn”, “1 skill hỏng”, hoặc “5 skill lâu chưa kiểm tra remote”. Mỗi đề xuất chỉ dẫn đúng bước kế tiếp: 📦 để ghi nguồn, 🔄 để kiểm tra/sửa/cập nhật, 🧭 để so sánh hoặc phát hiện trùng lặp. Không có tín hiệu thì QLSVN nói kho đang ổn, không tạo việc cho có.

```text
@bang-quan-ly-kho-skill
📊 Quét toàn bộ kho skill trong máy và trả về bảng quản lý. Chỉ báo cáo, chưa sửa gì.
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
        ↑
        │  cần nhìn toàn cảnh, phát hiện mất nguồn/lệch brand/cảnh báo
        │
📊 Bảng quản lý kho skill
```

## Ba skill bảo trì độc lập

Ba skill dưới đây được tách riêng, không nằm trong `🔄 Kiểm tra skill` hoặc `🧭 Chọn skill`. Vì vậy tên mỗi skill đúng chức năng và bạn gọi thẳng đúng việc cần làm.

### 🩺 Kiểm tra sức khoẻ skill

Hãy hình dung kho skill như một tủ dụng cụ. Một cái búa bị gãy cán, một tuốc-nơ-vít thiếu đầu hay một ngăn không có nhãn đều làm công việc chậm đi. Skill này quét từng skill để kiểm tra YAML, tên mã, mô tả, metadata giao diện, reference, TODO và nội dung bắt buộc.

Kết quả rất dễ đọc:

```text
🟢 Khỏe      Skill đầy đủ và có thể dùng.
🟡 Cảnh báo  Skill vẫn dùng được nhưng cần xem lại, ví dụ link reference thiếu.
🔴 Hỏng      Skill thiếu phần bắt buộc hoặc có lỗi cản trở Codex tải/dùng.
```

Ví dụ:

```text
@kiem-tra-suc-khoe-skill
🩺 Kiểm tra sức khoẻ toàn bộ kho skill. Chỉ báo cáo, chưa sửa.
```

### 🧬 Quét skill trùng lặp từ 80%

Hai skill có tên khác nhau chưa chắc làm việc khác nhau. Skill này so nội dung workflow của các `SKILL.md`, không chỉ nhìn tên. Nếu tỷ lệ trùng từ 80% trở lên, QLSVN sẽ đánh dấu là ứng viên xem xét; từ 60–79% là cần đọc kỹ; dưới 60% thường là khác biệt rõ.

Ví dụ: một skill “review code” và một skill “kiểm tra chất lượng” đều yêu cầu review bảo mật, test, hiệu năng theo cùng thứ tự. QLSVN sẽ chỉ ra phần chung, nhưng cũng nêu nếu một bên có rule release riêng để bạn không gộp nhầm.

```text
@quet-skill-trung-lap
🧬 Quét toàn bộ kho skill, báo các cặp trùng lặp từ 80%.
```

### 🧩 Hợp nhất skill an toàn

Gộp skill không phải là dán hai file vào nhau. Skill này cảnh báo phần có thể mất, backup cả hai skill, tạo **một skill mới** để xem trước và giữ nguyên hai skill gốc. Chỉ khi bạn xác nhận bản mới hoạt động, hai skill cũ mới được đánh dấu archive trong registry; chúng không bị xoá tự động.

```text
@hop-nhat-skill-an-toan
🧩 Đề xuất gộp hai skill trùng lặp này. Tạo bản xem trước và backup, chưa archive bản cũ.
```

Luồng an toàn là:

```text
🧬 Phát hiện trùng lặp
        ↓
⚠️ Cảnh báo phần riêng và rủi ro
        ↓
💾 Backup hai skill gốc
        ↓
🧩 Tạo skill mới để xem trước
        ↓
🩺 Kiểm tra lại rồi mới archive bản cũ nếu bạn xác nhận
```

## Icon và tiếng Việt

Khi cài, bạn chọn một trong ba cách:

- Không dùng icon.
- Dùng một icon chung cho cả repo.
- Để hệ thống tự chọn theo nhóm chức năng, ví dụ UI `🎨`, quản lý `⚙️`, bảo mật `🛡️`, kiểm thử `🧪`, tài liệu `📚`, hiệu năng `⚡`, debug `🐞`.

Lựa chọn được lưu lại. Lần sau cài hoặc cập nhật cùng repo, Codex không hỏi lặp nếu bạn đã chọn chế độ mặc định.

Mọi câu hỏi, preview, bảng so sánh và báo cáo dùng tiếng Việt. Icon chỉ dùng trong `display_name`; tên kỹ thuật của skill không có dấu và không có emoji để luôn tương thích Codex.

## Cài bộ skill

Trong Codex, bạn có thể gửi link repo này và yêu cầu cài. Nếu đã có công cụ cài skill, cài toàn bộ thư mục `skills/` để giữ đủ bốn skill và metadata hiển thị.

```text
https://github.com/nhattuan612/quan-ly-skill-vn
Cài toàn bộ skill trong repo này.
```

Repo đang ở chế độ private. Người cài cần có quyền truy cập GitHub tương ứng.

## Nguyên tắc an toàn

- Không tự cài, cập nhật, reset hoặc xoá khi bạn mới yêu cầu kiểm tra.
- Không chạy script lạ từ repo chỉ để khảo sát.
- Luôn preview tên/icon khi cần thay đổi hiển thị.
- Luôn backup đúng skill trước update hoặc rollback.
- Không đưa registry cá nhân, token hay đường dẫn nhạy cảm vào repository.
