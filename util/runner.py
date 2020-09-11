from typing import Any


def runall(module: Any, startswith: str):
    for i in dir(module):
        if i.startswith(startswith):
            item = getattr(module, i)
            if callable(item):
                print(f"{i}\n")
                item()
                print("")
