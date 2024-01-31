"""
ASK: Write a function that given a list of strings, returns the longest string present.

Test cases:  
[ hello, goodbye, wave, jump ] → goodbye
[ up, down, up, other, longer ] → longer
[ biggest, smallest, smaller, small ] → small
[ one, two, three, four, five, six, seven, eight, nine, ten ] → three OR seven OR eight

Edge Cases:
[] -> ""

initialize a dictionary => word: length
iterate through input str
    if this string exists in dictionary
    if it doesn't exist in dictionary => add it to dictionary word: len(str)

initialize a max_word => holds on to max word
initialize a max_count => starts at -infinity

loop thorugh items in the dictionary
    if value is greater than max_count
        max_count new higher count
        max_word key that corresponds to that higher value

return max_word
"""


def longestString(str):
    dictionary = {}

    for string in str:
        if string not in dictionary:
            dictionary[string] = len(string)

    print("this is the dictionary", dictionary)

    max_word = ""
    max_count = float("-inf")

    for key in dictionary:
        if dictionary[key] > max_count:
            max_count = dictionary[key]
            max_word = key

    return max_word


print(longestString(["hello", "goodbye", "wave", "jump"]))  # "goodbye"
print(longestString(["123", "12", "234", "1"]))  # "123"
print(longestString([]))
