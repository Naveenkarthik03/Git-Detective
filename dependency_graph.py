from pathlib import Path
import ast
import networkx as nx


# ---------------------------------
# Get all Python files
# ---------------------------------
def get_python_files(repo_path):

    return list(
        Path(repo_path).rglob("*.py")
    )


# ---------------------------------
# Read imports
# ---------------------------------
def get_imports(file_path):

    imports = []

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            tree = ast.parse(
                f.read()
            )

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for alias in node.names:

                    imports.append(
                        alias.name
                    )

            elif isinstance(
                node,
                ast.ImportFrom
            ):

                if node.module:

                    imports.append(
                        node.module
                    )

    except Exception as e:

        print(
            f"Error reading {file_path}: {e}"
        )

    return imports


# ---------------------------------
# Build Graph
# ---------------------------------
def build_graph(repo_path):

    graph = nx.DiGraph()

    files = get_python_files(
        repo_path
    )

    # Remove unnecessary files

    files = [

        file

        for file in files

        if "__pycache__" not in str(file)

        and "test" not in file.name.lower()

        and "migration" not in str(file).lower()

        and "__init__" not in file.name

        and "dotenv" not in file.name.lower()

        and file.name.lower() != "env.py"

        and not file.name.startswith("fe")

        and not file.name.startswith("e2")

    ]

    # Important files only

    important_files = {

        "main.py",

        "config.py",

        "db.py",

        "deps.py",

        "models.py",

        "crud.py",

        "users.py",

        "user.py",

        "items.py",

        "item.py",

        "security.py",

        "utils.py"

    }

    filtered = []

    for file in files:

        if file.name in important_files:

            filtered.append(file)

    if filtered:

        files = filtered

    # Lookup table

    file_lookup = {}

    for file in files:

        file_lookup[

            file.stem

        ] = file.name

    # Add nodes

    for file in files:

        graph.add_node(

            file.name

        )

    # Add edges

    for file in files:

        imports = get_imports(

            file

        )

        for imp in imports:

            parts = imp.split(".")

            for part in parts:

                if part in file_lookup:

                    graph.add_edge(

                        file.name,

                        file_lookup[part]

                    )

                    break

    return graph


# ---------------------------------
# Test
# ---------------------------------
if __name__ == "__main__":

    graph = build_graph(

        "temp_repo"

    )

    print(

        list(graph.nodes())

    )

    print(

        list(graph.edges())

    )