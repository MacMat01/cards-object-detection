import unittest

from main.python.camera_util.camera import Camera
from tests.python.tests_card_detection.card_detection.card_detector import CardDetector
from main.python.player_logic.player import Player


class TestPlayer(unittest.TestCase):
    """
    This class contains unit tests for the Player class.
    The Player class is part of a larger system that involves card detection and camera utilities.
    """

    def setUp(self):
        """
        This method is called before each test. It sets up the test environment.
        Here, it creates a new instance of the Player, Camera, and CardDetector classes, and opens the camera.
        """
        self.player = Player()
        self.camera = Camera()
        self.card_detector = CardDetector()
        self.camera.open()

    def test_player_thinking_time(self):
        """
        This test checks the get_player_thinking_time method of the Player class.
        The player plays a card, the camera detects the card back, and the method should return the thinking time.
        The test sets the player's fruit,
        simulates the detection of the card back,
        and checks if the method get_player_thinking_time returns a positive number.
        """
        # Set the player's fruit
        self.player.set_fruit('apple')

        # Simulate the detection of the card back
        ret, frame = self.camera.read_frame()
        self.assertTrue(ret)
        self.assertIsNotNone(frame)

        while self.card_detector.detect_back(frame) != self.player.fruit:
            ret, frame = self.camera.read_frame()
            self.assertTrue(ret)
            self.assertIsNotNone(frame)

        # Check if the method get_player_thinking_time returns a positive number
        # (i.e., the timer was started and then stopped)
        self.assertGreater(self.player.get_player_thinking_time(), 0)

    def tearDown(self):
        """
        This method is called after each test.
        It cleans up the test environment.
        Here, it releases the Camera instance by calling its close method.
        """
        self.camera.close()


if __name__ == '__main__':
    """
    This is the entry point for the script. It calls unittest.main(), which runs all the tests.
    This is a standard Python idiom for making a script executable as well as importable as a module.
    """
    unittest.main()
