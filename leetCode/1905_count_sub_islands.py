# 1905. Count Sub Islands
"""
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

 

Example 1:


Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
Example 2:


Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
 

Constraints:

m == grid1.length == grid2.length
n == grid1[i].length == grid2[i].length
1 <= m, n <= 500
grid1[i][j] and grid2[i][j] are either 0 or 1.
"""


class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        v = set()
        # count variable
        count = 0
        # iterate through rows
        for r in range(len(grid2)):
            # iterate throughc columns
            for c in range(len(grid2[0])):
                # run dfs with the grid1, grid2, r, c, visited
                if (
                    (r, c) not in v
                    and grid2[r][c] == 1
                    and self.dfs(grid1, grid2, r, c, v)
                ):
                    count += 1

        # return count
        return count

    def dfs(self, grid1, grid2, r, c, v):
        # set up row and column boundaries, they must be in range 0 to end
        row_bound = 0 <= r < len(grid2)
        col_bound = 0 <= c < len(grid2[0])
        # set up false possibilities
        # not in row bound, not in col bound, in visited, grid2[r][c] is a 0, grid1[r][c] is a 0
        if not row_bound or not col_bound or grid2[r][c] == 0 or (r, c) in v:
            return True
        elif grid2[r][c] == 1 and grid1[r][c] == 0:
            return False
        elif grid2[r][c] == 1 and grid1[r][c] == 1:
            v.add((r, c))

        # run self.dfs on r + 1, r - 1, c + 1, c - 1
        up = self.dfs(grid1, grid2, r + 1, c, v)
        down = self.dfs(grid1, grid2, r - 1, c, v)
        right = self.dfs(grid1, grid2, r, c + 1, v)
        left = self.dfs(grid1, grid2, r, c - 1, v)

        return up and down and right and left
