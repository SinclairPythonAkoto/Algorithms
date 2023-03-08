"""Two Sum II Input Array Is Sorted

LEETCODE: 167
COMPANY: Amazon

Given a 1-indexed array of integers numbers that is already 
sorted in non-decreasing order, find two numbers such that 
they add up to a specific target number. Let these two numbers 
be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, 
added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. 
You may not use the same element twice.

Your solution must use only constant extra space.

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Input: numbers = [2,3,4], target = 6
Output: [1,3]

Input: numbers = [-1,0], target = -1
Output: [1,2]

Brute Force With Pointers
- If we use a pointer to mark the beginning and ending of the
  list, we can then we can use the sorted list to check if
  the two pointers are equal to the target number.
- If the right pointer (the one at the end), is higher than the
  target, we can then move the pointer to the left and redo 
  the sum with the new values.
- If the new sum is lower than the target then we move the left 
  pointer to the right. When we move the left pointer we 
  recalculate the sum, if it is higher than the target we move
  the right pointer to the left; if it is lower than the target
  then we move the left pointer to the right.
- To move the right pointer to the left we subtract 1 from the 
  pointers index.
- To move the left pointer to the right we plus 1 to the 
  pointers index.
"""
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # create left & right pointers for start & end
        left_pointer = 0
        right_pointer = len(numbers) - 1

        while left_pointer < right_pointer:
            curSum = numbers[left_pointer] + numbers[right_pointer]

            # if sum bigger than target shift right pointer to the left
            if curSum > target:
                right_pointer -= 1
            # if sum less than target shift left pointer to the right
            elif curSum < target:
                left_pointer += 1
            else:
                # we +1 to return true index
                return [left_pointer + 1, right_pointer + 1]


answer: Solution = Solution()

example1: List[int] = [2,7,11,15]
target = 9
print(answer.twoSum(example1, target))    # [1, 2]

example2: List[int] = [2,3,4] 
target = 6
print(answer.twoSum(example2, target))    # [1, 3]

example3: List[int] = [-1,0]
target = -1
print(answer.twoSum(example3, target))    # [1, 2]