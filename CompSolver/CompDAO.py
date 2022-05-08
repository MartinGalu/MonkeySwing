from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable


class CompDAO:
    def __init__(self):
        bolt_url = "%%BOLT_URL_PLACEHOLDER%%"
        user = "<Username for database>"
        password = "<Password for database>"
        self.driver = GraphDatabase.driver(bolt_url, auth=(user, password))

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    def create_friendship(self, person1_name, person2_name):
        with self.driver.session() as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.write_transaction(
                self._create_and_return_friendship, person1_name, person2_name)
            for row in result:
                print("Created friendship between: {p1}, {p2}".format(p1=row['p1'], p2=row['p2']))

    @staticmethod
    def _create_and_return_friendship(tx, person1_name, person2_name):
        query = (
            "CREATE (p1:Person { name: $person1_name }) "
            "CREATE (p2:Person { name: $person2_name }) "
            "CREATE (p1)-[:KNOWS]->(p2) "
            "RETURN p1, p2"
        )
        result = tx.run(query, person1_name=person1_name, person2_name=person2_name)
        try:
            return [{"p1": row["p1"]["name"], "p2": row["p2"]["name"]}
                    for row in result]
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise

    def get_boss(self, boss_name):
        with self.driver.session() as session:
            result = session.read_transaction(self._find_and_return_boss_req, boss_name)
            return result

    @staticmethod
    def _find_and_return_boss_req(tx, boss_name):
        query = (
            "match (b:Boss {name:$boss_name})-[n:Needs]->(r) "
            "return r.name AS name, n.amount AS amount "
        )
        result = tx.run(query, boss_name=boss_name)
        return [row["name", "amount"] for row in result]
