# MODULES

Modules are files that can be imported in a python program.

They privide a way to resue code multiple times in python programs.

Usage involves importing them first with an `import` statement.

## Imports

When imported, they are fetched, compiled (if necessary), executed and then their objects stored in a special `namespace` object from which they can be accessed as attributes to the module object's import name.

### STEPS

#### fetching

This involves look up of the module referenced by the name in the import statment from the search path. The search path contains modules from

1. The home directroy,
2. The PYTHONPATH entry in the system environment variables,
3. Standard library modules, and
4. any file whose directroy is listed in a .pth file found from with in the above locations.
   The search process is curried out in the above oreder and any `.py, .pyc, .so, .zip, .dll, .pyd, java class for jthon and .NET component for ironPython` file that matches the import name first is loaded, and any object found with in is loaded in the module's namespace.

#### compile

The file loaded is then converted into python bytecode if necessary

#### execute (run)

and then run line by line top to bottom (if possible) to create the objects defined with in.

#### namespace creation

The objects created aftar the execution phase are then stored in a special namespace object referenced by the name with which the mmodule was imported.

_Since files are executed at import, any print statement or other code with physical side effects will produce the side effects whenever the module is imported._

## Namespaces

These are the objects created after the module has been successfully imprted.

### How they work

- Modules can be imported using the import or from statement.
- Both statements create namespace objects in memory.
- The import statement attaches objects in the global scope of the imported module as attributes to the imported module's namespace.
- The from statement however creates actuall objects of the imported objects in the importing module's global scope. It can therefore overwrite objects in the importing scope without warning.
- The from space can be used in place for the import statement for the most part, however, it can't be used to import more than one object of the samae name from different objects... for older pythons without import aliases.
- The `from mod import *` statement can even be more destructive than the `from` statement because it spreads all the objects of the imported module in the importer's globals scope, doing overwrites if an object of the same name exists there in.
- All variants of importing statements can only be used once per module in the importer's lifespan. Successive imports just reference the same namespace object in memory and don't rerun the module... since reloading it straight from the file is so expensive.
- There therefore exists a `reload` function that can be used in case the the imported module has been modified.
- The reload statement reruns the file and changes the imported module's namespace object in place. it therefore affects all import subscribers since they reference to the same object after the reload.
- The `reload` function can't however work if the module has not yet beenn imported.
- `from` and `import *` subscriptions are not affected since their imports exist in the importing scope and not in the reloaded namespace object.
- If the imported module also imports other modules in its global scope, their attributes can aslo be accessed by the importer, including other module imports.
- Nested imports can therefore be accessed by simply chaining references to any level of nesting.

## Module Packages

A package is a directory containing importable python modules and a compulsory `__init__.py` file.

The `__init__.py` file works as the initialization module and can therefore contain initialization code for the package for instance database connections. However, it can be left black since all that is required for a directory to be a packageis the presence of the file with the name `__init__.py`. As an initialization file therefore, it's code is run the first time a package is imported or reloaded with the `reload` function.

### how they work

#### normal imports

These folow the normal import search path

- Any directory wiht a file named `__init__.py` qualifies to be a package in python, this includes subdirectories that are also intended to be packages.
- the package can then be imported with the usual import statement as in:

```python
import mypkg
```

- the modules in the package can the be accessed using the dot-syntax as in:

```python
print(mypkg.mymod.x)
```

- however, if the module is to be imported specifically, it can be accessed at at import time using the same dot-syntax, and then used normally as imported:

```python
import mypkg.mymod
print(mypkg.mymod.x)
```

- this, as it looks can be tedious to type everythime you need an attribute of the module. The `from` statement can therefore be used to import modules with their specific names and therefore used directly in the importing scope without having to write down the whole package directory to to the intended module in the dot-notation.

```python
from mypkg import mymod
print(mymod.x)
```

- this however can be used when to similar names are to be imported from different sources. In such circumstances, the import statement can provide a workable solution.
- one other solution to avoiding long paths also exists, that is, using import synonyms to use a different name instead of the long directory path.

```python
import mypkg.mymod as mymod
print(mymod.x)
```

#### relative imports

Module packages provide a way of specifying imports from with in the package. The major difference is in python 3.x which provides a strict new way of accessing other modules from with in the package.

Relative imports, unlike absolute imports apply only to importers located from with in package. In 3.x, when a module is imported, the import protocal skips the module directory and automatically looks at other locations in the python import paths, as specified in the sys.path list.

