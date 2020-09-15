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


def exercise4():
    guests = ["Jeff Bezos", "Bill Gates", "Elon Musk"]
    message = "Dear {}, I would like to invite you to dinner."
    for guest in guests:
        print(message.format(guest))


def exercise5():
    guests = ["Jeff Bezos", "Bill Gates", "Elon Musk"]
    message = "Dear {}, I would like to invite you to dinner."
    for guest in guests:
        print(message.format(guest))
    print("Sadly Jeff Bezos will not be able to attend")
    guests.remove("Jeff Bezos")
    for guest in guests:
        print(message.format(guest))


def exercise6():
    guests = ["Jeff Bezos", "Bill Gates", "Elon Musk"]
    message = "Dear {}, I would like to invite you to dinner."
    for guest in guests:
        print(message.format(guest))
    print("We have a new location so more guests can attend.")
    guests.insert(0, "Steve Jobs")
    guests.insert(2, "Larry Page")
    guests.append("Sergey Brin")
    for guest in guests:
        print(message.format(guest))


def exercise7():
    guests = ["Jeff Bezos", "Bill Gates", "Elon Musk"]
    message = "Dear {}, I would like to invite you to dinner."
    for guest in guests:
        print(message.format(guest))
    print("We have a new location so more guests can attend.")
    guests.insert(0, "Steve Jobs")
    guests.insert(2, "Larry Page")
    guests.append("Sergey Brin")
    for guest in guests:
        print(message.format(guest))
    removal = "Sorry {}, you can't be invted to dinner."
    print(removal.format(guests.pop(0)))
    print(removal.format(guests.pop(2)))
    print(removal.format(guests.pop(1)))
    print(removal.format(guests.pop(2)))
    for guest in guests:
        print(message.format(guest))
    del guests[1]
    del guests[0]
    print(guests)


if __name__ == "__main__":
    runall(import_module(__name__), "exercise")
