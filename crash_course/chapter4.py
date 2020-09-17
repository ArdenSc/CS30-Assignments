from util.runner import runall
from importlib import import_module


def exercise3():
    print([n for n in range(1, 21)])


def exercise4():
    numbers = range(1, 1000001)
    for n in numbers:
        print(n)


def exercise5():
    numbers = range(1, 1000001)
    print(min(numbers))
    print(max(numbers))
    print(sum(numbers))


def exercise6():
    numbers = range(1, 21, 2)
    for n in numbers:
        print(n)


def exercise7():
    numbers = range(3, 31, 3)
    for n in numbers:
        print(n)


def exercise8():
    numbers = [n**3 for n in range(1, 11)]
    for n in numbers:
        print(n)


def exercise9():
    print([n**3 for n in range(1, 11)])


if __name__ == "__main__":
    runall(import_module(__name__), "exercise")
