from extract_card import *
from global_variables import *

# extract all the cards from a video frames
video_dir = "data/video"
extension = "mp4"
imgs_dir = "data/cards"

for suit in card_suits:
    for value in card_values:

        card_name = value + suit
        video_fn = os.path.join(video_dir, card_name + "." + extension)
        output_dir = os.path.join(imgs_dir, card_name)
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)
        imgs = extract_cards_from_video(video_fn, output_dir)
        print("Extracted images for %s : %d" % (card_name, len(imgs)))
