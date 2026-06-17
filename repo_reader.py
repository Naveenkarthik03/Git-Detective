from pathlib import Path


def read_repository(repo_path):

    content = ""

    for file in Path(repo_path).rglob("*.py"):

        try:

            with open(file, "r", encoding="utf-8") as f:

                content += f"\n\nFILE: {file.name}\n"

                content += f.read()

        except Exception:

            pass

    return content