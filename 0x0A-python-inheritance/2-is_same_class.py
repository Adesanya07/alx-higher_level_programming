#!/usr/bin/python3

"""a function that checks if the class is exact with the object"""

def is_same_class(obj, a_class):
     """Return true if object is an instance of the
     class, otherwise return false
     """
     if type(obj) == a_class:
        return True
     else:
        return False