import unittest

import cv2 as cv

from main.python.camera_util.camera import Camera
from main.python.card_detection.card_detector import CardDetector


class TestCardDetector(unittest.TestCase):
    def setUp(self):
        self.camera = Camera()
        self.camera.open()
        self.card_detector = CardDetector()

    def test_detect_card_face(self):
        while True:
            ret, frame = self.camera.read_frame()
            self.assertTrue(ret)
            self.assertIsNotNone(frame)

            # Detect the face of the card in the frame
            detected_face = self.card_detector.detect_face(frame)

            # Check the returned value
            # This will depend on the implementation of the detect_face method
            # For now, let's assume it returns a string indicating the detected face
            self.assertIsInstance(detected_face, str)
            print(f"Detected face: {detected_face}")

            # If the 'q' key is pressed, break the loop and stop the test
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        cv.destroyAllWindows()  # Destroy all windows created by cv.imshow()

    def tearDown(self):
        self.camera.close()


if __name__ == '__main__':
    unittest.main()
