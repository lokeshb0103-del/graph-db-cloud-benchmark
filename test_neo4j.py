from database.connection import driver


with driver.session() as session:

    result = session.run("""
    MATCH (n)
    RETURN labels(n) AS labels, count(n) AS count
    GROUP BY labels
    """)

    for record in result:
        print(record)


driver.close()