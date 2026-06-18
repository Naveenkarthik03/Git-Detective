import os

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

import networkx as nx

from dependency_graph import build_graph


# ---------------------------------
# Generate diagram
# ---------------------------------
def generate_diagram(repo_path):

    graph = build_graph(
        repo_path
    )

    if len(graph.nodes()) == 0:

        return None

    os.makedirs(

        "static",

        exist_ok=True

    )

    plt.figure(

        figsize=(16, 10)

    )

    pos = nx.spring_layout(

        graph,

        k=2.5,

        iterations=100,

        seed=42

    )

    nx.draw(

        graph,

        pos,

        with_labels=True,

        node_size=7000,

        node_color="#90EE90",

        edge_color="gray",

        font_size=10,

        font_weight="bold",

        arrows=True,

        arrowsize=25,

        width=2

    )

    plt.title(

        "Repository Architecture Diagram",

        fontsize=16

    )

    plt.axis(

        "off"

    )

    plt.tight_layout()

    output_file = (

        "static/architecture_diagram.png"

    )

    plt.savefig(

        output_file,

        dpi=300,

        bbox_inches="tight"

    )

    plt.close()

    print(

        f"{output_file} generated successfully."

    )

    return output_file


# ---------------------------------
# Test
# ---------------------------------
if __name__ == "__main__":

    generate_diagram(

        "temp_repo"

    )