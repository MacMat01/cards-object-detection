class CardManager:
    def __init__(self):
        self.cards_set = ['1a', '2a', '3a', '4a', '5a', '1b', '2b', '3b', '4b', '5b', '1o', '2o', '3o', '4o', '5o',
                          '1p', '2p', '3p', '4p', '5p']
        self.cards = []
        self.last_detected_card = None
        self.last_detected_card_count = 0

    def increment_card_count(self, card):
        if card == self.last_detected_card:
            self.last_detected_card_count += 1
        else:
            self.last_detected_card = card
            self.last_detected_card_count = 1

    def add_card_to_played(self, card):
        if self.last_detected_card_count > 6 and card not in self.cards:
            self.cards.append(card)
            print(f"Card '{card}' was played.")

    def detect_card_played(self, detected_cards):
        for card in self.cards_set:
            if card in detected_cards and card not in self.cards:
                self.increment_card_count(card)
                self.add_card_to_played(card)
