"""Remove Nth Node From End of List

LEETCODE: 19
COMPANY:  Oracle

Given the head of a linked list, remove the nth node from the 
end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]


Solution
- We will need to use two pointers and a dummy node to complete
  this cahallenge.
- First we create a dummy node where set the value to 0 and initialise
  the next vaiable to the head of the linked list.
- The left (L) pointer starts at the dummy node and the right (R) pointer
  will be n on the index of the list.  Meaning if n=2, then the 
  R pointer will be placed on the 2nd value of the linked list.
- This means there is 2x nodes between the L pointer and the R pointer.
- When looping through the linked list both L & R pointers are moved
  by one; this loop ontinues until the R pointer has no more 
  elements to loop through.
- When this happens, the L pointer will be at the value BEFORE 
  the node that needs to be deleted.  Now we can return the removed 
  item from the list using the L pointer's next variable; we use
  next.next to skip the removed node and jump to the last node.

  head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
  n = 2
  dummy = ListNode(0, head)
  L = dummy
  R = 

  LOOP
  0  1  2  3  4  5
  L        R

  
  0  1  2  3  4  5
     L        R

     
  0  1  2  3  4  5
        L        R

        
  0  1  2  3  4  5  *Null        L.next.next = 5
           L        R
"""
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # create a dummy node and make the head the next
        dummy = ListNode(0, head)
        # create your pointers
        left = dummy
        right = head

        # move R pointer n times
        while n > 0:
            right = right.next
            n -= 1

        # move both ppointers
        while right:
            left = left.next
            right = right.next

        # delete node
        # 1 -> 2 -> 3 = 1 -> 3
        left.next = left.next.next
        # return dummy node
        return dummy.next


# function to print values
def print_node_values(result: ListNode) -> List[int]:
    output_list = []
    node = result
    while node:
        output_list.append(node.val)
        node = node.next

    print(output_list)


answer: Solution = Solution()

example1: ListNode = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = answer.removeNthFromEnd(example1, n=2)

print_node_values(result)    # [1, 2, 3, 5]

example2: ListNode = ListNode(1)
result = answer.removeNthFromEnd(example2, n=1)

print_node_values(result)    # [1]


example3: ListNode = ListNode(1, ListNode(2))
result = answer.removeNthFromEnd(example3, n=1)

print_node_values(result)    # []