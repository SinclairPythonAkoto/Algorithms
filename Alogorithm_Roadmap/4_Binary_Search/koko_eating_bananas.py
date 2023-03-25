"""Koko Eating Bananas

LEETCODE: 875
COMPANY:  Google

Koko loves to eat bananas. There are n piles of bananas, the 
ith pile has piles[i] bananas. The guards have gone and will 
come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each 
hour, she chooses some pile of bananas and eats k bananas from 
that pile. If the pile has less than k bananas, she eats all 
of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all 
the bananas before the guards return.

Return the minimum integer k such that she can eat all the 
bananas within h hours.

Input: piles = [3,6,7,11], h = 8
Output: 4

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Input: piles = [30,11,23,4,20], h = 6
Output: 23


Solution
- We find the maximum value from the piles list and then use
  that value to create a range. The left pointer will start from
  1, and the right pointer will be the maximum value.
- We use the range to caluclate the value k by iterating through the
  range and dividing each index by the piles index, 
  then sum the values to see if its greater or lower 
  than the number of hours.
- We use the L & R pointers to iterate from the start and end of the range.
  We add the L + R pointer togther then divide by 2 to get the middle value.
  If the sum is lower then we move the R pointer to the middle position, if
  the sum is higher then we move the L pointer intead.

  piles = [3, 6, 7, 11]
  H = 8

  # create L & R pointers
  L = 1
  R = max(piles)

  # now use pointers to binary search
  k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
       L              k               R

       (L + R) // 2 = k  =>  (1 + 11) // 2 = 6 

       piles[n] / k = result (to nearest number)
       (3/6 = 1) + (6/6 = 1) + (7/6 = 2) + (11/6 = 2) = 6

  k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
       L     k     R

       (L + R) // 2 = k  =>  (1 + 5) // 2 = 3
       
       piles[n] / k = result (to nearest number)
       (3/3 = 1) + (6/3 = 2) + (7/3 = 3) + (11/3 = 4) = 10

  k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
                L  R
                k

       (L + R) // 2 = k  =>  (4 + 5) // 2 = 4

       piles[n] / k = result (to nearest number)
       (3/4 = 1) + (6/4 = 2) + (7/4 = 2) + (11/4 = 3) = 8

  k = 4
"""
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left_pointer = 1
        right_pointer = max(piles)
        res = max(piles)

        while left_pointer <= right_pointer:
            k = (left_pointer + right_pointer) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)
            if totalTime <= h:
                res = min(res, k)
                # check previous number from R pointer
                right_pointer = k - 1
            else:
                # check next L pointer if res over hours
                left_pointer = k + 1
        return res


answer: Solution = Solution()

example1: List[int] = [3,6,7,11]
print(answer.minEatingSpeed(example1, h=8))

example2: List[int] = [30,11,23,4,20]
print(answer.minEatingSpeed(example2, h=5))

example3: List[int] = [30,11,23,4,20]
print(answer.minEatingSpeed(example3, h=6))