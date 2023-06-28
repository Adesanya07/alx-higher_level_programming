#!/usr/bin/python3


"""writing a module that writes a string  to a file """

def write_file(filename="", text=""):
    """creating the function for the string"""
    with open(filename, "w", encoding="utf-8")as f:
        return f.write(text)
    
    