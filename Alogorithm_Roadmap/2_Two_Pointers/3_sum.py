"""3 Sum

LEETCODE: 15
COMPANY: Facebook

Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, 
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = [0,1,1]
Output: []

Input: nums = [0,0,0]
Output: [[0,0,0]]

Pointer Solution
- We first need to sort the list to make our solution work.
- Then we loop through the list twice in order to add the
  three elements.
- The first loop will start from the beginning of the list
  index, while the 2nd loop will select the left & right pointers.
- By creating pointer variables we can check the elements via
  their index and move the pointers by adding/subtracting 1.
- This reduces the time complexity to O(n^2).
- The space/memomry should be O(1) - it maybe O(n) in other 
  languages/libraries if the sorting takes up extra memory.
- This is basically the same pointer solution as Two Sum 1 & 2
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create result list
        res = []
        # sort the list
        nums.sort()

        # use enumerate for loop
        for index, val in enumerate(nums):
            # Skip positive integers
            if val > 0:
                break

            # check if the same number as previous
            if index > 0 and val == nums[index - 1]:
                continue

            # create left & right pointers
            left_pointer = index + 1
            right_pointer =  len(nums) - 1
            while left_pointer < right_pointer:
                # create our 3sum target value to chekc against
                threeSum = val + nums[left_pointer] + nums[right_pointer]
                # move right pointer to the left if greater than 0
                if threeSum > 0:
                    right_pointer -= 1
                # move left pointer to the right if less than 0
                elif threeSum < 0:
                    left_pointer += 1
                # if equal to 0
                else:
                    # update result list
                    res.append([val, nums[left_pointer], nums[right_pointer]])
                    # update pointers
                    left_pointer += 1
                    right_pointer -= 1
                    # check if left pointer is not same as previous & lower than right pointer 
                    while nums[left_pointer] == nums[left_pointer - 1] and left_pointer < right_pointer:
                        left_pointer += 1
        return res


answer: Solution = Solution()

example1: List[int] = [-1,0,1,2,-1,-4]
print(answer.threeSum(example1))

example2: List[int] = [0,1,1]
print(answer.threeSum(example2))

example3: List[int] = [0,0,0]
print(answer.threeSum(example3))