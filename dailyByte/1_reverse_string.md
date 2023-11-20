# 1. Reverse String

Given a string, reverse all of its characters and return the resulting string.

Ex: Given the following strings...
```
“Cat”, return “taC”
“The Daily Byte”, return "etyB yliaD ehT”
“civic”, return “civic”
```

## JavaScript Solution
```js
const reverseString = s => {
  const final = "";
  for (let i = s.length - 1; i >= 0; i--) {
    final += s[i];
  }
  return final;
}
```

## Java Solution
```java
// Solution 1
class Solution {
  public String reverseString (String s) {
    String final = "";
    for (let i = s.length() - 1; i >= 0; i--) {
      final += s.charAt(i);
    }
    return final;
  }
}
```
### Notes 
- Solution 1 is not very performant because strings are immutable in Java
  - Thus, every time we add new character to string, entirely new copy of the string is made containing the new character
  - To optimize, initialize a buffer to hold the reversed string before returning the results. Use a variable to store the index of where to place the next character  

```java
// Solution 2 (better)
class Solution {
  public String reverseString (String s) {
    char[] characters = new char[s.length()];
    int j = 0;
    for (int i = s.length() - 1; i >= 0; i--) {
      characters[j++] = s.charAt(i);
    }
    return new String(characters);
  }
}

```

## Python Solution
```py3
class Solution:
  def reverseString(s:str) -> str:
    return s[::-1]
```
### Notes
str[::-1] slices string from start to end with step of -1, reversing it

SLICE METHOD
sequence[start:stop:step]
  start - index where slice starts (inclusive)
  stop - index where slice ends (exclusive)
  step - interval between each element in the slice

If you use positive step (ie: step = 2)
  - python retrieves every step-th element from start to stop - 1
  - ie: sequence[0:6:2] will extract elements at index 0, 2, 4

If you use negative step (ie: step = -1)
  - negative step is used to reverse sequence or part of it
  - when using negative, python starts from start and moves backwards
  - if start and stop are ommitted, it reverses the entire sequence
  - ie: sequence[5:1:-1] will extract from 5, 4, 3, 2
  - ie2: sequence[1:10:-1] will extract nothing, because start is greater than stop. Can't decrease 1 to get to 10

Ommitted indices
  - if start is omitted, python defaults to beginning
  - if stop is omitted, slice goes till end

## Overall Strategy
- Time Complexity: O(n)
- Space Complexity: O(n)