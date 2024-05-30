import pickle
from glob import glob

import matplotlib.image as mpimg

backgrounds_pck_fn = 'data/backgrounds.pck'

dtd_dir = "dtd/images/"
bg_images = []
for subdir in glob(dtd_dir + "/*"):
    for f in glob(subdir + "/*.jpg"):
        bg_images.append(mpimg.imread(f))
print("Nb of images loaded :", len(bg_images))
print("Saved in :", backgrounds_pck_fn)
pickle.dump(bg_images, open(backgrounds_pck_fn, 'wb'))
