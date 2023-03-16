"""Generate Parentheses 

LLETCODE: 22
COMPANY:  Amazon

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]

Solution
- We can base our logic from the following rules:
  ** we must have n open, n closed brackets
  ** number of opening brackets must be higher 
     than closing bracket to close => close < open

- From the number initiaised with n, we use that in our logic
  to calculate the maximum number of open & closed brackets
  are allowed; then to make the brackets we detarmine how 
  many open brackets there are and then and a closing bracket.

How It Works
- Lets say we initialise n to 3.
- The logic starts with an empty list then creates an open bracket.
  [] => ["("]
- It now has a choice to create a closing bracket or another
  opening bracket. This is because it will calculate if the 
  number of closed brackets is less than opening brackets. 
  Because there is only one open bracket we can eitehr close 
  it or ad an extra bracket.

  o = open bracket
  c = closed brackets
  n = 3n 

  [] => ["("] => ["(("] , ["()"]
             1o < 3n : 1o +1
             0c < 1o : 0c +1

  ["(("] => ["((("], ["(()"]  |  ["()"] => ["()("]
        2o < 3n : 2o +1                1o < 3n : 1o +1
        0c < 2o : 0c +1

  ["((("] => ["((()"]         |  ["(()"] => ["(()("], ["(())"]  |  ["()("] => ["()(("], ["()()"]
        3o == 3n : 0c +1                2o < 3n : 2o +1                   2o < 3n : 2o +1
                                        1c < 2o : 1c +1                   1c < 2o : 1c +1

  ["((()"] => ["((())"]       |  ["(()("] => ["(()()"]          |  ["(())"] => ["(())("]          |  ["()(("] => ["()(()"]     |    ["()()"] => ["()()("]
        3o == 3n : 1c + 1              3o == 3n : 1c + 1                   2o < 3n : 2o +1                 3o == 3n : 1c + 1              2o < 3n : 2o +1  

  ["((())"] => ["((()))"]     |  ["(()()"] => ["(()())"]        |  ["(())("] => ["(())()"]        |  ["()(()"] => ["()(()"]    |    ["()()("] => ["()()()"]
         3o == 3n : 2c + 1              3o == 3n : 1c + 1                 3o == 3n : 1c + 1                 3o == 3n : 1c + 1              3o == 3n : 1c + 1

- Each matching combination is added to our result.
"""
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open paranthesis if open < n
        # only add a closing parenthesis if closed < open
        #  only valid if open == closed == n

        # create stack
        stack = []
        # list of result
        res = []

        # this is a recursive function
        def backtrack(openN, closedN):
            # check if open& closed brackets match n
            # this is our base case
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            # add open (
            if openN < n:
                stack.append("(")
                # update open bracket in backtrack() once added
                backtrack(openN + 1, closedN)
                # we pop the new item because backtrack() will regenerate list
                stack.pop()

            # add closed )
            if closedN < openN:
                stack.append(")")
                # update closed bracket in backtrack() once added
                backtrack(openN, closedN + 1)
                stack.pop()

        # initialise open & closed to 0
        backtrack(0, 0)
        return res


answer: Solution = Solution()

example1: int = 3
print(answer.generateParenthesis(example1))
# ['((()))', '(()())', '(())()', '()(())', '()()()']

example2: int = 1
print(answer.generateParenthesis(example2))
# ['()']

example3: int = 4
print(answer.generateParenthesis(example3))
# ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']


