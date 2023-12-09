# 128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 
```
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

## JavaScript Solution
```js
const longestConsecutive = function(nums) {
  if (nums == null || nums.length === 0) return 0;
  
  const set = new Set(nums);
  let max = 0;

  for (let num of set) {
    if (!set.has(num - 1)) {
      let currNum = num;
      let currMax = 1;

      while (set.has(currNum + 1)) {
        currNum++;
        currMax++;
      }
      max = Math.max(max, currMax);
    }
  }

  return max;
};
```
### Notes
- If you do this with a normal object / map, you will need to `parseInt` the keys
- If you do this with a Set, types are preserved so no need to convert to int

## Java Solution
```java
class Solution {
  public int longestConsecutive(int[] nums) {
    Set <Integer> set = new HashSet<>();
    for (int num : nums) {
      set.add(num);
    }

    int max = 0;

    for (int num: set) {
      if (!set.contains(num - 1)) {
        int currNum = num;
        int currMax = 1;

        while (set.contains(currNum + 1)) {
          currNum += 1;
          currMax += 1;
        }

        max = Math.max(max, currMax);
      }
    }
    return max;        
  }
}
```

## Python Solution
```py3
class Solution:
  def longestConsecutive(self, nums):
    if not nums:
      return 0

    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
      if num - 1 not in num_set:
        current_num = num
        current_streak = 1

        while current_num + 1 in num_set:
          current_num += 1
          current_streak += 1

        longest_streak = max(longest_streak, current_streak)

    return longest_streak
```

## Overall Strategy
- Time Complexity: O(n) - Because we iterate through the set twice, but the second iteration is only for the numbers that start a sequence, the time complexity is O(n + n) -> O(n)
- Space Complexity: O(n)

- Use a set to store all the numbers
- Iterate through the set
- If the current number - 1 is not in the set, then we know that we have the start of a sequence
- We then iterate through the set again, incrementing the current number and the current max
- We keep track of the max and return it at the end
