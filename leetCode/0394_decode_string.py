# 394. Decode String

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        currStr = ''

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stack.append(currStr)
                stack.append(num)
                currStr = ''
                num = 0
            elif c == ']':
                repeat = stack.pop()
                prevStr = stack.pop()
                currStr = prevStr + currStr * repeat
            else:
                currStr += c
        
        return currStr

