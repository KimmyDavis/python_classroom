import math
from mytimer import timer, best

def sq_pow(num):
    return pow(num, .5)

def sq_math(num):
    return math.sqrt(num)

def sq_stmt(num):
    return num ** .5

for func in (sq_math, sq_pow, sq_stmt):
    time, res = timer(func, 2 ** 100, _reps=1000000)
    print("{0:<9}: {1:.20f}  {2}".format(func.__name__, time, res))