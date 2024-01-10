# 278 First Bad Version

"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
 

Constraints:

1 <= bad <= n <= 231 - 1


Test Case Better:

You are given anonymous function that checks if passed in value is greater than 18
test 1 = solution(anonymous_function)

print(test1(32))

1            16              32
start        mid             end
#1 API Call on mid => false
  start = mid + 1

17           24             32
start       mid             end

#2 API Call on mid => true
  end = mid - 1

until start end same
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


def firstBadVersion(self, n: int) -> int:
    i = 1
    j = n
    while i <= j:
        mid = (i + j) // 2
        if isBadVersion(mid):
            j = mid - 1
        else:
            i = mid + 1
    return i
