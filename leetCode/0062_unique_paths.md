# 62. Unique Paths

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 \* 109.

'''
Example 1:
![Alt text](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:

1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
   '''

## JavaScript Solution

```js
const uniquePaths = function (m, n) {
	const cache = new Map();

	const backtrack = (x, y) => {
		const key = `${x}, ${y}`;
		if (cache.has(key)) return cache.get(key);
		if (x === 0 && y === 0) {
			return 1;
		}
		let right = 0;
		let down = 0;
		if (x > 0) right = backtrack(x - 1, y);
		if (y > 0) down = backtrack(x, y - 1);

		const total = right + down;
		cache.set(key, total);

		return total;
	};

	return backtrack(m - 1, n - 1);
};
```

## Java Solution

```java
public class Solution {
    public int uniquePaths(int m, int n) {
        return backtrack(m - 1, n - 1, new Integer[m][n]);
    }

    private int backtrack(int x, int y, Integer[][] cache) {
        if (x == 0 && y == 0) {
            return 1;
        }

        if (cache[x][y] != null) {
            return cache[x][y];
        }

        int right = 0, down = 0;
        if (x > 0) {
            right = backtrack(x - 1, y, cache);
        }
        if (y > 0) {
            down = backtrack(x, y - 1, cache);
        }

        cache[x][y] = right + down;
        return cache[x][y];
    }
}

```

## Python Solution

```py3
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def backtrack(x, y, cache = {}):
          if (x, y) in cache:
            return cache[(x, y)]
          if x == 0 and y == 0:
            return 1

          right = down = 0
          if x > 0:
            right = backtrack(x - 1, y, cache)
          if y > 0:
            down = backtrack(x, y - 1, cache)
          cache[(x, y)] = right + down

          return right + down

        return backtrack(m - 1, n - 1)
```

## Overall Strategy

- Time Complexity: O(m \* n)
- Space Complexity: O(m \* n)

- Backtracking with memoization
- This is a classic backtracking problem. We can either go right or down. We can use memoization to cache the results of the subproblems.
