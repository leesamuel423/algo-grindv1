# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_volume = float("-inf")
        while left < right:
            curr_volume = min(height[left], height[right]) * (right - left)
            max_volume = max(max_volume, curr_volume)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_volume
