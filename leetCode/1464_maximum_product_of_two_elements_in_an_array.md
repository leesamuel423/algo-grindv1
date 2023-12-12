# 1464. Maximum Product of Two Elements in an Array

Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 
```
Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 

Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

Example 3:

Input: nums = [3,7]
Output: 12
```

Constraints:

2 <= nums.length <= 500
1 <= nums[i] <= 10^3

## JavaScript Solution
```js
function maxProduct(nums) {
    let big1 = -Infinity;
    let big2 = -Infinity;

    for (let x of nums) {
        if (x > big1) {
            big2 = big1;
            big1 = x;
        } else if (x > big2) {
            big2 = x;
        }
    }

    return (big1 - 1) * (big2 - 1);
}

```

## Java Solution
```java
public class Solution {
    public int maxProduct(int[] nums) {
        int big1 = Integer.MIN_VALUE;
        int big2 = Integer.MIN_VALUE;

        for (int x : nums) {
            if (x > big1) {
                big2 = big1;
                big1 = x;
            } else if (x > big2) {
                big2 = x;
            }
        }

        return (big1 - 1) * (big2 - 1);
    }
}

```

## Python Solution
```py3
class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    big1 = float('-inf')
    big2 = float('-inf')

    for x in nums:
      if x > big1:
        big2 = big1
        big1 = x
      elif x > big2:
        big2 = x
    
    return (big1 - 1) * (big2 - 1)
```

## Overall Strategy
- Time Complexity: O(n)
- Space Complexity: O(1)

- Iterate through the array and keep track of the two biggest numbers
- Return the product of the two biggest numbers minus 1