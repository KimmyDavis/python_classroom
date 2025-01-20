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