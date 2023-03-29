"""Longest Repeating Character Replacement

LEETCODE: 424
COMPANY:  Google

You are given a string s and an integer k. You can 
choose any character of the string and change it to any 
other uppercase English character. You can perform this 
operation at most k times.

Return the length of the longest substring containing the 
same letter you can get after performing the above operations.

Input: s = "ABAB", k = 2
Output: 4

Input: s = "AABABBA", k = 1
Output: 4


Solution
- We need a sliding window and a hashmap to solve this problem.
- Our L & R pointers start at the first index, then we iterate 
  through the string using the R pointer. 
- We get the count of most frequent charatcer of the window, and
  subtract it from the length of the current window.
- A hashmap of the alphabet is created in order to store 
  count the characters in each sliding window.

  A B A B B A      k=2
  LR
                   hashmap:
                   A: 0
                   B: 0

- At the begining all the characters in the hashmap is initialised
  to 0 (all characters from A - Z).
- The first sliding window is the siize of 1, because both pointers
  are at "A". We can also update the hashmap.

  A B A B B A      k=2
  LR
                   hashmap:         calculation:
                   A: 1             (len_window - count[char]) =< k
                   B: 0             1 - 1 = 0 =< 2
                   replacements = 1

  A B A B B A      k=2
  L R
                   hashmap:         calculation:
                   A: 1             (len_window - count[char]) =< k
                   B: 1             2 - 1 = 1 =< 2
                   replacements = 2

  A B A B B A      k=2
  L   R
                   hashmap:         calculation:
                   A: 2             (len_window - count[char]) =< k
                   B: 1             3 - 2 = 1 =< 2
                   replacements = 3

  A B A B B A      k=2
  L     R
                   hashmap:         calculation:
                   A: 2             (len_window - count[char]) =< k
                   B: 2             4 - 2 = 2 =< 2
                   replacements = 4

  A B A B B A      k=2
  L       R
                   hashmap:         calculation:
                   A: 2             (len_window - count[char]) =< k
                   B: 3             5 - 3 = 2 =< 2
                   replacements = 5

  A B A B B A      k=2
  L         R
                   hashmap:         calculation:
                   A: 3             (len_window - count[char]) =< k
                   B: 3             6 - 3 = 3 =< 2
                   replacements = 5

- Becuase the result after the subtraction is higher than the value of 
  k, we move the L pointer and decrement the character's
  value from the hashmap by 1.

  A B A B B A      k=2
    L       R
                   hashmap:         calculation:
                   A: 2             (len_window - count[char]) =< k
                   B: 3             5 - 3 = 2 =< 2
                   replacements = 5
- The loop stops here becuase the R pointer doesn't have any more 
  characters to loop through.  Now we can return the number
  of replacements as the answer.
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # initialise hashmap & pointers
        count = {}
        res = 0

        left_pointer = 0
        maxf = 0
        for right_pointer in range(len(s)):
            count[s[right_pointer]] = 1 + count.get(s[right_pointer], 0)
            # update the maxf
            maxf = max(maxf, count[s[right_pointer]])

            # find valid replacement
            if (right_pointer - left_pointer + 1) - maxf > k:
                count[s[left_pointer]] -= 1
                left_pointer += 1

            # get current value
            res = max(res, right_pointer - left_pointer + 1)
        return res


answer: Solution = Solution()

example1: str = "ABAB"
print(answer.characterReplacement(example1, k=2))    # 4

example2: str = "AABABBA"
print(answer.characterReplacement(example2, k=1))    # 4

example3: str = "ABABBA"
print(answer.characterReplacement(example3, k=2))    # 5