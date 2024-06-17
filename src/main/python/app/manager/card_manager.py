class CardManager:
    """
    A class used to manage cards in a card game.

    Attributes
    ----------
    cards_set : list
        a list of all possible cards that can be played in the game.
    cards : list
        a list of cards that have been played so far.
    last_detected_card : str
        the last detected card.
    last_detected_card_count : int
        the number of times the last detected card has been detected.

    Methods
    -------
    increment_card_count(card):
        Increments the count of the given card if it is the last detected card, or resets the count if it is a new card.
    add_card_to_played(card):
        Adds the given card to the list of played cards if it has been detected more than 6 times and it has not been played before.
    detect_card_played(detected_cards):
        Detects if a card from the set of possible cards has been played and updates the list of played cards accordingly.
    """

    def __init__(self):
        """
        Constructs a new CardManager.

        The CardManager starts with a predefined set of possible cards and an empty list of played cards.
        The last detected card and its count are initially None and 0, respectively.
        """
        self.cards_set = ['1a', '2a', '3a', '4a', '5a', '1b', '2b', '3b', '4b', '5b', '1o', '2o', '3o', '4o', '5o',
                          '1p', '2p', '3p', '4p', '5p']
        self.cards = []
        self.last_detected_card = None
        self.last_detected_card_count = 0

    def increment_card_count(self, card):
        """
        Increments the count of the given card if it is the last detected card, or resets the count if it is a new card.

        Parameters
        ----------
        card : str
            The card to increment the count for.
        """
        if card == self.last_detected_card:
            self.last_detected_card_count += 1
        else:
            self.last_detected_card = card
            self.last_detected_card_count = 1

    def add_card_to_played(self, card):
        """
        Adds the given card to the list of played cards if it has been detected more than 6 times and it has not been played before.

        Parameters
        ----------
        card : str
            The card to add to the list of played cards.
        """
        if self.last_detected_card_count > 6 and card not in self.cards:
            self.cards.append(card)
            print(f"Card '{card}' was played.")

    def detect_card_played(self, detected_cards):
        """
        Detects if a card from the set of possible cards has been played and updates the list of played cards accordingly.
    
        Parameters
        ----------
        detected_cards : list
            The list of detected cards.
        """
        for card in self.cards_set:
            if card in detected_cards and card not in self.cards:
                self.increment_card_count(card)
                self.add_card_to_played(card)

        # Check if 16 indexes are detected by YOLO
        if len(detected_cards) == 16 and len(self.cards) < 8:
            self.duplicate_cards()

    def duplicate_cards(self):
        """
        Duplicates the cards whose letter after the number does not appear twice.
        """
        # Create a dictionary to count the occurrences of each letter after the number
        letter_counts = {}
        for card in self.cards:
            letter = card[-1]
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1

        # Duplicate the cards whose letter after the number does not appear twice
        for card in self.cards:
            letter = card[-1]
            number = card[:-1]
            if letter_counts.get(letter, 0) < 2:
                self.cards.append(number + letter)
                print(f"Card '{number + letter}' was duplicated.")
                break
