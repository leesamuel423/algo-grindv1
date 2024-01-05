# Vacuum Cleaner Route

Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position. The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively.

Ex: Given the following strings...

```
"LR", return true
"URURD", return false
"RUULLDRD", return true
```

## JavaScript Solution

```js
const vacuumCleanerRoute = (str) => {
  let x = 0;
  let y = 0;

  for (const letter of str) {
    switch (letter) {
      case "L":
        x -= 1;
        break;
      case "R":
        x += 1;
        break;
      case "U":
        y += 1;
        break;
      case "D":
        y -= 1;
        break;
    }
  }

  return x === 0 && y === 0;
};
```

## Java Solution

```java
class Solution {
  public boolean vacuumCleanerRoute(String s) {
    int x = 0, y = 0;

    for (int i = 0; i < s.length(); i++) {
      char letter = s.charAt(i);
    // Can also do for (char letter : s.toCharArray())
      switch (letter) {
        case 'L':
          x -= 1;
          break;
        case 'R':
          x += 1;
          break;
        case 'U':
          y += 1;
          break;
        case 'D':
          y -= 1;
          break;
      }
    }
    return x == 0 && y == 0;
  }
}
```

## Python Solution

```py3
class Solution:
  def vacuum_cleaner_route(s: str) -> bool:
    x, y = 0, 0

    for letter in s:
      match letter:
        case 'L':
          x -= 1
        case 'R':
          x += 1
        case 'U':
          y += 1
        case 'D':
          y -= 1

    return x == 0 and y == 0
```

### Notes

- Bitwise AND (&): This operator performs a bitwise AND operation, where each bit of the output is 1 if the corresponding bits of both operands are 1, otherwise it's 0. It's used for bitwise operations, typically with integers.

- Logical AND (and): This is a logical operator that returns True if both the operands are true. It's used for logical operations, like in conditional statements.

## Overall Strategy

- Time Complexity: O(n)
- Space Complexity: O(1)

- Initialize x and y for the robot's position, with origin (0,0) being original position
- Iterate through the string, updating x and y based on the current letter
- Return whether or not the robot is back at the origin

