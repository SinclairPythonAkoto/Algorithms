"""Reorder List

LEETCODE: 143
COMPANY:  LinkedIn

You are given the head of a singly linked-list. The list can 
be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes 
themselves may be changed.

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Solution
- What we will need to do is split the list in half to be able
  to alternate the list index being returned.
- In the second half of the split list, we reverse the order 
  of the links so it starts at the end and works backwards.
- In order to be able to split the list in half correctly, we 
  create two pointers that will be placed on the 1st and 2nd 
  index values.  We will move pointer1 (slow pointer) by one, 
  while we move pointer2 (fast pointer) by two spaces.
- If there are even elements in the linked list then the two 
  lists will be split evenly. If the number of elements are odd
  then pointer1 will always have the most amount of elements.
- The slow pointer (pointer1) will always stop at the half-way 
  mark, and the fast pointer (pointer2) will stop when there are 
  no more elements to loop through. 
- To be able to shift the pointers after breaking the links, we
  would have to create a temporary variable that will store 
  the proceeding node before the link is broken.  This allows us 
  to still acees the node values after we break the link and 
  shift our pointers to the next node.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
