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
- 
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
                right_pointer = k - 1
            else:
                left_pointer = k + 1
        return res


answer: Solution = Solution()

example1: List[int] = [3,6,7,11]
print(answer.minEatingSpeed(example1, h=8))

example2: List[int] = [30,11,23,4,20]
print(answer.minEatingSpeed(example2, h=5))

example3: List[int] = [30,11,23,4,20]
print(answer.minEatingSpeed(example3, h=6))