In order to import a module from with in the package, the imports should be preceeded by a dot(.).

so an import statement like

```python
from . import mymod
#looks in the package in which the importer is located and imports a module called mymod.
```

another one like:

```python
from .mymod import x
# imports an object x from a module mymod located in the importer's package.
```

When two dots(..) are used, the search is done in an enclosing parent package.

```python
from .. import mod2
# imports a module mod2 in an enclosing parent package.
```

similarly:

```python
from ..mod3 import x
# imports an attribute x from mod3 in an enclosing packages's directory.
```

_This type of import however doesn't work in module files that are not part of a package. that is modules whose directories do not contain the `__init__.py` file._

## Other concepts

### Data hiding

Some objects in a module can be hidden from the `from *` statement. During such imports, the importer looks for objects in the module that are listed in its `__all__` list whose names don't begin with a single underscore. Hence to hide a variable from such imports, preceed its name wi a single underscore... or create a list named `__all__` and include all the varibles you want to be exported and exclude those you dont.

### Future features

When a feature that might break existing code is introduced to python, it is provided as an optional feature and can only be activated by importing it from the `__future__` module. forexample the python3.0 `print` function can be imported in python2.6 through the future import.

### Mixed usage modes

If a module can be imported and also run as a main fail, some code can be restricted to only run if the module is run as the main file. Every module has a special `__name__` attribute whose value is the name of the module in a given usage mode. When the module is run as the main file, this name evaluates to the string `'__main__'` therefore, an `if` test can be run to restrict execution of some code to the `main` usage mode.

```python
# program code
if __name__ = '__main__'
   # statements to be executed in the main usage mode
```

This is trick is sometimes used for module test code.

### Changing the module search path

For every module, there exists a path attribute in the system module which is a list containing the module search path directories. This list can be changed in anyway for a given process... this means that a module can add directories to the search path during execution and also remove them.

### The `as` import extension

New pythons include an import statement that allows you to import a module or an attribute of the module under a different name. This statement works for package imports too.

```python
import some_long_module_name as short_name
import pkg1.pkg2.modx.func_name as func_name
from mod3 import some_func_name as new_name
from mod1 import util as util1
from mod2 import util as util2
```

This comes in as a solution to importing attributes of the same name from different modules.

### Modules are objects

In the simplest terms, modules are just objects with attributes attached. They expose their properties and details through these attributes. Access to these attributes comes in handly for alot of non-basic applications, forexample building developer tools. The following statements are diffrent ways one can access attributes of a module for instance:

```python
import sys
import my_mod

attr = my_mode.attr
attr = my_mode.__dict__["attr"]
attr = sys.modules["my_mod"].attr
attr = getattr(my_mod, "attr")
```

This gives flexibility to a lot of applications.

### Import by name string

Sometimes one may want import a module given it's name as a string during execution. the normal import statements don't all strings because they'll assume commas in the module name, neither do they allow the use of varibles because they'll try to import the varible name instead. One way around this is through use of the `exec` function. It is not the best way though because it compiles every time it's executed.

```python
exec("import " + "mod_name_string")
mod_name = "some_dynamic_value"
exec("import " + mod_name)
```

an alternative to this is the use of the builtin `__import__` function. This works works just like the normal import statement, fetching the module from memory if it has already been imported.

```python
mod_name = __import__("mod_name_string")
mod_name = "some_dynamic_name"
mod_name = __import__(mod_name)
```

### Transitive reloads

A module can be reloaded during execution if it has already been imported. However, the reload function doesn't reload nested modules. Given such behaviour, you may have to write a tool that does so manually, and as an approach you can use recursion to traverse the import tree, keeping track of already reloaded modules to avoid repeatitions and posibly stack overflows due to infinite recursion. This however doesn't work with `from` import statements.

```python
import types
from importlib import reload

def progress(statement):
    if __name__ == "__main__":
        print(statement)

def transitive_reload(mod, reloaded):
    if not mod.__name__ in reloaded:
        progress("reloading " + mod.__name__)
        try:
            reload(mod)
        except ImportError:
            progress("---------------- failed to reload " + mod.__name__ + " -----------------")
        reloaded.add(mod.__name__)
        for attr in mod.__dict__.values():
            if type(attr) == types.ModuleType:
                transitive_reload(attr, reloaded)


def reload_all(*args):
    finished = set()
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, finished)

if __name__ == "__main__":
    progress("-------testing----------")
    import myreload
    reload_all(myreload)
```
