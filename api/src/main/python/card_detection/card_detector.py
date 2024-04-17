import os

import cv2 as cv


class CardDetector:
    def __init__(self, assets_folder=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources')):
        # Load the card images from the assets folder
        self.card_images = {}
        for card_name in ['Apple.png', 'Peach.png', 'Pear.png', 'Pineapple.png']:
            image_path = os.path.join(assets_folder, card_name)
            image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
            if image is not None:
                # Resize the image to ensure it is smaller than the frames
                image = cv.resize(image, (100, 100))
                self.card_images[card_name] = image

    def detect_face(self, frame):
        # Convert the frame to grayscale
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Initialize the best match values
        best_match = None
        best_match_value = 0

        # Compare the frame to each card image using template matching
        for card_name, card_image in self.card_images.items():
            result = cv.matchTemplate(gray_frame, card_image, cv.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv.minMaxLoc(result)

            # If this match is better than the current best match, update the best match
            if max_val > best_match_value:
                best_match = card_name
                best_match_value = max_val

        # If no card image could be matched, return a default value
        if best_match is None:
            return 'No match found'

        # Return the best match
        return best_match
