#! /usr/bin/python

# Filename:    6_gamer_farzad.py
# Description: Solution to <Series 1 - Problem 6>
# Author:      Ali Mousavi <ali.mousavi@gmail.com>
# Instructor:  Mr. Ali Rezaee
# Date:        2018/10/25
import sys


def multiply_matrix(first_matrix, second_matrix):
    """Multiplies two matrices

    Keyword arguments:
    first-matrix: tuple of tuples representing the first matrix
    second-matrix: tuple of tuples representing the second matrix

    returns None or tuple of tuples representing the result of mulitplication
    """
    if len(first_matrix[0]) != len(second_matrix):
        print('Incompatible matrices for mulitplication', file=sys.stderr)
        raise ValueError
    result = []
    for f_row in range(len(first_matrix)):
        result.append([])
        for s_col in range(len(second_matrix[0])):
            elem = 0
            for f_col in range(len(first_matrix[f_row])):
                elem += (first_matrix[f_row][f_col]
                         * second_matrix[f_col][s_col])
            result[f_row].append(elem)
    return tuple(result)


def matrix_determinant(matrix):
    """Recursive function to calculate and return the determinant of a matrix

    Keyword arguments:
    matrix -- the matrix to calculate its determinant

    returns number
    """
    if len(matrix) != len(matrix[0]):
        print('Incompatible dimensions for calculating determinant.')
        raise ValueError

    if len(matrix) == 1:  # base case to terminate recursion
        return matrix[0][0]

    determinant = 0
    # iterate on the first row to find cofactors
    for idx, elem in enumerate(matrix[0]):
        determinant += ((-1) ** (2 + idx) * elem
                        * matrix_determinant(
                            [row[0:idx] + row[idx + 1:] for row in matrix[1:]]
                        ))

    return determinant


def input_square_matrix(dimension):
    """Takes data from the user and returns a matrix

    Keyword arguments:
    dimension -- the dimension of the matrix

    returns tuple of tuples representing the matrix.
    """

    SUFFIXES = ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th']
    matrix = []
    for row_number in range(dimension):
        # try 3 times to get each row.
        for idx in range(3):
            try:
                row_string = input(
                    'Enter the {0}{1} row (separate elements with space): '
                    .format(row_number + 1, SUFFIXES[row_number + 1 % 10])
                )
                row = [int(elem) for elem in row_string.split()]
                # Check if it is a square matrix
                if len(row) != dimension:
                    print(
                        'Row length doesn\'t match the dimension.',
                        file=sys.stderr
                    )
                    raise ValueError
                matrix.append(row)
            except ValueError:
                print(
                    'You did not provide valid information.',
                    file=sys.stderr
                )
            else:
                break
        else:
            print('You seem not to be able to provide a row.', file=sys.stderr)
            raise ValueError

    return tuple(matrix)


if __name__ == '__main__':
    try:
        # try 3 times to get the dimension from the users
        for idx in range(3):
            try:
                dimension = int(input(
                    "Please enter dimensions of this matrices: ")
                )
                if dimension <= 0:
                    raise ValueError
            except ValueError:
                print('You need to provide a positive integer.',
                      file=sys.stderr)
            else:
                break
        else:
            print('You did not enter a valid dimension size.', file=sys.stderr)
            raise ValueError

        print('---- First Matrix ----')
        first_matrix = input_square_matrix(dimension)
        print('---- Second Matrix ----')
        second_matrix = input_square_matrix()
        result = multiply_matrix(first_matrix, second_matrix)
        if matrix_determinant(result) % 2:
            print('Danial')
        else:
            print('Farzad')
    except ValueError:
        sys.exit(1)

    # matrix = [
    #     [4, 6],
    #     [3, 8]
    # ]  # determinant = -14
    #
    # matrix_2 = [
    #     [1, 2, 3, 4, 1],
    #     [0, -1, 2, 4, 2],
    #     [0, 0, 4, 0, 0],
    #     [-3, -6, -9, -12, 4],
    #     [0, 0, 1, 1, 1]
    # ]   # determinant = 28
    #
    # print(matrix_determinant(matrix_2))
