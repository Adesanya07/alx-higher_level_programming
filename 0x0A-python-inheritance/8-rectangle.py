#!/usr/bin/python3

""" module subclass rectangle
"""

Basegeometry = __import__('7-base_geometry.py').Basegeometry

class Rectangle(Basegeometry):
    """rectangle that inherits from base geometry"""
    def __init__(self, width, height):
        Basegeometry.integer_validator(self, 'height', height)
        self.__height = height
        Basegeometry.integer_validator(self, 'width', width)
        self.__width = width
