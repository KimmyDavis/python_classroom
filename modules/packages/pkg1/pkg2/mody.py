x = 33
from consts import mod_heading_line
print("in mody inside pkg2", mod_heading_line)

from .modx import x

print("printing x after importing it from modx with relative imports ->", x)