# 3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.


## JavaScript Solution
```js
const lengthOfLongestSubstring = n => {
    const cache = {};
    let maxCount = 0;
    let startIdx = 0;
    for (let i = 0; i < n.length; i++) {
        const currentChar = n[i];
        if (cache[currentChar] !== undefined && cache[currentChar] >= startIdx) { //careful HERE
            startIdx = cache[currentChar] + 1;
        }
        cache[currentChar] = i;
        maxCount = Math.max(maxCount, i - startIdx + 1);
    }
    return maxCount;
};
```
### Notes
- If a character hasn't been seen before, its value in the cache object would be undefined. However, the check `cache[currentChar]` will evaluate to false not only for undefined but also for 0. This means that if the first character (at index 0) is repeated later in the string, it won't be correctly handled because 0 is falsy in JavaScript.

## Java Solution
```java
class Solution {
  public int lengthOfLongestSubstring(String s) {
    HashMap<Character, Integer> cache = new HashMap<>();
    int maxCount = 0;
    int startIdx = 0;

    for (int i = 0; i < s.length(); i++) {
      char currentChar = s.charAt(i);

      if (cache.containsKey(currentChar) && cache.get(currentChar) >= startIdx) {
        startIdx = cache.get(currentChar) + 1;
      }

      cache.put(currentChar, i);
      maxCount = Math.max(maxCount, i - startIdx + 1);
    }
    return maxCount;
  }
}
```

## Python Solution
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        max_count = 0
        start_index = 0
        for i, char in enumerate(s):
            if char in hashmap and hashmap[char] >= start_index:
                start_index = hashmap[char] + 1
            hashmap[char] = i
            max_count = max(max_count, i - start_index + 1)
        return max_count
```

## Overall Strategy
- Use sliding window approach with data structure (HashMap or dictionary) to track characters and their indices in the string
- As you iterate thorugh string, keep track of start index of the current window and the end index (current character's index)
- Check if it is in dictionary, and when repeat detected, start index of window "slides" forward to one index after repeated character

- Time Complexity: O(n)
- Space Complexity: O(min(m, n)), where n is size of string and m is size of character set or alphabet