"""
This module experiments the module advanced concepts discussed in the info markdown file"""
import sys

# Hiding Data
_hidden_name = "secret" # from * statements will be blind to this varible

def my_utility():
    x = 123
    print(x)
    # some function body

# restricting execution based on mode
if __name__ == "__main__":
    my_utility() # this will only run if this file is the main file


new_import_dir = "C:/users/me/pymods"
sys.path.append(new_import_dir)
# Can now import from my new directory.

# string module names
exec("import " + "string")
# or
string = __import__("string")