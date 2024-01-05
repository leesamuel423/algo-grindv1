# Add Binary
""
Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).
Note: neither binary string will contain leading 0s unless the string itself is 0

Ex: Given the following binary strings...

"100" + "1", return "101"
"11" + "1", return "100"
"1" + "0", return  "1"

https://study.com/academy/lesson/how-to-add-binary-numbers.html#:~:text=The%20process%20for%20how%20to,over%20to%20a%200%20again.
"""


def add_binary(s1, s2):
    """adds two binary numbers together"""
    p1 = len(s1) - 1
    p2 = len(s2) - 1
    final = []
    carry_over = 0

    while p1 >= 0 or p2 >= 0 or carry_over:
        num1 = int(s1[p1]) if p1 >= 0 else 0
        num2 = int(s2[p2]) if p2 >= 0 else 0

        total = num1 + num2 + carry_over

        carry_over = total // 2

        final.append(str(total % 2))

        p1 -= 1
        p2 -= 1

    return "".join(reversed(final))


print(add_binary("100", "1"))  #  "101"
print(add_binary("11", "1"))  # "100"
print(add_binary("1", "0"))  # "1"
