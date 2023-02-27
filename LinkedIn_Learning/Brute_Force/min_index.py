# Find the smallest number in a list

def find_min(xs: list[int]) -> int:
    min_index: int = 0
    for num in range(len(xs)):
        if xs[num] < xs[min_index]:
            min_index = num
    return xs[min_index]


xs: list = [3, 2, 1, 5, 4]
min_value: int = find_min(xs)

print(f"The minimum value is: {min_value}")

