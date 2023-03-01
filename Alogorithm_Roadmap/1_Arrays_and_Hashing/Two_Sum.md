# Intuition
We can use a hashmap to solve this problem.  We itereate trough the list of numbers and and place each number in the hashmap.  With each iteration we can find the two numbers if they exisit in the hashmap and return the index.

# Approach
1. Create a hashmap to store the values from the list.  This will be a key-value pair because the hashmap i sa dictionary object.
```
prevMap = {}
```
2. We will loop through the list using `enumerate`.  This will loop through the list and automatically keep count of index and value of every element in the list.  This makes it easier to add information from the list to our dictionary object.
```
for index, num in enumerate(nums)
```
3. We can now find the difference of each element compared to the target.
```
for index, num in enumerate(nums):
    diff = target - num
```
4. Then we can check if the `diff` variable already exists in the hashmap.  If does, we can return the dictionary object.  `prevMap` is our dictionary object, so in order to return the correct index we need to point to the key which will be the `diff`.  So when we do `prevMap[diff]` we are calling the key to get it's index value.  The `index` variable in the for loop is the index for the list elements.  **Remember, `prevMap` is a dictionary so we are checking if `diff` (the key) is in the dictioary object.  If it is, we return the value of that dictionary key and the current list index the loop is on.**
```
for index, num in enumerate(nums):
    diff = target - num
    if diff in prevMap:
        return [prevMap[diff], index]
```
5. So if the difference is not in the hashmap (not in the dictionary object), then we create a new dictionary object and store the value to it's current index within the list.
```
for index, num in enumerate(nums):
    diff = target - num
    if diff in prevMap:
        return [prevMap[diff], index]
    prevMap[num] = index
return
```

# Code
```
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap to store values
        prevMap = {}  # val : index


        for index, num in enumerate(nums):
            # set the difference
            diff = target - num
            # check if difference is already in hashmap
            if diff in prevMap:
                return [prevMap[diff], index]    # return diff in hashmap & current index value
            # add new key-value pair to hashmap 
            prevMap[num] = index
        return


answer: Solution = Solution()

example1: List[int] = [2, 7, 11, 15]
target1 = 9
print('Example 1')
print(answer.twoSum(example1, target1))
example2: List[int] = [3, 2, 4]
target2 = 6
print('Example 2')
print(answer.twoSum(example2, target2))
example3: List[int] = [3,3]
target3 = 6
print('Example 3')
print(answer.twoSum(example3, target3))


# Output
# Example 1
# [0, 1]
# Example 2
# [1, 2]
# Example 3
# [0, 1]
```