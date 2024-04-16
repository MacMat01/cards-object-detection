class RoundManager:
    """
    This class represents a game that manages players and rounds.
    Each player is represented by a fruit,
    and the order of the fruits in the list represents the clockwise order of the players.
    """

    def __init__(self):
        """
        Initializes a new instance of the RoundManager class.
        The fruits attribute is set to a list of fruits in clockwise order.
        """
        self.fruits = ['apple', 'pear', 'orange', 'pineapple']

    def get_player_enemy(self, player, round_number):
        """
        Gets the enemy player for the given player and round number.
        The enemy is determined based on the player's fruit and the round number.
        The method first finds the index of the player's fruit in the fruits list.
        Then, it uses the round number to determine the enemy's fruit.
        In a clockwise round (round number modulo 3 equals 1), 
        the enemy's fruit is the next fruit in the fruits list.
        In a crosswise round (round number modulo 3 equals 2),
        the enemy's fruit is the fruit two places ahead in the list.
        In a counter-clockwise round (round number modulo 3 equals 0),
        the enemy's fruit is the previous fruit in the list.
        The modulo operator is used
        to ensure that the index wraps around to the start of the list when it reaches the end.
        Finally, the method returns the enemy's fruit.

        Args:
            player (Player): The player for whom to get the enemy.
            round_number (int): The round number.

        Returns:
            str: The enemy's fruit.
        """
        player_fruit_index = self.fruits.index(player.fruit)
        if round_number % 3 == 1:  # Clockwise round
            enemy_fruit_index = (player_fruit_index + 1) % len(self.fruits)
        elif round_number % 3 == 2:  # Crosswise round
            enemy_fruit_index = (player_fruit_index + 2) % len(self.fruits)
        else:  # Counter-clockwise round
            enemy_fruit_index = (player_fruit_index - 1) % len(self.fruits)
        return self.fruits[enemy_fruit_index]
