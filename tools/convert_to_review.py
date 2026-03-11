#!/usr/bin/env python3
"""
Convert koko-script format to clean dialogue-only review files (.txt).
Only keeps: story headers and AI/User dialogue lines.
"""

import re
import os

LANG_NAMES = {
    "ja": "Japanese",
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "zh": "Chinese",
    "ko": "Korean",
}

STORY_HEADER = re.compile(r"^# [A-Z]{2,4}-\d+\s*:")
DIALOGUE = re.compile(r"^(AI|User):")


def strip_line_prefix(line: str) -> str:
    match = re.compile(r"^\d+#[A-Z]{2}\|(.*)$").match(line)
    if match:
        return match.group(1)
    return line


def extract_dialogue(input_path: str) -> list:
    with open(input_path, "r", encoding="utf-8") as f:
        raw_lines = f.readlines()

    out = []
    prev_was_dialogue = False
    for raw in raw_lines:
        text = strip_line_prefix(raw.rstrip("\n"))
        if STORY_HEADER.match(text):
            if out and out[-1] != "":
                out.append("")
            # Strip markdown # prefix for plain text
            title = text.lstrip("# ").strip()
            out.append(f"[ {title} ]")
            out.append("")
            prev_was_dialogue = False
        elif DIALOGUE.match(text):
            role = text.split(":")[0]
            if prev_was_dialogue and role == "AI":
                out.append("")
            out.append(text)
            prev_was_dialogue = True
        else:
            prev_was_dialogue = False

    return out


def get_a0_path(base: str, lang: str) -> str:
    if lang == "es":
        return os.path.join(base, "a0", "es", "female.txt")
    elif lang == "fr":
        return os.path.join(base, "a0", "fr", "female.txt")
    else:
        return os.path.join(base, "a0", f"{lang}.txt")


def save_level(lang: str, level: str, base: str, output_dir: str):
    lang_name = LANG_NAMES.get(lang, lang.upper())

    if level == "a0":
        input_path = get_a0_path(base, lang)
    else:
        input_path = os.path.join(base, level, f"{lang}.txt")

    if not os.path.exists(input_path):
        print(f"  ⚠️  {level.upper()} not found: {input_path}")
        return

    lines = extract_dialogue(input_path)

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{lang}-{level}.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    dialogue_count = sum(1 for l in lines if DIALOGUE.match(l))
    print(f"  ✅  {lang_name} {level.upper()}: {output_path} ({dialogue_count} lines)")


def main():
    base = os.path.expanduser("~/koko-script")
    output_dir = os.path.join(base, "review")
    langs = ["ja", "en", "es", "fr", "zh"]
    levels = ["a0", "a1"]

    # Clean up old .md files
    for lang in langs:
        for ext in [".md", ".txt"]:
            for lv in levels:
                old = os.path.join(output_dir, f"{lang}-{lv}{ext}")
                if ext == ".md" and os.path.exists(old):
                    os.remove(old)

    print("Converting scripts to dialogue-only review files...\n")
    for lang in langs:
        for level in levels:
            save_level(lang, level, base, output_dir)

    print(f"\n🎉 Done! Files saved to: {output_dir}/")


if __name__ == "__main__":
    main()
