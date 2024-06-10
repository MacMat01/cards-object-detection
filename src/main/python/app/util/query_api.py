import os

from influxdb_client import InfluxDBClient


def execute_query(query_api, query, measurement):
    tables = query_api.query(query, org="Cris&Matt")
    for table in tables:
        for record in table.records:
            if measurement == "thinking_time":
                print(f"{record.values.get('player')} has played after {record.values.get('_value')} seconds")
            elif measurement == "card_detection":
                print(f"{record.values.get('_value')} was played")


client = InfluxDBClient(url="http://localhost:8086", token=os.getenv("INFLUXDB_TOKEN"), org="Cris&Matt")
query_api = client.query_api()

query_thinking_time = '''
from(bucket: "StrategicFruitsData")
  |> range(start: -2m)
  |> filter(fn: (r) => r._measurement == "thinking_time")
  |> map(fn: (r) => ({ r with _value: r._time, player: r.player }))
'''

query_card_detection = '''
from(bucket: "StrategicFruitsData")
  |> range(start: -2m)
  |> filter(fn: (r) => r._measurement == "card_detection")
  |> map(fn: (r) => ({ r with _value: r.card_detection }))
'''

execute_query(query_api, query_thinking_time, "thinking_time")
execute_query(query_api, query_card_detection, "card_detection")
