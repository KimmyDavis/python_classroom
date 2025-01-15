x = 23
from consts import mod_heading_line
print("in mod1 inside pkg1", mod_heading_line)

import pkg1.pkg2.modx
print("printing pkg1.pkg2.modx.x ->", pkg1.pkg2.modx.x)

import pkg1.pkg2.mody as mody
print("printing mody.x after importing it as a synonym of pkg1.pkg2.mody ->", mody.x)