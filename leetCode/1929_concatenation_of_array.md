# 1929. Concatenation of Array

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
 
```
Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
```

## JavaScript Solution
```js
const getConcatenation = function(nums) {
  return nums.concat(nums);
};
```

## Java Solution
```java
class Solution {
  public int[] getConcatenation(int[] nums) {
    int[] ans = new int[2 * nums.length];
    System.arraycopy(nums, 0, ans, 0, nums.length);
    System.arraycopy(nums, 0, ans, nums.length, nums.length);
    return ans;
  }
}
```
### Notes
- `System.arraycopy()` is a native method that copies a range of elements from one array to another. It's faster than a for loop.
- `System.arraycopy(Object src, int srcPos, Object dest, int destPos, int length)`
  - `src` - This is the source array.
  - `srcPos` - This is the starting position in the source array.
  - `dest` - This is the destination array.
  - `destPos` - This is the starting position in the destination data.
  - `length` - This is the number of array elements to be copied.
- Time Complexity: O(n)
- Space Complexity: O(n)

## Python Solution
```py3
class Solution:
  def getConcatenation(self, nums: List[int]) -> List[int]:
    return nums + nums
```

## Overall Strategy
- Time Complexity: O(n)
- Space Complexity: O(n)

