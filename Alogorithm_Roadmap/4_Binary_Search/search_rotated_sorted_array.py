"""Search In Rotated Sorted Array

LEETCODE: 33
COMPANY:  Google

There is an integer array nums sorted in ascending order 
(with distinct values).

Prior to being passed to your function, nums is possibly 
rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is
 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer 
target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1

Solution
- We conduct our binary search by creating our L & R pointers,
  then calculate the middle value M.
- We then check if M is equal to the target, if its not then we
  check if M is greater or equal to L. This will tell us if M
  belongs in the left or right portion of the list.
- If it is in the left portion, we check if L is equal to
  our target. If it is not, we check if L is less or greater 
  than the target.
- If L is greater than the target we shift the pointer to the
  right side of M.  We repeat the process untill we find a match
  or return -1 if a match is not found.
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            mid = (left_pointer + right_pointer) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[left_pointer] <= nums[mid]:
                if target > nums[mid] or target < nums[left_pointer]:
                    left_pointer = mid + 1
                else:
                    right_pointer = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[right_pointer]:
                    right_pointer = mid - 1
                else:
                    left_pointer = mid + 1
        return -1


answer: Solution = Solution()

example1: List[int] = [4,5,6,7,0,1,2]
print(answer.search(example1, target=0))    # 4

example2: List[int] = [4,5,6,7,0,1,2]
print(answer.search(example2, target=3))    # -1

example3: List[int] = [1]
print(answer.search(example3, target=0))    # -1