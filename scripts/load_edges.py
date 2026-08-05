import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from database.connection import driver


BATCH_SIZE = 5000


def create_edges(tx, edges):

    query = """
    UNWIND $edges AS edge

    MATCH (a:Node {id: edge.source})
    MATCH (b:Node {id: edge.target})

    CREATE (a)-[:VOTES_FOR]->(b)
    """

    tx.run(query, edges=edges)


def load_edges():

    file_path = os.path.join(
        BASE_DIR,
        "datasets",
        "wiki_Vote.txt"
    )

    print("Reading file:", file_path)

    edge_count = 0
    edges = []


    with open(file_path, "r") as file:

        for line in file:

            # Skip comment lines
            if line.startswith("#"):
                continue


            source, target = line.strip().split()


            edges.append({
                "source": source,
                "target": target
            })


            # Insert batch
            if len(edges) == BATCH_SIZE:

                with driver.session() as session:

                    session.execute_write(
                        create_edges,
                        edges
                    )


                edge_count += len(edges)

                print(
                    edge_count,
                    "edges inserted"
                )

                edges = []


    # Insert remaining edges
    if edges:

        with driver.session() as session:

            session.execute_write(
                create_edges,
                edges
            )

        edge_count += len(edges)


    print("-------------------------")
    print("Total edges inserted:", edge_count)
    print("Edge loading completed!")
    print("-------------------------")


if __name__ == "__main__":

    load_edges()

    driver.close()