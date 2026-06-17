from pathlib import Path

IGNORE_DIRS = {
    ".git",
    "node_modules",
    "__pycache__",
    ".next",
    "dist",
    "build",
    "venv"
}


def scan_repository(repo_path):

    files = []

    for path in Path(repo_path).rglob("*"):

        if any(folder in path.parts for folder in IGNORE_DIRS):
            continue

        if path.is_file():

            files.append(
                {
                    "name": path.name,
                    "path": str(path),
                    "extension": path.suffix
                }
            )

    return files