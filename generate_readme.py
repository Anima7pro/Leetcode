import os
from collections import defaultdict

ROOT_DIR = os.getcwd()
README_FILE = "README.md"


def group_by_subcategory(problem_dirs, category):
    groups = defaultdict(list)

    for p in problem_dirs:
        parts = p.replace("\\", "/").split("/")
        if len(parts) >= 2 and parts[0] == category:
            subcategory = parts[1]
        else:
            subcategory = "Others"

        groups[subcategory].append(p)

    return dict(groups)


def find_problem_dirs(base_dir):
    """
    递归查找所有包含 solution.py 的目录
    """
    problem_dirs = []

    for root, dirs, files in os.walk(base_dir):
        if "solution.py" in files:
            problem_dirs.append(root)
            # 不再向下递归
            dirs.clear()

    return sorted(problem_dirs)

def sort_key(path):
    """
    按题号数值排序：0001, 2, 10, 1031
    """
    name = os.path.basename(path)
    try:
        return int(name.split("_", 1)[0])
    except ValueError:
        return float("inf")


def parse_problem_name(folder_name):
    """
    解析题号和标题
    """
    if "_" in folder_name:
        num, title = folder_name.split("_", 1)
        title = title.replace("_", " ").title()
    else:
        num = folder_name
        title = folder_name.replace("_", " ").title()
    return num, title

def generate_readme():
    categories = [
        d for d in os.listdir(ROOT_DIR)
        if os.path.isdir(d) and not d.startswith(".") and d not in ["__pycache__"]
    ]

    progress = {}
    category_problems = {}

    for cat in categories:
        problem_dirs = find_problem_dirs(cat)
        category_problems[cat] = problem_dirs
        progress[cat] = len(problem_dirs)

    total_count = sum(progress.values())

    max_cat_len = max(len("Category"), *(len(cat) for cat in progress))
    max_count_len = max(len("Count"), *(len(str(v)) for v in progress.values()), len(str(total_count)))

    with open(README_FILE, "w", encoding="utf-8") as f:
        # Header
        f.write("# LeetCode Solutions\n\n")
        f.write("Personal LeetCode practice repository.\n")
        f.write("Focus on clear solutions, core ideas, and complexity analysis.\n\n---\n\n")

        # Progress
        f.write("## Progress\n\n")
        f.write(f"| {'Category'.ljust(max_cat_len)} | {'Count'.ljust(max_count_len)} |\n")
        f.write(f"|{'-' * (max_cat_len + 2)}|{'-' * (max_count_len + 2)}|\n")
        for cat, cnt in progress.items():
            f.write(f"| {cat.ljust(max_cat_len)} | {str(cnt).ljust(max_count_len)} |\n")
        f.write(f"| {'Total'.ljust(max_cat_len)} | {str(total_count).ljust(max_count_len)} |\n\n---\n\n")

        # Categories
        for cat, problems in category_problems.items():
            f.write(f"## {cat}\n\n")

            sub_groups = group_by_subcategory(problems, cat)

            for subcat in sorted(sub_groups):
                f.write(f"### {subcat}\n\n")
                f.write("| # | Title | Path |\n")
                f.write("|---|-------|------|\n")

                for p in sorted(sub_groups[subcat], key=sort_key):
                    folder = os.path.basename(p)
                    num, title = parse_problem_name(folder)
                    rel_path = p.replace("\\", "/")
                    f.write(f"| {num} | {title} | [Code]({rel_path}) |\n")

                f.write("\n")
            f.write("---\n\n")


        # Notes
        f.write("## Notes\n\n")
        f.write("- Language: Python\n")
        f.write("- Only directories containing `solution.py` are counted as solved problems\n")
        f.write("- Directory structure may be nested under each category\n\n---\n\n")

        # TODO
        f.write("## TODO\n\n")
        f.write("- [ ] Add explanation markdown for selected problems\n")
        f.write("- [ ] Add multiple solutions for classic problems\n")

if __name__ == "__main__":
    generate_readme()
    print("README.md generated successfully.")
