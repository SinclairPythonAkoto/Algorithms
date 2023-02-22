from typing import List


def spiral_matrix(matrix: List[List[int]]) -> List[List[int]]:
    # check if list exist
    if not matrix:
        return []

    result: List[List[int]] = []
    rows: int = len(matrix)
    column: int = len(matrix[0])
    row_start: int = 0
    column_start: int = 0

    while row_start < rows and column_start < column:
        for index in range(column_start, column):
            result.append(matrix[row_start][index])
        row_start += 1

        for index in range(row_start, rows):
            result.append(matrix[index][column - 1])
        column -= 1

        if row_start < rows:
            for index in range(column - 1, column_start - 1, -1):
                result.append(matrix[rows - 1][index])
            rows -= 1

        if column_start < column:
            for index in range(rows - 1, row_start - 1, -1):
                result.append(matrix[index][column_start])
            column_start

    return result


nums: List[List[int]] = [[1,2,3], [4,5,6], [7,8,9]]

print(spiral_matrix(nums))
# Output: [1, 2, 3, 6, 9, 8, 7, 4, 4, 5]