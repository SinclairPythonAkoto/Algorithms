"""Longest Substring Without Repeating Characters

LEETCODE: 3
COMPANY:  Facebook

Given a string s, find the length of the longest 
substring without repeating characters.

**A substring is a contiguous non-empty sequence of characters within a string.

Input: s = "abcabcbb"
Output: 3

Input: s = "bbbbb"
Output: 1

Input: s = 3
Output: 3


Solution
- We are basically checking to see if we have duplicate 
  characters in a string, and return the number of characters
  the longest string without duplicates.
- To this we need to create 2x pointers to iterate through the
  charaters and use a set to check if the characters are a duplicate.
  We will add each charater to the set and if we find a duplicate
  we remove the charater and then move onto the next letter in the string.
- At each interation we are counting the number of characters in
  each subtring and then returning the result at the end.

  word = "abcabcbb"
          LR         subString = 2
                     subSet = "ab"

  word = "abcabcbb"
          L R       subString = 3
                    subSet = "abc"

- This is the longest subtring. When the loop finds a duplicate
  the duplicate in the substring is removed.

  word = "abcabcbb"
          L  R      subString = 2
                    subSet = "bc"

- Now we move the left pointer and the loop will check if the 
  character "b" is a duplicate. If we find a duplicate then we 
  remove it from the subSet.


  word = "abcabcbb"
           L  R     subString = 2
                    subSet = "bc"

  word = "abcabcbb"
            L  R    subString = 1
                    subSet = "c"
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initialise set, result & pointers
        charSet = set()
        left_pointer = 0
        res = 0

        # iterate string through R
        # range length of list to iterate each char
        for right_pointer in range(len(s)):

            # remove char if duplicate in set
            while s[right_pointer] in charSet:
                charSet.remove(s[left_pointer])
                # move L pointer
                left_pointer += 1

            # add char to set if no duplicate
            charSet.add(s[right_pointer])
            # find if current R result is higher than previous 
            # subract int index str values
            # +1 becuase of the range on str
            res = max(res, right_pointer - left_pointer + 1)
        return res


answer: Solution = Solution()

string1: str = "abcabcbb"
print(answer.lengthOfLongestSubstring(string1))    # 3

string2: str = "bbbbb"
print(answer.lengthOfLongestSubstring(string2))    # 1

string3: str = "pwwkew"
print(answer.lengthOfLongestSubstring(string3))    # 3