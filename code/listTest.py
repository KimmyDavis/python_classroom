def listTest(lst):
    order = lst[0] < lst[1] if len(lst) > 1 else True
    if order:
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                return False
    else:
        for i in range(len(lst) - 1):
            if lst[i] <= lst[i + 1]:
                return False
    return True

print("test 1", listTest([]))   # -> True
print("test 2", listTest([1]))   # -> True  
print("test 3", listTest([1, 10]))   # -> True
print("test 4", listTest([1, 2]))   # -> True
print("test 5", listTest([2, 1]))   # -> True
print("test 6", listTest([1, 2, 3, 4, 6, 5]))   # -> False
print("test 7", listTest([5, 6, 4, 3, 2, 1]))   # -> False
print("test 8", listTest([1, 2, 3, 4, 5, 6]))   # -> True
print("test 9", listTest([6, 5, 4, 3, 2, 1]))   # -> True
print("test 10", listTest([5, 6, 3, 2, 1, 4]))   # -> False
print("test 11", listTest([5, 5, 5, 5]))   # -> False
