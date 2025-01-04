# def adder(*args):
#     init = args[0]
#     for arg in args:
#         init = init + arg if arg != args[0] else args[0]
#     return init

# print(adder(1, 2))
# print(adder("kim", " Davis"))
# print(adder([1, 3], [4]))
# print(adder(1, 2, 3))
# print(adder("Kimwera ", "Davis ", "Junior."))
# # adder(1, 2)

def copyDict(dict):
    newDict = {}
    for key in dict:
        newDict[key] = dict[key]
    return newDict

print(copyDict({"a": 1,"b": 2}))

def addDict(dict1, dict2):
    newDict = {}
    for key in dict1:
        newDict[key] = dict1[key]
    for key in dict2:
        newDict[key] = dict2[key]
    return newDict
    
print(addDict({"a": 1,"b": 2}, {"c": 3, "d": 4}))