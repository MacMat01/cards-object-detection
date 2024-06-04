import os

import cv2
from pyzbar.pyzbar import decode
from ultralytics import YOLO

# TODO: Test QR Code Functionality

os.chdir("..")

# Load the trained YOLO model
model = YOLO('model_training/runs/detect/yolov8n_custom/weights/best.pt')

# Start capturing video
cap = cv2.VideoCapture(0)  # 0 for the default camera

# Set the frame width and height
cap.set(3, 1280)  # Width
cap.set(4, 720)  # Height

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    # Apply the YOLO model to detect cards in the frame
    detect_result = model(frame)

    # Draw bounding boxes and labels on the detections
    detect_image = detect_result[0].plot()

    # Decode the QR code from the frame
    decoded_objects = decode(frame)
    for obj in decoded_objects:
        print("Type:", obj.type)
        print("Data:", obj.data.decode("utf-8"), "\n")

    # Display the frame
    cv2.imshow('Card Detection', detect_image)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
