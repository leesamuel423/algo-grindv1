# 169. Majority Element
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""


class Solution:
    def majorityElement(self, nums):
        cache = {}

        for num in nums:
            cache[num] = cache[num] + 1 if num in cache else 1

        maximum = float("-inf")
        maximum_val = None
        for item in cache:
            if cache[item] > maximum:
                maximum = cache[item]
                maximum_val = item

        return maximum_val
