import math

# for loop
nums = [2, 4, 9, 16, 25]
roots = []
for i in nums:
    roots.append(math.sqrt(i))

print(roots)

print(list(map(math.sqrt, nums)))

print([math.sqrt(i) for i in nums])