# 1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
 
```
Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
```

## JavaScript Solution
```js
const runningSum = function(nums) {
  for (let i = 1; i < nums.length; i++) {
    nums[i] += nums[i - 1];
  }
  return nums;
};
```

## Java Solution
```java
class Solution {
  public int[] runningSum(int[] nums) {
    for (int i = 1; i < nums.length; i++) {
      nums[i] += nums[i - 1];
    }
    return nums;
  }
}
```

## Python Solution
```py3
class Solution:
  def runningSum(self, nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
      nums[i] += nums [i - 1]
    return nums
```

## Overall Strategy
- Time Complexity: O(n)
- Space Complexity: O(1)
- Iterate through the array and add the previous element to the current element. This will give us the running sum of the array.