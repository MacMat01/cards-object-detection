from alphamask_layer import *
from functions import give_me_filename


def extract_cards_from_video(video_fn, output_dir=None, keep_ratio=3, min_focus=20, debug=False, limit=None):
    """
        Extract cards from media file 'video_fn'
        If 'output_dir' is specified, the cards are saved in 'output_dir'.
        One file per card with a random file name
        Because 2 consecutives frames are probably very similar, we don't use every frame of the video,
        but only one every 'keep_ratio' frames

        Returns list of extracted images
    """
    if not os.path.isfile(video_fn):
        print(f"Video file {video_fn} does not exist !!!")
        return -1, []
    if output_dir is not None and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_fn)

    frame_nb = 0
    imgs_list = []
    while True:
        ret, img = cap.read()
        if not ret: break
        # Work on every 'keep_ratio' frames
        if frame_nb % keep_ratio == 0:
            if output_dir is not None:
                output_fn = give_me_filename(output_dir, "png")
            else:
                output_fn = None
            valid, card_img = extract_card(img, output_fn, min_focus=min_focus, debug=debug)
            if debug:
                k = cv2.waitKey(1)
                if k == 27: break
            if valid:
                imgs_list.append(card_img)
                if limit is not None and len(imgs_list) >= limit:
                    break
        frame_nb += 1

    if debug:
        cap.release()
        cv2.destroyAllWindows()

    return imgs_list
