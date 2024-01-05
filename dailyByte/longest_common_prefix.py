# Longest Common Prefix

"""
Given an array of strings, return the longest common prefix that is shared amongst all strings.
Note: you may assume all strings only contain lowercase alphabetical characters.

Ex: Given the following arrays...

["colorado", "color", "cold"], return "col"
["a", "b", "c"], return ""
["spot", "spotty", "spotted"], return "spot"
"""


def longest_common_prefix(arr):
    """return longest common prefix of strings"""
    longest = ""
    index = 0

    for letter in arr[0]:
        for string in range(1, len(arr)):
            if index >= len(arr[string]) or letter != arr[string][index]:
                return longest

        longest += letter
        index += 1

    return longest


print(
    longest_common_prefix(["colorado", "color", "cold"]),
    longest_common_prefix(["a", "b", "c"]),
    longest_common_prefix(["spot", "spotty", "spotted"]),
)

# Time Complexity: O(m * n) - where m is length of arr and n is length of first string
# Space Complexity: O(n) - where n is length of first word - storing letters in variable, worst case scenario length of string
