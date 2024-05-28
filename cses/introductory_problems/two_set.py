
n = int(input())

sum = (n * (n + 1)) / 2

# 7 -> (7 * 8) / 2 = 28 possible
# 6 -> (6 * 7) / 2 = 21 not possible
# 4 -> (4 * 5) / 2 = 10 Possible
# 3 -> (3 * 4) / 2 = 6 Possible
# 2 -> (2 * 3) / 2 = 3 Not possible

if sum % 2 != 0:
    print("NO")
else:
# ---- YES SCENARIO ----

    print("YES")

    set1 = []
    set2 = []

    set1Sum = 0
    set2Sum = 0

    for i in range(n, 0, -1):
        if set2Sum < set1Sum:
            set2.append(i)
            set2Sum += i
        else:
            set1.append(i)
            set1Sum += i

    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)


