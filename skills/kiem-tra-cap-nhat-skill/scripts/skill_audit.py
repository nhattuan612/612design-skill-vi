#!/usr/bin/env python3
"""Read-only health and duplicate audit for Codex skills."""

from __future__ import annotations

import argparse
import itertools
import os
import re
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9-]{1,63}$")
WORD_RE = re.compile(r"[^\W_]+", re.UNICODE)
REF_RE = re.compile(r"(?:\.\.?/|references/)(?:[\w.-]+/)*[\w.-]+\.md")
TODO_RE = re.compile(r"(?im)^\s*(?:[-*]\s*)?(?:\[[ xX]?\]\s*)?TODO\s*[:\-]")


def codex_skills_dir() -> Path:
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    return codex_home / "skills"


def split_frontmatter(text: str) -> tuple[dict[str, str], str, list[str]]:
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, text, ["thiếu YAML frontmatter mở đầu"]

    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text, ["thiếu YAML frontmatter kết thúc"]

    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip('"\'')
    return values, text[end + 5 :], errors


def normalized_tokens(text: str) -> list[str]:
    return WORD_RE.findall(text.lower())


def fingerprints(tokens: list[str]) -> set[tuple[str, ...]]:
    if len(tokens) < 5:
        return {tuple(tokens)} if tokens else set()
    return {tuple(tokens[index : index + 5]) for index in range(len(tokens) - 4)}


def similarity(left: str, right: str) -> float:
    left_items = fingerprints(normalized_tokens(left))
    right_items = fingerprints(normalized_tokens(right))
    if not left_items and not right_items:
        return 100.0
    union = left_items | right_items
    return 100.0 * len(left_items & right_items) / len(union)


def relative_reference_errors(skill_file: Path, body: str) -> list[str]:
    errors: list[str] = []
    for reference in sorted(set(REF_RE.findall(body))):
        target = (skill_file.parent / reference).resolve()
        if not target.exists():
            errors.append(f"reference thiếu: {reference}")
    return errors


def audit_skill(skill_file: Path) -> tuple[list[str], list[str], str]:
    text = skill_file.read_text(encoding="utf-8")
    frontmatter, body, errors = split_frontmatter(text)
    warnings: list[str] = []
    name = frontmatter.get("name", "")
    if not NAME_RE.fullmatch(name):
        errors.append("name thiếu hoặc không đúng slug Codex")
    if not frontmatter.get("description"):
        errors.append("description bị thiếu")
    if "[TODO" in text or TODO_RE.search(text):
        warnings.append("còn TODO chưa hoàn tất")
    if not body.strip():
        errors.append("nội dung hướng dẫn trống")
    warnings.extend(relative_reference_errors(skill_file, body))

    metadata = skill_file.parent / "agents" / "openai.yaml"
    if metadata.exists() and "display_name:" not in metadata.read_text(encoding="utf-8"):
        warnings.append("metadata UI không có display_name")
    return errors, warnings, body


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills-dir", type=Path, default=codex_skills_dir())
    parser.add_argument("--threshold", type=float, default=80.0)
    args = parser.parse_args()

    root = args.skills_dir.expanduser().resolve()
    if not root.is_dir():
        parser.error(f"không tìm thấy thư mục skill: {root}")
    if not 0 <= args.threshold <= 100:
        parser.error("threshold phải từ 0 đến 100")

    skill_files = sorted(root.glob("*/SKILL.md"))
    bodies: dict[Path, str] = {}
    broken = 0
    warnings = 0
    print(f"🩺 Kiểm tra sức khoẻ skill: {len(skill_files)} skill")
    for skill_file in skill_files:
        errors, notes, body = audit_skill(skill_file)
        bodies[skill_file] = body
        label = skill_file.parent.name
        if errors:
            broken += 1
            print(f"🔴 Hỏng  {label}: {'; '.join(errors)}")
        elif notes:
            warnings += 1
            print(f"🟡 Cảnh báo  {label}: {'; '.join(notes)}")
        else:
            print(f"🟢 Khỏe  {label}")

    print(f"\n🧬 Quét skill trùng lặp từ {args.threshold:.0f}%")
    matches: list[tuple[float, Path, Path]] = []
    for left, right in itertools.combinations(skill_files, 2):
        score = similarity(bodies[left], bodies[right])
        if score >= args.threshold:
            matches.append((score, left, right))
    if matches:
        for score, left, right in sorted(matches, reverse=True):
            print(f"🧬 {score:.1f}%  {left.parent.name} ↔ {right.parent.name}")
    else:
        print("Không có cặp nào vượt ngưỡng.")

    print(f"\nTổng kết: {len(skill_files) - broken - warnings} khỏe, {warnings} cảnh báo, {broken} hỏng, {len(matches)} cặp trùng.")
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
