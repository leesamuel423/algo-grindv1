# 125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

```
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

## JavaScript Solution
```js
const validPalindrome = s => {
  // helper function to check if is letter or digit
  const isLetterOrDigit = char => {
    return /^[a-z0-9]+$/i.test(char);
  }

  if (!s.length) return true;
  let start = 0;
  let last = s.length - 1;
  while (start <= last) {
    const firstChar = s[start];
    const lastChar = s[last];
    if (!isLetterOrDigit(firstChar)) start++;
    else if (!isLetterOrDigit(lastChar)) last--;
    else {
      if (firstChar.toLowerCase() !== lastChar.toLowerCase()) return false;
      start++;
      last--;
    }
  }
  return true;
};
```

## Java Solution
```java
class Solution {
  public boolean isPalindrome(String s) {
    if (s.isEmpty()) return true;
    
    int start = 0;
    int last = s.length() - 1;
    while (start <= last) {
      char firstChar = s.charAt(start);
      char lastChar = s.charAt(last);
      if (!Character.isLetterOrDigit(firstChar)) start++;
      else if (!Character.isLetterOrDigit(lastChar)) last--;
      else {
        if (Character.toLowerCase(firstChar) != Character.toLowerCase(lastChar)) return false;
        start++;
        last--;
      }
    }
    return true;
  }
}
```

## Python Solution
```py3
class Solution:
  def is_palindrome(s: str) -> bool:
    start, end = 0, len(s) - 1

    while start <= end:
      if not s[start].isalnum():
        start += 1
      elif not s[end].isalnum():
        end -= 1
      else:
        if s[start].lower() != s[end].lower():
          return False
            start += 1
            end -= 1

    return True
```

## Overall Strategy
- Time Complexity: O(n)
- Space Complexity: O(1)

- Utilize two pointers on both ends and check whether they are pointing to the same value (only taking into account alphabet and numbers)
