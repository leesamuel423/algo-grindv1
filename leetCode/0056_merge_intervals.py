# 56. Merge Intervals
"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        final = []
        for el in intervals:
            if not final or final[-1][1] < el[0]:
                final.append(el)
            elif final[-1][1] < el[1]:
                final[-1][1] = el[1]
        return final


"""
sort first
final = []
iterate through intervals
  if final is empty or index 1 of last value in final is less than index 0 of el
    append to final
  else:
    replace index 1 of last val in final with index 1 of el
return final
"""
