# Intuition
There are a few ways in whcih we can solve this problem.  The easiest way is to use the `sorted` function. where we woudl sort the two strings and check if they were equal.  We can also use the `collections` library to use the `Collections` module.  This is a data structure that automatically counts the elements for you, which then you can check against.

The third solution is creating a hashmap for the two strings, and then running a loop that will ieterate through the first string. In the loop we will record each character and count how many times it appears within the string (the for loop). Once we repeat the process we will have two hashmaps of both the strings.  We can then check any of elements from the 1st hashmap is found in the 2nd hashmap and we can return `True` or `False` depending on the results.

# Approach
1. We will get the length of both strings and then check the length against each other.  If the length is **not** the same, we can return `False` becasue the two strings connot be an anagram.
```
if len(str1) != len(str2):
    return False
```
2. If the length is equal we can create our hashmaps.  We will create two variables `count_str1` & `count_str2` that will be empty dictionarie that will store key-value pairs of the characters and the amount of times the character appears in each string.
```
count_str1, count_str2 = {}, {}
```
3. Now we want to loop through the number of charatcers within the string. Because both strings are equal, we can pick any string - for simplicity, we will pick the first string.  To do this we will use the range method. This will loop through every character from 0 to the length of the string (recursively).
```
for char in range(len(str1)):
```
4. Now for iteration we want to add each letter to the hashmap and count every letter in the string.  To do this we will get our first hashmap will assign the key to `str1` and the value to the character iterable `char`.  This is basically taking each letter of `str1` and making it a dictionary key.  To assign the key a value `[char]` is assigned an integer value of 1; but we also want to get the current value of the same character so we use the .get() method.  We place 0 in the method so if the character does not exist in the hashmap (i.e it is a new character not yet stored), we can still assign a value to they key with 1 + 0.
```
for char in range(len(str1)):
    count_str1[str1[char]] = 1 + count_str1.get(str1[char], 0)
    count_str2[str2[char]] = 1 + count_str2.get(str2[char], 0)
```
5. Once the range is comeplete we will have our hashmaps complete, so we can use one of them to itereate through (remember because they are dictionay objects, the defualt itereation is through the keys).  So with each iteration of one hashmap, we are checking if the element is **not** in the second hashmap.  If it isn't, then we return `Fasle` because we can determine the two strings are not an anagram.  If there is a match, the we return `True` out of the if-statement.
```
for char in count_str1:
        if count_str1[char] != count_str2.get(char, 0):
            return False
    return True
```

# Code
```
# solution 1 - hashmap O(n)
class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        # check if the two strings are equal length
        if len(str1) != len(str2):
            return False
        
        # create hashmaps of both strings
        count_str1, count_str2 = {}, {}

        # loop through the first string
        for char in range(len(str1)):
            # add each letter to hashmap & count how many times
            # letter is in loop.  Repeat for both strings
            count_str1[str1[char]] = 1 + count_str1.get(str1[char], 0)    # add 1 to existing character in hashmap
            count_str2[str2[char]] = 1 + count_str2.get(str2[char], 0)    # if new to hashmap add 0
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
```