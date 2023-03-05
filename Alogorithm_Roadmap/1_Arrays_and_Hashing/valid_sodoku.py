"""Valid Sudoku

LEETCODE: 36
COMPANY: Amazon

Determine if a 9 x 9 Sudoku board is valid. 
Only the filled cells need to be validated according 
to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain 
the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not 
necessarily solvable.
Only the filled cells need to be validated according to the 
mentioned rules.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false

Hashset Solution
- Each row must have values from 1-9.
- Each column must have values from 1-9.
- Each 3x3 grid also must have number from 1-9.
- The best way to solve this problem is with a hashset.
- We will use a hashset for each row, column & 3x3 grid
  to check for duplicates.
- Remember sets don't store duplicates
- To calculate the 3x3 grids correctly, we use the indexes of
  both the row and column to create an iterator for the grid.
  Like a graph, the rows will be the Y axis and, the column will 
  be the X axis.  Each number pair will signify a number, with
  a loop we can easily check if the same number appears and we 
  know if its a valid sudoku board or not.
- To be able to map the board game we would have to create two
  lists, one to map the rows and the other to map the columns.
  i.e 
  game_rows = [0, 1, 2]
  game_columns = [0, 1, 2]
  grid1 = game_rows[0], game_columns[0]  # 1st 3x3 gird
- We take the index numbers and then divide them by 3 to get 
  the number on the grid (we have to round it down)
- To find the correct grid for each number, we take the X and Y 
  numbers and divide both of them by 3 (integer divison).  
  This will give you the coordinates for the 3x3 grid.
"""
import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create hashset for board row, column & grid
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        # loop each row
        for r in range(9):
            # loop each column
            for c in range(9):
                # check if no number
                if board[r][c] == ".":
                    continue
                if (
                    # check if value in current row
                    board[r][c] in rows[r]
                    # check if value in column
                    or board[r][c] in cols[c]
                    # check if number in 3x3 grid
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                # add numbers if no duplicate found
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
    

answer: Solution = Solution()

game1: List[str] = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(answer.isValidSudoku(game1))    # True


game2: List[str] = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(answer.isValidSudoku(game2))    # False

# Time: O(n)
# Space: O(1)