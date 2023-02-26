"""O(1)

The O(1) notation means that the algorithm takes a constant
amount of time, no matter how big the problem is.

This function prints the first element of a list, and it 
takes a constant amount of time, no matter how big the 
list is. So we can say that the time complexity of this 
algorithm is O(1).
"""
def print_first_element(lst: list[int]):
    print(lst[0])

# Array
nums = [1, 2, 3]

print_first_element(nums)

nums.append(4)           # push to end O(1)
print(nums.pop())        # pop from end O(1)
print(nums[0])           # lookup O(1)
nums[1]
nums[2]

# HashMap / Set
hashMap = {}
hashMap["key"] = 10     # insert O(1)
print("key" in hashMap) # lookup O(1)
print(hashMap["key"])   # lookup O(1)
hashMap.pop("key")      # remove O(1)


# Output
# 1
# 4
# 1
# True
# 10