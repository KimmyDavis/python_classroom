
# Local names are detected statically
x = 97

def myfunc_1():
    print(x) # -> prints 97

def myfunc_2():
    print(x)
    x = 23 # -> raises an exception on the print because X is now local and the print line reads it before it is assigned a value

def myfunc_3():
    import __main__
    print(__main__.x)
    x = 23 # -> doesn't error because x is accessed through a module's namespace

# default argument values that are mutable are created at def time not run  time.

def appfunc(x=[]):
    x.append(1)
    print(x)

appfunc() # [1]
appfunc() # [1, 1]
appfunc() # [1, 1, 1]
appfunc() # [1, 1, 1, 1]  successive calls will edit the same mutable object in place

# similar behaviour can be achieved by
def appfunc_2():
    appfunc_2.x.append(1)
    print(appfunc_2.x)
appfunc_2.x = []
appfunc_2() # -> [1]
appfunc_2() # -> [1, 1]


# functions without return or yield statements return None
def noreturn():
    x = 123
    print(x)
the_val = noreturn() # -> 123
print(the_val) # -> None
## Such functions are called procedures in other languages and usualy just leave side effects after execution
my_list = [1, 2, 3]
my_list = my_list.append(4) # the append method returns None because it performs an inplace change to the list
print(my_list) # -> None

