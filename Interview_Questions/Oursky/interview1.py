"""Interview Question 1
Find the longest sequence of the string 

Given a dictionary of variable names where each name follows CamelCase notation,
print the item containing most words. Please note, abbr, like ID , IP are considered one
word. i.e. name IPAddress contains two words, IP and Address .

If the name contains the same number of words, it output the longest and the first
appearance.

Dictionary=["Hi","Hello","HelloWorld", "HiWorld", "HelloWorldWideWeb", "HelloWWW"]
Output="HelloWorldWideWeb"

Dictionary=["Oursky","OurSky","OurskyLimited", "OurskyHK", "SkymakersDigitalLTD", "Skymake
rsDigitalLtd"]
Output="SkymakersDigitalLTD"
"""
import re
from typing import List

class Solution:
    def get_most_words(self, dict_items) -> str:
        max_word_count = 0
        max_word_item = ""

        for item in dict_items:
            # Split the item based on uppercase letters using regular expression
            words = re.findall('[A-Z][^A-Z]*', item)
            # Count the number of words in the item
            word_count = len(words)
            # Check if the current item has more words than the previously found max item
            if word_count > max_word_count:
                max_word_count = word_count
                max_word_item = item
            elif word_count == max_word_count:
                # If the current item has the same number of words as the max item, check which is longer
                if len(item) > len(max_word_item):
                    max_word_item = item

        return max_word_item


# Example usage
dict1 = ["Hi", "Hello", "HelloWorld", "HiWorld", "HelloWorldWideWeb", "HelloWWW"]
dict2 = ["Oursky", "OurSky", "OurskyLimited", "OurskyHK", "SkymakersDigitalLTD", "SkymakersDigitalLtd"]
# print(get_most_words(dict1))  # Output: "HelloWorldWideWeb"
# print(get_most_words(dict2))  # Output: "SkymakersDigitalLTD"


answer: Solution = Solution()

example1: List[str] = ["Hi","Hello","HelloWorld", "HiWorld", "HelloWorldWideWeb", "HelloWWW"]
# print(answer.longest_word(example1))

print(answer.get_most_words(example1))