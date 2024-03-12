size = int(input())

arr = list([int(x) for x in input().split()])

res = 0
for i in range(1, len(arr)):
    if arr[i] < arr[i - 1]:
        res += arr[i - 1] - arr[i]
        arr[i] = arr[i - 1]

print(res)

