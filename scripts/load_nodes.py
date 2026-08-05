import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from database.connection import driver


BATCH_SIZE = 5000


def create_nodes(tx, nodes):

    query = """
    UNWIND $nodes AS node
    MERGE (n:Node {id: node.id})
    """

    tx.run(query, nodes=nodes)


def load_nodes():

    file_path = os.path.join(
        BASE_DIR,
        "datasets",
        "wiki_Vote.txt"
    )

    print("Reading file:", file_path)

    nodes = set()


    with open(file_path, "r") as file:

        for line in file:

            if line.startswith("#"):
                continue

            source, target = line.strip().split()

            nodes.add(source)
            nodes.add(target)


    print("Total unique nodes:", len(nodes))


    node_list = []

    for node_id in nodes:

        node_list.append({
            "id": node_id
        })


        if len(node_list) == BATCH_SIZE:

            with driver.session() as session:
                session.execute_write(
                    create_nodes,
                    node_list
                )

            print(
                len(node_list),
                "nodes inserted"
            )

            node_list = []


    # Insert remaining nodes
    if node_list:

        with driver.session() as session:
            session.execute_write(
                create_nodes,
                node_list
            )


    print("Nodes loading completed!")


if __name__ == "__main__":

    load_nodes()

    driver.close()