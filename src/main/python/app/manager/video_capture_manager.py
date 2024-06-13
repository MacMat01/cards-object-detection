import cv2


class VideoCaptureManager:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 1280)
        self.cap.set(4, 720)

    def read_frame(self):
        return self.cap.read()

    def release(self):
        self.cap.release()
