import os

from influxdb_client import InfluxDBClient, Point


class InfluxDBManager:
    def __init__(self):
        self.client = InfluxDBClient(url="https://us-east-1-1.aws.cloud2.influxdata.com",
                                     token=os.getenv("INFLUXDB_TOKEN"), org="Cris-and-Matt")
        self.write_api = self.client.write_api()

    def write_to_influxdb(self, player, card, elapsed_time):
        point = Point("game").tag("player", player).tag("card", card).field("thinking_time", elapsed_time)
        print(f"Writing to InfluxDB: {point.to_line_protocol()}")
        self.write_api.write(bucket="StrategicFruitsData", org="Cris-and-Matt", record=point.to_line_protocol())
