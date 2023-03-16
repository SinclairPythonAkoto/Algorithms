"""Min Stack

LEETCODE:  155
COMPANY:  Amazon

Design a stack that supports push, pop, top, and retrieving 
the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

- We need to create two stacks - one for the list elements and the
  other to calculate the minimum value between the numbers.
- By having two stacks we can make the time complexity more 
  efficient by being able to find the minimum value from the
  MinStack and add new values to the other. The workload is 
  spread so when we want to get data we can use just one operation 
  on our data structure, rather than a series of logical actions
  that would end up increasing the time complexity.
- Having the functions spread out makes it easier to create 
  operations that have linear time complexity O(1).
- When we add a number to the stack, the same number is added to 
  the MinStack. Everytime we add a new number to the stack, 
  it is added to the top of the list, and in the MinStack it
  calculates the minimum value each time.
- If we pop an item from the stack, we also pop the item from 
  the MinStack.
- To get the top element from the stack we get the last item 
  in the list.  To get the minimum value we get the last 
  item in the MinStack.
"""
class MinStack:
    def __init__(self):
        # initialise empty stacks
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # update val after adding it to stack 
        # get min value between stack and top of minStack
        # check if stack exists else val
        val = min(val, self.minStack[-1] if self.minStack else val)
        # add new val to minStack
        self.minStack.append(val)

    def pop(self) -> None:
        # pop from both stacks to remove item 
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # get last value of stack
        return self.stack[-1]

    def getMin(self) -> int:
        # get last value of minStack
        return self.minStack[-1]


# Create a new MinStack object
min_stack: MinStack = MinStack()

# Call the push method to add -2, 0, and -3 to the stack
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)

# Call the getMin method to get the minimum value in the stack (-3)
print(min_stack.getMin())  # -3

# Call the pop method to remove the top item (-3) from both stacks
min_stack.pop()

# Call the top method to get the top item in the stack (0)
print(min_stack.top())  # 0

# Call the getMin method to get the minimum value in the stack (-2)
print(min_stack.getMin())  # -2
