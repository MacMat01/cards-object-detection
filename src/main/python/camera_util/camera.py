import cv2 as cv


class Camera:
    """
    The Camera class encapsulates the functionality of a camera in the context of a card detection system.
    It uses OpenCV's VideoCapture class to interact with the camera hardware.
    """

    def __init__(self, camera_id=0):
        """
        Initializes a new instance of the Camera class.

        :param camera_id: The ID of the camera to use. Default to 0.
        """
        self.camera_id = camera_id
        self.cap = None

    def open(self):
        """
        Opens the camera for capturing video. Sets the frame width and height to 1920x1080.
        """
        self.cap = cv.VideoCapture(self.camera_id)
        self.cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
        self.cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
        self.cap.set(cv.CAP_PROP_FPS, 30)  # Set the frame rate to 30 FPS

    def is_opened(self):
        """
        Checks if the camera is open.

        :return: True if the camera is open, False otherwise.
        """
        return self.cap.isOpened() if self.cap else False

    def read_frame(self):
        """
        Reads a frame from the camera.

        :return: A tuple where the first element is a boolean indicating if the frame was successfully read,
                 and the second element is the frame itself.
        :raises Exception: If the camera is not open.
        """
        if not self.cap:
            raise Exception("Camera is not open. Call open() before reading frames.")
        return self.cap.read()

    def display_frame(self, frame, window_name='Camera Frame'):
        """
        Displays a frame in a window. The frame is mirrored before being displayed.

        :param frame: The frame to display.
        :param window_name: The name of the window in which to display the frame. Defaults to 'Camera Frame'.
        :return: False if the 'q' key is pressed, True otherwise.
        """
        # Mirror the frame
        # frame = cv.flip(frame, 1)

        # Display the frame in a window
        cv.imshow(window_name, frame)

        # If the 'q' key is pressed, return False
        if cv.waitKey(1) & 0xFF == ord('q'):
            return False

        return True

    def close(self):
        """
        Closes the camera and releases any resources it was using.
        Also destroys all windows created by cv.imshow().
        """
        if self.cap:
            self.cap.release()
            self.cap = None
        cv.destroyAllWindows()  # Destroy all windows created by cv.imshow()
