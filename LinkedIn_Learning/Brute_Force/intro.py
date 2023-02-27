# Brute Force solution: print even numbers from 1 - 100
for num in range(1, 101):
    if num % 2 == 0:
        print(num)


# More efficient solution
for evens in range(2, 101, 2):
    print(evens)