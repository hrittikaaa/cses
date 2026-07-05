t = int(input())

for _ in range(t):
    row, col = list(map(int, input().split()))

    up = max(row, col)
    if (up % 2 == 0):
        if (up == row):
            print(up ** 2 - col + 1)
        else:
            print((up-1) ** 2 + row)
    else: 
        if (up == row):
            print((up-1) ** 2 + col)
        else:
            print(up**2 - row + 1)