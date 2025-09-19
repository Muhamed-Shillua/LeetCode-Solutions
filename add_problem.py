import os
import argparse
import json
import shutil
import requests

# Load config.json
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

def fetch_problem_metadata(problem_name: str):
    """
    Fetch problem ID and slug from LeetCode API using the problem title.
    """
    api_url = "https://leetcode.com/api/problems/all/"
    response = requests.get(api_url, timeout=10)
    if response.status_code != 200:
        raise RuntimeError("Failed to fetch problems from LeetCode API")

    data = response.json()
    for problem in data.get("stat_status_pairs", []):
        title = problem["stat"]["question__title"].strip().lower()
        if title == problem_name.strip().lower():
            qid = problem["stat"]["frontend_question_id"]
            slug = problem["stat"]["question__title_slug"]
            folder_name = f"{qid:04d}-{slug}"
            return folder_name, slug, qid
    raise ValueError(f"Problem '{problem_name}' not found in LeetCode API")

def generate_readme(problem_name: str, problem_url: str, difficulty: str, language: str, author: str) -> str:
    return f"""# Problem: {problem_name}

- **LeetCode Link:** [{problem_name}]({problem_url})
- **Difficulty:** {difficulty.capitalize()}
- **Language:** {language}

## Problem Description
<Write a brief description of the problem in your own words.>

## Approach
<Explain your solution approach clearly:>
- Mention any algorithms or data structures used.
- Step-by-step explanation if necessary.
- Highlight any tricky parts or optimizations.

## Time Complexity
<O notation explanation, e.g., O(n), O(n log n)>

## Space Complexity
<O notation explanation, e.g., O(1), O(n)>

## Example
```
Input: <example input>
Output: <example output>
Explanation: <brief explanation of the output>
```

## Notes / Edge Cases
- Any special cases or considerations.
- Things to watch out for while implementing.

---
*Author: {author}*
"""

def main():
    parser = argparse.ArgumentParser(description="Add a new LeetCode problem solution.")
    parser.add_argument("--name", required=True, help="Problem name, e.g., 'Roman to Integer'")
    parser.add_argument("--difficulty", required=True, choices=["easy", "medium", "hard"], help="Problem difficulty")
    parser.add_argument("--lang", choices=["cpp", "py"], default=config.get("default_language", "cpp"), help="Solution language")
    parser.add_argument("--solution", help="Path to your solution file (optional)")
    parser.add_argument("--commit", action="store_true", help="Commit and push changes to GitHub")
    args = parser.parse_args()

    # Fetch problem metadata from LeetCode
    folder_name, slug, qid = fetch_problem_metadata(args.name)
    folder_path = os.path.join(args.difficulty.capitalize(), folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Create solution file (copy user file or generate empty)
    solution_file = os.path.join(folder_path, f"solution.{args.lang}")
    if not os.path.exists(solution_file):
        if args.solution:
            shutil.copy(args.solution, solution_file)
            print(f"Solution file copied from {args.solution}")
        else:
            with open(solution_file, "w", encoding="utf-8") as f:
                if args.lang == "cpp":
                    f.write("class Solution {\npublic:\n    // Implement here\n};\n")
                else:
                    f.write("class Solution:\n    def solve(self):\n        pass\n")
            print("Empty solution file generated.")

    # Create README.md
    readme_file = os.path.join(folder_path, "README.md")
    if not os.path.exists(readme_file):
        problem_url = f"https://leetcode.com/problems/{slug}/"
        readme_content = generate_readme(args.name, problem_url, args.difficulty, "C++" if args.lang == "cpp" else "Python", config["author"])
        with open(readme_file, "w", encoding="utf-8") as f:
            f.write(readme_content)

    # Commit and push
    if args.commit:
        lang_name = "C++" if args.lang == "cpp" else "Python"
        commit_message = f'feat({args.difficulty}): add {args.name} ({lang_name})'
        os.system(f'git add "{folder_path}"')
        os.system(f'git commit -m "{commit_message}"')
        os.system('git push origin main')

        repo_url = config.get("repo_url")
        if repo_url:
            github_link = f"{repo_url}/tree/main/{args.difficulty.capitalize()}/{folder_name}"
            print(f"GitHub link: {github_link}")

if __name__ == "__main__":
    main()
