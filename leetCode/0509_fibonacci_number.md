# 509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

```
Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
```

## JavaScript Solution
```js
const memo = {};
const fib = n => {
  if (memo[n]) return memo[n];
  if (n <= 2) return 1;
  else {
    const result = fib(n - 1) + fib(n - 2);
    memo[n] = result;
    return result;
}
```

## Java Solution
```java
import java.util.HashMap;
import java.util.Map;

public class Fibonacci {
  Map<Integer, Integer> memo = new HashMap<>();

  public int fib(int n) {
    if (memo.containsKey(n)) return memo,get(n);
    if (n <= 2) return 1;
    else {
      int result = fib(n - 1) + fib(n - 2);
      memo.put(n, result);
      return result;
    }
  }
}
```

## Python Solution
```py3
# Memoization Approach
memo = {}
def fib(n):
  if n in memo:
    return memo[n]
  if n <= 2:
    return 1
  else:
    result = fib(n - 1) + fib(n - 2)
  memo[n] = result
  return result
```
### Notes
- Naive approach is O(2^n) time complexity because each call branches into two more calls
- Memoization is O(n) time complexity because each call is only made once
- Note: variables defined in `if` `else` blocks are accessible within the entire function scope (a bit different from JS)

## Overall Strategy
- Time Complexity: O(n)
- Space Complexity: O(n)

- Utilize a memoization approach to store the results of previous calls
- If the result of a call is already in the memo, return the result
- If the result of a call is not in the memo, calculate the result and store it in the memo
- Return the result