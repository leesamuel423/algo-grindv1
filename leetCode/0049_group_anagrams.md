# 49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 
```
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
```

## JavaScript Solution
```js
const groupAnagrams = strs => {
  const cache = {};
  for (const str of strs) {
    const sortedStr = str.split('').sort().join('');
    if (cache[finalStr]) cache[finalStr].push(str);
    else cache[finalStr] = [str];
  }
  return Object.values(cache);
}
```

## Java Solution
```java
class Solution {
  public List<List<String>> groupAnagrams(String[] strs) {
    HashMap <String, List<String>> cache = new HashMap<>();
      for (String str : strs) {
        char[] chars = str.toCharArray();
        Arrays.sort(chars);
        String sortedStr = new String(chars);

        cache.computeIfAbsent(sortedStr, k -> new ArrayList<>()).add(str);
      }
    return new ArrayList<>(cache.values());
  }
}
```

## Python Solution
```py3
from collections import defaultdict

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    cache = defaultdict(list)
    for str in strs:
      sorted_str = ''.join(sorted(str))
      cache[sorted_str].append(str)
    return list(cache.values())
```
### Notes
- `defaultdict` from `collections` module to simplify adding items to dictionary. This auto initializes a new list if key is not already present
- Sort characters using `sorted(str)` and join with `''.join(sorted(str))`
- Append original string to list in dict where key is the sorted string
- Return values of dictionary

## Overall Strategy
Time Complexity: O(n * mlogm) -> sort is O(mlogm), where m is length of string, and insertion into hashmap can be O(n) in worst case scenario
Space Complexty: O(n * m) -> n is number of strings and m is average length of strings. If no two strings are anagrams, then dictionary contains as many entires as there are strings, with each entry storing a single string

- Utilize a cache/dictionary/hashmap
- Sort each item in string and check if it is in the dictionary
  - Key value pairs of dictionary are keys-> sorted string, values -> array of original strings