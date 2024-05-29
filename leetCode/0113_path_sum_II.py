# 113. Path Sum II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        output = []

        def dfs(curr, sum, slate):
            slate.append(curr.val)
            sum += curr.val
            if not curr.left and not curr.right and sum == targetSum:
                output.append(slate)
                return
    
            if curr.left:
                dfs(curr.left, sum, slate[:])
            if curr.right:
                dfs(curr.right, sum, slate[:])
    
        dfs(root, 0, [])
        return output

