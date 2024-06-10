import os
import time

import cv2
from influxdb_client import InfluxDBClient, Point
from influxdb_client.domain.write_precision import WritePrecision
from pyzbar.pyzbar import decode
from ultralytics import YOLO


def initialize():
    client = InfluxDBClient(url="http://localhost:8086", token=os.getenv("INFLUXDB_TOKEN"), org="Cris&Matt")
    write_api = client.write_api()
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    os.chdir('..')
    model = YOLO('model_training/runs/detect/yolov8n_custom/weights/best.pt')
    return write_api, cap, model


def detect_qrcodes(frame):
    return {obj.data.decode("utf-8").split(" has played")[0]: time.time() for obj in decode(frame)}


def process(write_api, detected_set, detected_items, player, measurement, timestamp=None):
    for i, item in enumerate(detected_items):
        if item not in detected_set:
            detected_set.add(item)
            point = Point(measurement).tag("player", player).tag(measurement, item).time(
                timestamp or time.time() + i * 0.001, WritePrecision.NS)
            write_api.write(bucket="StrategicFruitsData", org="Cris&Matt", record=point)


def process_frame(write_api, frame, model, qrcodes_set, detected_cards_set):
    detect_result = model(frame)
    detected_cards_indices = detect_result[0].boxes.cls.tolist()
    detected_cards = [detect_result[0].names[i] for i in detected_cards_indices]
    detected_qrcodes = detect_qrcodes(frame)

    for player, timestamp in detected_qrcodes.items():
        process(write_api, qrcodes_set, [player], player, "thinking_time", timestamp)
        process(write_api, detected_cards_set, detected_cards, player, "card_detection")

    return detect_result[0].plot()


def main():
    write_api, cap, model = initialize()
    qrcodes_set = set()
    detected_cards_set = set()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detect_image = process_frame(write_api, frame, model, qrcodes_set, detected_cards_set)
        cv2.imshow('Card Detection', detect_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
