import logging
import os

from ultralytics import YOLO

logging.getLogger('ultralytics').setLevel(logging.ERROR)


class YOLOModelManager:
    """
    A class used to manage the YOLO model for object detection.

    Attributes
    ----------
    model : YOLO
        a YOLO object detection model from the Ultralytics library

    Methods
    -------
    detect_objects(frame):
        Detects objects in the given frame using the YOLO model.
    """

    def __init__(self):
        """
        Constructs a new YOLOModelManager.

        The YOLOModelManager will use the YOLO model weights from the specified path.
        """
        os.chdir('..')
        self.model = YOLO('model_training/runs/detect/yolov8n_custom/weights/best.pt')

    def detect_objects(self, frame):
        """
        Detects objects in the given frame using the YOLO model.

        Parameters
        ----------
        frame : numpy.ndarray
            The frame to detect objects in.

        Returns
        -------
        list
            A list of detected objects. Each object is represented by a dictionary containing
            information about the object, such as its coordinates and class.
        """
        return self.model(frame)
