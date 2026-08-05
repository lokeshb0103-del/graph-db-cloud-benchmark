from database.connection import driver


with driver.session() as session:

    result = session.run("""
    MATCH (n:Node)
    RETURN n.id AS id
    LIMIT 20
    """)

    for record in result:
        print(record["id"])


driver.close()