arr = list(input())

maxCount = 0
count = 1
for i in range(1, len(arr)):
    if arr[i] == arr[i - 1]:
        count += 1
    else:
        maxCount = max(maxCount, count)
        count = 1

print(max(maxCount, count))
