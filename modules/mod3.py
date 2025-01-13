
import mod2
x = 5


# another instance of namespace nesting... to access module namespace attributes down the import chain.
print(x, mod2.x, mod2.mod1.x)

# after editing mod1 by changing the value of x,
from importlib import reload
reload(mod2)
print(mod2.x) # reflects the new value of x.

# the reload statement in one importer will affect all other importers because it affects the imported module's namespace in place
# however, it doesn't affect importers that use the "from" statement 
# because such imports create objects in the importers global scope rather than creating a single namespace object.
# they are therefore not affected after a reaload.