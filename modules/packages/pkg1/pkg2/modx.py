x = 25
from consts import mod_heading_line
print("in modx inside pkg2", mod_heading_line)

from .. import mod1
print("printing mod1.x inside of pkg2.modx after importing it with relative imports ->", mod1.x)