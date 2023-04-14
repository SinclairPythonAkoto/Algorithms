"""Invert Binary Tree

LEETCODE: 226
COMPANY:  Google

Given the root of a binary tree, invert the tree, and return its root.

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Input: root = [2,1,3]
Output: [2,3,1]

Input: root = []
Output: []

Solution
- We have to look at the root node, take it's children and then 
  swap (invert) their positions. We keep doing this recursively
  until we meet the end of the tree. 
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # swap the children
        # store left in tmp variable
        tmp = root.left
        # swap the L with R
        root.left = root.right
        # swap R with L
        root.right = tmp

        # recursive call to function (both L & R)
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    

def print_inorder(root) -> List[TreeNode]:
    if root is None:
        return []
    result: List[TreeNode] = []
    result.append(root.val)
    result += print_inorder(root.left)
    result += print_inorder(root.right)
    return result


answer: Solution = Solution()

node1: TreeNode = TreeNode(1)
node3: TreeNode = TreeNode(3)
node6: TreeNode = TreeNode(6)
node9: TreeNode = TreeNode(9)
node2: TreeNode = TreeNode(2, node1, node3)
node7: TreeNode = TreeNode(7, node6, node9)
root: TreeNode = TreeNode(4, node2, node7)

inverted_root = answer.invertTree(root)

inverted_values = print_inorder(inverted_root)

print(inverted_values)    # [4, 7, 9, 6, 2, 3, 1]