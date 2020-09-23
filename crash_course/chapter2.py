from util import runall
from importlib import import_module


def exercise3():
    name = "Arden"
    print(f"Hello, {name}, how are you?")


def exercise4():
    name = "Arden"
    print(name.lower())
    print(name.upper())
    print(name.title())


def exercise5():
    quote = "A person who never made a mistake never tried anything new."
    author = "Albert Einstein"
    print(f'{author.title()} once said, "{quote}"')


def exercise6():
    famous_person = "Albert Einstein"
    message = f'{famous_person} once said, "A person who never made a mistake \
never tried anything new."'

    print(message)


def exercise7():
    name = "  \tArden\n "
    print(name)
    print(name.lstrip())
    print(name.rstrip())
    print(name.strip())


def exercise8():
    print(3 + 5)
    print(9 - 1)
    print(4 * 2)
    print(16 / 2)


def exercise9():
    number = 2
    message = f"My favorite number is {number}"
    print(message)


if __name__ == "__main__":
    runall(import_module(__name__), "exercise")
