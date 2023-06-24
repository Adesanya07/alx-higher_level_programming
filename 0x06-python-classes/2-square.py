#!/usr/bin/python3


"""creating a class module """

class Square:
    """creating a method next"""
    def __init__(self, size=0):
        """checking if size is an integer"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        """checking if size is less greater than 0"""
        if size < 0:
            raise ValueError("size must be >= 0")
        