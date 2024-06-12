import logging
import os
import time

import cv2
from influxdb_client import InfluxDBClient, Point
from pyzbar.pyzbar import decode
from ultralytics import YOLO

logging.getLogger('ultralytics').setLevel(logging.ERROR)


class RealTimeApp:
    def __init__(self):
        self.last_detected_card = None
        self.last_detected_card_count = 0
        self.cards_set = ['1a', '2a', '3a', '4a', '5a', '1b', '2b', '3b', '4b', '5b', '1o', '2o', '3o', '4o', '5o',
                          '1p', '2p', '3p', '4p', '5p']
        self.write_api = self.initialize_influxdb()
        self.cap = self.initialize_video_capture()
        self.model = self.initialize_yolo_model()
        self.script_start_time = time.time()
        self.qrcodes_set = set()
        self.detected_cards_set = set()
        self.NUMBER_OF_CARDS = 4
        self.round_number = 1
        self.players = []
        self.cards = []
        print(f"Round {self.round_number} starting.")

    def increment_round(self):
        self.round_number += 1
        print(f"Round {self.round_number} starting.")

    def clear_players(self):
        self.players.clear()

    def clear_cards(self):
        self.cards.clear()

    # This method initializes the InfluxDB client and returns the write API.
    @staticmethod
    def initialize_influxdb():
        client = InfluxDBClient(url="https://us-east-1-1.aws.cloud2.influxdata.com", token=os.getenv("INFLUXDB_TOKEN"),
                                org="Cris-and-Matt")
        return client.write_api()

    # This method initializes the video capture object and sets the resolution.
    @staticmethod
    def initialize_video_capture():
        cap = cv2.VideoCapture(1)
        cap.set(3, 1280)
        cap.set(4, 720)
        return cap

    # This method initializes the YOLO model for object detection.
    @staticmethod
    def initialize_yolo_model():
        os.chdir('..')
        return YOLO('model_training/runs/detect/yolov8n_custom/weights/best.pt')

    # This method decodes the QR codes in the given frame and returns the player names.
    @staticmethod
    def detect_players(frame):
        return [obj.data.decode("utf-8").split(" has played")[0] for obj in decode(frame)]

    # This method processes the detected QR codes and writes the thinking time to the InfluxDB.
    def process_qrcode(self, detected_qrcodes):
        for qrcode in detected_qrcodes:
            if qrcode not in [player for player, _ in self.players]:
                self.players.append((qrcode, time.time()))
                print(f"{qrcode} has played.")

    def increment_card_count(self, card):
        if card == self.last_detected_card:
            self.last_detected_card_count += 1
        else:
            self.last_detected_card = card
            self.last_detected_card_count = 1

    def add_card_to_played(self, card):
        if self.last_detected_card_count > 10 and card not in self.cards:
            self.cards.append(card)
            print(f"Card '{card}' was played.")

    def detect_card_played(self, detected_cards):
        for card in self.cards_set:
            if card in detected_cards and card not in self.cards:
                self.increment_card_count(card)
                self.add_card_to_played(card)

    def check_round_end(self):
        if len(self.cards) == self.NUMBER_OF_CARDS:
            print(f"Round {self.round_number} ended and starting 10 seconds delay")
            time.sleep(10)
            print(f"10 seconds delay ended and starting {self.round_number + 1} round.")
            self.clear_players()
            self.clear_cards()
            self.increment_round()

    def process_card_detection(self, detected_cards):
        self.detect_card_played(detected_cards)
        self.check_round_end()

    def detect_and_process_qrcodes(self, frame):
        detected_qrcodes = self.detect_players(frame)
        self.process_qrcode(detected_qrcodes)

    def detect_and_process_cards(self, frame):
        detect_result = self.model(frame)
        detected_cards_indices = detect_result[0].boxes.cls.tolist()
        detected_cards = [detect_result[0].names[i] for i in detected_cards_indices]
        self.process_card_detection(detected_cards)

    def write_to_influxdb(self):
        for player, player_time in self.players[:]:
            for card in self.cards[:]:
                if player[0].lower() == card[-1].lower():
                    self.players.remove((player, player_time))
                    self.cards.remove(card)
                    elapsed_time = time.time() - player_time
                    point = Point("game").tag("player", player).tag("card", card).field("thinking_time", elapsed_time)
                    print(f"Writing to InfluxDB: {point.to_line_protocol()}")
                    self.write_api.write(bucket="StrategicFruitsData", org="Cris-and-Matt",
                                         record=point.to_line_protocol())
                    break

    def process_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return False

        self.detect_and_process_qrcodes(frame)
        self.detect_and_process_cards(frame)
        self.write_to_influxdb()

        return True

    # This method runs the real-time card detection application.
    def run(self):
        while True:
            if not self.process_frame() or cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    app = RealTimeApp()
    app.run()
