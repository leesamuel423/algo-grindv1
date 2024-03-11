n = int(input())
arr = set([int(x) for x in input().split()])

for i in range(1, n + 1):
    if i not in arr:
        print(i)
