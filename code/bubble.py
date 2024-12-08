l = [3, 2, 1, 4, 9, 8, 7]
for a in range(len(l)):
    for b in  range(len(l) - 1):
        if l[a] < l[b]:
            l[a], l[b] = l[b], l[a]
print(l)