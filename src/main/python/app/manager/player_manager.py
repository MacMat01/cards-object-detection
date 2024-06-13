import time


class PlayerManager:
    """
    A class used to manage players in a card game.

    Attributes
    ----------
    players_first_set : list
        a list of tuples where each tuple represents a player who has played in the first set.
        Each tuple contains the player's QR code, and the time they played.
    players_second_set : list
        a list of tuples where each tuple represents a player who has played in the second set.
        Each tuple contains the player's QR code and the time they played.

    Methods
    -------
    process_qrcode(detected_qrcodes, round_number, cards, first_phase_rounds):
        Processes the detected QR codes, updating the players' sets accordingly.
    """

    def __init__(self):
        """
        Constructs a new PlayerManager.

        The PlayerManager starts with empty sets for the first and second sets of players.
        """
        self.players_first_set = []
        self.players_second_set = []

    def process_qrcode(self, detected_qrcodes, round_number, cards, first_phase_rounds):
        """
        Processes the detected QR codes, updating the players' sets accordingly.

        If a player's QR code is detected and they have not played in the current set yet,
        they are added to the set and a message is printed.

        Parameters
        ----------
        detected_qrcodes : list
            The detected QR codes.
        round_number : int
            The current round number.
        cards : list
            The cards that have been played.
        first_phase_rounds : int
            The number of rounds in the first phase.

        """
        for qrcode in detected_qrcodes:
            if not any(player == qrcode for player, _ in self.players_first_set):
                self.players_first_set.append((qrcode, time.time()))
                print(f"{qrcode} has played.")
            if not any(player == qrcode for player, _ in
                       self.players_second_set) and round_number > first_phase_rounds and len(cards) == 4:
                self.players_second_set.append((qrcode, time.time()))
                print(f"{qrcode} has played.")
