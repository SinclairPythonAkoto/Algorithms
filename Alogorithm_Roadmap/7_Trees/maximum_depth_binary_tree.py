"""Maximum Depth of Binary Tree

LEETCODE: 104
COMPANY:  Amazon


Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along 
the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2


Solution
- We can use Depth-First Search (DFS) & Breadth-First Search (BFS)
  algorithms to solve this challenge.

- Recursive DFS: We can use a recursive approach to solve this challenge.
       We fist find the root of the tree, then check the left and right nodes
       of of the root.  We are checking if the left and right nodes are not null.
       We check the left node first, then the right node.  We keep doing this untill 
       there are no nodes left.  For each node we check, we count the depth of the node 
       (meaning we count how many child nodes it has).  
       In the code, we return the max values of the left and right nodes, and +1 for the root node.
       This wiill then return the max depth of the tree.

- BFS (Breath-First Search)): 
                 This a level order traversal of the tree. This means we loop through the tree
                 level by level until there are no nodes left.  With this, we can calulate the
                 max depth of the tree by counting the number of levels.
                 We use a stack to keep track of the nodes by appending the nodes of each level.
                 We then pop the nodes off the stack and check if the node is not null.  We keep
                 track of every iteration by incrementing the depth by 1 - this will give us the
                 max depth of the tree.
                 This still uses recursion because we are applying the same logic to each level.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# RECURSIVE DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# ITERATIVE DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res


# BFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        from collections import deque
        q = deque()
        if root:
            q.append(root)

        # keep track of the level
        level = 0

        while q:

            for i in range(len(q)):
                # pop the node off the stack
                node = q.popleft()
                # add to the stack if the node is not null
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # move to the next level
            level += 1
        return level
