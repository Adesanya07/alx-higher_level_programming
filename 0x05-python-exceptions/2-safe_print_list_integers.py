#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for a in range(x):
            if isinstance(my_list[a], int):
                count += 1
                print(":{d}".format(my_list[a], end=""))
    except TypeError as er:
        print(er)
    else:
        print("")
        return count