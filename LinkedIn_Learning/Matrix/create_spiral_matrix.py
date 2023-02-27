# create a function that builds a spiral matrix
from typing import List

def spiral_matrix(num: int) -> List[List[int]]:
    matrix: List[List[int]] = [[0] * num for _ in range(num)] # create a matrix of size n x n filled with zeros
    row_start: int = 0 # initialize the starting row
    row_end: int = num - 1 # initialize the ending row
    col_start: int = 0 # initialize the starting column
    col_end: int = num - 1 # initialize the ending column
    count: int = 1 # initialize the starting value to be filled in the matrix

    while row_start <= row_end and col_start <= col_end:
        # fill the top row
        for index in range(col_start, col_end+1):
            matrix[row_start][index] = count
            count += 1
        row_start += 1

        # fill the right column
        for index in range(row_start, row_end+1):
            matrix[index][col_end] = count
            count += 1
        col_end -= 1

        # fill the bottom row
        if row_start <= row_end:
            for index in range(col_end, col_start-1, -1):
                matrix[row_end][index] = count
                count += 1
            row_end -= 1

        # fill the left column
        if col_start <= col_end:
            for index in range(row_end, row_start-1, -1):
                matrix[index][col_start] = count
                count += 1
            col_start += 1

    return matrix

print(spiral_matrix(3))