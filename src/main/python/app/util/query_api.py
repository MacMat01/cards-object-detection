import os

from influxdb_client import InfluxDBClient

# Initialize InfluxDB client
token = os.getenv("INFLUXDB_TOKEN")
org = "Cris&Matt"
url = "http://localhost:8086"
client = InfluxDBClient(url=url, token=token, org=org)

# Create an instance of the query API
query_api = client.query_api()

# Define the Flux query
query = 'from(bucket: "StrategicFruitsData") |> range(start: -2m) |> filter(fn: (r) => r._measurement == "thinking_time" or r._measurement == "card_played")'

# Execute the query and get the result tables
tables = query_api.query(query, org=org)

# Print the player names, and their thinking times
for table in tables:
    for record in table.records:
        player = record.values["player"]
        thinking_time = record.get_value()
        print(f"Player: {player}, Thinking Time: {thinking_time}")
