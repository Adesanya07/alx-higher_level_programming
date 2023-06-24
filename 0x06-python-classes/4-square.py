#!/usr/bin/python3

"""creating a class """

class Square:
    """creating a attribute"""
    __size = 0
    """creating a property getter"""
    @property
    def size(self):
        return self.__size
    

    """creating the property setter"""


    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integers")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __init__(self, size=0):
        if  not isinstance(size, int):
            raise TypeError("size must be an integers")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2