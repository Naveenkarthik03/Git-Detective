from pathlib import Path


def review_repository(repo_path):

    print("\nCode Review Report\n")

    python_files = list(
        Path(repo_path).rglob("*.py")
    )

    for file in python_files:

        try:

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                lines = f.readlines()

            print(f"\n{file.name}")

            print("-" * 30)

            print(
                f"Lines of code: {len(lines)}"
            )

            if len(lines) > 200:

                print(
                    "⚠️ Large file. Consider splitting it."
                )

            imports = 0

            for line in lines:

                line = line.strip()

                if line.startswith("import"):

                    imports += 1

                elif line.startswith("from"):

                    imports += 1

            print(
                f"Imports: {imports}"
            )

            if imports > 10:

                print(
                    "⚠️ Too many imports."
                )

            todo_found = False

            for line in lines:

                if "TODO" in line:

                    todo_found = True

            if todo_found:

                print(
                    "⚠️ TODO comments found."
                )

            print(
                "✅ Review completed."
            )

        except Exception:

            pass


if __name__ == "__main__":

    review_repository(
        "temp_repo"
    )