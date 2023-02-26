"""O(n*m)

"m" is simply another variable that represents the size of 
a different input. For example, if we have a function that 
takes two lists as inputs, we can represent the time complexity 
as O(n*m), where "n" is the size of the first list, and "m" 
is the size of the second list.

This function prints all pairs of elements from two lists, and 
the time it takes to complete grows proportionally with the 
size of both lists. So we can say that the time complexity 
of this algorithm is O(n*m).

REMEMBER!!
- m means another variabe
- O(n*m) runs very similar to O(n^2)
"""
# Get every pair of elements from two arrays
def print_all_pairs(lst1: list[int], lst2: list[int]) -> tuple[int]:
    for element1 in lst1:
        for element2 in lst2:
            print(element1, element2)

nums1, nums2 = [1, 2, 3], [4, 5]
print_all_pairs(nums1, nums2)


# Traverse rectangle grid
nums = [[1, 2, 3], [4, 5, 6]]
for i in range(len(nums)):
    for j in range(len(nums[i])):
        print(nums[i][j])

# Output
# 1 4
# 1 5
# 2 4
# 2 5
# 3 4
# 3 5
# 1
# 2
# 3
# 4
# 5
# 6