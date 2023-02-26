"""O(logN)

The O(logN) notation means that the algorithm's running time
grows logarithmically in size of the problem.

Let's talk about what "log" means in Big-O Notation. "Log" stands for 
logarithm, which is a mathematical function that helps us measure how 
many times we need to divide a number by a certain value to get to 1. 
In Big-O Notation, we use log to represent algorithms that divide the 
problem in half at each step.

This function implements binary search, which is an algorithm that searches 
for a target value in a sorted list by dividing the list in half at each step. 
The time it takes to complete grows logarithmically with the size of the list. 
So we can say that the time complexity of this algorithm is O(logn).

REMEMBER!!
- Binary Search & Binary Search Trees use O(logN).
- O(longN) is basically saying how many times can we divide
  the number N by 2 until we get 1.
- Same as saying how many times can you take 1 and multiply by
  2 until you get the value of N. The answer is O(logN)
- You start the binary search with an O(n) object; as you conduct 
  the search you eliminate half of the list and repeat the 
  process until a match is found or not found - O(logN).
- O(logN) is the second most efficient algorithm running time, behind O(1).
- The diffrence between O(logN) and O(n) greatly increases.
"""
def binary_search(lst: list[int], target: int):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

nums: list[int] = [16, 10, 6, 86, 12, 4, 82, 53]
target: int = 12
# you need to sort the list values before running binary search 
nums.sort()

print(binary_search(nums, target))


# Binary Search on BST
def search(root, target):
    if not root:
        return False
    if target < root.val:
        return search(root.left, target)
    elif target > root.val:
        return search(root.right, target)
    else: 
        return True


# Heap Push and Pop
import heapq
minHeap = []
heapq.heappush(minHeap, 5)
heapq.heappop(minHeap)

# Output
# 3