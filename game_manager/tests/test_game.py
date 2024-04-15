import unittest

from game import Game
from player import Player


class TestGame(unittest.TestCase):
    """
    This class contains unit tests for the Game class.
    """

    def setUp(self):
        """
        This method is called before each test. It sets up the test environment.
        Here, it creates a new instance of the Game and Player classes.
        """
        self.game = Game()
        self.player = Player()
        self.player.set_fruit('apple')  # replace 'apple' with the fruit you want to assign

    def test_get_player_enemy(self):
        """
        This test checks the get_player_enemy method of the Game class.
        It compares the result of the method with an expected result.
        The method is supposed to take a player (fruit) and the round number as input and return the enemy player for that round.
        """
        round_number = 1  # replace with the round number you want to test
        expected_enemy = 'expected_enemy_value'  # replace with the expected enemy player
        self.assertEqual(self.game.get_player_enemy(self.player, round_number), expected_enemy)


if __name__ == '__main__':
    """
    This is the entry point for the script. It calls unittest.main(), which runs all the tests.
    """
    unittest.main()
