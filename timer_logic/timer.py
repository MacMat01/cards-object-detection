import time


class Timer:
    """
    The Timer class is used to measure elapsed time.
    It provides methods to start and stop a timer, 
    and to retrieve the currently running timer.
    It uses a class variable to keep track of the running timer.
    """

    running_timer = None  # Class variable to keep track of the running timer

    def __init__(self):
        """
        Initializes a new instance of the Timer class.
        The start_time attribute is set to None, 
        indicating that the timer has not yet started.
        """
        self.start_time = None

    @classmethod
    def start(cls):
        """
        Starts the running timer if it's not already running.
        It does this by creating a new Timer instance, 
        setting its start_time to the current time, and assigning it to the running_timer class variable. 
        It then returns the running timer.
        """
        if cls.running_timer is None:
            cls.running_timer = cls()
            cls.running_timer.start_time = time.time()
        return cls.running_timer

    def stop(self):
        """
        Stops the running timer.
        It first checks if the timer has started by checking if start_time is None. 
        If the timer hasn't started, it raises an exception.
        If the timer has started, it calculates the elapsed time 
        by subtracting the start_time from the current time,
        resets the start_time to None, and resets the running_timer 
        class variable to None.
        It then returns the elapsed time.
        """
        if self.start_time is None:
            raise Exception("Timer has not started. Call start() before stopping.")
        elapsed_time = time.time() - self.start_time
        self.start_time = None
        Timer.running_timer = None  # Reset the running timer when it's stopped
        return elapsed_time

    @classmethod
    def get_running_timer(cls):
        """
        Returns the currently running timer instance. It does this by simply returning the running_timer class variable.
        """
        return cls.running_timer
