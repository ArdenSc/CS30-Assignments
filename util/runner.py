from typing import Callable, Dict


def runall(functions: Dict[str, Callable[[], None]]):
    for k, v in functions.items():
        print(f"[{k}]\n")
        v()
        print("")
