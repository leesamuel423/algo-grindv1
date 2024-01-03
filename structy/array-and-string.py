# uncompress

def uncompress(s):
    string = ''
    i = 0
    j = 0
    while j < len(s):
        if s[j].isnumeric():
            j += 1
        else:
            num = int(s[i:j])
            string += s[j] * num
            j += 1
            i = j
    return string

# compress
def compress(s):
    s += '!'
    string = ''
    i = 0
    j = 0

    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            num = j - i
            if num == 1:
                string += s[i]
            else:
                string += s(j - i) + s[i]
            i = j
    return string

# anagrams
def anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    char_count = {}

    for char in s1:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    for char in s2:
        if char not in char_count or char_count[char] == 0:
            return False
        else:
            char_count[char] -= 1

    return True

# most frequent char
'''
def most_frequent_char(s):
    max = 0
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        if char_count[char] > max:
            max = char_count[char]
    
    most_frequent_chars = [char for char, count in char_count.items() if count == max]

    return most_frequent_chars[0]

'''
from collections import Counter

def most_frequent_char(s):
    counter = Counter(s)
    best = None
    for char in s:
        if best is None or counter[char] > counter[best]:
            best = char
    return best
# O(n) Time and Space. Utilizing hashmap(Counter) to seed data first

# pair sum
def pair_sum(numbers, target_sum):
    map = {}
    for i, int in enumerate(numbers):
        remainder = target_sum - int
        if remainder in map:
            return (map[remainder], i)
        else:
            map[int] = i
            

# pair product
def pair_product(numbers, target_product):
    map = {}
    for i, int in enumerate(numbers):
        quotient = target_product / int
        if quotient in map:
            return (map[quotient], i)
        else:
            map[int] = i

# intersection 
'''
def intersection(a, b):
    set_a = set(a)
    final = []
    for int in b:
        if int in set_a:
            final.append(int)

    return sorted(final)
'''
def intersection(a,b):
    set_a = set(a)
    return [ item for item in b if item in set_a ]

# five sort
def five_sort(nums):
    i, j = 0, len(nums) - 1
    while (i < j):
        while nums[i] != 5:
            i += 1
        while nums[j] == 5:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return nums

