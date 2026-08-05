from database.connection import driver

with driver.session() as session:
    result = session.run("RETURN 'Connected Successfully' AS message")
    print(result.single()["message"])

driver.close()