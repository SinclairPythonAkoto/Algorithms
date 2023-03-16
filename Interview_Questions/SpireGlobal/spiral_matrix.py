"""Spiral Matrix

LEETCODE: 54
COMPANY:  Microsoft, Spire Global

Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        # need to be tuples to check values against each other.
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every i in the top row
            for index in range(left, right):
                res.append(matrix[top][index])
            top += 1
            # get every i in the right col
            for index in range(top, bottom):
                res.append(matrix[index][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            # get every i in the bottom row
            for index in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][index])
            bottom -= 1
            # get every i in the left col
            for index in range(bottom - 1, top - 1, -1):
                res.append(matrix[index][left])
            left += 1

        return res


answer: Solution = Solution()

example1: List[int] = [[1,2,3],[4,5,6],[7,8,9]]
print(answer.spiralOrder(example1))
# [1, 2, 3, 6, 9, 8, 7, 4, 5]

example2: List[int] = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(answer.spiralOrder(example2))
# [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]