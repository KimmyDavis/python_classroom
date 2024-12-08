import sys
def print101(*objs, sep=" ", end="\n"):
    for obj in objs:
        sys.stdout.write(str(obj) + (sep if (obj is not objs[-1]) else ""))
    sys.stdout.write(end)

print101("kim", 12, 13, [1], {"name": "kim", "age": 21}, {1, 5, 6}, sep=", ")
print("kim", 12, 13, [1], {"name": "kim", "age": 21}, {1, 5, 6}, sep=", ")