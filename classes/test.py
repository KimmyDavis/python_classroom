"""
This contains the test code for my coverage of classes
"""
# creation
class First_class:
    x = 12

# attribute
print(First_class.x)

# instantiation
inst = First_class()
inst.x = 21
print(inst.x)

# constructor
class shirt:
    def __init__(self, color, size=31):
        self.color = color
        self.size = size
    def __str__(self):
        return "shirt: size -> %s, color -> %s" % (self.size, self.color)
    
red_shirt = shirt("red")
print(red_shirt)

# inheritance and customization
class t_shirt(shirt):
    def __init__(self, collar, size=28, color="blue"):
        self.collar = collar
        self.color = color
        self.size = size

tshirt1 = t_shirt("short")
print(tshirt1)

# operator overloading
class cmplx:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def __add__(self, other):
        return cmplx(self.i + other.i, self.j + other.j)
    def __str__(self):
        return f"{self.i}i + {self.j}j"
    
a = cmplx(1, 2)
b = cmplx(6, 3)
c = a + b # presence of the __add__ method supports normal addition statements but with custom behaviour.
print(c) # presence of the __str__ method changes print behaviour.