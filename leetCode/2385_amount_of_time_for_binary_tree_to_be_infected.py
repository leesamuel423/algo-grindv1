# 2385. Amount of Time for Binary Tree to Be Infected
"""
You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

 

Example 1:


Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.
Example 2:


Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 105
Each node has a unique value.
A node with a value of start exists in the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = defaultdict(list)
        self.adjacency_graph(root, adj)
        print(adj)
        return self.infect(adj, start)

    def adjacency_graph(self, root, adj):
        """need to include parent node in adj"""
        queue = deque([root])

        while queue:
            curr = queue.popleft()

            if curr.left:
                adj[curr.val].append(curr.left.val)
                adj[curr.left.val].append(curr.val)
                queue.append(curr.left)
            if curr.right:
                adj[curr.val].append(curr.right.val)
                adj[curr.right.val].append(curr.val)
                queue.append(curr.right)

    def infect(self, adj, inf):  # this is a bfs
        queue = deque([(inf, 0)])
        infected = set()
        infected.add(inf)
        maxtime = 0

        while queue:
            curr, time = queue.popleft()

            for i in adj[curr]:
                if i not in infected:
                    queue.append((i, time + 1))
                    infected.add(i)
                else:
                    maxtime = max(maxtime, time)
        return maxtime
