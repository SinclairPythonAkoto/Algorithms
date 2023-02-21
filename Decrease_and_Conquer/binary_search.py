# items must be sorted for a binary search
# Calculate the first & last index, use that to find the mid_point
# mid_point = (low_point + high_point) // 2
# The new first index is changed to mid_point+1 then calculate last index
# Follow the same pattern to find the mid_point, repeat until number is or not found



import random
from typing import List


def binary_search(data: List[int], target: int) -> int:
    low_pointer: int = 0
    high_pointer: int = len(data) - 1
    while low_pointer <= high_pointer:
        mid_point: int = (low_pointer + high_pointer) // 2
        if data[mid_point] == target:
            return mid_point
        elif data[mid_point] < target:
            low_pointer = mid_point + 1
        else:
            high_pointer = mid_point - 1
    return -1


num: int = 10
max_val: int = 100
data: List[int] = [random.randint(1, max_val) for index in range(num)]
data.sort()
print(f"Data: {data}")
target: int = int(input("Enter your target value: "))
target_position: int = binary_search(data, target)
if target_position == -1:
    print("Your target is not in the list")
else:
    print("Your target value has been found at index", target_position)