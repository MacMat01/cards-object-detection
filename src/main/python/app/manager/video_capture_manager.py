import cv2


class VideoCaptureManager:
    """
    A class used to manage video capture.

    Attributes
    ----------
    cap : cv2.VideoCapture
        a OpenCV VideoCapture object

    Methods
    -------
    read_frame():
        Reads the next frame from the video capture.
    release():
        Releases the video capture.
    """

    def __init__(self, video_file=None):
        """
        Constructs a new VideoCaptureManager.

        If a video file is provided, the VideoCaptureManager will read from the file.
        If no video file is provided, the VideoCaptureManager will default to real-time capture.

        Parameters
        ----------
        video_file : str, optional
            The path to the video file to read from (default is None, which means real-time capture)
        """
        if video_file:
            self.cap = cv2.VideoCapture(video_file)
        else:
            self.cap = cv2.VideoCapture(0)
            self.cap.set(3, 1280)
            self.cap.set(4, 720)

    def read_frame(self):
        """
        Reads the next frame from the video capture.

        Returns
        -------
        tuple
            A tuple where the first element is a boolean indicating if the frame was read successfully,
            and the second element is the frame itself.
        """
        return self.cap.read()

    def release(self):
        """
        Releases the video capture.

        After calling this method, no more frames can be read from the video capture.
        """
        self.cap.release()
