# Fizz Buzz

"""
- count to 100.
- every multiple of 3, replace with "fizz"
- every multiple of 5, replace with "buzz"
- multiples of 3 & 5, replace with "fizz buzz"
"""
for num in range(1, 101):
    # check both conditions first
    if num % 3 == 0 and num % 5 == 0:
        print("fizz buzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
