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
        # TODO: Implement the detect_face method
        return None
