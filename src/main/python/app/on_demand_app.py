import os

import cv2
from ultralytics import YOLO

os.chdir("..")

# Percorso del modello YOLO addestrato
model_path = 'model_training/runs/detect/yolov8n_custom/weights/best.pt'

# Percorso del video MKV
video_path = 'app/videos/video.mp4'

# Carica il modello YOLO
model = YOLO(model_path)

# Apri il video
cap = cv2.VideoCapture(video_path)

while True:
    # Leggi un frame dal video
    ret, frame = cap.read()
    if not ret:
        break

    # Applica il modello YOLO per rilevare gli oggetti nel frame
    detect_result = model(frame)

    # Disegna i riquadri di delimitazione e le etichette sulle rilevazioni
    detect_image = detect_result[0].plot()

    # Mostra il frame
    cv2.imshow('Object Detection', detect_image)

    # Interrompi il ciclo se viene premuto 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Rilascia l'oggetto di cattura video
cap.release()

# Chiudi tutte le finestre di OpenCV
cv2.destroyAllWindows()