from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
AUTH = ("neo4j", "snsaifactory")  

driver = GraphDatabase.driver(URI, auth=AUTH)