import unittest

from main.python.camera_util.camera import Camera


class TestCamera(unittest.TestCase):
    """
    The TestCamera class contains unit tests for the Camera class.
    """

    def setUp(self):
        """
        Set up for the tests.
        This method is called before each test.
        It initializes a Camera object and opens the camera.
        """
        self.camera = Camera()
        self.camera.open()

    def test_camera_open(self):
        """
        Test for the open method of the Camera class.
        It checks if the camera is opened after calling the open method.
        """
        self.assertTrue(self.camera.is_opened())

    def test_camera_frame(self):
        """
        Test for the read_frame method of the Camera class.
        It checks if the read_frame method returns a frame and if the frame is not None.
        """
        ret, frame = self.camera.read_frame()
        self.assertTrue(ret)
        self.assertIsNotNone(frame)

    def test_display_frame(self):
        """
        Test for the display_frame method of the Camera class.
        It checks if the display_frame method works without throwing an exception.
        """
        ret, frame = self.camera.read_frame()
        self.assertTrue(ret)
        self.assertIsNotNone(frame)

        # Test the display_frame method.
        # This is a bit tricky to test, as it involves user interaction (pressing 'q' to close the window).
        # For now, we'll just call the method and assume it works if no exception is thrown
        self.camera.display_frame(frame)

    def test_camera_close(self):
        """
        Test for the close method of the Camera class.
        It checks if the camera is closed after calling the close method.
        """
        self.camera.close()
        self.assertFalse(self.camera.is_opened())

    def tearDown(self):
        """
        Tear down for the tests.
        This method is called after each test.
        It closes the camera.
        """
        self.camera.close()


if __name__ == '__main__':
    unittest.main()
