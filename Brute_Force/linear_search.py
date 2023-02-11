def linear_search(data: list[int], target: int) -> int:
    for indx, val in enumerate(data):
        if val == target:
            return indx
    return -1

data: list = [4, 5, 2, 7, 1, 8]
target: int = 1

result: int = linear_search(data, target)
if result == -1:
    print("Item not found.")
print(f"Item found at position: {result}")