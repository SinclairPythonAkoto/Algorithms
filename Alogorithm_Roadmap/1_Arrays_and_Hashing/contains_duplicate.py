"""Contains Dupliacte

LEETCODE: 217
COMPANY: Microsoft

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true

- We need to check if there are any duplicates in the list, and return True if we find 
  at least one duplicate.
- If there are no duplicates in the list then we return False.
- We could use brute force and check if each element is a duplicate; this would be 
  O(n^2) time complexity - becuase we check against the rest of the elements for a 
  ducplicate and use the same method for every single element.
- We could sort the elements in the list then run a loop to check if there are
  duplicates. An algorithm like this would be O(nlogn) and the space/memory would be O(1).
- We can also create a hash set to check if there are duplicates in the hash set.
  If there is a duplicate in the set it will return True. This will be done in a single loop
  so the complexitity will be O(n) and the space/memory will be O(n) becuase we creates the hash set.
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a hashset
        hashset = set()

        # run a loop to check for duplicates
        for element in nums:
            # check if number is in the hash set
            if element in hashset:
                return True
            # add to set if no number found
            hashset.add(element)
        return False

answer: Solution = Solution()

example1: List[int] = [1, 2, 3, 1]
example2: List[int] = [1, 2, 3, 4]
example3: List[int] = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

print(answer.containsDuplicate(example1))    # True
print(answer.containsDuplicate(example2))    # False
print(answer.containsDuplicate(example3))    # True

# Time: O(n)
# Space: O(n)
# Company: Microsoft