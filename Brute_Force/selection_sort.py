# create a function that sorts the elements of the list from smallest to highest

def selection_sort(xs):
    for i in range(len(xs)):
        min_index: int = i
        for j in range(i + 1, len(xs)):
            if xs[j] < xs[min_index]:
                min_index = j
        xs[i], xs[min_index] = xs[min_index], xs[i]

xs: list = [3, 2, 1, 5, 4]

print(f"Unsorted list: {xs}")

selection_sort(xs)

print(f"Sorted list: {xs}")

# a Pythonic way to check list is sorted
print(
    all(
        xs[i] <= xs[i + 1] for i in range(len(xs) - 1)
    )
)