"""
generators in python
they yield values one at a time instead of returning all of them at one
they are a one-shot traversal meaning you can't back-track yielded values
they are supported by all iteration contexts with the next() builtin call on them or their G.__next__() method
"""
def sq_gen(N):
    for i in range(N):
        yield(i ** 2)

ten_sqs = sq_gen(10)

print("1st ->", next(ten_sqs))
print("2nd ->", next(ten_sqs))
print("3rd ->", next(ten_sqs))
print("4th ->", next(ten_sqs))

# send method test
# this method is what the yield statement calls for the generator to provide a value
def send_gen():
    for i in range(7):
        x = yield i
        print(x)

myG = send_gen()

print(next(myG))
print(myG.send(120)) # send provides the generator with a value
print(myG.send(80))
print(myG.send(13))
print(next(myG)) # next() sends None 

# generator comprehensions (coded in parentheses)
gen_comp = (x ** .5 for x in range(10))
print(gen_comp) # prints a generator object
print(next(gen_comp)) # that supports the itersation protocol
# which ca be used in other iteration contexts
for i in gen_comp:
    print(i ** 2)

# the expressions are equivalents of the generatror functions... although more logic can be coded in a function
#expression
strGen = (c.upper() * 5 for c in "davis")
print(list(strGen)) # the list call is to force the result in a list

# function
def upper_five(wrd):
    for c in wrd:
        yield c.upper() * 5
my_upper_five = upper_five("davis") # same as strGen
print(list(my_upper_five))

# map emulation
def new_map(func, *itrs):
    res = []
    for args in zip(*itrs):
        res.append(func(*args))
    return res
print(new_map(lambda x: x ** 2, [1, 2, 3]))

# or with a list comprehension
def new_map_2(func, *itrs):
    return [func(*args) for args in zip(*itrs)]

print(new_map_2(lambda x: x ** 2, [1, 2, 3]))

# application of generators in the mix
def new_map(func, *itrs):
    for args in zip(*itrs):
        yield func(*args)

# or
def new_map_2(func, *itrs):
    return (func(*args) for args in zip(*itrs))

# value generators
myD = {"a": 1, "b": 2, "c": 3}
d_iter = iter(myD)
print(next(d_iter)) # iterate over the dictionary keys
print(next(d_iter))
print(next(d_iter))

# the dictionary provides a generator for its keys that can be traversed with a for-loop
for key in myD:
    print(key, myD[key])
    
# other objects like files and classes provide this interface 