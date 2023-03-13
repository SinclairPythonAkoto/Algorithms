"""Valid Parentheses

LEETCODE:  20
COMPANY:  Facebook

Given a string s containing just the characters '(', ')',
 '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Stack & Hashmap Solution
- Create a hashmap of all the closing brackets. Each key should
  be the closing brackets.
- We should check for an opening bracket for the start of
  the string.  If this is false we can determine that the string
  is False; if there is an opening bracket, we can add more 
  opening brackets (as much as we want).
- Now we can check if the parentheses are correct by looking for
  the matching closing bracket in the string.  When there is a
  match we can remove the pair of brackets and search for the nex match.
- When there are no more brackets left we can return True because
  there are no more brackets to try and match (all open brackets
  are now closed).
- We use a stack data structure so we can keep adding a new open/closed
  bracket to the end of the list. A stack is also benificial 
  because we can pop (remove) the matching brackets from the 
  start/end of the list - in our solution it will be removed from the end. 
- To match every closing parentheses to it's opening bracket we
  create a hashmap (dictionary) - where each key-value pair will
  be closed-open brackets.

  KEY : VALUE
  ")" : "("
  "]" : "["
  "}" : "{"

  input = "[{()"

- In the example above we check the last string index type is
  the same as our initialised keys. If it the same, then we
  get the key's value and then check if the value is the same
  as the element BEFORE the last string. If it does then we 
  have a match and the match is removed.
- ")" would match the ")" key. We take the value "(" and check
  if it is equal to the previous index in the string. Because
  "(" is the matching element prior to ")" in the string, we
  can remove "()" because we have a match.
- We use this logic to complete the solution.  This will be 
  O(n) time & space complexity.
"""
from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        # create hashmap - map closing bracket to opening bracket
        Map = {")": "(", "]": "[", "}": "{"}
        # create stack
        stack = []

        for char in s:
            # check if it starts with end bracket
            if char not in Map:
                stack.append(char)
                continue
            # check if not matched with hashmap key
            if not stack or stack[-1] != Map[char]:
                return False
            # if there is a match (reduced else block)
            stack.pop()

        return not stack


answer: Solution = Solution()

example1: str = "()"
print(answer.isValid(example1))    # True

example2: str = "()[]{}"
print(answer.isValid(example2))    # True

example3: str = "(]"
print(answer.isValid(example3))    # False