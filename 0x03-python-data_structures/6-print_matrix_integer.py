#!/usr/bin/python3
# 6-print_matrix_integer.py


def print_matrix_integer(matrix=[[]]):
    if not isinstance(matrix, list):
     raise ValueError("matrix must be a list")

    for row in matrix:
       if not isinstance(row, list):
          raise ValueError("matrix must be a list of lists")

    for item in row:
      if not isinstance(item, int):
        raise ValueError("matrix must be a list of lists of integers")

    for row in matrix:
      print(' '.join(str(item) for item in row))
  
  

           
           

  