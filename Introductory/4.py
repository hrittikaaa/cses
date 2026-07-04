n = int(input())
array = input().split()
array = [int(x) for x in array]
moves = 0

for i in range(n-1):
    diff = array[i] - array[i+1]
    if(diff > 0):
        moves += diff
        array[i+1] += diff

print(moves)
