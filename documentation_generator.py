from pathlib import Path


def generate_documentation(repo_path):

    documentation = []

    documentation.append("# Repository Documentation\n")

    documentation.append("## Project Files\n")

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

            documentation.append(
                f"### {file.name}"
            )

            documentation.append(
                f"- Path: {file}"
            )

            documentation.append(
                f"- Lines of code: {len(lines)}"
            )

            imports = []

            for line in lines:

                line = line.strip()

                if line.startswith("import "):

                    imports.append(line)

                elif line.startswith("from "):

                    imports.append(line)

            if imports:

                documentation.append(
                    "- Imports:"
                )

                for item in imports:

                    documentation.append(
                        f"  - {item}"
                    )

            documentation.append("")

        except Exception:

            pass

    documentation.append(
        "\n## Workflow\n"
    )

    documentation.append(
        """
GitHub URL

↓

Clone Repository

↓

Scan Files

↓

Dependency Graph

↓

AI Analysis

↓

Architecture Diagram

↓

Documentation Generation
"""
    )

    with open(
        "PROJECT_DOCUMENTATION.md",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            "\n".join(documentation)
        )

    print(
        "PROJECT_DOCUMENTATION.md created successfully."
    )


if __name__ == "__main__":

    repo_path = input(
        "Enter repository folder name: "
    )

    generate_documentation(
        repo_path
    )