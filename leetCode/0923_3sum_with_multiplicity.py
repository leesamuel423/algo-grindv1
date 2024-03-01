# 923. 3Sum With Multiplicity
"""
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
Example 2:

Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
Example 3:

Input: arr = [2,1,3], target = 6
Output: 1
Explanation: (1, 2, 3) occured one time in the array so we return 1.
 

Constraints:

3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300
"""

from collections import Counter
import math


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        res = 0
        cnt = Counter(arr)

        i = 0
        while i < len(arr) - 2:
            j = i
            k = len(arr) - 1
            while j < k:
                total = arr[i] + arr[j] + arr[k]
                if total < target:
                    j += cnt[arr[j]]
                elif total > target:
                    k -= cnt[arr[k]]
                else:
                    if arr[i] != arr[j] != arr[k]:
                        res += cnt[arr[i]] * cnt[arr[j]] * cnt[arr[k]]
                    elif arr[i] == arr[j] != arr[k]:
                        res += math.comb(cnt[arr[j]], 2) * cnt[arr[k]]
                    elif arr[i] != arr[j] == arr[k]:
                        res += math.comb(cnt[arr[j]], 2) * cnt[arr[i]]
                    else:
                        res += math.comb(cnt[arr[i]], 3)
                    j += cnt[arr[j]]
                    k -= cnt[arr[k]]
            i += cnt[arr[i]]
        return res % 100000000
