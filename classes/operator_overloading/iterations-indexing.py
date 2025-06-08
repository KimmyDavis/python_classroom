"""experimenting with interations and indexing with operator overloading"""

# using __getitem__
# this intercepts all indexing operations and supports all iteration contexts
# however, it uses indexing and therefore stores a full object in memory which is costly
class iter1:
    def __init__(self, data):
        self.data = data
    def __getitem__(self, index):
        return self.data[index]
    
my_iter1 = iter1("davis")
print(my_iter1[0]) # -> "d"
print("a" in my_iter1) # -> "True"
for c in my_iter1:
    print(c, end=" ") # -> "d a v i s "
else: 
    print()

print("".join(map(str.upper, my_iter1))) # -> "DAVIS"

# using __iter__ and __next__
# these provide a more memory safe way of traversing through a sequence
# however, they don't support indexing
# this supports all iteration contexts and the in membership test
class iter2:
    def __init__(self, data):
        self.data = data
        self.offset = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.offset >= len(self.data):
            raise StopIteration
        else:
            next_item = self.data[self.offset]
            self.offset += 1
            return next_item
        
my_iter2 = iter2([i for i in range(5)])
print(iter(my_iter2)) # returns the iterator (the instance object in this case)
print(next(my_iter2)) # -> 0 # calls the __next__ method of this instance
print(next(my_iter2)) # -> 1
print(next(my_iter2)) # -> 2


# the __contains__ membership test
# this is used for membership tests
class iter3:
    data = "kimmy"
    def __contains__(self, member):
        return member in self.data
my_iter3 = iter3()
print("k" in my_iter3) # -> True
print("j" in my_iter3) # -> False

"""
membership tests prefer a __contains__ method if present
else, they look for an iterator object with __next__
if that too isn't provided, they fall back to a __getitem__
if defined.
iteration contexts prefer an iterator if one is provided
else, they also fall back to the __getitem__ if defined.
indexing only looks for a __getitem__
"""