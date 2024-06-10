import os
import time

import cv2
from influxdb_client import InfluxDBClient, Point
from pyzbar.pyzbar import decode
from ultralytics import YOLO


class RealTimeApp:
    def __init__(self):
        self.cards_set = ['1a', '2a', '3a', '4a', '5a', '1b', '2b', '3b', '4b', '5b', '1o', '2o', '3o', '4o', '5o',
                          '1p', '2p', '3p', '4p', '5p']
        self.write_api = self.initialize_influxdb()
        self.cap = self.initialize_video_capture()
        self.model = self.initialize_yolo_model()
        self.script_start_time = time.time()
        self.qrcodes_set = set()
        self.detected_cards_set = set()

    @staticmethod
    def initialize_influxdb():
        client = InfluxDBClient(url="http://localhost:8086", token=os.getenv("INFLUXDB_TOKEN"), org="Cris&Matt")
        return client.write_api()

    @staticmethod
    def initialize_video_capture():
        cap = cv2.VideoCapture(0)
        cap.set(3, 1280)
        cap.set(4, 720)
        return cap

    @staticmethod
    def initialize_yolo_model():
        os.chdir('..')
        return YOLO('model_training/runs/detect/yolov8n_custom/weights/best.pt')

    @staticmethod
    def detect_players(frame):
        return [obj.data.decode("utf-8").split(" has played")[0] for obj in decode(frame)]

    def process_qrcode(self, detected_qrcodes):
        for qrcode in detected_qrcodes:
            if qrcode not in self.qrcodes_set:
                self.qrcodes_set.add(qrcode)
                elapsed_time = time.time() - self.script_start_time
                print(f"{qrcode} has played after {elapsed_time} seconds.")
                point = Point("thinking_time").tag("player", qrcode).field("elapsed_time", elapsed_time)
                self.write_api.write(bucket="StrategicFruitsData", org="Cris&Matt", record=point.to_line_protocol())

    def process_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return False

        detect_result = self.model(frame)
        detected_cards_indices = detect_result[0].boxes.cls.tolist()
        detected_cards = [detect_result[0].names[i] for i in detected_cards_indices]

        detect_image = detect_result[0].plot()
        detected_qrcodes = self.detect_players(frame)
        self.process_qrcode(detected_qrcodes)

        for card in self.cards_set:
            if card in detected_cards and card not in self.detected_cards_set:
                self.detected_cards_set.add(card)
                elapsed_time = time.time() - self.script_start_time
                print(f"Card '{card}' has been detected after {elapsed_time} seconds.")
                point = Point("card_detection").tag("card", card).field("elapsed_time", elapsed_time)
                self.write_api.write(bucket="StrategicFruitsData", org="Cris&Matt", record=point.to_line_protocol())

        cv2.imshow('Card Detection', detect_image)
        return True

    def run(self):
        while True:
            if not self.process_frame() or cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    app = RealTimeApp()
    app.run()
