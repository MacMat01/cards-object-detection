import os
import time

import cv2
from influxdb_client import InfluxDBClient, Point
from pyzbar.pyzbar import decode
from ultralytics import YOLO


def initialize():
    """
    Initialize the InfluxDB client, video capture, and YOLO model.

    Returns:
        write_api: The write API of the InfluxDB client.
        cap: The videocapture object.
        model: The YOLO model.
    """
    client = InfluxDBClient(url="http://localhost:8086", token=os.getenv("INFLUXDB_TOKEN"), org="Cris&Matt")
    write_api = client.write_api()
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    os.chdir('..')
    model = YOLO('model_training/runs/detect/yolov8n_custom/weights/best.pt')
    return write_api, cap, model


def detect_qrcodes(frame):
    """
    Detect QR codes in the given frame.

    Args:
        frame: The frame to detect QR codes in.

    Returns:
        A list of decoded QR codes.
    """
    return [obj.data.decode("utf-8").split(" has played")[0] for obj in decode(frame)]


def process_qrcode(write_api, qrcodes_player_set, script_start_time, detected_qrcodes):
    """
    Process the detected QR codes.

    Args:
        write_api: The write API of the InfluxDB client.
        qrcodes_player_set: The set of QR codes that have been processed.
        script_start_time: The start time of the script.
        detected_qrcodes: The detected QR codes.
    """
    for player in detected_qrcodes:
        if player not in qrcodes_player_set:
            qrcodes_player_set.add(player)
            elapsed_time = time.time() - script_start_time
            print(f"{player} has played after {elapsed_time} seconds.")
            point = Point("thinking_time").tag("player", player).field("elapsed_time", elapsed_time)
            write_api.write(bucket="StrategicFruitsData", org="Cris&Matt", record=point)


def process_card(write_api, detected_cards_set, script_start_time, detected_cards):
    """
    Process the detected cards.

    Args:
        write_api: The write API of the InfluxDB client.
        detected_cards_set: The set of cards that have been detected.
        script_start_time: The start time of the script.
        detected_cards: The detected cards.
    """
    if '2p' in detected_cards and '2p' not in detected_cards_set:
        detected_cards_set.add('2p')
        elapsed_time = time.time() - script_start_time
        print(f"Card '2p' has been detected after {elapsed_time} seconds.")
        point = Point("card_detection").tag("card", '2p').field("elapsed_time", elapsed_time)
        write_api.write(bucket="StrategicFruitsData", org="Cris&Matt", record=point)


def main():
    """
    The main function of the application.
    """
    write_api, cap, model = initialize()
    script_start_time = time.time()
    qrcodes_set = set()
    detected_cards_set = set()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detect_result = model(frame)
        detected_cards_indices = detect_result[0].boxes.cls.tolist()
        detected_cards = [detect_result[0].names[i] for i in detected_cards_indices]

        detect_image = detect_result[0].plot()
        detected_qrcodes = detect_qrcodes(frame)

        process_qrcode(write_api, qrcodes_set, script_start_time, detected_qrcodes)
        process_card(write_api, detected_cards_set, script_start_time, detected_cards)

        cv2.imshow('Card Detection', detect_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
