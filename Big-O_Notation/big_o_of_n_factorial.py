"""O(n!)

The O(n!) notation means that the algorithm's running time
grows quickly with the size of the problem, even more than
O(2^n).

This function generates all possible permutations of a list, 
and the time it takes to complete grows very quickly with the 
size of the list. So we can say that the time complexity of 
this algorithm is O(n!).

REMEMBER!!
- Factorial means 5+4+3+2+1 etc
- Used for graph problems, permutations ^ Travelling Salesman Problem
- It's very ineffiecient if your code is O(n!), but sometimes
  it could be the only solution.
- O(n!), O(2^n) & O(n^3) are the least efficient algorithms.
"""
def permutation(lst: list[int]) -> list[list[int]]:
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        result = []
        for i in range(len(lst)):
            item = lst[i]
            rest = lst[:i] + lst[i+1:]
            for perm in permutation(rest):
                result.append([item] + perm)
        return result


lst: list[int] = [1, 2, 3]
result = permutation(lst)
print(result)


# Output
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]