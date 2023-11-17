# 1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

```
Example 1:
  Input: nums = [2,7,11,15], target = 9
  Output: [0,1]
  Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
  Input: nums = [3,2,4], target = 6
  Output: [1,2]

Example 3:
  Input: nums = [3,3], target = 6
  Output: [0,1]
```

## JavaScript Solution
```javascript
const twoSum = (nums, target) => {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    const remainder = target - nums[i];
    if (map.has(remainder)) return [i, map.get(remainder)];
    map.set(nums[i], i);
  }
}
```

## Java Solution
```java
class Solution {
  public int[] twoSum(int[] nums, int target) {
    HashMap <Integer, Integer> cache = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
      int remainder = target - nums[i];
      if (cache.containsKey(remainder)) return new int[]{i, cache.get(remainder)};
      cache.put(nums[i], i);
    }
    throw new IllegalArgumentException("no solution is found");
  }
}
```
### Notes
- Java is strongly typed => types are explicitly declared and enforced as well as statically typed => types are checked at compile time
  - note that `int[]` after public is declaring that the method returns an array of integers
- `HashMap` in Java is collection that stores key-value pairs, and the key-values are also typed
  - HashMap `.containsKey` method checks if key is mapped into HashMap or not
  - HashMap `.get` method returns value stored in key
  - HashMap `.put` method stores `(key, value)`
- When returning array as solution, need to declare new instance of array and pass in items inside `{}`
  - Arrays are immutable (size fixed once created)
- The throw new IllegalArgumentException("no solution is found"); is an example of Java's exception handling mechanism. It's used here to indicate an error condition when no solution exists.

## Python Solution
```python
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i, num in enumerate(nums):
      remainder = target - num
      if remainder in hashmap:
        return [hashmap[remainder], i]
      hashmap[num] = i
```
### Notes
- Python is dynamically typed, so don't have to declare variable types. However, adding type hints (like `List[int]`) allow for better code readability and help with type checking in certain dev env
- Dictionaries in Python -> think of HashMap. Store key-values
  - Checking `if remainder in hashmap` checks if key exists in dictionary
- 'enumerate' function adds counter to an iterable. Here it is used to get both the index (`i`) and the value (`num`) of each element in list `nums`.

## Overall Strategy
- Can utilize a double for loop, but that would give O(n^2) time complexity
- Rather, utilizing a cache (HashMap) will allow for one iteration thorugh original nums array, thereby decreasing time complexity to O(n)
- Space complexity is O(n). Size of the dictionary/map grows linearly with number of elements in the array `nums`