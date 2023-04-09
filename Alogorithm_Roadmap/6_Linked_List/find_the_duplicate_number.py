"""Find The Duplicate Number

LETTCODE: 237
COMPANY:  Amazon

Given an array of integers nums containing n + 1 integers where each integer 
is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only 
constant extra space.

Input: nums = [1,3,4,2,2]
Output: 2

Input: nums = [3,1,3,4,2]
Output: 3


Solution
- To complete this challenge we need to break it down into 2x phases.
- Phase 1: Create a fast & slow pointer to traverse the linked lists.
           When the two pointers meet, we stop the loop and return the slow pointer.
- Phase 2: Create a second slow pointer and use both slow1 & slow2 pointers
           to traverse the linked lists.  If the two pointers meet,
           we can return the duplicate.
- For this solution to work you must recognise that a linked list cycle solution
  would be needed to solve the first half of the challenge..
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # create pointers
        slow, fast = 0, 0

        # phase 1
        while True:
            slow = nums[slow]          # 1 step
            fast = nums[nums[fast]]    # 2 step
            if slow == fast:
                break

        # phase 2
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


answer: Solution = Solution()

example1: List[int] = [1, 3, 4, 2, 2]
print(answer.findDuplicate(example1))    # 2

example2: List[int] = [3, 1, 3, 4, 2]
print(answer.findDuplicate(example2))    # 3