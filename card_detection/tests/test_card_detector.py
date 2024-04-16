import unittest

from camera_util.camera import Camera
from card_detection.card_detector import CardDetector


class TestCard(unittest.TestCase):
    """
    This class contains unit tests for the Card class.
    """

    def setUp(self):
        """
        This method is called before each test. It sets up the test environment.
        Here, it creates a new instance of the Card and Camera classes.
        """
        self.card = CardDetector()
        self.camera = Camera()
        self.camera.open()

    def test_card_face(self):
        """
        This test checks the detect_face method of the Card class.
        It compares the result of the method with an expected result.
        The method is supposed to take a camera feed as input and return the detected face of the card.
        """
        ret, frame = self.camera.read_frame()
        self.assertTrue(ret)
        self.assertIsNotNone(frame)
        expected_face = 'expected_face_value'
        self.assertEqual(self.card.detect_face(frame), expected_face)

    def test_card_back(self):
        """
        This test checks the detect_back method of the Card class.
        It compares the result of the method with an expected result.
        The method is supposed to take a camera feed as input and return the detected back of the card.
        """
        ret, frame = self.camera.read_frame()
        self.assertTrue(ret)
        self.assertIsNotNone(frame)
        expected_back = 'expected_back_value'
        self.assertEqual(self.card.detect_back(frame), expected_back)

    def tearDown(self):
        """
        This method is called after each test.
        It cleans up the test environment.
        Here, it releases the Camera instance.
        """
        self.camera.close()


if __name__ == '__main__':
    """
    This is the entry point for the script. It calls unittest.main(), which runs all the tests.
    """
    unittest.main()
