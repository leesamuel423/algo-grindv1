# 283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

```
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
```

## JavaScript Solution
```js
const moveZeroes = nums => {
  let left = 0;
  for (let right = 0; right < nums.length; right++) {
    if (nums[right]) {
      [nums[left], nums[right]] = [nums[right], nums[left]];
      left++;
    }
  }
  return nums;
}
```

## Java Solution
```java
class Solution {
    public void moveZeroes(int[] nums) {
      int left = 0;
      for (int right = 0; right < nums.length; right++) {
        if (nums[right] != 0) {
          // there is no shortcut for swapping in Java
          int temp = nums[right];
          nums[right] = nums[left];
          nums[left] = temp;
          left++;
        }
      }
    }
}
```

## Python Solution
```py3
class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    left = 0
    for right in range(len(nums)):
      if nums[right]:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
    return nums
```

## Overall Strategy
- Time Complexity: O(n)
- Space Complexity: O(1)

- Two pointers, left and right
- Iterate through the array with the right pointer
- If the right pointer is not 0, swap the left and right values and increment the left pointer
