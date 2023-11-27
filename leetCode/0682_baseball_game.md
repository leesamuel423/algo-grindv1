# 682. Baseball Game

You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

 ```
Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
Example 2:

Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
Example 3:

Input: ops = ["1","C"]
Output: 0
Explanation:
"1" - Add 1 to the record, record is now [1].
"C" - Invalidate and remove the previous score, record is now [].
Since the record is empty, the total sum is 0.
```

## JavaScript Solution
```js
function calPoints(operations) {
  const stack = [];
  let s = 0;
  operations.forEach(op => {
    switch (op) {
      case '+':
        stack.push(stack[stack.length - 1] + stack[stack.length - 2]);
        s += sum;
        break;
      case 'D':
        stack.push(2 * stack[stack.length - 1]);
        s += doubleLast;
        break;
      case 'C':
        s -= stack.pop();
        break;
      default:
        stack.push(parseInt(op));
        s += num;
    }
  });
  return s;
}

```

## Java Solution
```java
import java.util.List;
import java.util.ArrayList;

public class Solution {
  public int calPoints(List<String> operations) {
    List<Integer> stack = new ArrayList<>();
    int s = 0;

    for (String i : operations) {
      switch (i) {
        case "+":
          stack.add(stack.get(stack.size() - 1) + stack.get(stack.size() - 2));
          s += sum;
          break;
        case "D":
          stack.add(2 * stack.get(stack.size() - 1));
          s += doubleLast;
          break;
        case "C":
          s -= stack.remove(stack.size() - 1);
          break;
        default:
          stack.add(Integer.parseInt(op));
          s += num;
      }
    }
    return s;
  }
}
```

## Python Solution
```py3
class Solution:
  def calPoints(self, operations: List[str]) -> int:
    stack = []
    s = 0
    for i in operations:
      if i == '+':
        stack.append(stack[-1] + stack[-2])
        s += stack[-1]
      elif i == 'D':
        stack.append(2 * stack[-1])
        s += stack[-1]
      elif i == 'C':
        s -= stack.pop()
      else:
        stack.append(int(i))
        s += stack[-1]
    return s
```

## Overall Strategy
- Time Complexity: O(n)
- Space Complexity: O(n)

- Initialize a stack and a sum variable
- Iterate through the operations array
- If the current operation is a '+', then push the sum of the last two elements in the stack to the stack and add that sum to the sum variable
- If the current operation is a 'D', then push the double of the last element in the stack to the stack and add that double to the sum variable
- If the current operation is a 'C', then pop the last element in the stack and subtract that element from the sum variable
- Otherwise, the current operation is a number, so push that number to the stack and add that number to the sum variable
- Return the sum variable