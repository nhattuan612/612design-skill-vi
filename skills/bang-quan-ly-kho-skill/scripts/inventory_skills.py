#!/usr/bin/env python3
"""Xuất bảng kiểm kê chỉ đọc cho toàn bộ skill trên máy."""

from __future__ import annotations

import argparse
import os
import re
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9-]{1,63}$")
REF_RE = re.compile(r"(?:\.\.?/|references/)(?:[\w.-]+/)*[\w.-]+\.md")
TODO_RE = re.compile(r"(?im)^\s*(?:[-*]\s*)?(?:\[[ xX]?\]\s*)?TODO\s*[:\-]")
SLUG_RE = re.compile(r"skills/([a-z0-9-]+)")
ICON_RE = re.compile(r"`([a-z0-9-]+)`\s+`([^`]+)`")


@dataclass
class Source:
    title: str
    repo: str
    recorded: date | None
    key: str
    paths: set[str]
    icons: dict[str, str]


@dataclass
class Item:
    path: Path
    group: str
    folder: str
    name: str
    description: str
    display_name: str
    errors: list[str]
    warnings: list[str]
    source: Source | None


def codex_home() -> Path:
    return Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")).expanduser()


def split_frontmatter(text: str) -> tuple[dict[str, str], str, list[str]]:
    if not text.startswith("---\n"):
        return {}, text, ["thiếu YAML frontmatter mở đầu"]
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text, ["thiếu YAML frontmatter kết thúc"]
    values: dict[str, str] = {}
    lines = text[4:end].splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        match = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if match:
            key, value = match.group(1), match.group(2).strip().strip("\"'")
            if value in {">", "|", ">-", "|-", ">+", "|+"}:
                block: list[str] = []
                index += 1
                while index < len(lines) and lines[index][:1].isspace():
                    block.append(lines[index].strip())
                    index += 1
                values[key] = ("\n" if value.startswith("|") else " ").join(block).strip()
                continue
            values[key] = value
        index += 1
    return values, text[end + 5 :], []


def read_sources(registry: Path) -> list[Source]:
    if not registry.exists():
        return []
    sections = re.split(r"(?m)^## ", registry.read_text(encoding="utf-8"))[1:]
    sources: list[Source] = []
    for section in sections:
        title, _, content = section.partition("\n")
        repo_match = re.search(r"(?m)^- Repo:\s*(\S+)", content)
        if not repo_match:
            continue
        recorded_match = re.search(r"(?m)^- Ngày ghi nhận:\s*(\d{4}-\d{2}-\d{2})", content)
        try:
            recorded = date.fromisoformat(recorded_match.group(1)) if recorded_match else None
        except ValueError:
            recorded = None
        key_match = re.search(r"(?m)^- (?:Key hiển thị|Key/prefix):\s*`?([^`\n]+?)`?\s*$", content)
        key = key_match.group(1).strip() if key_match else ""
        if key == "không dùng":
            key = ""
        paths = set(SLUG_RE.findall(content))
        icons = {skill: icon for skill, icon in ICON_RE.findall(content)}
        sources.append(Source(title.strip(), repo_match.group(1), recorded, key, paths, icons))
    return sources


def find_source(folder: str, name: str, sources: list[Source]) -> Source | None:
    for source in sources:
        if folder in source.paths:
            return source
    for source in sources:
        if source.key and name.startswith(source.key):
            return source
    return None


def candidates(home: Path, local_only: bool) -> list[tuple[Path, str]]:
    found: list[tuple[Path, str]] = []
    local = home / "skills"
    found.extend((path, "Local") for path in local.glob("*/SKILL.md"))
    found.extend((path, "Hệ thống") for path in (local / ".system").glob("*/SKILL.md"))
    if not local_only:
        agent_root = Path.home() / ".agents" / "skills"
        found.extend((path, "Agent") for path in agent_root.glob("*/SKILL.md"))
        cache = home / "plugins" / "cache"
        found.extend((path, "Plugin") for path in cache.glob("**/skills/**/SKILL.md"))
    unique: dict[Path, str] = {}
    for path, group in found:
        unique[path.resolve()] = group
    return sorted(unique.items(), key=lambda pair: (pair[1], pair[0].parent.name))


