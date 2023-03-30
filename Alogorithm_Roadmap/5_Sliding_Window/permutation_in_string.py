"""Permutation in String

LEETCODE: 567
COMPANY:  Microsoft

Given two strings s1 and s2, return true if s2 contains a 
permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is 
the substring of s2.

Input: s1 = "ab", s2 = "eidbaooo"
Output: true

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Solution
- We can use a hashmap and sliding window to solve the problem.
- If we create hashmaps for both s1 & s2 variables, we can then
  count each character of the string and map it to the hashmap.
- The hashmap will have letters from a - z.
- We will also create another variable to count the number of
  matches there are between the two hashmaps.
- As we loop through s2, we are checking the first group of 
  elements to see if the count of characters match the s1 
  hashmap.
- We adjust the number of matches accordingly by increasing
  or decreasing the number if matches are/not found.

  s1 = "abc"        s2 = "baxyzabc"    loop: bax

  s1 count a-z:     s2 count a-z:        matches: 24
  a: 1              a: 1
  b: 1              b: 1
  c: 1              c: 0
  x: 0              x: 1
  y: 0              y: 0
  z: 0              z: 0

- There are 24 matches because each hashmap have matching results
  except for x & c.  s1 x is values at 0, while in s2 the x is 
  valued at 1. The same for the c value, in s1 the value is 1
  while in s2 the value is 0.  These two mismatches are taken 
  away from the total number of possible matches (which is 26
  for the 26 letters of the alphabet).

  s1 = "abc"        s2 = "baxyzabc"    loop: axy

  s1 count a-z:     s2 count a-z:        matches: 22
  a: 1              a: 1
  b: 1              b: 0
  c: 1              c: 0
  x: 0              x: 1
  y: 0              y: 1
  z: 0              z: 0

  
  s1 = "abc"        s2 = "baxyzabc"    loop: xyz

  s1 count a-z:     s2 count a-z:        matches: 20
  a: 1              a: 0
  b: 1              b: 0
  c: 1              c: 0
  x: 0              x: 1
  y: 0              y: 1
  z: 0              z: 1

  
  s1 = "abc"        s2 = "baxyzabc"    loop: yza

  s1 count a-z:     s2 count a-z:        matches: 22
  a: 1              a: 1
  b: 1              b: 0
  c: 1              c: 0
  x: 0              x: 0
  y: 0              y: 1
  z: 0              z: 1

  
  s1 = "abc"        s2 = "baxyzabc"    loop: zab

  s1 count a-z:     s2 count a-z:        matches: 23
  a: 1              a: 1
  b: 1              b: 1
  c: 1              c: 0
  x: 0              x: 0
  y: 0              y: 0
  z: 0              z: 1

  
  s1 = "abc"        s2 = "baxyzabc"    loop: abc

  s1 count a-z:     s2 count a-z:        matches: 26
  a: 1              a: 1
  b: 1              b: 1
  c: 1              c: 1
  x: 0              x: 0
  y: 0              y: 0
  z: 0              z: 0
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case - if s2 is shorter than s1
        if len(s1) > len(s2):
            return False

        # create hashmap list for s1 & s2
        s1Count = [0] * 26
        s2Count = [0] * 26
        # loop length s1 str
        for i in range(len(s1)):
            # get ASCII value of i and subtract ASCII value 'a'
            # to map to 0-26. 
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        # compare both hashmaps
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        
        # L & R pointers for sliding window
        left_pointer = 0
        for right_pointer in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[right_pointer]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[left_pointer]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            left_pointer += 1
        return matches == 26

answer: Solution = Solution()

str1: str = "abc"
str2: str = "baxyzabc"
print(answer.checkInclusion(str1, str2))    # True

str3: str = "ab"
str4: str = "eidbaooo"
print(answer.checkInclusion(str3, str4))    # True

str5: str = "ab"
str6: str = "eidboaoo"
print(answer.checkInclusion(str5, str6))    # False