from neo4j import GraphDatabase
from config.config import (
    COGNODB_URI,
    COGNODB_USER,
    COGNODB_PASSWORD
)

driver = GraphDatabase.driver(
    COGNODB_URI,
    auth=(COGNODB_USER, COGNODB_PASSWORD)
)