def inspect(skill_file: Path, group: str, sources: list[Source]) -> Item:
    text = skill_file.read_text(encoding="utf-8", errors="replace")
    front, body, errors = split_frontmatter(text)
    warnings: list[str] = []
    name = front.get("name", "")
    if group == "Local" and not NAME_RE.fullmatch(name):
        errors.append("name không đúng slug Codex")
    if not front.get("description"):
        errors.append("thiếu mô tả")
    if not body.strip():
        errors.append("nội dung hướng dẫn trống")
    if TODO_RE.search(text):
        warnings.append("còn TODO")
    for reference in set(REF_RE.findall(body)):
        if not (skill_file.parent / reference).resolve().exists():
            warnings.append("reference thiếu")
            break
    display_name = ""
    metadata = skill_file.parent / "agents" / "openai.yaml"
    if metadata.exists():
        display_match = re.search(r'(?m)^\s*display_name:\s*["\']?(.+?)["\']?\s*$', metadata.read_text(encoding="utf-8"))
        if display_match:
            display_name = display_match.group(1).strip()
        else:
            warnings.append("metadata thiếu display_name")
    return Item(skill_file, group, skill_file.parent.name, name, front.get("description", ""), display_name, errors, warnings, find_source(skill_file.parent.name, name, sources))


def health(item: Item) -> str:
    if item.errors:
        return "🔴 Hỏng"
    if item.warnings:
        return "🟡 Cảnh báo"
    return "🟢 Khỏe"


def install_state(item: Item) -> str:
    if item.group == "Hệ thống":
        return "⚙️ Hệ thống"
    if item.group == "Plugin":
        return "🧩 Plugin"
    if item.group == "Agent":
        return "🤖 Agent"
    if not item.source:
        return "⚪ Chưa rõ"
    vietnamese = bool(re.search(r"[À-ỹ]", item.description))
    changed = vietnamese or (item.source.key and item.name.startswith(item.source.key)) or bool(item.source.icons.get(item.folder))
    return "🟦 612 đã chỉnh" if changed else "⚪ Nguyên gốc"


def brand(item: Item) -> str:
    source = item.source
    if not source:
        return "—"
    if source.key and not item.name.startswith(source.key):
        return "⚠️ Lệch key"
    icon = source.icons.get(item.folder)
    if icon and not item.display_name.startswith(icon):
        return "⚠️ Lệch icon"
    return "✅ Đồng bộ"


def update_state(item: Item, stale_days: int) -> str:
    if item.group in {"Hệ thống", "Plugin", "Agent"}:
        return "—"
    if not item.source:
        return "⚪ Chưa ghi nguồn"
    if not item.source.recorded:
        return "🟡 Chưa ghi ngày"
    age = (date.today() - item.source.recorded).days
    return "🟡 Cần kiểm tra" if age >= stale_days else f"🟢 {age} ngày"


def action(item: Item, stale_days: int) -> str:
    if item.errors:
        return "Dùng 🔄 kiểm tra/sửa"
    if item.warnings:
        return "Xem cảnh báo"
    if not item.source and item.group == "Local":
        return "Ghi nguồn bằng 📦"
    if brand(item).startswith("⚠️"):
        return "Xác nhận chuẩn hoá"
    if update_state(item, stale_days).startswith("🟡"):
        return "Dùng 🔄 kiểm tra remote"
    return "Không cần"


def note(item: Item) -> str:
    return compact("; ".join(item.errors + item.warnings) or "—", 52)


def compact(text: str, width: int = 78) -> str:
    value = " ".join(text.replace("|", "/").split())
    return value if len(value) <= width else value[: width - 1].rstrip() + "…"


