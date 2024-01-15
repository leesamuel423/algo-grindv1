# 226. Invert Binary Tree

"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return
    stack = [root]

    while stack:
        current = stack.pop()
        if current.left and current.right:
            [current.right, current.left] = [current.left, current.right]
        elif current.left:
            current.right = current.left
            current.left = None
        elif current.right:
            current.left = current.right
            current.right = None
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return root


# Solution can be solved iteratively

def invertTreeIterative(self, root):
    if root:
        root.left, root.right = self.invertTreeIterative(root.right), self.invertTreeIterative(root.left)
    return root
