import matplotlib.pyplot as plt
import networkx as nx


def generate_diagram():

    graph = nx.DiGraph()

    # Main application flow
    graph.add_edge("dependency_graph.py", "main.py")

    graph.add_edge("main.py", "parser.py")
    graph.add_edge("main.py", "utils.py")

    # AI flow
    graph.add_edge("ai_engine.py", "repo_reader.py")

    plt.figure(figsize=(10, 7))

    pos = {
        "dependency_graph.py": (0, 2),

        "main.py": (0, 1),

        "parser.py": (-1, 0),

        "utils.py": (1, 0),

        "ai_engine.py": (0, -1),

        "repo_reader.py": (0, -2)
    }

    nx.draw(
        graph,
        pos,

        with_labels=True,

        node_size=5000,

        node_color="#90EE90",

        font_size=11,

        font_weight="bold",

        arrows=True,

        arrowsize=20
    )

    plt.title(
        "Git-Detective Architecture Diagram",
        fontsize=16
    )

    plt.axis("off")

    plt.tight_layout()

    plt.savefig(
        "architecture_diagram.png",
        dpi=300
    )

    print("Architecture diagram saved successfully.")


if __name__ == "__main__":

    generate_diagram()