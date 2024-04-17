import unittest

from main.python.player_logic.player import Player
from main.python.round_manager.round_manager import RoundManager


class TestRoundManager(unittest.TestCase):
    """
    This class contains unit tests for the RoundManager class.
    The RoundManager class is part of a larger system that involves managing rounds in a game.
    """

    def setUp(self):
        """
        This method is called before each test. It sets up the test environment.
        Here, it creates a new instance of the RoundManager and Player classes, and sets the player's fruit.
        """
        self.round_manager = RoundManager()
        self.player = Player()
        self.player.set_fruit('apple')

    def test_get_player_enemy_clockwise(self):
        """
        This test checks the get_player_enemy method of the RoundManager class for a clockwise round.
        The test sets the round number to 1 (representing a clockwise round),
        and checks if the method get_player_enemy returns the expected enemy for a clockwise round.
        """
        round_number = 1
        expected_enemy = 'expected_enemy_for_clockwise_round'
        self.assertEqual(self.round_manager.get_player_enemy(self.player, round_number), expected_enemy)

    def test_get_player_enemy_crosswise(self):
        """
        This test checks the get_player_enemy method of the RoundManager class for a crosswise round.
        The test sets the round number to 2 (representing a crosswise round),
        and checks if the method get_player_enemy returns the expected enemy for a crosswise round.
        """
        round_number = 2
        expected_enemy = 'expected_enemy_for_crosswise_round'
        self.assertEqual(self.round_manager.get_player_enemy(self.player, round_number), expected_enemy)

    def test_get_player_enemy_counter_clockwise(self):
        """
        This test checks the get_player_enemy method of the RoundManager class for a counter-clockwise round.
        The test sets the round number to 3 (representing a counter-clockwise round),
        and checks if the method get_player_enemy returns the expected enemy for a counter-clockwise round.
        """
        round_number = 3
        expected_enemy = 'expected_enemy_for_counter_clockwise_round'
        self.assertEqual(self.round_manager.get_player_enemy(self.player, round_number), expected_enemy)


if __name__ == '__main__':
    """
    This is the entry point for the script. It calls unittest.main(), which runs all the tests in this file.
    This is a standard Python idiom for making a script executable as well as importable as a module.
    """
    unittest.main()
