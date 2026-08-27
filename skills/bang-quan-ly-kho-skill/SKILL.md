---
name: bang-quan-ly-kho-skill
description: Lập bảng quản lý và thống kê toàn bộ kho skill Codex, phân loại nguồn và trạng thái, phát hiện skill hỏng, thất lạc nguồn, lệch brand hoặc cần kiểm tra cập nhật; trả về đề xuất bằng tiếng Việt.
---

# Bảng quản lý kho skill

Kích hoạt khi người dùng muốn xem toàn bộ skill đã cài, lập bảng thống kê kho skill, xem trạng thái, nguồn gốc, độ sạch thương hiệu, hoặc cần đề xuất bảo trì kho skill.

## Mục tiêu và phạm vi

- Mặc định là **chỉ đọc**: không cài, cập nhật, reset, đổi tên, gộp hoặc xoá skill.
- Quét kho skill Codex, thư mục skill của agent và skill từ plugin cache nếu có; phân loại rõ `Local`, `Hệ thống`, `Agent` hoặc `Plugin` để không nhầm skill người dùng cài với thành phần đi kèm Codex.
- Đọc `${CODEX_HOME:-$HOME/.codex}/skill-sources.md` nếu có để nhận biết repo ngoài, nguồn GitHub, key/icon đã lưu và skill đã được SFKVN Việt hoá.
- Không kiểm tra remote hay chạy script từ repo ngoài trong lượt thống kê. Trạng thái “cần kiểm tra cập nhật” là tín hiệu cần bàn giao sang skill `🔄 Kiểm tra và cập nhật skill`, không phải kết luận rằng remote chắc chắn có bản mới.

## Cách thực hiện

1. Xác định thư mục Codex từ `CODEX_HOME`, mặc định `~/.codex`.
2. Chạy `python3 scripts/inventory_skills.py`. Chỉ dùng `--local-only` khi người dùng chỉ cần kho `~/.codex/skills` để bảng gọn hơn.
3. Trả về bảng Markdown theo đúng dữ liệu quét được, tối thiểu gồm: số thứ tự, tên skill, mô tả, nguồn, tình trạng cài đặt, sức khoẻ, brand, tín hiệu cập nhật và hành động gợi ý.
4. Sau bảng phải có phần `Thống kê` với tổng skill, phân loại nguồn/cài đặt và số lượng xanh-vàng-đỏ.
5. Sau thống kê phải có phần `Đề xuất`, chỉ liệt kê việc có tín hiệu: skill hỏng, cảnh báo, chưa ghi nguồn, lệch key/icon/brand, hoặc nguồn đã lâu chưa được kiểm tra. Nếu không có tín hiệu, nói rõ kho đang ổn và không bịa đề xuất.

## Ý nghĩa trạng thái

| Trạng thái | Ý nghĩa | Việc tiếp theo |
| --- | --- | --- |
| `🟢 Khỏe` | Đủ frontmatter, tên mã, mô tả và nội dung cơ bản. | Không cần làm gì. |
| `🟡 Cảnh báo` | Vẫn dùng được nhưng có TODO, reference hoặc metadata cần xem. | Dùng `🔄` để kiểm tra/sửa có xác nhận. |
| `🔴 Hỏng` | Thiếu thành phần cần thiết để dùng ổn định. | Không tự sửa; báo nguyên nhân và bàn giao `🔄`. |
| `🟦 SFKVN đã chỉnh` | Có nguồn trong sổ và dấu hiệu tên/mô tả/icon Việt hoá SFKVN. | Bảo toàn tuỳ biến khi cập nhật/reset. |
| `⚪ Nguyên gốc` | Có nguồn theo dõi nhưng chưa có dấu hiệu SFKVN chỉnh. | Theo dõi bình thường. |
| `⚠️ Lệch brand` | Key hoặc icon đã lưu không khớp metadata hiện tại. | Xác nhận trước khi chuẩn hoá lại. |
| `🟡 Cần kiểm tra` | Bản ghi nguồn đã quá mốc theo dõi, hoặc chưa có ngày ghi nhận. | Chạy kiểm tra remote bằng `🔄`. |

## Bàn giao đúng việc

- Muốn sửa lỗi, cập nhật, reset hoặc rollback: bàn giao `🔄 Kiểm tra và cập nhật skill` sau khi người dùng xác nhận.
- Skill mất nguồn: bàn giao `📦 Cài skill từ repo` để xác định repo và lưu registry.
- Có nhiều skill cùng chức năng hoặc muốn gộp: bàn giao `🧭 So sánh và chọn skill` để quét trùng; chỉ gộp qua luồng backup an toàn của `🔄`.
- Không suy đoán repo nguồn từ tên thư mục. Gắn nhãn `chưa ghi nguồn` cho đến khi người dùng hoặc registry xác nhận.
