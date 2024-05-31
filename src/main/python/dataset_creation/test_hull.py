from glob import glob

from functions import *
from global_variables import *
from hull import findHull

# Test find_hull on a random card image
# debug = "no" or "pause_always" or "pause_on_pb"
# If debug!="no", you may have to press a key to continue execution after pause
debug = "no"
imgs_dir = "data/cards"
imgs_fns = glob(imgs_dir + "/*/*.png")
img_fn = random.choice(imgs_fns)
print(img_fn)
img = cv2.imread(img_fn, cv2.IMREAD_UNCHANGED)

hullHL = findHull(img, refCornerHL, debug=debug)
hullLR = findHull(img, refCornerLR, debug=debug)

if refCornerHL is not None and refCornerLR is not None and hullHL is not None and hullLR is not None:
    display_img(img, [refCornerHL, refCornerLR, hullHL, hullLR])
    plt.show()
else:
    print("One or more hulls not found. Cannot display image.")
if debug != "no": cv2.destroyAllWindows()
