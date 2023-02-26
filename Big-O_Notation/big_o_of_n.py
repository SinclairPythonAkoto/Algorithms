"""O(n)

The O(n) notation means that the algorithm's running time grows
linearly with the size of the problem.

This function prints all the elements in a list, and the time 
it takes to complete grows linearly with the size of the list. 
So we can say that the time complexity of this algorithm is O(n).

REMEMBER!!
- Looping through an array is O(n)
- Inserting/removing in the middle of an array is O(n). This is
  because the rest of the elements need to rearranged to it's new index.
- You can build a heap directly from the array using heapify. This is
  much more efficient and makes it an O(n) operation.
"""
def print_all_elements(lst: list):
    for element in lst:
        print(element)


nums = [1, 2, 3]
print_all_elements(nums)
sum(nums)           # sum of array O(n)
for n in nums:      # looping O(n)
    print(n)

nums.insert(1, 100) # insert middle O(n)
nums.remove(100)    # remove middle O(n)
print(100 in nums)  # search O(n)

import heapq
heapq.heapify(nums) # build heap O(n)

# sometimes even nested loops can be O(n)
# (e.g. monotonic stack or sliding window)

# Output
# 1
# 2
# 3
# 1
# 2
# 3
# False

