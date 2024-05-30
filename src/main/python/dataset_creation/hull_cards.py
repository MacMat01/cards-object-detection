import pickle
from glob import glob

from functions import *
from global_variables import *
from hull import findHull

# find the convex hull for all the cards and store them in a pickle file
imgs_dir = "data/cards"

cards = {}
for suit in card_suits:
    for value in card_values:
        card_name = value + suit
        card_dir = os.path.join(imgs_dir, card_name)
        if not os.path.isdir(card_dir):
            print(f"!!! {card_dir} does not exist !!!")
            continue
        cards[card_name] = []
        for f in glob(card_dir + "/*.png"):
            img = cv2.imread(f, cv2.IMREAD_UNCHANGED)
            hullHL = findHull(img, refCornerHL, debug="no")
            if hullHL is None:
                print(f"File {f} not used.")
                continue
            hullLR = findHull(img, refCornerLR, debug="no")
            if hullLR is None:
                print(f"File {f} not used.")
                continue
            # We store the image in "rgb" format (we don't need opencv anymore)
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
            cards[card_name].append((img, hullHL, hullLR))
        print(f"Nb images for {card_name} : {len(cards[card_name])}")

print("Saved in :", cards_pck_fn)
pickle.dump(cards, open(cards_pck_fn, 'wb'))

cv2.destroyAllWindows()
