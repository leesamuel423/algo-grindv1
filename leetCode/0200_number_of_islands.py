# 200. Number of Islands
"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        visited = set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                count += self.dfs(grid, r, c, visited)
        return count

    def dfs(self, grid, r, c, visited):
        row_range = 0 <= r < len(grid)
        col_range = 0 <= c < len(grid[0])

        if not row_range or not col_range or (r, c) in visited or grid[r][c] == "0":
            return 0

        visited.add((r, c))

        self.dfs(grid, r + 1, c, visited)
        self.dfs(grid, r - 1, c, visited)
        self.dfs(grid, r, c + 1, visited)
        self.dfs(grid, r, c - 1, visited)

        return 1
