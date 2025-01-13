import mod1
# the same variable name can't be overwritten because mod1's import creates a namespace for it's globa scope
x = 4

# however a from statment can overwrite varibles in the impoerting scope
# accessing mod1's object... will print two  different values of x because every module retains its objects
print(x, mod1.x)


# accessing an object from a module imported by mod1... since it is also an object in the imported mod1
my_platform = mod1.sys.platform