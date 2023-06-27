#!/usr/bin/python3

"""writing a subclass"""

Rectangle = __import__('9-rectangle.py').Rectangle

class Square(Rectangle):
    """initializing the class"""

    def __init__(self, size):
        """Initialize a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size