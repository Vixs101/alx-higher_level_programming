#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = map(lambda y: list(map(lambda x: x * x, y)), matrix)
    result = list(new_matrix)
    return result
