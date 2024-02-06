# 944. Rotting Oranges

"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        visited = {}
        rotten = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    self.dfs(grid, r, c, 0, visited)
                    rotten += 1
                if grid[r][c] == 1:
                    rotten += 1

        if rotten != len(visited):
            return -1

        return max(visited.values()) if visited else 0

    def dfs(self, grid, r, c, t, visited):
        valid_r = 0 <= r < len(grid)
        valid_c = 0 <= c < len(grid[0])

        loc = "({},{})".format(r, c)

        if (
            not valid_r
            or not valid_c
            or (loc in visited and visited[loc] < t)
            or grid[r][c] == 0
        ):
            return 0
        else:
            visited[loc] = t

        self.dfs(grid, r + 1, c, t + 1, visited)
        self.dfs(grid, r - 1, c, t + 1, visited)
        self.dfs(grid, r, c + 1, t + 1, visited)
        self.dfs(grid, r, c - 1, t + 1, visited)


"""
try with dfs => should be better with bfs but just for challenge
visited set() -> store as a tuple(r, c)

iterate through r
  iterate through c
    if [r][c] is a rotten orange and it is not in visited:
      apply dfs

dfs (grid, r, c, t visited)
  row range 
  col range

  if it is not in row range or not in col range or in visited or is 0:
    return 
  
  add tuple (r,c) to visited set

  dfs up 
  dfs down
  dfs right
  dfs left

  return time



"""
