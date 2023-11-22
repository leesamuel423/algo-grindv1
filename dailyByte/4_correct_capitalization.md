# 4. Correct Capitalization

Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

Ex: Given the following strings...
```
"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true
```

## JavaScript Solution
```js
const correctCapitalization = s => {
  const sUpper = s.toUpperCase();
  const sLower = s.toLowerCase();
  const sFirst = s[0].toUpperCase() + s.slice(1).toLowerCase();
  return s === sUpper || s === sLower || s === sFirst;
}
```

## Java Solution
```java
class Solution {
  public boolean correctCapitalization(String s) {
    String sUpper = s.toUpperCase();
    String sLower = s.toLowerCase();
    String sFirst = Character.toUpperCase(s.charAt(0)) + s.substring(1).toLowerCase();

    return s.equals(sUpper) || s.equals(sLower) || s.equals(sFirst);
  }
}
```
### Notes
- `.substring(beginningIndex, endIndex)`, where beginning index is inclusive and end is exclusive

## Python Solution
```py3
class Solution:
  def correct_capitalization(s: str) -> bool:
    s_upper = s.upper()
    s_lower = s.lower()
    s_first = s[0].upper() + s[1:].lower() if s else ''
    return s == s_upper or s == s_lower or s == s_first
```
### Notes
- Slice syntax in py3 is `[start:end]`
- Accessing character at an out-of-bounds index (like s[0] for an empty string s) leads to `IndexError` so conditional needed, whereas JS would just return undefined

## Overall Strategy
- Time Complexity: O(n)
- Space Complexity: O(1)

- Create three strings: one with all uppercase letters, one with all lowercase letters, and one with the first letter capitalized and the rest lowercase
- Return whether or not the input string is equal to any of the three strings

Alternatively
- Create a counter for the number of capital letters
- Iterate through the string, incrementing the counter if the current letter is uppercase
- Return true if the counter is 0, 1, or equal to the length of the string
  - For counter is 1, check if the first letter is uppercase