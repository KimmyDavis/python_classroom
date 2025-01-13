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
- The `import * from mod` statement can even be more destructive than the `from` statement because it spreads all the objects of the imported module in the importer's globals scope, doing overwrites if an object of the same name exists there in.
- All variants of importing statements can only be used once per module in the importer's lifespan. Successive imports just reference the same namespace object in memory and don't rerun the module... since reloading it straight from the file is so expensive.
- There therefore exists a `reload` function that can be used in case the the imported module has been modified.
- The reload statement reruns the file and changes the imported module's namespace object in place. it therefore affects all import subscribers since they reference to the same object after the reload.
- The `reload` function can't however work if the module has not yet beenn imported.
- `from` and `import *` subscriptions are not affected since their imports exist in the importing scope and not in the reloaded namespace object.
- If the imported module also imports other modules in its global scope, their attributes can aslo be accessed by the importer, including other module imports.
- Nested imports can therefore be accessed by simply chaining references to any level of nesting.
