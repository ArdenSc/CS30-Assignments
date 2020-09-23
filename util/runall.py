from types import ModuleType


def runall(module: ModuleType, startswith: str):
    for i in dir(module):
        if not i.startswith(startswith): continue
        item = getattr(module, i)
        if not callable(item): continue
        print(f"{i}\n")
        item()
        print("")
