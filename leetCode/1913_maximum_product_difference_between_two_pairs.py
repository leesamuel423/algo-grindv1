# 1913. Maximum Product Difference Between Two Pairs
"""
The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.

 

Example 1:

Input: nums = [5,6,2,7,4]
Output: 34
Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.
Example 2:

Input: nums = [4,2,5,9,7,4,8]
Output: 64
Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
The product difference is (9 * 8) - (2 * 4) = 64.
 

Constraints:

4 <= nums.length <= 104
1 <= nums[i] <= 104
"""


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max_1 = float("-inf")
        max_2 = float("-inf")
        min_1 = float("inf")
        min_2 = float("inf")

        for i in nums:
            if i > max_1:
                max_2 = max_1
                max_1 = i
            elif i > max_2:
                max_2 = i
            if i < min_1:
                min_2 = min_1
                min_1 = i
            elif i < min_2:
                min_2 = i

        return max_1 * max_2 - min_1 * min_2


"""
essentially wanna keep track of 2 max and 2 min

max_1 = -inf
max_2 = -inf
min_1 = inf
min_2 = inf

iterate through
if i > max_1:
  max_2 = max_1
  max_1 = i
elif i > max_2:
  max_2 = i
if i < min_1:
  min_2 = min_1
  min_1 = i
elif i < min_2
  min_2 = i


"""
