"""Find Minimum in Rotated Sorted Array

LEETCODE: 153
COMPANY:  Facebook

Suppose an array of length n sorted in ascending order is 
rotated between 1 and n times. For example, the array 
nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., 
a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, 
return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Input: nums = [3,4,5,1,2]
Output: 1

Input: nums = [4,5,6,7,0,1,2]
Output: 0

Input: nums = [11,13,15,17]
Output: 11

Solution
- When we say we are rotating the number we are saying that we
  are taking the n numbers from the end of the list and place
  them at the beginning of the list.
- This means when we rotate sorted values in a list, we will
  always have the highest numbers on the left side of the
  list, and the smallest numbers will be on the right side.
- This makes it easier when we conduct a binary search; to find
  the smallest values we can search from the right side of the 
  list after finding the middle value.
- We check if the middle value is greater or equal to the left 
  pointer, if it is that means the middle value is part of the 
  higher end of the sorted list.  If it is lower, then it means
  the middle value is a part of the lower sorted list. 

  nums = [3, 4, 5, 1, 2]    res = 5
          L     M     R
  M = (L + R)// 2

  if nums[M] >= nums[L]:
      search right
  else:
      search left
  nums = [3, 4, 5, 1, 2]    res = 1
                   L  R
                   M

"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # create pointers
        start = 0 
        end = len(nums) - 1 
        curr_min = float("inf")
        
        while start  <  end :
            mid = (start + end ) // 2
            # update new curr_min
            curr_min = min(curr_min,nums[mid])
            
            # right has the min 
            if nums[mid] > nums[end]:
                start = mid + 1
                
            # left has the  min 
            else:
                end = mid - 1 
                
        return min(curr_min,nums[start])


answer: Solution = Solution()

example1: List[int] = [3,4,5,1,2]
print(answer.findMin(example1))    # 1

example2: List[int] = [4,5,6,7,0,1,2]
print(answer.findMin(example2))    # 0

example3: List[int] = [11,13,15,17]
print(answer.findMin(example3))    # 11