x = 25 
print("in mod2 inside pkg1", "_"*100)

from . import mod1
print("mod2 prints mod1's x ->",mod1.x)