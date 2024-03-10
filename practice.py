def findReviewScore(review, prohibitedWords):
    review = review.lower()

    start = 0
    end = 0
    maxLength = 0

    while start < len(review) and end < len(review):
        end += 1
        for i in prohibitedWords:
            if end - start + 1 >= len(i):
                section = review[start : end + 1]
                if isPresent(section, i):
                    maxLength = max(maxLength, end - start)
                    start = section.index(i) + start + 1

    maxLength = max(maxLength, end - start)
    return maxLength


def isPresent(str, bad):
    if bad in str:
        return True
    return False


test1 = "fastdeliveryokayproduct"  # expect 11
test2 = "extremevalueformoney"  # expect 20

print(findReviewScore(test1, ["eryoka", "yo", "eli"]))
print(findReviewScore(test2, ["tuper", "douche"]))


def getMinNumMoves(blocks):
    count = 0
    max_idx = blocks.index(max(blocks))
    min_idx = blocks.index(min(blocks))

    while max_idx < len(blocks) - 1:
        blocks[max_idx], blocks[max_idx + 1] = blocks[max_idx + 1], blocks[max_idx]
        if max_idx + 1 == min_idx:
            min_idx -= 1
        max_idx += 1
        count += 1
    while min_idx > 1:
        blocks[min_idx], blocks[min_idx - 1] = blocks[min_idx - 1], blocks[min_idx]
        if min_idx - 1 == max_idx:
            max_idx += 1
        min_idx -= 1
        count += 1

    return count


test1 = [4, 11, 9, 10, 12]  # expect 0
test2 = [2, 4, 3, 1, 6]  # expect 2
test3 = [5, 2, 4, 3, 1, 6]  # expect 3
"""

"""

print(getMinNumMoves(test1))
print(getMinNumMoves(test2))
print(getMinNumMoves(test3))


# 2, 5, 9, 10, 12, 13
# 0, 4, 6, 7, 8, 11, 14
