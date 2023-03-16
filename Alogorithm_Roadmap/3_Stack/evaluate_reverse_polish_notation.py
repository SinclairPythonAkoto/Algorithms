"""Evaluate Reverse Polish Notation

LEETCODE: 150
COMPANY:  Amazon

You are given an array of strings tokens that represents an 
arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents 
the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse 
polish notation.
The answer and all the intermediate calculations can be 
represented in a 32-bit integer.

Input: tokens = ["2","1","+","3","*"]
Output: 9

Input: tokens = ["4","13","5","/","+"]
Output: 6

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22

Stack Solution
- Using a stack data structure is the easiest way to solve the
  problem.
- Each operation is applied to the previous index values, which
  is then updated to a new value for the result. That result is 
  then used if more operations are met in the list/stack.
- When we come across an operation we pop the previous values
  out from the list in order to complete the arithmetic operation.
- The result is then pushed back onto the stack, replacing the
  previous values.
- We repeat the same process when we come across another operator 
  in the list.
- The time complexity is O(n) because we are just reading through
  the list and then adding each value to the stack, then removing 
  it once we come across an operator, then replacing it with the 
  result value in a new index. This also means that the list/stack
  will always be valid (as in non empty).
"""
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # loop through list
        for c in tokens:
            if c == "+":
                # pop last values add result to stack
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                # pop last values in list
                a, b = stack.pop(), stack.pop()
                # add calculation to stack
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                # if not an operator its a number so 
                # convert str to int
                stack.append(int(c))
        return stack[0]


answer: Solution = Solution()

example1: List[int] = ["2","1","+","3","*"]
print(answer.evalRPN(example1))    # 9

example2: List[int] = ["4","13","5","/","+"]
print(answer.evalRPN(example2))    # 6

example3: List[int] = [
    "10","6","9","3","+","-11","*","/","*","17","+","5","+"
]
print(answer.evalRPN(example3))    # 22
