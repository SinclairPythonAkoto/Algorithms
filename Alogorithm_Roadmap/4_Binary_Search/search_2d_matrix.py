"""Search A 2D Matrix

LEETCODE: 74
COMPANY:  Microsoft / Windows

You are given an m x n integer matrix matrix with the following 
two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer 
of the previous row.
Given an integer target, return true if target is in matrix 
or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Double Binary Search Solution
- We do a binary search on every last number in each list,
  and check if its higher than the target number. If it is
  we move onto the next list.
- We also search every first number in the list and check if
  it is lower than the target.  It if it lower then we move
  back to the previous list.
- Once the search finds the list then we do another binary search
  on the selected list. If the target is not found we return
  False, if the target is found we return True.

  

"""
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top_row = 0
        bottom_row = ROWS - 1
        while top_row <= bottom_row:
            row = (top_row + bottom_row) // 2
            if target > matrix[row][-1]:
                top_row = row + 1
            elif target < matrix[row][0]:
                bottom_row = row - 1
            else:
                break

        if not (top_row <= bottom_row):
            return False
        row = (top_row + bottom_row) // 2

        left_pointer = 0
        right_pointer = COLS - 1
        while left_pointer <= right_pointer:
            mid = (left_pointer + right_pointer) // 2
            if target > matrix[row][mid]:
                left_pointer = mid + 1
            elif target < matrix[row][mid]:
                right_pointer = mid - 1
            else:
                return True
        return False


answer: Solution = Solution()

example1: List[List[int]] = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(answer.searchMatrix(example1, target=3))     # True

example2: List[List[int]] = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(answer.searchMatrix(example2, target=13))    # False