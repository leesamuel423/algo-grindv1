# 70. Climbing Stairs

"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""


def __init__(self):
    self.cache = {}


def climbStairs(self, n):
    if n <= 3:
        return n
    if n in self.cache:
        return self.cache[n]
    self.cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
    return self.cache[n]


"""
to get to 1 stair, it is 1 step
to get to 2 stairs it is 2 steps
to get to 3 stairs, it is 3 steps
to get to 4 stairs, it is {{1,1,1,1}, {1,2,1}, {2,1,1}, {1, 1, 2}, {2,2}}, 5 steps

we can see this is fib where we can also cache the number of steps from before
"""
