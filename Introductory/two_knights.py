k = int(input())

for i in range(1, k + 1):
    c = 0
    sq = i ** 2
    total = ((sq - 1) * sq) // 2

    total_slabs = 2 * (i - 1) * (i - 2) # two for both hz + ver
    attack = 2 * total_slabs

    print(total - attack)