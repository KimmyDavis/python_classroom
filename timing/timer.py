import time
reps = 1000
reprange = range(reps)

def timer(func, *pargs, **kargs):
    start_time = time.time()
    for i in reprange:
        ret = func(*pargs, **kargs)
    elapsed = time.time() - start_time
    return (elapsed, ret)

def best_time(func, *pargs, **kargs):
    best = 2 ** 32
    for i in reprange:
        start = time.time()
        ret = func(*pargs, **kargs)
        end = time.time()
        if end - start < best:
            best = end -start
    return best, ret