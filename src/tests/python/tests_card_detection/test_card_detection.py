import unittest

import cv2 as cv

from main.python.camera_util.camera import Camera
from tests.python.tests_card_detection.card_detection.card_detector import CardDetector


class TestCardDetector(unittest.TestCase):
    """
    The TestCardDetector class contains unit tests for the CardDetector class.
    """

    def setUp(self):
        """
        Set up for the tests.
        This method is called before each test.
        It initializes a Camera object, opens the camera, and initializes a CardDetector object.
        """
        self.camera = Camera()
        self.camera.open()
        self.card_detector = CardDetector()

    def test_detect_card_face(self):
        """
        Test for the detect_face method of the CardDetector class.
        It checks if the detect_face method returns a string (the name of the detected card face).
        It also checks if the display_frame method of the Camera class works without throwing an exception.
        """
        while True:
            ret, frame = self.camera.read_frame()
            self.assertTrue(ret)
            self.assertIsNotNone(frame)

            # Detect the face of the card in the frame
            detected_face = self.card_detector.detect_face(frame)

            # Check the returned value
            self.assertTrue(isinstance(detected_face, str) or detected_face is None)

            # Display the detected face on the frame
            frame = cv.putText(frame, f"Detected face: {detected_face}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1,
                               (0, 255, 0), 2)

            # Display the frame in a window using the display_frame method of the Camera class
            if not self.camera.display_frame(frame):
                break

        self.camera.close()

    def tearDown(self):
        """
        Tear down for the tests.
        This method is called after each test.
        It closes the camera.
        """
        self.camera.close()


if __name__ == '__main__':
    unittest.main()
