"""
Given two strings s and t return whether or not s is an anagram of t.
Note: An anagram is a word formed by reordering the letters of another word.

s = "cat", t = "tac", return true
s = "listen", t = "silent", return true
s = "program", t = "function", return false
"""

from collections import Counter

def valid_anagram(s, t):
    s_dict = Counter(s)
    t_dict = Counter(t)
    
    for letter in t_dict:
        if letter not in s_dict or s_dict[letter] != t_dict[letter]:
            return False
    
    return len(s_dict) == len(t_dict)
    

print(
    valid_anagram("cat", "tac"),
    valid_anagram("listen", "silent"),
    valid_anagram("program", "function")
)


