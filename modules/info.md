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
