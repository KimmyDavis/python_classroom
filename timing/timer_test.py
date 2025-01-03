import timer, mytimer

it_times = range(10000)

def list_comp():
    return [i for i in it_times]

def for_statement():
    ls = []
    for i in it_times:
        ls.append(i)
    return ls

def gen_comp():
    return list(i for i in it_times)

def gen_func():
    def my_list_gen():
        for i in it_times:
            yield i
    return list(my_list_gen())

for func in (list_comp, for_statement, gen_comp, gen_func):
    time, call_res = timer.timer(func)
    print("{0:<15} -----> {1:f} [{2} ... {3}]".format(func.__name__, time, call_res[0], call_res[-1]) )

print()

for func in (list_comp, for_statement, gen_comp, gen_func):
    time, call_res = mytimer.best(func)
    print("{0:<15} -----> {1:.10f} [{2} ... {3}]".format(func.__name__, time, call_res[0], call_res[-1]) )
