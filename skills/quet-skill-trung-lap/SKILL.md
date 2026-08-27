---
name: quet-skill-trung-lap
description: Quét nội dung workflow của kho skill Codex để phát hiện cặp trùng lặp từ 80% trở lên, phân biệt phần chung và riêng; chỉ báo cáo bằng tiếng Việt, không tự gộp.
---

# Quét skill trùng lặp từ 80%

Kích hoạt khi người dùng hỏi skill nào trùng, có nên gộp không, hoặc muốn tìm các skill có workflow gần giống. Skill này **không gộp, archive hoặc xoá** bất kỳ skill nào.

## Cách chạy

1. Chạy `python3 "${CODEX_HOME:-$HOME/.codex}/skills/kiem-tra-suc-khoe-skill/scripts/skill_audit.py" --skills-dir "${CODEX_HOME:-$HOME/.codex}/skills" --duplicates-only --threshold 60`.
2. Phân loại kết quả theo nội dung `SKILL.md`, không chỉ theo tên hoặc mô tả: `🧬 Trùng lặp cao từ 80%`, `🔎 Cần xem từ 60–79%`, `🟢 Khác biệt rõ dưới 60%`.
3. Đọc phần workflow và điều kiện kích hoạt riêng của các cặp 80% trở lên; loại trừ boilerplate, license, link hoặc câu hướng dẫn chung.

## Kết quả

Với mỗi cặp đáng chú ý, báo tỷ lệ, phần trùng, phần riêng và khuyến nghị: giữ cả hai, làm rõ tên/phạm vi, hoặc bàn giao `🧩 Hợp nhất skill an toàn`. Không gọi hai skill là trùng hoàn toàn chỉ dựa vào phần trăm, và không tự gộp.
