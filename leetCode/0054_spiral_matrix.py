# 54. Spiral Matrix
""""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        start_x = 0
        end_x = len(matrix[0])
        start_y = 0
        end_y = len(matrix)

        while start_x < end_x and start_y < end_y:
            for i in range(start_x, end_x):
                res.append(matrix[start_y][i])
            start_y += 1
            for i in range(start_y, end_y):
                res.append(matrix[i][end_x - 1])
            end_x -= 1
            if start_y == end_y or start_x == end_x:
                return res
            for i in range(end_x - 1, start_x - 1, -1):
                res.append(matrix[end_y - 1][i])
            end_y -= 1
            for i in range(end_y - 1, start_y - 1, -1):
                res.append(matrix[i][start_x])
            start_x += 1

        return res


"""
1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7, 8

start_x = 0
end_x = length of matrix[0]
start_y = 0
end_y = length of matrix

res = []

while start_x is not end_x and start_y is not end_y:
  iterate through matrix[start_y] from start_x to end_x and add to res
  start_y += 1
  iterate through matrix from start_y to end_y and add index endx to res
  end_x -= 1
  iterate backwards through matrix[end_y] from end_x to start_x and add to res
  end_y -= 1
  iterate backwards through matrix from end_y to start_y and add index startx to res
  start_x += 1

return res
"""
