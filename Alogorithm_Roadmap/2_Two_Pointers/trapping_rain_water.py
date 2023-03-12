"""Trapping Rain Water

LEETCODE:  42
COMPANY:  Google

Given n non-negative integers representing an elevation map 
where the width of each bar is 1, compute how much water it 
can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Input: height = [4,2,0,3,2,5]
Output: 9

- Need to take the max number on the left & right of the 
  iterator, and then take the minimum of the two numbers
  and subtract it from the current list index/iterator.

  min(left_pointer, right_pointer) - height[index]

- We can use this formula to loop through each element
  and sum the collected values to get the result.

Hashmap Solution
- We need to create hashmaps for the maximum left value (maxLeft),
  the maximum right value (maxRight) and a hashmap for the minimum
  value between the two (min(maxLeft, maxRight)).
- To calculate the maxLeft we iterate through the loop, and for 
  each iteration we get the previous (maximum) index value.  
  If the index does not exist then the value is 0.

  height                  : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
  maxLeft                 : [0, 0, 1, 0, 2, 2, 2, 2, 3, 3, 3, 3]

- Notice we only select the maximum value - so if the current 
  maxLeft value is higher than the one before, then the maxLeft
  is updated to current maxLeft value.
- To calculate the maxRight we iterate through the loop starting
  at the end, and finishing at the beginning.  For each iteration
  we get the previous (maximum) number - by comparing if the 
  previous or current index value is the highest.

  height                  : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
  maxLeft                 : [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
  maxRight                : [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0]
  min(maxLeft, maxRight)  : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 0]

- If the previous number does not exist the value is 0.
- Now we can use the min() method to find the minimum value of 
  each index.

  height                  : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
  maxLeft                 : [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
  maxRight                : [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0]
  min(maxLeft, maxRight)  : [0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0]

- Now we can subtract the minimum value (min_val) from each index,
  while we loop through the list. We round the results up to 0 if
  negative numbers.

  height                  : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
  maxLeft                 : [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
  maxRight                : [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0]
  min(maxLeft, maxRight)  : [0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0]
  min_val - list_index    : [0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0]

- With with we can sum up the results to get our answer to the solution.
- This solution uses O(n) time & space complexity.

Pointer Solution
- Instead of creating hashmaps, we can create left & right
  variables and maxLeft & maxRight variables.
- We can pretty much use the same logic now as above to 
  accomplish the same result.  So now we only need to loop 
  through the list to calculate the maxLeft & maxRight using the
  left & right pointers.  Then we calculate the minimum value
  between the maxLeft & maxRight, so we can the value to subtract
  the current index value from it.

  height                  : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
  pointers                :  L                                R
  maxLeft (start)         : 0
  maxRight (start)        : 1

- We shift the pointer that has the smaller max value => if L < R : L += 1

  height                  : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
  pointers                :     L                             R
  maxLeft                 : 0
  maxRight                : 1

- The maxLeft value is 0 because the value before the L pointer is 0.
- We can then use maxLeft and the height list and subtract the 
  value at the L pointer index from the maxLeft. We then round up
  the number to 0 if negative number => 0 - 1 = -1 = 0

  height                  : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
  pointers                :        L                          R
  maxLeft                 : 1
  maxRight                : 1
  index values            : [0, 0, 0, -, -, -, -, -, -, -, -, -]

- In this case we still use the maxLeft even though both pointers
  are equal. => 1 - 1 = 0

  height                  : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
  pointers                :           L                       R
  maxLeft                 : 1
  maxRight                : 1
  index values            : [0, 0, 0, 0, -, -, -, -, -, -, -, -]
  calculation             : maxLeft - height[L] => 1 - 2 = -1 = 0

  height                  : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
  pointers                :           L                       R
  maxLeft                 : 2
  maxRight                : 1
  index values            : [0, 0, 0, 0, -, -, -, -, -, -, -, 0]
  calculation             : maxRight - height[R] => 1 - 0 = 0

  height                  : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
  pointers                :           L                    R
  maxLeft                 : 2
  maxRight                : 1
  index values            : [0, 0, 0, 0, -, -, -, -, -, -, 0, 0]
  calculation             : maxRight - height[R] => 1 - 2 = -1 = 0 

- The maxRight value is still 1 because the maximum value to the right of
  the R pointer is 1. We then take away the index value of R from the maxRight.

  height                  : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
  pointers                :           L                 R  
  maxLeft                 : 2
  maxRight                : 2
  index values            : [0, 0, 0, 0, -, -, -, -, -, 0, 0, 0]
  calculation             : maxRight - height[L] => 2 - 2 = 0

- We can updated either pointer because both are equal (in this example we update the left)
  
  height                  : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
  pointers                :              L              R  
  maxLeft                 : 2
  maxRight                : 2
  index values            : [0, 0, 0, 0, 1, -, -, -, -, 0, 0, 0]
  calculation             : maxLeft - height[L] => 2 - 1 = 1

  height                  : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
  pointers                :                 L           R  
  maxLeft                 : 2
  maxRight                : 2
  index values            : [0, 0, 0, 0, 1, 2, -, -, -, 0, 0, 0]
  calculation             : maxLeft - height[L] => 2 - 0 = 2

  height                  : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
  pointers                :                    L        R  
  maxLeft                 : 2
  maxRight                : 2
  index values            : [0, 0, 0, 0, 1, 2, 1, -, -, 0, 0, 0]
  calculation             : maxLeft - height[L] => 2 - 1 = 1

  height                  : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
  pointers                :                       L     R  
  maxLeft                 : 2
  maxRight                : 2
  index values            : [0, 0, 0, 0, 1, 2, 1, 0, -, 0, 0, 0]
  calculation             : maxLeft - height[L] => 2 - 3 = -1 = 0

  height                  : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
  pointers                :                       L     R  
  maxLeft                 : 3
  maxRight                : 2
  index values            : [0, 0, 0, 0, 1, 2, 1, 0, -, 1, 0, 0]
  calculation             : maxRight - height[R] => 2 - 1 = 1

  height                  : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
  pointers                :                       L  R     
  maxLeft                 : 3
  maxRight                : 2
  index values            : [0, 0, 0, 0, 1, 2, 1, 0, 0, 1, 0, 0]
  calculation             : maxRight - height[L] => 3 -  = 1

- This solution uses O(n) time complexity & O(1) of memory.
  The difference here is that the pointer solution is carried
  out all in the single iteration. 

"""
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # if input is empty
        if not height:
            return 0
        
        # create left & right pointers 
        left_pointer = 0
        right_pointer = len(height) - 1
        # max values for pointers
        leftMax = height[left_pointer]
        rightMax =  height[right_pointer]
        # results counter
        res = 0
        while left_pointer < right_pointer:
            if leftMax < rightMax:
                left_pointer += 1
                # update new leftMax
                leftMax = max(leftMax, height[left_pointer])
                # update result
                res += leftMax - height[left_pointer]
            else:
                right_pointer -= 1
                # update new rightMax 
                rightMax = max(rightMax, height[right_pointer])
                # update result
                res += rightMax - height[right_pointer]
        return res


answer: Solution = Solution()

example1: List[int] = [0,1,0,2,1,0,1,3,2,1,2,1]
print(answer.trap(example1))    # 6

example2: List[int] = [4,2,0,3,2,5]
print(answer.trap(example2))    # 9