"""Interview Question 3

To prevent an infinite loop in a production system. Write a program doing the same
calculation without recursion. Please be reminded that a while loop is also considered
not good in a production system.

function recur(n, cur) {
    if (!cur) {
    cur = 0;
    }
    if (n < 2) {
    throw new Error('Invalid input');
    }
    if (n === 2) {
    return 1 / n + cur;
    }
    return recur(n - 1, cur + 1 / (n * (n -1)));
}

"""
def calculate(n):
    if n < 2:
        raise ValueError('Invalid input')

    cur = 0
    for i in range(2, n+1):
        cur += 1 / (i * (i-1))

    return cur

result = calculate(5)
print(result)    # 0.8