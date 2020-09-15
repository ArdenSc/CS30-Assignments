from util.runner import runall
from importlib import import_module


def exercise1():
    names = ["Aarsh", "Brahm", "Barnan"]
    for name in names:
        print(name)


def exercise2():
    names = ["Aarsh", "Brahm", "Barnan"]
    message = "Hey {}, how are you doing?"
    for name in names:
        print(message.format(name))


def exercise3():
    cars = ["BMW", "Audi", "Mercedes"]
    message = "I would love to have a {} car."
    for car in cars:
        print(message.format(car))


if __name__ == "__main__":
    runall(import_module(__name__), "exercise")
