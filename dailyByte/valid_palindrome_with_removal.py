"""
Given a string and the ability to delete at most one character, return whether or not it can form a palindrome.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

"abcba", return true
"foobof", return true (remove the first 'o', the second 'o', or 'b')
"abccab", return false
"""

def valid_palindrome_with_removal(str):
    p1 = 0
    p2 = len(str) - 1
    removed = False
    
    while p1 < p2:
        if str[p1] != str[p2]:
            if removed: return False
            if str[p1 + 1] == str[p2]:
                p1 += 1
                removed = True
            elif str[p2 - 1] == str[p1]:
                p2 -= 1
                removed = True
            else: return False
        p1 += 1
        p2 -= 1
    return str[p1] == str[p2]

print(
    valid_palindrome_with_removal("abcba"),
    valid_palindrome_with_removal("foobof"),
    valid_palindrome_with_removal("abccab")
)
    


"""
utilize two pointers

abcba

while p1 < p2:
    check if same, if not, mark variable as remove and move pointer based off next letter

"""
