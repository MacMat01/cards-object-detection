import os

import cv2
from ultralytics import YOLO

os.chdir("..")

# Path of the trained YOLO model
model_path = 'model_training/runs/detect/yolov8n_custom/weights/best.pt'

# Path of the MKV video
video_path = 'app/videos/video.mp4'

# Upload YOLO model
model = YOLO(model_path)

# Open video
cap = cv2.VideoCapture(video_path)

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    # Applies the YOLO model to detect objects in the frame
    detect_result = model(frame)

    # Draw bounding boxes and labels on the surveys
    detect_image = detect_result[0].plot()

    # Show the frame
    cv2.imshow('Object Detection', detect_image)

    # Interrupt the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
