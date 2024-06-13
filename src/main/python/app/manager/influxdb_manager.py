import os

from influxdb_client import InfluxDBClient, Point


class InfluxDBManager:
    """
    A class used to manage interactions with InfluxDB.

    Attributes
    ----------
    client : InfluxDBClient
        a client object to interact with InfluxDB
    write_api : WriteApi
        an API object to write data to InfluxDB

    Methods
    -------
    write_to_influxdb(player, card, elapsed_time):
         Write the player, card, and elapsed time data to InfluxDB.
    """

    def __init__(self):
        """
        Constructs a new InfluxDBManager.

        The InfluxDBManager will use the InfluxDB client with the specified URL, token, and organization.
        """
        self.client = InfluxDBClient(url="https://us-east-1-1.aws.cloud2.influxdata.com",
                                     token=os.getenv("INFLUXDB_TOKEN"), org="Cris-and-Matt")
        self.write_api = self.client.write_api()

    def write_to_influxdb(self, player, card, elapsed_time, round_number):
        """
        Writes the player, card, and elapsed time data to InfluxDB.

        The data is written as a point with the player and card as tags and the elapsed time as a field.

        Parameters
        ----------
        player : str
            The player who played the card.
        card : str
            The card that was played.
        elapsed_time : float
            The time elapsed since the player's last move.
        """
        if round_number <= 12:
            phase = 1
        elif 13 <= round_number <= 18:
            phase = 2
        else:
            phase = 3

        point = Point("game").tag("Phase", phase).tag("Round", round_number).tag("player", player).tag("card",
                                                                                                       card).field(
            "thinking_time", elapsed_time)
        print(f"Writing to InfluxDB: {point.to_line_protocol()}")
        self.write_api.write(bucket="StrategicFruitsData", org="Cris-and-Matt", record=point.to_line_protocol())
