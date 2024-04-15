import unittest

import cv2 as cv


class TestCamera(unittest.TestCase):
    """
    This class contains unit tests for the camera and OpenCV.
    """

    def setUp(self):
        """
        This method is called before each test. It sets up the test environment.
        Here, it creates a new instance of the VideoCapture class.
        """
        self.cap = cv.VideoCapture(0)  # 0 is the default camera

    def test_camera_open(self):
        """
        This test checks if the camera is open.
        """
        self.assertTrue(self.cap.isOpened())

    def test_camera_frame(self):
        """
        This test checks if the camera can read a frame.
        """
        ret, frame = self.cap.read()
        self.assertTrue(ret)
        self.assertIsNotNone(frame)

    def tearDown(self):
        """
        This method is called after each test. It cleans up the test environment.
        Here, it releases the VideoCapture instance.
        """
        self.cap.release()


if __name__ == '__main__':
    """
    This is the entry point for the script. It calls unittest.main(), which runs all the tests.
    """
    unittest.main()
