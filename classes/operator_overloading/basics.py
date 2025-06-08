"""The basics of operator overloading"""

class init_tester:
    def __init__(self, data=0): # this is called at instance contrustion time and is used to set per instance properties.
        self.data = data
        
# in addition expressions

class adder(init_tester):  # inheriting the constructor froma super class that defines one
    def __add__(self, other): # this method intercepts built-in addition operations 
        return self.data + other
    
one = adder(1)
print(one + 1)