# Intuition
The best way to approach this is to create a hashmap. We then can count every letter from each word, this will be the hashmap-key. Words that have the same number of letters will be put in a list, this will be the hashmap-value.  Because the hashmap is a dictionary, we can return just the values.

# Approach
1. Import `collections` in order to use the built-in hashmap function `defaultdict()`.  Now inside the function, create a varialbe `ans` that will create the hashmap.  We pass in list ad an edge-case so it will create an empty list if no matches are found.
```
        import collections
        ans = collections.defaultdict(list)
```
2. Now we run a for-loop in the list of strings..
```
for word in strs:
```
3. In the loop we will create a `count` variable which will be a list of 26x 0's in a list. Every index in the list will signify a character of the alphabet.
```
for word in strs:
    count = [0] * 26
```
4. Now th e`word` variable is a list of 26x 0 for each word in the given list.  We can now iterate through each letter in the list and match the index with the index of the `count` variable.  We use the ord() function to get the ASCII value of the iterator and subtract that away from lowercase "a". The value of this will give us a number between 0 - 25 which will give us the index of the alphabet in the `counter` list. We then increment the the number of times that letter is found in the counter variable with `+= 1`.
```
for char in word:
    count[ord(char) - ord("a")] += 1
```
5. We append each `word` to our `count` and convert it to a tuple in order for us to add this to our hashmap.  This line will map the two lists as tuples, where each key-value pair is a tuple.
```
for char in word:
    count[ord(char) - ord("a")] += 1
ans[tuple(count)].append(word)
```
6. The end result will be a dictionary (default dictionary from the collections module), which we can return the dictory values.
```
return ans.values()
```

# Code
```
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import collections
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
```