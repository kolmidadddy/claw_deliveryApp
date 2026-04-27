import os

class Settings:
    neo4j_uri = os.getenv("NEO4J_URI")
    neo4j_password = os.getenv("NEO4J_PASSWORD")

settings = Settings()