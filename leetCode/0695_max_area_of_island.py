# 695. Max Area of Island
"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
      visited = set()
      maximum = 0
      for r in range(len(grid)):
        for c in range(len(grid[0])):
          if grid[r][c] == 1 and (r, c) not in visited:
            maximum = max(maximum, self.bfs(grid, r, c, visited))
      return maximum
    
    def bfs(self, grid, r, c, visited):
      queue = deque([ (r, c) ])
      count = 0

      while queue:
        r, c = queue.popleft()
        rBound = 0 <= r < len(grid)
        cBound = 0 <= c < len(grid[0])

        if not rBound or not cBound or (r, c) in visited or grid[r][c] == 0:
          continue

        visited.add((r, c))
        count += 1


        queue.append((r + 1, c))
        queue.append((r - 1, c))
        queue.append((r, c + 1))
        queue.append((r, c - 1))
      return count 


      

