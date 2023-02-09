# 100 Doors

"""
- You have 100 closed doors in a list which you will loop through 100 times
- on the 1st loop you open all the doors
- on the 2nd loop you only open every 2nd door
- then on the 3rd loop you only open evey 3rd door and so on until the 100th loop meets the 100th door.
- print all the doors which will be open
"""

doors: list[bool] = [False] * 101

# print(doors)

for num in range(1, 101):
    for item in range(num, 101, num):
        doors[item] = not doors[item]

for num in range(1, 101):
    if doors[num] is True:
        print(num, end=", ")