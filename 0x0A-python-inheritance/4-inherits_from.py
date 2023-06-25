#!/usr/bin/python3

"""checks if object is an instance of a class that
inherited from the specified class or not"""

def inherits_from(obj, a_class):
     """Returns true if object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
    """
     
     if not isinstance(obj, a_class):
          return issubclass(obj, a_class)
     else:
          return False