"""Reversed Linked List

LEETCODE: 206
COMPANY:  Google, Facebook

Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []


Solution
- We can use two pointers to solve this problem.
- The pointers are used to mark the previous index and the current index.
  We start at the beginning and set the previous to the current index, then move the 
  current index by one.
- This is repeated until the iterated list is empty and the returned list is reversed.

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # create pointers
        previous_node = None
        current_node = head

        while current_node:
            # store the next node in temp variable
            temp = current_node.next
            # switch current node to previous
            current_node.next = previous_node
            # move the previous to current node
            previous_node = current_node
            # move current to temp
            current_node = temp
        
        return previous_node


answer = Solution()

# create the example linked lists
example1 = ListNode(1)
example1.next = ListNode(2)
example1.next.next = ListNode(3)
example1.next.next.next = ListNode(4)
example1.next.next.next.next = ListNode(5)

example2 = ListNode(1)
example2.next = ListNode(2)

# test the reverseList method
print(answer.reverseList(example1).val) # 5
print(answer.reverseList(example2).val) # 2