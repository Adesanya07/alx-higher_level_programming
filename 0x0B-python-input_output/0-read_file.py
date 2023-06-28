#!/usr/bin/python3

"""opening a file """

def read_file(filename=""):
    """writing a function that opens a file"""
    with open(filename, "r", encoding="UTF8") as file:
        print(file.read(), end="")