from pathlib import Path
import ast
import networkx as nx


# ---------------------------
# Find all Python files
# ---------------------------
def get_python_files(repo_path):

    files = []

    for file in Path(repo_path).rglob("*.py"):

        files.append(file)

    return files


# ---------------------------
# Read import statements
# ---------------------------
def get_imports(file_path):

    imports = []

    try:

        with open(file_path, "r", encoding="utf-8") as file:

            tree = ast.parse(file.read())

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for alias in node.names:

                    imports.append(alias.name)

            elif isinstance(node, ast.ImportFrom):

                if node.module:

                    imports.append(node.module)

    except Exception as e:

        print(f"Error reading {file_path}: {e}")

    return imports


# ---------------------------
# Build dependency graph
# ---------------------------
def build_graph(repo_path):

    graph = nx.DiGraph()

    files = get_python_files(repo_path)

    for file in files:

        current_file = file.name

        graph.add_node(current_file)

        imports = get_imports(file)

        for imp in imports:

            graph.add_edge(current_file, imp)

    return graph


# ---------------------------
# Test
# ---------------------------
if __name__ == "__main__":

    files = get_python_files("temp_repo")

    print("\nPython files found:")

    for file in files:

        print(file)

    graph = build_graph("temp_repo")

    print("\nNodes:")

    print(list(graph.nodes()))

    print("\nEdges:")

    print(list(graph.edges()))

    print("\nDependencies:")

    for source, target in graph.edges():

        print(f"{source} -> {target}")