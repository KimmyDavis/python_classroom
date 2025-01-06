# MODULES

Modules are files that can be imported in a python program.

They privide a way to resue code multiple times in python programs.

Usage involves importing them first with an `import` statement.

When imported, they are fetched, compiled (if necessary), executed and then their objects stored in a special `namespace` object from which they can be accessed as attributes to the module object's import name.

## STEPS

### fetching

This involves look up of the module referenced by the name in the import statment from the search path. The search path contains modules from

1. The home directroy,
2. The PYTHONPATH entry in the system environment variables,
3. Standard library modules, and
4. any file whose directroy is listed in a .pth file found from with in the above locations.
   The search process is curried out in the above oreder and any `.py, .pyc, .so, .zip, .dll, .pyd, java class for jthon and .NET component for ironPython` file that matches the import name first is loaded, and any object found with in is loaded in the module's namespace.

### compile

The file loaded is then converted into python bytecode if necessary

### execute (run)

and then run line by line top to bottom (if possible) to create the objects defined with in.

### namespace creation

The objects created aftar the execution phase are then stored in a special namespace object referenced by the name with which the mmodule was imported.

_Since files are executed at import, any print statement or other code with physical side effects will produce the side effects whenever the module is imported._
