"""Top K Frequent Elements

LEETCODE: 347
COMPANY: Amazon

Given an integer array nums and an integer k, return the k most 
frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]

- We can sort the element so the list and count how many times 
  the number is found in the list.
- We can use a hashmap and the Bucket Sort algorithim to use O(n) time & 
  space complexity.
- A bucket sort will take the list and count how many times the 
  number appears in the list.  This will take the list value
  and map it to the index in an empty list.
- To make the bucket sort algorithm more effiecient, the iterator
  will count the number of times the number appears in the list
  as a key, the value would be a list of numbers that match 
  the key-count.
- We make the algorithm O(n) complexity because we set the top 
  `k` to the length of the list. So we start at the end of the
  list (the highest value), and then work our way down. 
"""
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create hashmap to count each time number occurs in list
        count: dict = {}
        # create the array the same size as input list
        freq = [[] for index in range(len(nums) + 1)]

        # add matching iterator count to hashmap
        for val in nums:
            # list int (key) : count int (value)
            count[val] = 1 + count.get(val, 0)
            # how count is being looped:
            # {1: 1}
            # {1: 2}
            # {1: 3}
            # {1: 3, 2: 1}
            # {1: 3, 2: 2}
            # {1: 3, 2: 2, 3: 1}
            
        # for each item of hashmap we add the value to freq list
        for index,item in count.items():
            freq[item].append(index)
            # The loop will add each time the number
            # appears in its list index.
            # [[], [], [], [1], [], [], []]
            # [[], [], [2], [1], [], [], []]
            # [[], [3], [2], [1], [], [], []]

        res: List[int] = []
        # set range end to start, going backwards, reversed order (going backwards)
        for index in range(len(freq) - 1, 0, -1):
            # add values from freq object to results list
            for number_count in freq[index]:
                res.append(number_count)
                # check if the length of results match the value of k
                if len(res) == k:
                    return res

        # O(n)


answer: Solution = Solution()
nums = [1,1,1,2,2,3]
k = 2

print(answer.topKFrequent(nums, k))    # [1, 2]