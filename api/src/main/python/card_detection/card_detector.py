import os

import cv2 as cv


class CardDetector:
    def __init__(self):
        folder_path = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'resources'))
        self.card_images = {
            card_name: cv.resize(cv.imread(os.path.join(folder_path, card_name), cv.IMREAD_GRAYSCALE), (100, 100)) for
            card_name in ['apple.png', 'apple_transparent.png', 'peach.png', 'peach_transparent.png', 'pear.png',
                          'pear_transparent.png', 'pineapple.png', 'pineapple_transparent.png'] if
            cv.imread(os.path.join(folder_path, card_name), cv.IMREAD_GRAYSCALE) is not None}

    def detect_face(self, frame):
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        best_match, best_match_value = None, 0
        for card_name, card_image in self.card_images.items():
            _, max_val, _, _ = cv.minMaxLoc(cv.matchTemplate(gray_frame, card_image, cv.TM_CCOEFF_NORMED))
            if max_val > best_match_value:
                best_match, best_match_value = card_name, max_val
        return best_match if best_match else 'No match found'
