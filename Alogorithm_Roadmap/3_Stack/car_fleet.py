"""Car Fleet 

LEETCODE: 853
COMPANY:  Google

There are n cars going to the same destination along a one-lane 
road. The destination is target miles away.

You are given two integer array position and speed, both of 
length n, where position[i] is the position of the ith car 
and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch 
up to it and drive bumper to bumper at the same speed. The 
faster car will slow down to match the slower car's speed. The 
distance between these two cars is ignored (i.e., they are 
assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same 
position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination 
point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3

Input: target = 10, position = [3], speed = [3]
Output: 1

Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1

Solution
- If we use the index of position & speed to plot a graph we 
  will be able to see where the points intersect
- From the graph we can easily see which plots intersect and 
  reaches the target. Remember when they intersect, both 
  plots become a single fleet.

How The Solution Works
- First we need to combine the two lists together, pairing 
  the two indexes using the zip method.

  target = 10
  position = [3, 5, 7]
  speed = [3, 2, 1]
  pairs = [[p,s] for p,s in zip(position, speed)]
  # [[3,3], [5,2], [7,1]]

- We create an empty stack to store the number of fleets.
- Then we sort the cars and loop through the fleet starting 
  at the end, and finishing at the beginning.

  sorted(pairs)[::-1]
  # [[7,1], [5,2], [3,3]]

- In the loop we add each car to the stack.  As a new car 
  is added, we check if it its intersecting with the previous 
  car in the stack. If there aa collision is found, the 
  new car is removed from the top of the stack.
- We repeat the process as we loop through the pairs - 
  remember (target - position) / speed = distance 

  res = (10 - 3) / 3 = 2.3  = stack.append(res) = 2.3
  res = (10 - 5) / 2 = 2.5  = stack.append(res) = 2.5
  
  if stack[-1] 2.3 <= stack[-2] 2.5: stack.pop()

  res = (10 - 7) / 1 = 3.0   = stack.append(res) = 3.0

  if stack[-1] 2.3 <= stack[-2] 3.0: stack.pop()

  ** if the if stack[-2] is higher than stack[-1] then 
     it means a fleet has been found and the newest car
     is removed from the list.
  ** if stack[-2] is lower than stack[-1] then it means a 
     new car fleet has been added to the stack.

- To get the result we can return the length of the stack to 
  find the number of car fleets.

  return len(stack)
"""
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # combine two lists with list comp & zip
        pair: List[List[int]] = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        # create stack 
        stack: List[float] = []
        # iterate through pairs (backwards)
        for p, s in pair:
            # calculate distance of cars and add to stack
            stack.append((target - p) / s)
            # if stack greater/equal than 2 AND first entry the lowest
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


answer: Solution = Solution()

target1 = 10
position1: List[int] = [3, 5, 7]
speed1: List[int] = [3, 2, 1]
print(answer.carFleet(target1,position1, speed1))    # 1

target2 = 12
position2 = [10, 8, 0, 5,]
speed2 = [2, 4, 1, 1, 3]
print(answer.carFleet(target2, position2, speed2))    # 3

target3 = 10
position3 = [10]
speed3 = [3]
print(answer.carFleet(target3, position3, speed3))    # 1

target4 = 100
position4 = [0, 2, 4]
speed4 = [4, 2, 1]
print(answer.carFleet(target4, position4, speed4))    # 1