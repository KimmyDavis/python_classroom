## CLASSES AND OOP IN PYTHON

In python, the class is the ultimate tool used for object oriented programming. Though OOP, as other language define it, is a programming pattern that deals with self dependant entities that abstract complexities away from implementers, and posses the ability to pass on their properties and methods to other objects that inherit them.

Python centers its exploration to the inheritance bit of it. And that's basically the most special thing about classes as compared to other object types in python. Python sees everything as an object of a sort and classes are simply objects that can inherit and be inherited from by other classes.

The other part of the python OOP story is the instance object, which is simply an instance of a class implementation. Classes therefore are like factories of multiple object instances.

Take for instance a class describing a shirt. The class just defines how a shirt should look like and when a shirt is finally created from the class, the actual shirt becomes the instance. From the same implementation a shirt, multiple shirts can be created, but leaving the implementation as it was, so one class, multiple instances.

### Coding classes in python

In python, to create a class, you just define it in a `class` statement.

```python
class class_name:
    ... # class body
```

Any assignment from with in the class body creates an attribute to the class. such assignments include:

- assignment statements
- def statements (functions)
- module imports
- and nested class statements

```python
class my_class:
    a = 3
    def myfunc(): ...
    import some_mod
    class inner_class:
        ... # other stuff
```

classes can inherit from other classes by adding them in parentheses in the class statement.

```python
class my_class_2(class_name, my_class):
    ... # class body
```

when classes inherit attributes from other classes, the leftmost classes take higher precedence in the inheritance tree.

To access an atrribute of an object, the dot notaton is used.

```python
object.attribute
```

this statement triggers a such which begins at the instance or class on which it is queried. The search continues up the inheritance tree until when it comes across the attribute. If the attribute appears more than once, it evaluates to the first occurence found during the search.

Therefore classes can overwrite exixting attribute names in the inheritance tree. This is what makes them the best tools for code customization.

To create an instance of a class, you call the class as though it was a funtion

```python
some_instance = my_class()
```

this creates an instance of `my_class` called `some_instance`. This instance inherits all the attributes and methods of my_class including those it inherited from other classes.

any function defined from with in a class is called a method, and any other object assigned from with in is called a property.

```python
class my_class:
    prop_1 = 12 # properties
    prop_2 = "stuff"

    def my_method():
        ... # method body
```

all methods of a class receive the special `self` object which is the reference to the instance of the class on which the method is called.

```python
class shirt:
    color = "white"
    def set_color(self, color):
        self.color = color

my_new_shirt = shirt()
print(my_new_shirt.color) # -> white
my_new_shirt.set_color("green")
print(my_new_shirt.color) # -> green
```

classes also provide a special function `__init__` which is called everytime an instance of the class is created. This function as the name suggests is used to initialise the class with some properties. This type of fucntion is sometimes reffered to as a constructor. Any arguments passed to the instance creation call are supplied to this function.

```python
class shirt:
    def __init__(self, color, size=31):
        self.color = color
        self.size = size

blue_shirt = shirt("blue")
print(blue_shirt.color) # -> blue
```

however if this function is not available, it is simply ignored.

### Operator overloading

This is the ability of a class to override the normal behavior of operators in expressions.

It is possible through the use of special method names in a class. These names begin and end with double underscores.

This includes operations like:

- class construction
- addition expressions
- multiplication
- print statements
- ... and many others

```python
class overider:
    __init__(): pass # this constructs the class
    __add__(): pass # this changes behavior when the class is found in + statements
    __str__(): pass # this changes the way the class looks in print statements
    ... # and many others
```

To better support customization, classes allow you to create new methods from existing methods with the `super()` class refernce or directly calling the method on the class on which it is attached.

```python
class Parent:
    def __init__(self, attr1, attr2):
    self.attr1 = attr1
    self.attr2 = attr2

    def meth1(self, sth):
        return 25 + sth

class Child(Parent):
    def __init__(self, attr1):
        super().__init__(attr1, "my_val")
    def meth1(self):
        Parent.meth1(self, 26)
```
