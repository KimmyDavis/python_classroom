# S = "kimmy"
# for chr in S:
#     print(ord(chr))

# S = "kimmy"
# sum = 0
# for chr in S:
#     sum += ord(chr)
# print(sum)

# S = "kiimy"
# print([ord(chr) for chr in S])

L = []
for i in range(10):
    L.append(2 ** i)
X = 5
i = 0
# while i < len(L):
#     if L[i] == 2 ** X:
#         print("found at index", i)
#         break
#     i += 1
# else:
#     print(X, "is not found")

# for item in L:
#     if item == 2 ** X:
#         print("found at index", L.index(item))
#         break
# else:
#     print(X, "is not found")

if 2 ** X in L:
    print("found at index", L.index(2 ** X))
else:
    print(X, "is not found")