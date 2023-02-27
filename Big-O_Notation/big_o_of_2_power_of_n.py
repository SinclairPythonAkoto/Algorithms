"""O(2^n)

The O(2^n) notation means that the algorithm's running 
time grows exponentially with the size of the problem.

This function generates all possible subsets of a list, 
and the time it takes to complete grows exponentially with 
the size of the list. So we can say that the time complexity 
of this algorithm is O(2^n).

REMEMBER!!
- Recursion uses O(2^n) time complexity
- Solving the Fibonacci sequence recursively also uses O(2^n) runtime complexity
"""
def powerset(lst: list) -> list[list[int]]:
    if len(lst) == 0:
        return [[]]
    else:
        result = []
        for subset in powerset(lst[1:]):
            result.append(subset)
            result.append([lst[0]]+subset)
        return result

nums: list[int] = [16, 10, 86]

print(powerset(nums))    # [[], [16], [10], [16, 10], [86], [16, 86], [10, 86], [16, 10, 86]]

# Recursion, tree height n, two branches
def recursion(i: int, nums: list[int]):
    if i >= len(nums):
        return 0
    branch1 = recursion(i + 1, nums)
    branch2 = recursion(i + 2, nums)
    return max(nums[i] + branch1, branch2)

nums: int = [1, 2, 3, 4, 5, 6, 7, 8, 9]
height: int = recursion(0, nums)
print("Height of tree:", height)    # Height of tree: 45


def iteration(nums: list) -> int:
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    # initialize dp table with the base cases
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    # fill in the rest of the dp table iteratively
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    return dp[-1]


nums: list[int] = [3, 2, 1, 10, 5, 3, 9, 6]
max_sum = iteration(nums)
print(max_sum)  # 22