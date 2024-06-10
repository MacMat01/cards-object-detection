import os
import time

import cv2
from influxdb_client import InfluxDBClient, Point
from pyzbar.pyzbar import decode
from ultralytics import YOLO


def detect_players(frame):
    """
    Detect players from the given frame using QR code.

    Args:
        frame (np.array): The frame to detect players from.

    Returns:
        list: A list of player names detected in the frame.
    """
    return [obj.data.decode("utf-8").split(" has played")[0] for obj in decode(frame)]


def initialize_influxdb():
    """
    Initialize the InfluxDB client and return the write API.

    Returns:
        influxdb_client.write_api.WriteApi: The write API of the InfluxDB client.
    """
    client = InfluxDBClient(url="http://localhost:8086", token=os.getenv("INFLUXDB_TOKEN"), org="Cris&Matt")
    return client.write_api()


def initialize_video_capture():
    """
    Initialize the video capture.

    Returns:
        cv2.VideoCapture: The initialized video capture.
    """
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    return cap


def initialize_yolo_model():
    """
    Initialize the YOLO model.

    Returns:
        ultralytics.YOLO: The initialized YOLO model.
    """
    os.chdir('..')
    return YOLO('model_training/runs/detect/yolov8n_custom/weights/best.pt')


def process_qrcode(write_api, qrcodes_set, script_start_time, detected_qrcodes):
    """
    Process the detected QR codes.

    Args:
        write_api (influxdb_client.write_api.WriteApi): The write API of the InfluxDB client.
        qrcodes_set (set): A set of already detected QR codes.
        script_start_time (float): The start time of the script.
        detected_qrcodes (list): A list of detected QR codes.
    """
    for qrcode in detected_qrcodes:
        if qrcode not in qrcodes_set:
            qrcodes_set.add(qrcode)
            elapsed_time = time.time() - script_start_time
            print(f"{qrcode} has played after {elapsed_time} seconds.")
            point = Point("thinking_time").tag("player", qrcode).field("elapsed_time", elapsed_time)
            write_api.write(bucket="StrategicFruitsData", org="Cris&Matt", record=point)


def process_card(write_api, cards_set, detected_cards):
    """
    Process the detected cards.

    Args:
        write_api (influxdb_client.write_api.WriteApi): The write API of the InfluxDB client.
        cards_set (set): A set of already detected cards.
        detected_cards (list): A list of detected cards.
    """
    for card in detected_cards:
        if card not in cards_set:
            cards_set.add(card)
            print(f"{card} has been played.")
            point = Point("card_played").tag("card", card)
            write_api.write(bucket="StrategicFruitsData", org="Cris&Matt", record=point)


def main():
    """
    The main function of the application.
    """
    write_api = initialize_influxdb()
    cap = initialize_video_capture()
    model = initialize_yolo_model()
    script_start_time = time.time()
    qrcodes_set = set()
    cards_set = set()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detect_image = model(frame)[0].plot()
        detected_qrcodes = detect_players(frame)
        process_qrcode(write_api, qrcodes_set, script_start_time, detected_qrcodes)

        process_card(write_api, cards_set, detect_image)

        cv2.imshow('Card Detection', detect_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
