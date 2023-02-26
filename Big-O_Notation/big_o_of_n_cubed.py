"""O(n^3)

The O(n*m) notation means that the algorithm's running time grows 
cubically with the size of the problem.

This function prints all triplets of elements in a list, and the 
time it takes to complete grows cubically with the size of the list. 
So we can say that the time complexity of this algorithm is O(n^3).
"""
# Get every triplet of elements in array
def print_all_triplets(lst: list) -> tuple[int]:
    for i in range(len(lst)):
        for j in range(len(lst)):
            for k in range(len(lst)):
                print(lst[i], lst[j], lst[k])

nums: list[int] = [0, 1]

print_all_triplets(nums)

# Output
# 0 0 0
# 0 0 1
# 0 1 0
# 0 1 1
# 1 0 0
# 1 0 1
# 1 1 0
# 1 1 1