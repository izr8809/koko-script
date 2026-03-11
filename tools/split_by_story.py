#!/usr/bin/env python3
"""
Split koko-script files by story into individual text files.
Output: review/stories/{lang}/{level}_{story_id}.txt
e.g. review/stories/en/a0_PI-1.txt
"""

import re
import os

LANG_NAMES = {
    "ja": "Japanese",
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "zh": "Chinese",
}

# Story header pattern: # PI-1: ..., # TR-2: ..., # FAM-3: ..., etc.
STORY_HEADER = re.compile(r"^(?:\d+#[A-Z]{2}\|)?# ([A-Z]{2,4}-\d+)\s*:\s*(.+)$")

# Internal Korean metadata to strip
STRIP_PATTERNS = [
    re.compile(r"^- (대분류|중분류|난이도|분류|카테고리|서브카테고리):"),
    re.compile(r"^- \d+턴 \(\d+세트"),
]


def strip_prefix(line: str) -> str:
    match = re.match(r"^\d+#[A-Z]{2}\|(.*)$", line)
    return match.group(1) if match else line


def should_strip(text: str) -> bool:
    return any(p.match(text) for p in STRIP_PATTERNS)


def split_file(input_path: str, lang: str, level: str, output_dir: str):
    with open(input_path, "r", encoding="utf-8") as f:
        raw_lines = f.readlines()

    stories = []         # list of (story_id, story_title, [lines])
    current_id = None
    current_title = None
    current_lines = []

    for raw in raw_lines:
        text = strip_prefix(raw.rstrip("\n"))
        if should_strip(text):
            continue

        m = STORY_HEADER.match(raw.rstrip("\n"))
        if m:
            # Save previous story
            if current_id:
                stories.append((current_id, current_title, current_lines))
            current_id = m.group(1)
            current_title = m.group(2).strip()
            current_lines = [text]
        else:
            if current_id is not None:
                current_lines.append(text)

    # Save last story
    if current_id:
        stories.append((current_id, current_title, current_lines))

    # Write each story to its own file
    os.makedirs(output_dir, exist_ok=True)
    for story_id, story_title, lines in stories:
        filename = f"{level}_{story_id}.txt"
        filepath = os.path.join(output_dir, filename)

        # Trim trailing blank lines
        while lines and not lines[-1].strip():
            lines.pop()

        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        print(f"    {filename}  ({len(lines)} lines)")

    return len(stories)


def main():
    base = os.path.expanduser("~/koko-script")
    langs = ["ja", "en", "es", "fr", "zh"]
    levels = ["a0", "a1"]

    print("Splitting scripts by story...\n")

    for lang in langs:
        lang_name = LANG_NAMES.get(lang, lang.upper())
        output_dir = os.path.join(base, "review", "stories", lang)
        print(f"[{lang_name}]")

        for level in levels:
            input_path = os.path.join(base, level, f"{lang}.txt")
            if not os.path.exists(input_path):
                print(f"  ⚠️  Not found: {input_path}")
                continue
            count = split_file(input_path, lang, level, output_dir)
            print(f"  {level.upper()}: {count} stories")

        print()

    print(f"🎉 Done! Story files saved to: {base}/review/stories/")


if __name__ == "__main__":
    main()
