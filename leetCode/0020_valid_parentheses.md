# 20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
```
Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false
```

## JavaScript Solution
```js
const isValid = function(s) {
  const stack = [];
  const pairs = {
    "]": "[",
    "}": "{",
    ")": "("
  }

  for (const el of s) {
    if (el === "[" || el === "{" || el === "(") stack.push(el);
    else if (pairs[el]) {
      if (stack[stack.length - 1] !== pairs[el]) return false;
      stack.pop();
    }
  }
  return stack.length ? false : true;
};
```

## Java Solution
```java
class Solution {
  public boolean isValid(String s) {
    Stack<Character> stack = new Stack<>();
    HashMap<Character, Character> pairs = new HashMap<>();
    pairs.put('}', '{');
    pairs.put(']', '[');
    pairs.put(')', '(');

    for (int i = 0; i < s.length(); i++) {
      char c = s.charAt(i);
        if (pairs.containsKey(c)) {
          if (stack.isEmpty() || stack.pop() != pairs.get(c)) return false;
        } else {
            stack.push(c);
        }
    }
    return stack.isEmpty();
  }
}
```

## Python Solution
```py3
class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    pairs = {
      ')': '(', 
      '}': '{', 
      ']': '['
    }

    for c in s:
      if c in pairs:
        if not stack or stack.pop() != pairs[c]:
          return False
      else:
          stack.append(c)
    return not stack
```

## Overall Strategy
- Time Complexity: O(n)
- Space Complexity: O(n)
- Use a stack to keep track of the opening brackets
- If we encounter a closing bracket, we check if the top of the stack is the corresponding opening bracket
  - If it is, we pop it off the stack
  - If it is not, then we return false
- If we encounter an opening bracket, we push it onto the stack
- If we reach the end of the string, we return true if the stack is empty, and false if it is not