
n = int(input())

for _ in range(n):
    y, x = list([int(x) for x in input().split()])

    if y > x:
        if y & 1:
            res = (y - 1) ** 2 + x
        else:
            res = y ** 2 - x + 1
    else:
        if x & 1:
            res = x **2 - y + 1 
        else:
            res = (x - 1) ** 2 + y

    print(res)


    

