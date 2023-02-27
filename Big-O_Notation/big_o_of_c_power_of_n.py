"""O(c^n)

The O(c^n) notation means that the algorithm's running time grows 
exponentially with the sie of the problem, but the growth rate is
determined by the constant value "c".

What about "c" in Big-O Notation? "c" represents a constant that 
is independent of the size of the problem.

This function calculates the n-th number in the Fibonacci sequence, 
and the time it takes to complete grows exponentially with the value 
of n. However, the growth rate is determined by the constant value "c" 
(which is roughly equal to 1.618). So we can say that the time 
complexity of this algorithm is O(c^n).

REMEMBER!!
- c refers to another variable different to n
- The c constant is responsible for the growth rate (independent of the size)
  of the problem
"""
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

result: int = fib(10)
print(result)    # 55


# c branches, where c is sometimes n.
import sys
sys.setrecursionlimit(10**6)

def recursion(i: int, nums: list[int], c: int) -> int:
    if i == len(nums):
        return 0
    
    total = 0
    for j in range(i, min(i + c, len(nums))):
        total += recursion(j + 1, nums, c)
        
    return total + 1

nums: list[int] = [1, 2, 3, 4, 5, 6]
c: int = 3

result = recursion(0, nums, 3)
print(result)    # 28
