"""Encode and Decode Strings

LEETCODE: 271
COMPANY: Facebook

Design an algorithm to encode a list of strings to a string.
The encioded string is then sent over the network and is decoded
back to the original list of strings.

Please implement the encode and decode

Input: ["lint", "code", "love", "you"]
Output: ["lint", "code", "love", "you"]


- Becuase we cannot create new objects like a list, one way
  to solve this problem is to modify our delimeter - so it is
  an integer (signifying the length of the word), followed by our
  dilemeter (which can be any type of symbol you want).

  ["neet", "co#de"]
  "4#neet5#co#de"

- This will allow us to create our encode and decode functions.
"""
from typing import List

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # create delimeter & add it to string
            # do this for each string and add to result string
            res += str(len(s)) + "#" + s
        return res

    """
    @param: s: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, s: str) -> List[str]:
        # create empty list and init list index counter  
        res = []
        list_index = 0

        # if index val is less than string index use for loop 
        while list_index < len(s):
            # create iterator for string
            string_index = list_index
            # check if string_index is NOT a # sign
            while s[string_index] != "#":
                # count each character by adding 1
                string_index += 1
            # get length of each string via index
            length = int(s[list_index:string_index])
            # add entire word into the list result
            res.append(s[string_index + 1 : string_index + 1 + length])
            # update the list index after each word is added to list
            list_index = string_index + 1 + length
        return res


answer: Solution = Solution()

example: List[str] = ["lint", "code", "love", "you"]

encode: str = answer.encode(example)
decode: List[str] = answer.decode(encode)

print(encode)    # 4#lint4#code4#love3#you
print(decode)    # ['lint', 'code', 'love', 'you']

# Time: O(n)
# Space: O(n)