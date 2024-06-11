import os

from influxdb_client import InfluxDBClient


# The QueryAPI class is responsible for executing queries on the InfluxDB database.
class QueryAPI:
    # The constructor initializes the InfluxDB client and the query API.
    def __init__(self):
        self.client = InfluxDBClient(url="https://us-east-1-1.aws.cloud2.influxdata.com", token=os.getenv("INFLUXDB_TOKEN"), org="Cris-and-Matt")
        self.query_api = self.client.query_api()

    # This method processes the thinking time records and prints the player name and thinking time.
    def process_thinking_time(self, record):
        player = record.values["player"]
        thinking_time = record.get_value()
        print(f"Player: {player}, Thinking Time: {thinking_time}")

    # This method processes the card detection records and prints the card name.
    def process_card_detection(self, record):
        card = record.values["card"]
        elapsed_time = record.get_value()
        print(f"Card: {card}")

    # This method executes the given query on the InfluxDB database and processes the returned records.
    def execute_query(self, query):
        tables = self.query_api.query(query, org="Cris&Matt")
        for table in tables:
            for record in table.records:
                if record.values.get("_measurement") == "thinking_time":
                    self.process_thinking_time(record)
                elif record.values.get("_measurement") == "card_detection":
                    self.process_card_detection(record)


if __name__ == "__main__":
    # The query to be executed on the InfluxDB database.
    query = 'from(bucket: "StrategicFruitsData") |> range(start: -2m) |> filter(fn: (r) => r._measurement == "thinking_time" or r._measurement == "card_detection")'
    api = QueryAPI()
    api.execute_query(query)
