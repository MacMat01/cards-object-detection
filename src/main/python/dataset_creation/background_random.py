import pickle
import random
import os

import matplotlib.pyplot as plt

backgrounds_pck_fn = 'data/backgrounds.pck'

#stampa il percorso corrente
print(os.getcwd())

class Backgrounds():
    def __init__(self, backgrounds_pck_fn=backgrounds_pck_fn):
        self._images = pickle.load(open(backgrounds_pck_fn, 'rb'))
        self._nb_images = len(self._images)
        print("Nb of images loaded :", self._nb_images)

    def get_random(self, display=False):
        bg = self._images[random.randint(0, self._nb_images - 1)]
        if display: plt.imshow(bg)
        return bg


backgrounds = Backgrounds()

bg = backgrounds.get_random(display=True)
