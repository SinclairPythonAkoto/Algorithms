"""Group Anagram

LEETCODE: 49
COMPANY: Amazon

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

- We could sort all the elements in the list and then check 
  which ones are equal.  The equal elements in the list will 
  mean they are anagrams.  The time complexity would be too
  long - O(m*nlong)
- We can also create a hashmap to count the individual 
letters of each string, then map the pattern to a list 
of string values.  So the key would be the number of 
characters of each string, and the value would be a list of 
the string values.  This will be O(m*n) time complexity.
"""
import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)   # mapping char count to list of anagrams  

        for word in strs:
            # create letters to count
            count = [0] * 26  # a ... z
            for char in word:
                # get ASCII values
                count[ord(char) - ord("a")] += 1
            ans[tuple(count)].append(word)  # change list to a tuple

        return ans.values()

answer: Solution = Solution()

example1: List[str] = ["eat","tea","tan","ate","nat","bat"]
example2: List[str] = [""]

print(answer.groupAnagrams(example1))
print(answer.groupAnagrams(example2))


# Output
# dict_values([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
# dict_values([['']])