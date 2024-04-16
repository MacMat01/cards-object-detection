import time
import unittest

from camera_util.camera import Camera
from card_detection.card_detector import CardDetector
from timer_logic.timer import Timer


class TestTimer(unittest.TestCase):
    """
    This class contains unit tests for the Timer class.
    The Timer class is part of a larger system that involves card detection and camera utilities.
    """

    def setUp(self):
        """
        This method is called before each test. It sets up the test environment.
        Here, it creates a new instance of the Timer, CardDetector, and Camera classes, and opens the camera.
        """
        self.timer = Timer()
        self.card_detector = CardDetector()
        self.camera = Camera()
        self.camera.open()

    def test_timer_start_stop(self):
        """
        This test checks the start and stop methods of the Timer class.
        The timer should start when no card is detected and stop when four card backs are detected.
        """
        ret, frame = self.camera.read_frame()
        self.assertTrue(ret)
        self.assertIsNotNone(frame)

        # Start the timer when no card is detected
        if self.card_detector.detect_face(frame) is None and self.card_detector.detect_back(frame) is None:
            self.timer.start()

        # Simulate the detection of four card backs
        for _ in range(4):
            while self.card_detector.detect_back(frame) is None:
                time.sleep(1)  # wait for 1 second
                ret, frame = self.camera.read_frame()
                self.assertTrue(ret)
                self.assertIsNotNone(frame)

        # Stop the timer when four card backs are detected
        elapsed_time = self.timer.stop()

        # Check if elapsed_time is a positive number (i.e., the timer was started and then stopped)
        self.assertGreater(elapsed_time, 0)

    def tearDown(self):
        """
        This method is called after each test.
        It cleans up the test environment.
        Here, it releases the Camera instance by calling its close method.
        """
        self.camera.close()


if __name__ == '__main__':
    """
    This is the entry point for the script. It calls unittest.main(), which runs all the tests in this file.
    This is a standard Python idiom for making a script executable as well as importable as a module.
    """
    unittest.main()
