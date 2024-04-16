from card_detection.card_detector import CardDetector
from timer_logic.timer import Timer


class Player:
    """
    This class represents a player in the game.
    Each player is associated with a fruit and has a timer to measure
    the time taken to play a card.
    The player also interacts with a CardDetector to detect when a card of the same
    fruit as the player is detected.
    """

    def __init__(self, card_detector):
        """
        Initializes a new instance of the Player class.
        The fruit is initially None, indicating that the player
        has not yet been associated with a fruit.
        The timer is obtained from the Timer class, and a new CardDetector
        instance is created.
        """
        self.fruit = None
        self.timer = Timer.get_running_timer()
        self.card_detector = card_detector

    def set_fruit(self, fruit):
        """
        Sets the player's fruit.

        Args:
            fruit (str): The fruit to associate with the player.
        """
        self.fruit = fruit

    def card_played(self, frame):
        """
        Simulates the player's card being detected and stops the timer.
        If the detected card back is the same as the
        player's fruit, the timer is stopped and the elapsed time is returned.
        If not, None is returned.

        Args:
            frame: The frame in which to detect the card back.

        Returns:
            float or None:
            The elapsed time if the detected card back is the same as the player's fruit, or None otherwise.
        """
        if self.card_detector.detect_back(frame) == self.fruit:
            elapsed_time = self.timer.stop()
            self.timer.start_time = None
            return elapsed_time
        else:
            return None

    def get_player_thinking_time(self, frame):
        """
        Returns the time taken by the player to play a card.
        This is done by calling the card_played method and
        returning its result.

        Args:
            frame: The frame in which to detect the card back.

        Returns:
            float or None: The time taken by the player to play a card,
            or None if the detected card back is not the same as the player's fruit.
        """
        return self.card_played(frame)
