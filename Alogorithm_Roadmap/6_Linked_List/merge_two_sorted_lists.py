"""Merge Two Sorted Lists

LEETCODE: 21
COMPANY:  Microsoft

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]


Solution
- We use pointers to compare the value of the two lists.
- We are comparing which value is the smallest, then adding 
  the smallest value to our output list.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # empty list-node to store values
        dummy = ListNode()

        tail = dummy

        # check if both lists exist
        while list1 and list2:
            # move tail to next list1 node if less than list2
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            # move tail if list2 less or equal
            else:
                tail.next = list2
                list2 = list2.next
            # update tail no matter condition
            tail = tail.next

        # check if one list is empty but the other exists 
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        
        return dummy.next


# create input linked lists
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# merge the linked lists
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# construct output list
output_list = []
node = merged_list
while node:
    output_list.append(node.val)
    node = node.next


print(output_list)    # [1, 1, 2, 3, 4, 4]