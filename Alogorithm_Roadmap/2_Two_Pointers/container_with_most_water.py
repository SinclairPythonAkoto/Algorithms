"""Container With Most Water

LEETCODE: 11
COMPANY:  Facebook & Google

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints 
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Input: height = [1,1]
Output: 1

Pointer Solution
- To find the max area we can use the two pointer technique
- A left & right pointer is placed at the start & end of the
  list, so we can use the values to calcuate the value.

  left_pointer * right_pointer = area

- We calculate the which pointer to move by finding the 
  smallest height (the lowest value) of the two pointers.
  Whichever pointer is the lowest is the pointer we move.
- With this logic, we can loop the list and use the pointers 
  to check each possible area to compute the highest value.
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # create left & right pointers
        left_pointer = 0 
        right_pointer = len(height) - 1
        # result value
        res = 0

        while left_pointer < right_pointer:
            # take away right & left pointer to get index of value as answer, then multiply..
            area = (right_pointer - left_pointer) * min(height[left_pointer], height[right_pointer])
            # update result - make sure each loop there is a max result
            res = max(res, area)
            # move pointers
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            elif height[right_pointer] <= height[left_pointer]:
                right_pointer -= 1
            # if equal we can do either left or right action
            # so no need to do else block here.  It will be
            # a repeated action of either the left or right pointer
        return res


answer: Solution = Solution()


example1: List[int] = [1,8,6,2,5,4,8,3,7]
print(answer.maxArea(example1))    # 49

example2: List[int] = [1, 1]
print(answer.maxArea(example2))    # 1