import math
size = 11
for i in range(size):
    median = math.ceil(size/2)
    leftSpace = median - abs(median - (i + 1))
    midSpace = abs((size - 1)-2*i)
    print(f"{" " * leftSpace}goodnight!{" " * midSpace}goodnight!")

input()