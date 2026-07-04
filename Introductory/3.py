seq = input()
final_c = 1
temp_c = 1
for c in range(len(seq) - 1):
    if (seq[c] == seq[c+1]):
        temp_c += 1
    else:
        final_c = max(temp_c, final_c)
        temp_c = 1    

print(max(final_c, temp_c))