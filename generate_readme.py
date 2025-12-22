import os

# 配置你的分类目录
categories = {
    "Enumerate": "Enumerate",
    "SlidingWindow": "SlidingWindow",
    "DataStructure": "DataStructure"
}

readme_file = "README.md"

def generate_readme():
    # 统计每个分类题目数量
    category_counts = {}
    total_count = 0
    for display_name, folder in categories.items():
        if os.path.exists(folder):
            problems = [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]
            category_counts[display_name] = len(problems)
            total_count += len(problems)
        else:
            category_counts[display_name] = 0

    # 计算 Progress 表格列宽
    max_cat_len = max(len(cat) for cat in list(categories.keys()) + ["Total", "Category"])
    max_count_len = max(len(str(count)) for count in list(category_counts.values()) + [total_count, len("Count")])

    with open(readme_file, "w", encoding="utf-8") as f:
        # 顶部介绍
        f.write("# LeetCode Solutions\n\n")
        f.write("Personal LeetCode practice repository.\nFocus on clear solutions, core ideas, and complexity analysis.\n\n---\n\n")

        # Progress
        f.write("## Progress\n\n")
        f.write(f"| {'Category'.ljust(max_cat_len)} | {'Count'.ljust(max_count_len)} |\n")
        f.write(f"|{'-' * (max_cat_len + 2)}|{'-' * (max_count_len + 2)}|\n")
        for cat in categories.keys():
            f.write(f"| {cat.ljust(max_cat_len)} | {str(category_counts[cat]).ljust(max_count_len)} |\n")
        f.write(f"| {'Total'.ljust(max_cat_len)} | {str(total_count).ljust(max_count_len)} |\n\n---\n\n")

        # 每个分类题目表格
        for display_name, folder in categories.items():
            f.write(f"## {display_name}\n\n")
            f.write("| # | Title | Solution |\n")
            f.write("|---|-------|----------|\n")
            if os.path.exists(folder):
                problems = [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]
                problems.sort()
                for prob in problems:
                    if "_" in prob:
                        num, title = prob.split("_", 1)
                        title = title.replace("_", " ").title()
                    else:
                        num, title = prob, prob
                    link = f"{folder}/{prob}"
                    f.write(f"| {num} | {title} | [Code]({link}) |\n")
            f.write("\n---\n\n")

        # Notes
        f.write("## Notes\n\n")
        f.write("- Language: Python\n")
        f.write("- Focus on:\n")
        f.write("  - Correctness\n")
        f.write("  - Time / Space complexity\n")
        f.write("  - Clean logic\n")
        f.write("- Solutions are written after independent thinking.\n\n---\n\n")

        # TODO
        f.write("## TODO\n\n")
        f.write("- [ ] Add explanation markdown for selected problems\n")
        f.write("- [ ] Add multiple solutions for classic problems\n")

if __name__ == "__main__":
    generate_readme()
    print(f"{readme_file} generated successfully!")
