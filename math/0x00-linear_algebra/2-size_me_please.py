#!usr/bin/python3
"""This funciton calculates the shape of matrix"""
import numpy as np


def matrix_shape(matrix):
    """Function to calculate the shape"""

    row = len(matrix)
    column = len(matrix[0])

    print ("[{}, {}]".format(row, column))
