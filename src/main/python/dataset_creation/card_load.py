import pickle

from functions import *
from global_variables import *


class Cards():
    def __init__(self, cards_pck_fn=cards_pck_fn):
        self._cards = pickle.load(open(cards_pck_fn, 'rb'))
        # self._cards is a dictionary where keys are card names (ex:'Kc') and values are lists of (img,hullHL,hullLR) 
        self._nb_cards_by_value = {k: len(self._cards[k]) for k in self._cards}
        print("Nb of cards loaded per name :", self._nb_cards_by_value)

    def get_random(self, card_name=None, display=False):
        if card_name is None:
            card_name = random.choice(list(self._cards.keys()))
        card, hull1, hull2 = self._cards[card_name][random.randint(0, self._nb_cards_by_value[card_name] - 1)]
        if display:
            if display: display_img(card, [hull1, hull2], "rgb")
        return card, card_name, hull1, hull2


cards = Cards()
