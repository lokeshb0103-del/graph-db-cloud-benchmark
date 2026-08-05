import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from database.connection import driver


def check_graph():

    with driver.session() as session:

        # Count nodes
        node_result = session.run(
            "MATCH (n:Node) RETURN count(n) AS total_nodes"
        )

        nodes = node_result.single()["total_nodes"]


        # Count edges
        edge_result = session.run(
            "MATCH ()-[r:VOTES_FOR]->() RETURN count(r) AS total_edges"
        )

        edges = edge_result.single()["total_edges"]


        print("----------------------")
        print("Total Nodes:", nodes)
        print("Total Edges:", edges)
        print("----------------------")


if __name__ == "__main__":
    check_graph()
    driver.close()