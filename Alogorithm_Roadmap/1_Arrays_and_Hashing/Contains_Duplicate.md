# Intuition
We need to loop through the list and check for duplicates; one way of doing this is by using a `set()`.  We can use a hash set and then loop through the list, adding each element to the set. If we find a number that's already in the set, we will return `True`, if not we will continue to add it to the set until there are no numbers left. If a match isn't found after the loop then it  will return `False`.

# Approach
1. Create a variable `hashset` which will be a set.
```
hashset = set()
```
2. Create a for-loop that will loop through the elements in the list.
```
for element in nums:
```
3. Within the for-loop, we will check if the `element` already exists in the `hashset`. To do this, we will create an if-statement to check if each `element` is in the `hashset`. If it does, we can return `True`.
```
for element in nums:
    if element in hashset:
        return True
```
4. So now in the else block, we can add each element to the set that is not a duplicate. We can then return `False` becasue if our set is eventually full it means we did not find any duplicates.
```
for element in nums:
    if element in hashset:
        return True
    else:
        hashset.add(element)]
return False
``` 
We can improve this if-statement by removing the `else` command and shifting `hashset.add(element)]` out of the if-statement. We can do this because there are only two options for this logic, so if we think about it only first option needs to be in the if-statement, the rest can just be in the for-loop.
```
for element in nums:
    if element in hashset:
        return True
    hashset.add(element)]
return False
```

# Code

```
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a hashset
        hashset = set()

        # run a loop to check for duplicates
        for element in nums:
            # check if number is in the hash set
            if element in hashset:
                return True
            # add to set if no number found
            hashset.add(element)
        return False


answer: Solution = Solution()

example1: List[int] = [1, 2, 3, 1]
example2: List[int] = [1, 2, 3, 4]
example3: List[int] = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

print(answer.containsDuplicate(example1))    # True
print(answer.containsDuplicate(example2))    # False
print(answer.containsDuplicate(example3))    # True

# Time: O(n)
# Space: O(n)
# Company: Microsoft
```