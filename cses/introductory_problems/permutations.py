'''
5 -> 4 2 5 3 1
6 -> 1 3 5 2 6
'''

n = int(input())

res = []

for i in range(2, n + 1, 2):
    res.append(str(i))
for j in range(1, n + 1, 2):
    res.append(str(j))

if 1 < n < 4:
    print("NO SOLUTION")
else:
    print(" ".join(res))
