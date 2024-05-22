# 6. Zigzag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzag = [[] for _ in range(numRows)]
        row = 0
        direction = "d"
        for i in range(len(s)):
            zigzag[row].append(s[i])
            if row == 0 and direction == "u":
                direction = "d"
            elif row == numRows - 1 and direction == "d":
                direction = "u"
            if direction == "d":
                row += 1
            elif direction == "u":
                row -= 1

        output = "".join("".join(i) for i in zigzag)
        return output
