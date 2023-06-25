#!/usr/bin/python3

"""
 this module inherits from a list

"""

class Mylist(list):
    """
    class that inherits from a list
    """

    def print_sorted(self):
        sorted_list = sorted(self)
        """sort the list in ascending order."""
        print(sorted_list)