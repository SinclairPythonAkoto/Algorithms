"""Daily Temperatures

LEETCODE: 739
COMPANY:  Facebook

Given an array of integers temperatures represents the daily 
temperatures, return an array answer such that answer[i] is 
the number of days you have to wait after the ith day to get 
a warmer temperature. If there is no future day for which this 
is possible, keep answer[i] == 0 instead.

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Input: temperatures = [30,60,90]
Output: [1,1,0]

Solution
- Monotonic Decreasing Order stack (the stack will always be in
  decreasing order) could be used to efficiently solve the problem.
- We create a stack then loop through each item in the list. We 
  check if the list item is less than the last item in the stack
  before it is appended to the stack.
- If the list item is less than the last value in the stack, we
  append the value to the end of the stack. 
- If the list item is higher than last value of the stack, we pop
  the smallest value from the stack until the list item is lower
  than the last value in the stack.
- This will make the efficiency of the code 

  list: 73, 72, 71, 73, 74

  stack: 73
         73, 72
         73, 72, 71
         73, 72
         73
         73, 73
         73
         74

  temp   =  [73,74,75,71,69,72,76,73]
  stack  =  [73,--,--,--,--,--,--,--]
  output =  [--,--,--,--,--,--,--,--]

  temp   =  [73,74,75,71,69,72,76,73]
  stack  =  [--,74,--,--,--,--,--,--] 
  output =  [ 1,--,--,--,--,--,--,--]  =>  74 index - 73 index

  temp   =  [73,74,75,71,69,72,76,73]
  stack  =  [--,--,75,--,--,--,--,--]
  output =  [ 1, 1,--,--,--,--,--,--]  =>  75 index - 74 index

  temp   =  [73,74,75,71,69,72,76,73]
  stack  =  [--,--,75,71,--,--,--,--]  =>  71 is smaller than 75 so we add value to stack
  output =  [ 1, 1,--,--,--,--,--,--]

  temp   =  [73,74,75,71,69,72,76,73]
  stack  =  [--,--,75,71,69,--,--,--]  
  output =  [ 1, 1,--,--,--,--,--,--]

  temp   =  [73,74,75,71,69,72,76,73]
  stack  =  [--,--,75,71,--,72,--,--]  
  output =  [ 1, 1,--,--, 1,--,--,--]  =>  72 index - 69 index


  temp   =  [73,74,75,71,69,72,76,73]
  stack  =  [--,--,75,--,--,72,--,--]  
  output =  [ 1, 1,--, 2, 1,--,--,--]  =>  72 index - 71 index

  temp   =  [73,74,75,71,69,72,76,73]
  stack  =  [--,--,75,--,--,--,76,--]  
  output =  [ 1, 1,--, 2, 1, 1,--,--]  =>  76 index - 72 index

  temp   =  [73,74,75,71,69,72,76,73]
  stack  =  [--,--,--,--,--,--,76,--]  
  output =  [ 1, 1, 4, 2, 1, 1,--,--]  =>  76 index - 75 index

  temp   =  [73,74,75,71,69,72,76,73]
  stack  =  [--,--,--,--,--,--,76,73]  
  output =  [ 1, 1, 4, 2, 1, 1,--,--]

  temp   =  [73,74,75,71,69,72,76,73]
  stack  =  [--,--,--,--,--,--,76,73]  
  output =  [ 1, 1, 4, 2, 1, 1, 0, 0]  =>  add 0 as default if no higher number found
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # create a list of default 0s
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for index, temp in enumerate(temperatures):
            # check if temp higher than last value in stack
            while stack and temp > stack[-1][0]:
                # remove the tuple
                # tuple unpacking to pop index & temp
                stackT, stackInd = stack.pop()
                # update the results list
                res[stackInd] = index - stackInd
            # add to stack if numbers are lower than the previous
            stack.append((temp, index))
        return res


answer: Solution = Solution()

temp1: List[int] = [73,74,75,71,69,72,76,73]
print(answer.dailyTemperatures(temp1))
# [1, 1, 4, 2, 1, 1, 0, 0]

temp2: List[int] = [30,40,50,60]
print(answer.dailyTemperatures(temp2))
# [1, 1, 1, 0]

temp3: list[int] = [30,60,90]
print(answer.dailyTemperatures(temp3))
# [1, 1, 0]