import unittest

from player import Player


class TestPlayer(unittest.TestCase):
    """
    This class contains unit tests for the Player class.
    """

    def setUp(self):
        """
        This method is called before each test. It sets up the test environment.
        Here, it creates a new instance of the Player class.
        """
        self.player = Player()
        self.player.set_fruit('fruit')  # replace with the fruit you want to test

    def test_get_player_thinking_time(self):
        """
        This test checks the get_player_thinking_time method of the Player class.
        It compares the result of the method with an expected result.
        The method is supposed to return the time elapsed since the player's turn started to the time the player made a play.
        """
        expected_time = 'expected_time_value'
        self.assertEqual(self.player.get_elapsed_time(), expected_time)


if __name__ == '__main__':
    """
    This is the entry point for the script. It calls unittest.main(), which runs all the tests.
    """
    unittest.main()
