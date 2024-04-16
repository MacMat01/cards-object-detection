import unittest

from camera_util.camera import Camera


class TestCamera(unittest.TestCase):
    """
    This class contains unit tests for the Camera class.
    The Camera class is part of a larger system that involves video capture using OpenCV.
    """

    def setUp(self):
        """
        This method is called before each test. It sets up the test environment.
        Here, it creates a new instance of the Camera class and opens the camera.
        """
        self.camera = Camera()
        self.camera.open()

    def test_camera_open(self):
        """
        This test checks if the camera is open.
        It asserts that the is_opened method of the Camera class returns True.
        This is to ensure that the camera opens correctly when the open method is called.
        """
        self.assertTrue(self.camera.is_opened())

    def test_camera_frame(self):
        """
        This test checks if the camera can read a frame.
        It reads a frame from the camera and asserts that the read was successful
        (ret is True) and the frame is not None.
        This is to ensure that the camera can successfully capture frames when the read_frame method is called.
        """
        ret, frame = self.camera.read_frame()
        self.assertTrue(ret)
        self.assertIsNotNone(frame)

    def tearDown(self):
        """
        This method is called after each test. It cleans up the test environment.
        Here, it closes the camera by calling the close method of the Camera class.
        This is to ensure that the camera closes correctly when the close method is called.
        """
        self.camera.close()


if __name__ == '__main__':
    """
    This is the entry point for the script. It calls unittest.main(), which runs all the tests in this file.
    This is a standard Python idiom for making a script executable as well as importable as a module.
    """
    unittest.main()
