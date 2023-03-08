"""Valid Palindrome

LEETCODE:  125
COMPANY:  Spotify

A phrase is a palindrome if, after converting all uppercase 
letters into lowercase letters and removing all 
non-alphanumeric characters, it reads the same forward and 
backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or 
false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true

Input: s = "race a car"
Output: false


Solution 1
- We can write our own function to check if the value of the
  string is alpha-numeric (A-Z, a-z or 0-9 characters).
- Then create pointers for the first and last character and
  check if the pointers match. 
- We move the pointers across until both pointers meet at the
  middle. If we encounter a space we move the pointer across
  an extra space.
"""
from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create your pointers
        left_pointer = 0
        right_pointer = len(s) - 1 
        while left_pointer < right_pointer:
            # move to next value if left pointer has a space
            while left_pointer < right_pointer and not self.alphanum(s[left_pointer]):
                left_pointer += 1
            # do the same for right pointer
            while left_pointer < right_pointer and not self.alphanum(s[right_pointer]):
                right_pointer -= 1
            # return False if both pointers are not equal
            if s[left_pointer].lower() != s[right_pointer].lower():
                return False
            # move pointers after checking each value
            left_pointer += 1
            right_pointer -= 1
        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (
            # check ASCII values to see if alpha-numeric
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )


answer: Solution = Solution()

example1: str = "A man, a plan, a canal: Panama"
print(answer.isPalindrome(example1))    # True

example2: str = "race a car"
print(answer.isPalindrome(example2))    # False