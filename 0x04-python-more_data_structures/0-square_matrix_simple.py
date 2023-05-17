#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
  """
  Computes the square value of all integers of a matrix.

  Args:
    matrix: A 2D array.

  Returns:
    A new matrix with the same size as the input matrix, where each value is the square of the corresponding value in the input matrix.
  """

  return [list(map(lambda a: a**2, row)) for row in matrix]



   
        
