import os
import cv2
from pyzbar.pyzbar import decode
from ultralytics import YOLO

def detect_players(frame):
    decoded_objects = decode(frame)
    players = []
    for obj in decoded_objects:
        player = obj.data.decode("utf-8").split(" ")[0]
        players.append(player)
    return players

def main():
    os.chdir("..")
    model = YOLO('model_training/runs/detect/yolov8n_custom/weights/best.pt')
    cap = cv2.VideoCapture(1)
    cap.set(3, 1280)
    cap.set(4, 720)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detect_result = model(frame)
        detect_image = detect_result[0].plot()

        players = detect_players(frame)
        for player in players:
            print(player + " has played a card.")

        cv2.imshow('Card Detection', detect_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Usage
main()