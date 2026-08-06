import sys
import os
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from database.connection import driver


ITERATIONS = 5


def get_test_node():

    query = """
    MATCH (n:Node)-[:VOTES_FOR]->(m)
    RETURN n.id AS id, count(m) AS connections
    ORDER BY connections DESC
    LIMIT 1
    """

    with driver.session() as session:
        result = session.run(query)
        return result.single()["id"]


def run_query(name, query, params):

    times = []
    total_records = 0

    for i in range(ITERATIONS):

        with driver.session() as session:

            start = time.time()

            result = session.run(query, params)

            records = list(result)

            end = time.time()


            execution_time = end - start
            times.append(execution_time)

            total_records = len(records)


    average_time = sum(times) / ITERATIONS


    print("-------------------------")
    print(name)
    print("Records:", total_records)
    print("Runs:", ITERATIONS)
    print("Times:")

    for i, t in enumerate(times, 1):
        print(f"Run {i}: {round(t, 6)} seconds")

    print("Average Time:",
          round(average_time, 6),
          "seconds")


def benchmark():

    node_id = get_test_node()

    print("Testing Node ID:", node_id)


    # 1-Hop Neighbor Query
    query1 = """
    MATCH (n:Node {id:$id})-[:VOTES_FOR]->(neighbor)
    RETURN neighbor.id
    """

    run_query(
        "1-Hop Neighbor Query",
        query1,
        {"id": node_id}
    )


    # 2-Hop Traversal Query
    query2 = """
    MATCH (n:Node {id:$id})-[:VOTES_FOR*2]->(neighbor)
    RETURN neighbor.id
    LIMIT 100
    """

    run_query(
        "2-Hop Traversal Query",
        query2,
        {"id": node_id}
    )


    # Most Connected Nodes Query
    query3 = """
    MATCH (n:Node)-[:VOTES_FOR]->(other)
    RETURN n.id, count(other) AS connections
    ORDER BY connections DESC
    LIMIT 10
    """

    run_query(
        "Most Connected Nodes Query",
        query3,
        {}
    )


if __name__ == "__main__":

    benchmark()

    driver.close()