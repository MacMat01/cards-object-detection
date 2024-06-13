import time


class PlayerManager:
    def __init__(self):
        self.players_first_set = []
        self.players_second_set = []

    def process_qrcode(self, detected_qrcodes, round_number, cards, first_phase_rounds):
        for qrcode in detected_qrcodes:
            if not any(player == qrcode for player, _ in self.players_first_set):
                self.players_first_set.append((qrcode, time.time()))
                print(f"{qrcode} has played.")
            if not any(player == qrcode for player, _ in self.players_second_set) and round_number > first_phase_rounds and len(
                    cards) == 4:
                self.players_second_set.append((qrcode, time.time()))
                print(f"{qrcode} has played.")
