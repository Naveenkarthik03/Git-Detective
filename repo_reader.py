from pathlib import Path


def read_repository(repo_path):

    content = ""

    MAX_CHARS = 8000

    for file in Path(repo_path).rglob("*.py"):

        try:

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                file_content = f.read()

                content += f"\n\nFILE: {file.name}\n"

                content += file_content

                # Stop if content becomes too large

                if len(content) >= MAX_CHARS:

                    break

        except Exception:

            pass

    return content[:MAX_CHARS]