#!/usr/bin/python3
# 8-uppercase.py
# Gabriel Adesanya <Adesanya07>


def uppercase(str):
    """Print a string in uppercase."""
    for c in str:
        if ord(c) >= 65 and ord(c) <= 90:
            print("{}".format(c), end="")
            print("")