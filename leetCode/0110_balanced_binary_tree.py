# 110. Balanced Binary Tree
"""
Given a binary tree, determine if it is 
height-balanced
.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0, True
            left, is_left_balanced = dfs(node.left)
            right, is_right_balanced = dfs(node.right)

            if not is_left_balanced or not is_right_balanced:
                return 0, False

            if abs(left - right) > 1:
                return 0, False

            return max(left, right) + 1, True

        _, isBalanced = dfs(root)
        return isBalanced
