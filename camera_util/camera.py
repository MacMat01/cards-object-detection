import cv2 as cv


class Camera:
    """
    This class represents a camera that uses OpenCV for video capture.
    """

    def __init__(self, camera_id=0):
        """
        Initializes a new instance of the Camera class.

        Args:
            camera_id (int, optional): The ID of the camera to use.
            Defaults to 0, which usually corresponds to the default or built-in camera.
        """
        self.camera_id = camera_id
        self.cap = None

    def open(self):
        """
        Opens the camera for video capture using OpenCV's VideoCapture class. 
        The camera ID specified during the initialization of this Camera instance is used.
        """
        self.cap = cv.VideoCapture(self.camera_id)

    def is_opened(self):
        """
        Checks if the camera is open.

        Returns:
            bool: True if the camera is open, False otherwise.
        """
        return self.cap.isOpened() if self.cap else False

    def read_frame(self):
        """
        Reads a frame from the camera.

        Raises:
            Exception: If the camera is not open.

        Returns:
            tuple: A tuple where the first element is a boolean indicating the success of the frame read, 
                   and the second element is the frame itself if the read was successful, or None otherwise.
        """
        if not self.cap:
            raise Exception("Camera is not open. Call open() before reading frames.")
        return self.cap.read()

    def close(self):
        """
        Closes the camera by releasing the OpenCV VideoCapture instance. 
        This should be called when the camera is no longer needed to free up system resources.
        """
        if self.cap:
            self.cap.release()
            self.cap = None
