#!/usr/bin/python3

def max_integer(my_list=[]):
    for a in my_list:
        if not my_list :
            return None
        
        max_integer = my_list[0]
        if max_integer > a:
            max_integer = a
        return max_integer
