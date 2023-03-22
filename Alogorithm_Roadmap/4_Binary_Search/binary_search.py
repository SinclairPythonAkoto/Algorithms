"""Binary Search

LEETCODE: 704
COMPANY:  Windows / Microsoft

Given an array of integers nums which is sorted in 
ascending order, and an integer target, write a function 
to search target in nums. If target exists, then return its 
index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1


Solution
- A binary search is when you take the left and right index
  and divide it by two. We check if the answer matches our 
  target, if it does the search stops. 
- If our answer is not found we remove all the previous index 
  values and repeat the process until a macth is found or when
  the right index & left index cross over.

  target = 3

  [-1, 0, 3, 5, 9, 12]
   L      M         R           M = L + ((R - L) // 2)

- We create our left and right pointers then calculate the
  middle index by taking the left index away from the right 
  index then dividing the number by 2 (to nearest number).
  Same as:

  -1 + ((5 + 0) // 2)
  
  5 + 0 = 5 // 2 = -1 + 2.5 = 1.5 = 2 (index) = 3 (M value)

- Now we can check if the value of M matches our target.
  If the value does not match we remove all the preceeding
  values from M from the list; the left pointer is also 
  updated to the position of M simply by changing the 
  value of L to:

  L = M + 1

- We add 1 because we want the right index to be the index
  after M (as the M value is no longer needed).

  [-1, 0, 3, 5, 9, 12]
             L  M   R 
  
  5 + ((5 + 3) // 2)

- Now we can check if the value M matches the result and 
  return the list index.

"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1


answer: Solution = Solution()

example1: List[int] = [-1, 0, 3, 5, 9, 12]
target1: int = 9
print(answer.search(example1, target1))    # 4

example2: List[int] = [-1, 0, 3, 5, 9, 12]
target2: int = 2
print(answer.search(example2, target2))    # -1