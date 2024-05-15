"""
Given a string representing your stones and another string representing a list of jewels, return the number of stones that you have that are also jewels.

jewels = "abc", stones = "ac", return 2
jewels = "Af", stones = "AaaddfFf", return 3
jewels = "AYOPD", stones = "ayopd", return 0
"""

def jewels_and_stones(jewels, stones):
    jewels_set = set(jewels)
    counter = 0
    for i in stones:
        if i in jewels_set:
            counter += 1
    
    return counter


print(
    jewels_and_stones("abc", "ac"),
    jewels_and_stones("Af", "AaaddfFf"),
    jewels_and_stones("AYOPD", "ayopd")
)

"""
create a set for jewels

iterate through stones and see which ones are jewels, update counter
"""
