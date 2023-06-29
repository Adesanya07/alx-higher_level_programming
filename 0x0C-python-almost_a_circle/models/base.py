#!/usr/bin/python3

"""this is a base model"""

class Base:
    __nb_objects = 0
    """creating a method"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects