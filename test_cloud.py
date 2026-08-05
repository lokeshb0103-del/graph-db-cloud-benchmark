from database.connection import driver

with driver.session() as session:
    result = session.run("RETURN 'Connected to CognoDB' AS msg")
    print(result.single()["msg"])

driver.close()