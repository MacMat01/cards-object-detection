import logging
import os

from ultralytics import YOLO

logging.getLogger('ultralytics').setLevel(logging.ERROR)


class YOLOModelManager:
    def __init__(self):
        os.chdir('..')
        self.model = YOLO('model_training/runs/detect/yolov8n_custom/weights/best.pt')

    def detect_objects(self, frame):
        return self.model(frame)
