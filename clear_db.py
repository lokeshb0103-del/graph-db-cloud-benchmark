from database.connection import driver

with driver.session() as session:
    session.run("MATCH (n:TestNode) DETACH DELETE n")

driver.close()

print("Test nodes deleted")