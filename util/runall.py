from types import ModuleType
from typing import Callable


def runall(module: ModuleType,
           startswith: str,
           key: Callable[[str], int] = lambda x: int(x[8:])):
    items = [i for i in dir(module) if i.startswith(startswith)]
    for i in sorted(items, key=key):
        item = getattr(module, i)
        if not callable(item): continue
        print(f"{i}\n")
        item()
        print()
