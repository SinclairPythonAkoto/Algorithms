"""Add Two Numbers

LEETCODE: 2
COMPANY:  Amazon

You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order, and each of their 
nodes contains a single digit. Add the two numbers and return the sum 
as a linked list.

You may assume the two numbers do not contain any leading zero, except 
the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Solution
- diff sizes add 0 for a int that doesnt exist
- We have to also remember to carry the 10th number accross to the 
  next node
- Because the nodes are reversed in the linked list, the value 342 would 
  be reversed to 243. With this in mind we can start from the begining of 
  the reversed lists to add the nodes togther.
- This will make the output of the answer reversed.
- We also have to think about if one of the lists are longer than the other.
  If it is, then we place a 0 where the value is supposed to be so we can still
  add the two nodes together.
- We also have to cater for when the sum is 10 or more and we have to carry the 
  10th unit across in order to add the nodes properly.
"""
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        carry = 0
        # check if l1 & l2 have numbers and add together 
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            # get the single digit eg 15->1 
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


def print_sum_nodes(list1: ListNode, list2: ListNode) -> List[int]:
    """Add two list nodes and print result"""
    result: List[int] = []

    current_node = answer.addTwoNumbers(list1, list2)

    while current_node:
        result.append(current_node.val)
        current_node = current_node.next
    print(result)


answer: Solution = Solution()


example1: ListNode = ListNode(2, ListNode(4, ListNode(3)))
example2: ListNode = ListNode(5, ListNode(6, ListNode(4)))

print_sum_nodes(list1=example1, list2=example2)    # [7, 0, 8]


example3: ListNode = ListNode(0)
example4: ListNode = ListNode(0)

print_sum_nodes(example3, example4)   # 0


example5: ListNode = ListNode(
    9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
)
example6: ListNode = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

print_sum_nodes(example5, example6)    # [8, 9, 9, 9, 0, 0, 0, 1]