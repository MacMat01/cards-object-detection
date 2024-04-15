import unittest

from card import Card


class TestCard(unittest.TestCase):
    """
    This class contains unit tests for the Card class.
    """

    def setUp(self):
        """
        This method is called before each test. It sets up the test environment.
        Here, it creates a new instance of the Card class.
        """
        self.card = Card()

    def test_card_face(self):
        """
        This test checks the detect_face method of the Card class.
        It compares the result of the method with an expected result.
        The method is supposed to take an image or a camera feed as input and return the detected face of the card.
        """
        image_or_feed = 'path_to_your_test_image_or_feed'
        expected_face = 'expected_face_value'
        self.assertEqual(self.card.detect_face(image_or_feed), expected_face)

    def test_card_back(self):
        """
        This test checks the detect_back method of the Card class.
        It compares the result of the method with an expected result.
        The method is supposed to take an image or a camera feed as input and return the detected back of the card.
        """
        image_or_feed = 'path_to_your_test_image_or_feed'
        expected_back = 'expected_back_value'
        self.assertEqual(self.card.detect_back(image_or_feed), expected_back)


if __name__ == '__main__':
    """
    This is the entry point for the script. It calls unittest.main(), which runs all the tests.
    """
    unittest.main()
