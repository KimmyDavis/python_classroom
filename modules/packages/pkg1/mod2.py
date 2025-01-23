x = 25
from consts import mod_heading_line
print("in mod2 inside pkg1", mod_heading_line)

from . import mod1
print("mod2 prints mod1's x ->",mod1.x)