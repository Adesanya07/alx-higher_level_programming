#!/usr/bin/python3

"""checks if object is an instance of a class
or an inherited class
"""

def is_kind_of_class(obj, a_class):
      """returns true if object is an instance of a class
    or a class that the class in question inherits from
    """
      if isinstance(obj, a_class):
            return True
      else:
            return False