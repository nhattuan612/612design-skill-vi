#!/bin/sh
# Cài toàn bộ skill trong repo mà không ghi đè bản đã có.
set -eu

repo_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
source_dir="$repo_dir/skills"
target_dir="${CODEX_HOME:-$HOME/.codex}/skills"
skills='cai-dat-skill-tu-dong so-sanh-va-chon-skill kiem-tra-cap-nhat-skill bang-quan-ly-kho-skill kiem-tra-suc-khoe-skill quet-skill-trung-lap hop-nhat-skill-an-toan'

for skill in $skills; do
  if [ ! -f "$source_dir/$skill/SKILL.md" ]; then
    printf 'Thiếu skill nguồn: %s\n' "$skill" >&2
    exit 1
  fi
  if [ -e "$target_dir/$skill" ]; then
    printf 'Skill đã tồn tại, chưa ghi đè: %s\n' "$target_dir/$skill" >&2
    exit 1
  fi
done

mkdir -p "$target_dir"
for skill in $skills; do
  cp -R "$source_dir/$skill" "$target_dir/$skill"
done

printf 'Đã cài 7 skill vào %s. Mở lượt chat Codex mới để dùng.\n' "$target_dir"