def print_report(items: list[Item], stale_days: int, local_only: bool) -> None:
    scope = "kho Codex local" if local_only else "toàn bộ kho skill đã phát hiện"
    print(f"# 📊 Bảng quản lý kho skill — {scope}\n")
    print("| # | Skill | Mô tả | Nguồn | Cài đặt | Sức khoẻ | Ghi chú | Brand | Cập nhật | Gợi ý |")
    print("| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for index, item in enumerate(items, 1):
        source = item.source.repo.rsplit("/", 1)[-1] if item.source else item.group
        print(f"| {index} | `{item.name or item.folder}` | {compact(item.description)} | {source} | {install_state(item)} | {health(item)} | {note(item)} | {brand(item)} | {update_state(item, stale_days)} | {action(item, stale_days)} |")

    groups = Counter(item.group for item in items)
    healths = Counter(health(item).split(" ", 1)[0] for item in items)
    states = Counter(install_state(item).split(" ", 1)[0] for item in items)
    print("\n## Thống kê\n")
    print(f"- Tổng cộng: **{len(items)} skill**. Phân loại: " + ", ".join(f"{group} {count}" for group, count in sorted(groups.items())) + ".")
    print(f"- Sức khoẻ: 🟢 {healths['🟢']}, 🟡 {healths['🟡']}, 🔴 {healths['🔴']}.")
    print(f"- Cài đặt: 🟦 612 {states['🟦']}, ⚪ nguyên gốc/chưa rõ {states['⚪']}, ⚙️ hệ thống {states['⚙️']}, 🧩 plugin {states['🧩']}, 🤖 agent {states['🤖']}.")

    proposals: list[str] = []
    broken = [item for item in items if item.errors]
    warnings = [item for item in items if item.warnings and not item.errors]
    untracked = [item for item in items if not item.source and item.group == "Local"]
    drift = [item for item in items if brand(item).startswith("⚠️")]
    stale = [item for item in items if update_state(item, stale_days).startswith("🟡")]
    if broken:
        proposals.append(f"🔴 {len(broken)} skill hỏng: dùng `🔄 Kiểm tra và cập nhật skill` để xem nguyên nhân, chưa tự sửa.")
    if warnings:
        proposals.append(f"🟡 {len(warnings)} skill có cảnh báo: xem TODO/reference trước khi cập nhật.")
    if untracked:
        proposals.append(f"📦 {len(untracked)} skill local chưa có nguồn: xác minh repo rồi lưu registry bằng `📦 Cài skill từ repo`.")
    if drift:
        proposals.append(f"⚠️ {len(drift)} skill lệch brand/key/icon: xác nhận trước khi chuẩn hoá lại.")
    if stale:
        proposals.append(f"🔄 {len(stale)} skill có nguồn cũ hoặc thiếu ngày: kiểm tra remote trước khi quyết định cập nhật.")
    print("\n## Đề xuất\n")
    if proposals:
        for proposal in proposals:
            print(f"- {proposal}")
    else:
        print("- 🟢 Kho đang rõ nguồn, đồng bộ brand và không có lỗi/cảnh báo cần xử lý.")


def self_check() -> None:
    front, body, errors = split_frontmatter("---\nname: demo\ndescription: Mô tả\n---\n\n# Demo\n")
    assert front["name"] == "demo" and body.strip() == "# Demo" and not errors
    assert compact("a | b", 10) == "a / b"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--local-only", action="store_true", help="chỉ quét CODEX_HOME/skills")
    parser.add_argument("--stale-days", type=int, default=30, help="số ngày trước khi nhắc kiểm tra remote")
    parser.add_argument("--self-check", action="store_true", help="chạy kiểm tra nội bộ")
    args = parser.parse_args()
    if args.stale_days < 1:
        parser.error("stale-days phải lớn hơn 0")
    if args.self_check:
        self_check()
        print("🟢 Self-check đạt.")
        return 0
    home = codex_home()
    sources = read_sources(home / "skill-sources.md")
    items = [inspect(path, group, sources) for path, group in candidates(home, args.local_only)]
    print_report(items, args.stale_days, args.local_only)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
