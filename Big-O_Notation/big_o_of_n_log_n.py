"""O(nlogn)

The O(nlogn) means that the algorithm's running time grows 
proportionally with the size of the problem.

This function implements merge sort, which is an algorithm 
that sorts a list by dividing it in half at each step and 
merging the sorted halves. The time it takes to complete 
grows proportionally with the size of the list, multiplied 
by the logarithm of the size of the list. So we can say that 
the time complexity of this algorithm is O(nlogn).

REMEMBER!!
- It is marginally more efficient than O(n), but a lot more
  efficient than O(n^2).
- Sorting algorithms are associated with O(nlogn)
- We can also have O(m+nlogn) where "m" would be another variable.
"""
def merge_sort(lst: list[int]) -> list[int]:
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
def merge(left: int, right: int) -> list[int]:
    result: list[int] = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

nums: list[int] = [5, 4, 3, 2, 1]
print(merge_sort(nums))    # [1, 2, 3, 4, 5]

# HeapSort
import heapq
nums: list[int] = [1, 2, 3, 4, 5]
heapq.heapify(nums)     # O(n)
while nums:
    heapq.heappop(nums) # O(logn)

# MergeSort (and most built-in sorting functions)