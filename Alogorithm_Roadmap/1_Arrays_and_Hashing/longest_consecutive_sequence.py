"""Longest Consecutive Sequence

LEETCODE:  128
COMPANY:   Google

Given an unsorted array of integers nums, return the length 
of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Hashest Solution
- If we use the sorted() method we can solve the problem easily,
  but the time complexity would be O(nlogn)
  
  nums = [100, 4, 2, 200, 3, 1]
  sorted(nums) = 1, 2, 3, 4, 100, 200    O(nlogn)

- If we use a set we can then use that object to create sequences
  and count the length of each one.  
- We use the the hashset to loop through each element to 
  calculate a sequence.
- We calcuate each sequence by checking if the number behind, 
  and the number in front already exist in the set. 
- If it does, then it means that the value is part of a 
  sequence, and the iterator moves onto the next number 
  in the set.
- If it there is no existing previous value, then it means 
  the number is a start of a sequence. Then it checks if the
  number ahead exists; if it does it adds the number to 
  the sequence, if not the sequence ends.
- At the end of each sequence we can count the number of 
  elements/numbers in each one by calculating the length
  of each sequence.

nums = [100, 4, 200, 1, 3, 2]
setNums = set(nums)

  1 2 3 4     100     200     3x sequences
    4          1       1      (number of values)
  
    100 ->   # 1
    200 ->   # 1
    1 -> 2 -> 3 -> 4    # 4

- To find the starting value of the sequence, we have to check
  if the sequence has 'no left neighnour' - meaning does a number
  before exist (we can do this easily by subtracting 1).
- We find the proceeding value of the sequence by adding 1 to
  the value and checking if the number exists in the hashset.
- If the number DOES exist in the set, then we add it to the 
  sequence, and keep applying the same logic until the sequence
  stops or there no more values left.
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert list to hashset
        numSet = set(nums)
        # counter to keep track of longest sequence
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                # initialise length of each sequence
                length = 1
                # check if number ahead in set
                while (n + length) in numSet:
                    # increase length if it does
                    length += 1
                # Get the highest value between length & 
                # longest using max(). 
                longest = max(length, longest)
        return longest


answer: Solution = Solution()

example1: List[int] = [100,4,200,1,3,2]
print(answer.longestConsecutive(example1))   # 4

example2: List[int] = [0,3,7,2,5,8,4,6,0,1]
print(answer.longestConsecutive(example2))    # 9

