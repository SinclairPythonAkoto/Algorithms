"""O(n^2)

The O(n^2) notation means that the algorithm's runnign time grows
exponentially with the size of the problem.

This function prints all pairs of elements in a list, and the time 
it takes to complete grows exponentially with the size of the list. 
So we can say that the time complexity of this algorithm is O(n^2).

REMEMBER!!
- Nested loops are O(n^2)
- If you itereate through a single list n times that would be O(n^2)
"""
def print_all_pairs(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(lst[i], lst[j])

nums: list[int] = [5, 6, 2, 23]
print_all_pairs(nums)

# Traverse a square grid
nums: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(nums)):
    for j in range(len(nums[i])): 
        print(nums[i][j])


# Get every pair of elements in array
nums = [1, 2, 3]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        print(nums[i], nums[j])

# Insertion sort (insert in middle n times -> n^2)


# Output
# 5 5
# 5 6
# 5 2
# 5 23
# 6 5
# 6 6
# 6 2
# 6 23
# 2 5
# 2 6
# 2 2
# 2 23
# 23 5
# 23 6
# 23 2
# 23 23
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 1 2
# 1 3
# 2 3