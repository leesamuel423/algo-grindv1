# 104. Maximum Depth of Binary Tree
"""

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2

dfs => recursively 
add count as parameter to recursive solution
base case: if we are at the end (no left, right) return 
left = recurisvely call on left , +1 
right = recursively call on right, +1
return max

"""


def maxDepth(self, root, count=0):
    if not root:
        return count

    left = self.maxDepth(root.left, count + 1)
    right = self.maxDepth(root.right, count + 1)

    return max(left, right)


def max_depth_alternate(self, root):
    """alternate solution to max depth"""
    if not root:
        return 0

    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)

    return max(left, right) + 0
