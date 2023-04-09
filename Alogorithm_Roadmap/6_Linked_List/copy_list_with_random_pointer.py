"""Copy List With Random Pointer

LEETCODE: 138
COMPANY:  Amazon

A linked list of length n is given such that each node contains 
an additional random pointer, which could point to any node in 
the list, or null.

Construct a deep copy of the list. The deep copy should consist 
of exactly n brand new nodes, where each new node has its value 
set to the value of its corresponding original node. Both the 
next and random pointer of the new nodes should point to new nodes 
in the copied list such that the pointers in the original list and 
copied list represent the same list state. None of the pointers 
in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, 
where X.random --> Y, then for the corresponding two nodes x and 
y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of 
n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the 
random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Input: head = [[3,null],[3,0],[3,null]
Output: [[3,null],[3,0],[3,null]]


Solution
- To solve this problem we can use a hashmap and 2x while loops.  This will copy each
  node and link it to it's respected list.
- We create an empty hashmap first, then we loop through the nodes so we can copy 
  each node to the hashmap.
- In the second loop we loop through the hashmap to copy all the nodes. Not only do we 
  just copy the nodes, but we also copy their attributes and match it to the nodes
  in the hashmap.  This means that curr.next & curr.random are copied from the nodes
  stored in the hashmap.
- Because we have created an instance of the copied object using:
  copy = oldToCopy[curr]
  We have accress to the random and next node within the copied object by simply 
  using copy.next & copy.random. Because we have made them equal to the same curr.next
  or curr.random, we are essentially creating the links between the nodes.
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        # hashmap to copy nodes
        oldToCopy = {None: None}

        # copy nodes to hashmap
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        
        # 2nd loop to map pointers
        cur = head
        while cur:
            # copy nodes from hashmap
            copy = oldToCopy[cur]
            # copy node attributes from hashmap
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            # move onto the next node in linked list
            cur = cur.next
        return oldToCopy[head]
    

answer: Solution = Solution()

# create linked lists
node0: Node = Node(7)
node1: Node = Node(13)
node2: Node = Node(11)
node3: Node = Node(10)
node4: Node = Node(1)

# link the nodes together
node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

# set random nodes
node0.random = None
node1.random = node0
node2.random = node4
node3.random = node2
node4.random = node0

new_head = answer.copyRandomList(node0)

# print linked list
result = []
curr = new_head
while curr:
    result.append([curr.val , curr.random.val if curr.random else None])
    curr = curr.next

print(result)    # [[7, None], [13, 7], [11, 1], [10, 11], [1, 7]]
