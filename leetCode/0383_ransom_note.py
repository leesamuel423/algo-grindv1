# 383. Ransom Notes
"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

initialize mag hashmap
iterate through magazine and add to hashmap
iterate through ransomNote
    if character that we are on is in magazine, decrement value in hashmap
    if character is not in magazine or character in hashmap has value of 0 FALSE
return True
"""


def can_Construct(ransomNote, magazine):
    mag = {}
    for char in magazine:
        if char in mag:
            mag[char] += 1
        else:
            mag[char] = 1
    for char in ransomNote:
        if char in magazine and mag[char] > 0:
            mag[char] -= 1
        else:
            return False

    return True
