import os
import sys

def generate_description(problem_dir):
    folder_name = os.path.basename(problem_dir)

    if "_" not in folder_name:
        print("Folder name format error.")
        return

    num, title_raw = folder_name.split("_", 1)
    title = title_raw.replace("_", " ")
    title_cap = title.title()

    url_title = title.lower().replace(" ", "-")
    leetcode_url = f"https://leetcode.cn/problems/{url_title}/"

    desc_path = os.path.join(problem_dir, "description.md")

    if os.path.exists(desc_path):
        print("description.md already exists.")
        return

    content = f"""# {num}. {title_cap}

## LeetCode Link
{leetcode_url}

---

## Description

<!-- Paste problem description here -->

---

## Examples

<!-- Paste examples here -->

---

## Constraints

<!-- Paste constraints here -->
"""

    with open(desc_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Generated {desc_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_description.py <problem_directory>")
    else:
        generate_description(sys.argv[1])
