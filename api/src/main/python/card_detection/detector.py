from abc import ABC, abstractmethod


class Detector(ABC):
    """
    This is an abstract base class that defines the interface for a detector.
    Any class that inherits from this class must implement the `detect_face` and `detect_back` methods.
    """

    @abstractmethod
    def detect_face(self, frame):
        """
        This is an abstract method that should be implemented by any class that inherits from Detector.
        The method should take a frame as input and return the detected face.

        Args:
            frame: The frame in which to detect the face.

        Returns:
            The detected face. The return type can be any type that makes sense for the specific implementation.
        """
        pass

    @abstractmethod
    def detect_back(self, frame):
        """
        This is an abstract method that should be implemented by any class that inherits from Detector.
        The method should take a frame as input and return the detected back of the card.

        Args:
            frame: The frame in which to detect the back.

        Returns:
            The detected back. The return type can be any type that makes sense for the specific implementation.
        """
        pass
