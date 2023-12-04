# 36. Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

![Alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```
## JavaScript Solution
```js
// Brute Force
const isValidSudoku = function(board) {
  const columnCheck = {};
  const subBox1 = {};
  const subBox2 = {};
  const subBox3 = {};
  const subBox4 = {};
  const subBox5 = {};
  const subBox6 = {};
  const subBox7 = {};
  const subBox8 = {};
  const subBox9 = {};
  for (let i = 0; i < board.length; i++) { // rows
    const rowCheck = {};
    for (let j = 0; j < board.length; j++) { // column
      const digit = board[i][j];
      if (digit !== '.') {
        if (!columnCheck[j]) columnCheck[j] = {};
        console.log('columnCheck', columnCheck, 'rowCheck', rowCheck)
        if (rowCheck[digit] || columnCheck[j][digit]) return false; // checking if it already exists in row or column
        if (i < 3 && j < 3) {
          if (subBox1[digit]) return false;
          subBox1[digit] = true;
        } else if (i < 3 && j < 6) {
          if (subBox2[digit]) return false;
          subBox2[digit] = true;
        } else if (i < 3 && j < 9) {
          if (subBox3[digit]) return false;
          subBox3[digit] = true;
        } else if (i < 6 && j < 3) {
          if (subBox4[digit]) return false;
          subBox4[digit] = true;
        } else if (i < 6 && j < 6) {
          if (subBox5[digit]) return false;
          subBox5[digit] = true;
        } else if (i < 6 && j < 9) {
          if (subBox6[digit]) return false;
          subBox6[digit] = true;
        } else if (i < 9 && j < 3) {
          if (subBox7[digit]) return false;
          subBox7[digit] = true;
        } else if (i < 9 && j < 6) {
          if (subBox8[digit]) return false;
          subBox8[digit] = true;
        } else if (i < 9 && j < 9) {
          if (subBox9[digit]) return false;
          subBox9[digit] = true;
        }
        rowCheck[digit] = true;
        columnCheck[j] ? columnCheck[j][digit] = true : columnCheck[j] = {digit: true};
      }
    }
  }
  return true;
};
// Can be cleaned up a lot
```
```js
// Clean Hash Set Solution 
const isValidSudoku = function(board) {
  const n = 9;

  const rows = new Array(n);
  const cols = new Array(n);
  const boxes = new Array(n);
  for (let r = 0; r < n; r++) {
    rows[r] = new Set();
    cols[r] = new Set();
    boxes[r] = new Set();
  }

  for (let r = 0; r < n; r++) {
    for (let c = 0; c < n; c++) {
      const val = board[r][c];

      if (val === '.') continue;

      // check row
      if (rows[r].has(val)) return false;
      rows[r].add(val);

      // check column
      if (cols[c].has(val)) return false;
      cols[c].add(val);

      // check the box
      const idx = Math.floor(r / 3) * 3 + Math.floor(c / 3);
      if (boxes[idx].has(val)) return false;
      boxes[idx].add(val);
    }
  }
  
  return true;
};
```

## Java Solution
```java
class Solution {
  public boolean isValidSudoku(char[][] board) {
    int N = 9;

    // Use hash set to record the status
    HashSet<Character>[] rows = new HashSet[N];
    HashSet<Character>[] cols = new HashSet[N];
    HashSet<Character>[] boxes = new HashSet[N];
    for (int r = 0; r < N; r++) {
      rows[r] = new HashSet<Character>();
      cols[r] = new HashSet<Character>();
      boxes[r] = new HashSet<Character>();
    }

    for (int r = 0; r < N; r++) {
      for (int c = 0; c < N; c++) {
        char val = board[r][c];

        // Check if the position is filled with number
        if (val == '.') {
          continue;
        }

        // Check the row
        if (rows[r].contains(val)) {
          return false;
        }
        rows[r].add(val);

        // Check the column
        if (cols[c].contains(val)) {
          return false;
        }
        cols[c].add(val);

        // Check the box
        int idx = (r / 3) * 3 + c / 3;
        if (boxes[idx].contains(val)) {
          return false;
        }
        boxes[idx].add(val);
      }
    }
    return true;
  }
}

```

## Python Solution
```py3
class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    N = 9

    # Use hash set to record the status
    rows = [set() for _ in range(N)]
    cols = [set() for _ in range(N)]
    boxes = [set() for _ in range(N)]

    for r in range(N):
      for c in range(N):
        val = board[r][c]
        # Check if the position is filled with number
        if val == ".":
          continue

        # Check the row
        if val in rows[r]:
          return False
        rows[r].add(val)

        # Check the column
        if val in cols[c]:
          return False
        cols[c].add(val)

        # Check the box
        idx = (r // 3) * 3 + c // 3
        if val in boxes[idx]:
          return False
        boxes[idx].add(val)

    return True

```

## Overall Strategy
- Time Complexity: O(n^2)
- Space Complexity: O(n^2)

- Can use a hash set to store the values in each row, column, and box
- Iterate through each row, column, and box and check if the value is already in the hash set
- If it is, then return false
- If it is not, then add it to the hash set