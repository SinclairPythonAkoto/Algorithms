"""Product of Array Except Self

LEETCODE: 238
COMPANY: Amazon

Given an integer array nums, return an array answer such that 
answer[i] is equal to the product of all the elements of nums 
except nums[i].

The product of any prefix or suffix of nums is guaranteed to 
fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without
using the division operation.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

- What we have to do is loop through each number of in list
  and multiply all th enumbers together except for the iterator.
  In the end you should have a list of the mutiplied values.
- Create a prefix to store each number before the iterator, 
  then a postfix to store each number after ther iterator.
  This will be used to the prefix & postfix values together 
  in order to find the value of the iterator. 

nums = [1, 2, 3, 4]
prefix = [1, 2, 6, 24] same as [(1*1), (1*2), (2*3), (6*4)]
postfix = [24, 24, 12, 4] same as [(1*24), (2*12), (3*4), (4*1)]

# to calculate output prefix * postfix
# we start prefx at 1 (before 1st index) and multiply the the prefix 2nd index.
# keep the same flow to complete output

output = [24, 12, 8, 6] same as [(1*24), (1*12), (2*4), (6*1)]

- In order to keep the time & space to O(n), we can can complete
  the same process without the need of creating a prefix & 
  postfix.  We can find the prefix of each value in accending,
  then decending order, returning the answer in an output object.

nums = [1, 2, 3, 4]

# initialise the prefix counter to 1
# start from first index to end of list

prefix count = 1
prefix_count * list_index = prefix_count

1 * 1 = [1]
1 * 1 = [1, 1]
1 * 2 = [1, 1, 2]
2 * 3 = [1, 1, 2, 6]
6 * 4 = [1, 1, 2, 6] 24   # this lst loop inst stored

# We do the same and start at the end of the list and work
# our way back to find the postfix values. We initialise the 
# postfix value to 1 for the first value then begin the loop.
# We take the existing values from the prefix loop and update
# them in the postfix loop.

1 * 6 = 6 * 1 = [1, 1, 2, 6]    # this is before we start the loop 
1 * 4 = 4 * 2 = [1, 1, 8, 6]
3 * 4 = 12 * 1 = [1, 12, 8, 6]
2 * 12 = 24 * 1 = [24, 12, 8, 6]

Time: O(n)
Space: O(1)
"""