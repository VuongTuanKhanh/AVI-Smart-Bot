import json
from core.helper import *


class Neo4jDB():
    def __init__(self):
        with open('../config/connection.json', 'r') as f:
            self.config = json.load(f)
            self.neo4j_connections = self.config['neo4j']
            print(self.config)

        pip_install('neo4j')

    def connect(self, url, username, password, encrypted=False):
        from neo4j import GraphDatabase
        return GraphDatabase.driver(url, auth=(username, password), encrypted=encrypted)


Neo4jDB()
