# 238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
 
```
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

## JavaScript Solution
```js
const productExceptSelf = function(nums) {
  const ans = Array(nums.length).fill(1)
  let r = 1;
  for (let i = 1; i < nums.length; i++) {
    ans[i] = ans[i - 1] * nums[i - 1]
  }
  for (let i = nums.length - 1; i >= 0; i--) {
    ans[i] = ans[i] * r;
    r *= nums[i]
  }

  return ans
};
```

## Java Solution
```java
public class Solution {
  public int[] productExceptSelf(int[] nums) {
    int[] ans = new int[nums.length];
    java.util.Arrays.fill(ans, 1);
    int r = 1;
    
    for (int i = 1; i < nums.length; i++) {
      ans[i] = ans[i - 1] * nums[i - 1];
    }
    
    for (int i = nums.length - 1; i >= 0; i--) {
      ans[i] = ans[i] * r;
      r *= nums[i];
    }
    
    return ans;
  }
}

```

## Python Solution
```py3
# Solution 1 - O(n) time, O(n) space
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    left = [1] * len(nums)
    right = [1] * len(nums)
    ans = [1] * len(nums)
    for i in range(1, len(nums)):
      left[i] = left[i - 1] * nums[i - 1]
    for i in reversed(range(len(nums) - 1)):
      right[i] = nums[i + 1] * right[i + 1]
    for i in range(len(nums)):
      ans[i] = left[i] * right[i]
    
    return ans
# The solution is to use two arrays, `left` and `right`, to store the product of all elements to the left and right of the current element, respectively. Then, the product of all elements except the current element is `left[i] * right[i]`.
```
```py3
# Solution 2 - O(n) time, O(1) space
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    ans = [1] * len(nums)
    right = 1
    for i in range(1, len(nums)):
      ans[i] = ans[i - 1] * nums[i - 1]
    for i in reversed(range(len(nums))):
      ans[i] = ans[i] * right
      right *= nums[i]
    
    return ans
```

## Overall Strategy
- Time Complexity: O(n)
- Space Complexity: O(1)

- Initialize just output array and right product variable.
- First loop: calculate left product and store in output array.
- Second loop: calculate right product and multiply with left product stored in ans to get final answer.
  - Make sure to update right product variable.