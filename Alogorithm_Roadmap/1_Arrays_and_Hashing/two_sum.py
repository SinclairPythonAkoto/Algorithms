"""Two Sum

LEETCODE: 1
COMPANY: Facebook

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

- You are trying to find which two numbers in your list make up for 
  the target value.
- Instead of returning the numbers that are equal to the target value, 
  we return the index of the numbers within the list.
- A brute force algorithm could be used to loop through each element of 
  the list and then find which two indexes are equal to our target value.
  This would be O(n^2) time complexity.
- A hashmap can be where we add each element of the list to the hashmap, 
  then we check if we subtract the element from the target.  The difference 
  in value will give us the number which will be in list if both elements 
  are equal to the target.
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap to store values
        prevMap = {}  # val : index


        for index, num in enumerate(nums):
            # set the difference
            diff = target - num
            # check if difference is already in hashmap
            if diff in prevMap:
                return [prevMap[diff], index]    # return diff in hashmap & current index value
            # add new key-value pair to hashmap 
            prevMap[num] = index
        return


answer: Solution = Solution()

example1: List[int] = [2, 7, 11, 15]
target1 = 9
print('Example 1')
print(answer.twoSum(example1, target1))
example2: List[int] = [3, 2, 4]
target2 = 6
print('Example 2')
print(answer.twoSum(example2, target2))
example3: List[int] = [3,3]
target3 = 6
print('Example 3')
print(answer.twoSum(example3, target3))


# Output
# Example 1
# [0, 1]
# Example 2
# [1, 2]
# Example 3
# [0, 1]