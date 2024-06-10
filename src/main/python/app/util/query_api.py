import os

from influxdb_client import InfluxDBClient


class QueryAPI:
    def __init__(self):
        self.client = InfluxDBClient(url="http://localhost:8086", token=os.getenv("INFLUXDB_TOKEN"), org="Cris&Matt")
        self.query_api = self.client.query_api()

    def execute_query(self, query):
        tables = self.query_api.query(query, org="Cris&Matt")
        for table in tables:
            for record in table.records:
                if record.values.get("_measurement") == "thinking_time":
                    player = record.values["player"]
                    thinking_time = record.get_value()
                    print(f"Player: {player}, Thinking Time: {thinking_time}")
                elif record.values.get("_measurement") == "card_detection":
                    card = record.values["card"]
                    elapsed_time = record.get_value()
                    print(f"Card: {card}")


if __name__ == "__main__":
    query = 'from(bucket: "StrategicFruitsData") |> range(start: -2m) |> filter(fn: (r) => r._measurement == "thinking_time" or r._measurement == "card_detection")'
    api = QueryAPI()
    api.execute_query(query)
