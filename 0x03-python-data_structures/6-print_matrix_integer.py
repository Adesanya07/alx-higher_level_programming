#!/usr/bin/python3
# 6-print_matrix_integer.py


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            print("{:d}".format(column), end=" " if column != row[-1] else "")
        print()
  

           
           

  