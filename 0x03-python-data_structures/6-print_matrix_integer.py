#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            if not row:
                print()
            for column in row:
                if column == row[len(row) - 1]:
                    print("{:d}".format(column), end="\n")
                else:
                    print("{:d}".format(column), end=" ")
