# 314. Binary Tree Vertical Order Traversal
"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(root, 0, 0)])
        cache = defaultdict(list)

        while queue:
            curr, r, c = queue.popleft()
            cache[c].append(curr.val)
            if curr.left:
                queue.append((curr.left, r + 1, c - 1))
            if curr.right:
                queue.append((curr.right, r + 1, c + 1))

        entries = list(cache.items())
        entries.sort()
        return [val for _, val in entries]


"""
think of each node as coordinate points
                    3 (0,0) (row, col)
          /                  \
        9(1, -1)               8(1, 1)
      /     \                 /       \
  4(2, -2)    0(2, 0)      1(2, 0).    7(2, 2)

We want to order by col in big output, and within the smaller array, order if it is in the same row


{
  col: [(value, row)]
  0:[(3, 0)]
}


def:
  if root doesn't exist, return []
  final = []
  initialize a queue (deque) with initial root and coordinate point(0,0)
  cache = defaultdict

  while queue exists:
    current, row, col destructured from leftpop of queue
    cache[col] is (current value, row)
    if left node exists, add to queue
    if right node exists, add to queue
    
  ---sorting cache to add to final---
  sort by key
  sort by value if in same row

  return final
"""
