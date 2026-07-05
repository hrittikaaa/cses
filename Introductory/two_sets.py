n = int(input())

total = (n * (n + 1)) // 2

if (total % 2):
    print("NO")
else:
    print("YES")
    lst1, lst2 = [], []
    sum1, sum2 = 0, 0

    for i in range(n):
        if (sum1 <= sum2):
            lst1.append(n)
            sum1 += n
        else:
            lst2.append(n)
            sum2 += n
        n -= 1
    print(len(lst1))
    for i in lst1: print(i, end=" ")
    print()
    print(len(lst2))
    for i in lst2: print(i, end=" ")