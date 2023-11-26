# 118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

![Alt text](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

```
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
```

## JavaScript Solution
```js
const generate = (numRows, output = [[1], [1, 1]]) => {
  if (numRows === 1) return [output[0]];
  if (numRows === 2) return output;

  let currentRow = 3;
  while (currentRow <= numRows) {
    const newArr = new Array(currentRow);
    newArr[0] = 1;
    newArr[currentRow - 1] = 1;
    for (let i = 1; i < newArr.length - 1; i++) {
      newArr[i] = output[currentRow - 2][i - 1] + output[currentRow - 2][i];
    }
    console.log(newArr)
    output.push(newArr);
    currentRow++;
  }
  console.log(output)
  return output;
}
```
```js
// Alternative Solution with Recursion
const generate = function(numRows, output = [[1],[1,1]]) {
    if (numRows == 1) return [output[0]];
    if (numRows == 2) return output;

    let pointer1 = 0;
    let pointer2 = 1;
    let level = [1];
    let prevOutput = output[output.length-1]
    
    while (pointer2<prevOutput.length){
        level.push(prevOutput[pointer1] + prevOutput[pointer2]);
        pointer1++;
        pointer2++;
    }
    level.push(1);
    output.push(level);

    if (output.length == numRows) return output;
    if (output.length != numRows) return generate(numRows, output);
};
/**
 * Time and space complexity is O(n^2) as well, but ...
 * First solution is more straightforward to understand and follows sequential logic easily
 * This recursive solution can be less efficient and more memory-intensive for large `numRows` because each recursive call adds a new layer to the call stack verses an iterative approach working on same callstack.
 *  Possible stack overflow issues for large input sizes
 */
```
## Java Solution
```java
class Solution {
  public List<List<Integer>> generate(int numRows) {
    List<List<Integer>> output = new ArrayList<>(
      Arrays.asList(
        Arrays.asList(1),
        Arrays.asList(1,1)
      )
    );
    if (numRows == 1) return new ArrayList<>(Arrays.asList(output.get(0)));
    if (numRows == 2) return output;

    int rowNum = 3;
    while (rowNum - 1 < numRows) {
      List<Integer> newArr = new ArrayList<>();
      newArr.add(1);

      for (int i = 1; i < rowNum - 1; i++) {
        newArr.add(output.get(rowNum - 2).get(i - 1) + output.get(rowNum - 2).get(i));
      }
      newArr.add(1);
      output.add(newArr);
      rowNum += 1;
    }

    return output;
  }
}
```
## Python Solution
```py3
class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    output = [[1], [1, 1]]
    if numRows == 1:
      return [output[0]]
    if numRows == 2:
      return output

    currentRow = 3

    while currentRow <= numRows:
      newArr = [1] * currentRow
      print(newArr)
      newArr[0] = 1
      newArr[currentRow - 1] = 1
      for i in range(1, currentRow - 1):
        newArr[i] = output[currentRow - 2][i - 1] + output[currentRow - 2][i]
      output.append(newArr)
      currentRow += 1

    return output
```

## Overall Strategy
- Time Complexity: O(n^2) -> Outer loop `while` runs `numRows` times, and inner `for` loop iterates over elements of new row being constructed
- Space complexity: O(n^2) because solution stores entire Pascal's Triangle up to `numRows`

- Initialize base cases of numRows being 1 or 2 (initial two rows of Pascal's triangle)
- Start building from the 3rd row
  - For each row, initialize a new array of the appropriate length, setting first and last elements to be 1
  - Fill in remaining elements based off of previous row's i - 1 and i elements
  - Add newly constructed row to the output array