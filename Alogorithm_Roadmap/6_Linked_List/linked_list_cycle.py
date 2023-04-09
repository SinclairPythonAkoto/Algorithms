"""Linked List Cycle

LEETCODE: 141
COMPANY:  Amazon

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true

Input: head = [1,2], pos = 0
Output: true

Input: head = [1], pos = -1
Output: false


Hashset Solution
- Loop through the numbers while creating a hashset.
- Then we can use the hashset to check if the number has a duplicate; if the number does 
  have a duplicate then it means that the number has been vsisted twice (meaning the
  linked list has a cycle).  This is O(n) time and memory.

Slow/Fast Pointer Solution
- We create a slow & fast (S & F) pointer that will start at the same point of linked list.
- The slow pointer moveS by 1, fast pointer moves by 2.
- As we loop through the linked list, both the slow and fast pointer are moved;
  when the two pointers meet again, thats when we know that the linked list has a cycle.
- This is O(1) time and memory.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # start the S & F pointer at same
        slow, fast = head, head

        # check if cycle exists
        while fast and fast.next:
            # move S pointer by 1
            slow = slow.next
            # move F pointer by 2
            fast = fast.next.next
            # check if pointers meet at same index
            if slow == fast:
                return True
        return False


answer: Solution = Solution()

# create nodes
node1: ListNode = ListNode(3)
node2: ListNode = ListNode(2)
node3: ListNode = ListNode(0)
node4: ListNode = ListNode(-4)

# link nodes togther and create a cycle
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(answer.hasCycle(node1))    # True


node1: ListNode = ListNode(1)
node2: ListNode = ListNode(2)

node1.next = node2
node2.next = node1

print(answer.hasCycle(node1))    # True


node1: ListNode = ListNode(1)

print(answer.hasCycle(node1))    # False