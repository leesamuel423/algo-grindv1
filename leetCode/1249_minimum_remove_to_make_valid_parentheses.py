# 1249. Minimum Remove to Make Valid Parentheses

"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        final = ""
        removed_indices = {}

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if not stack:
                    removed_indices[i] = True
                else:
                    stack.pop()

        for i in stack:
            removed_indices[i] = True

        print(removed_indices)

        for i, letter in enumerate(s):
            if i in removed_indices:
                continue
            final += letter

        return final


"""



stack => hold on to all instances of open parenthesis [ index           ]

iterate through str
  if it is "(" add index to stack

  if it is ")" pop off top of stack:
    if there is nothing to pop off => slice off the ")" from the string
  
while stack exists:
  pop off item from stack and slice off the "(" from the string

return s

"""
