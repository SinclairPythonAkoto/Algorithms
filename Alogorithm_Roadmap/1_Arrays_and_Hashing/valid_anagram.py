"""Valid Anagram

LEETCODE: 242
COMPANY: Uber

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false

- We need to check if all the characters from the first string variable matches the 
  characters of tehe second variable.
- We can solve this problem using 3 solutions:
- Solution 1: Create a hashmap that will match letters of both variables
- Solution 2: Can use the Counter() data structure 
- Solution 3: Can use O(1) space by using a sorting algorithm 
"""
# solution 1 - hashmap O(n)
class Solution:
    def isAnagram(self, string1: str, string2: str) -> bool:
        # check if the two strings are equal length
        if len(string1) != len(string2):
            return False
        
        # create hashmaps of both strings
        count_str1, count_str2 = {}, {}

        # loop through the first string
        for char in range(len(string1)):
            # add each letter to hashmap & count how many times
            # letter is in loop.  Repeat for both strings
            count_str1[string1[char]] = 1 + count_str1.get(string1[char], 0)    # add 1 to existing character in hashmap
            count_str2[string2[char]] = 1 + count_str2.get(string2[char], 0)    # if new to hashmap add 0
        for char in count_str1:
            if count_str1[char] != count_str2.get(char, 0):
                return False
        return True

answer1: Solution = Solution()

str1 = "anagram"
str2 = "nagaram"

print("Hashmap solution ")
print(answer1.isAnagram(str1, str2))    # True

str1 = "rat"
str2 = "car"

print(answer1.isAnagram(str1, str2))    # False


# soultion 2 - Counter() data structure O(n)
from collections import Counter

class Solution:
    def isAnagram(self, string1: str, string2: str) -> bool:
        return Counter(string1) == Counter(string2)

answer2: Solution = Solution()

str1 = "anagram"
str2 = "nagaram"

print("Counter solution")
print(answer2.isAnagram(str1, str2))    # True

str1 = "rat"
str2 = "car"

print(answer2
.isAnagram(str1, str2))    # False


# solution 3 - sorted() method O(1)
class Solution:
    def isAnagram(self, string1: str, string2: str) -> bool:
        return sorted(string1) == sorted(string2)

answer3: Solution = Solution()

str1 = "anagram"
str2 = "nagaram"

print("Sorted solution")
print(answer3.isAnagram(str1, str2))    # True

str1 = "rat"
str2 = "car"

print(answer3.isAnagram(str1, str2))    # False


# Output
# Hashmap solution 
# True
# False
# Counter solution
# True
# False
# Sorted solution
# True
# False