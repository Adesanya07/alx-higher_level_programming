#!/usr/bin/python3

"""
testing dpython docstrings
"""

class Square:
    """class has a size instant property"""
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    @property
    def position(self):
        """return the position of the square"""
        return self.__position
    @size.setter
    def position(self, value):
       """size must have 2 positive integers """
       if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
       elif not all(isinstance(x, int) for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
       elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
       else:
            self.__position = value


    def area(self):
        return self.__size ** 2
    
    def my_print(self):
        if self.__sizesize == 0:
            print()
        else:
            for i in range(self.__position[1]):
             print()
            for k in range(self.__position[0]):
                    print(" ", end='')
                    for j in range(self.__size):
                        print("#", end="")
                    print()
