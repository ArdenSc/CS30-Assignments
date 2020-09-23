from util import runall
from importlib import import_module


def exercise1():
    person = {
        "first_name": "Aarsh",
        "last_name": "Shah",
        "age": 17,
        "city": "Regina",
    }
    for k, v in person.items():
        print(f"{k} is {v}")


def exercise2():
    favorite_numbers = {
        "arden": 12,
        "aarsh": 9,
        "barnan": 96,
        "brahm": 69,
        "jack": 1,
    }
    for k, v in favorite_numbers.items():
        print(f"{k.capitalize()}'s favorite number is {v}'")


def exercise3():
    glossary = {
        "function":
        "A reusable block of code that takes parameters and returns a result.",
        "variable": "A named item that can store data.",
        "list": "An ordered list of values.",
        "dictionary": "A list of name and value pairs that isn't ordered.",
        "for loop":
        "Runs code for each value in a list or other iterable data.",
    }
    for k, v in glossary.items():
        print(f"{k.capitalize()}: {v}")


def exercise4():
    glossary = {
        "function":
        "A reusable block of code that takes parameters and returns a result.",
        "variable":
        "A named item that can store data.",
        "list":
        "An ordered list of values.",
        "dictionary":
        "A list of name and value pairs that isn't ordered.",
        "for loop":
        "Runs code for each value in a list or other iterable data.",
        "while loop":
        "Continues to run code until a condition is no longer met.",
        "set":
        "An unordered list of values that has no duplicates.",
        "parameter":
        "Part of a function definition that takes a value when the function \
is called.",
        "argument":
        "A value provided when calling a function that fills one of the \
parameters.",
        "comment":
        "Part of the program that will be ignored by the compiled, often used \
for documentation.",
    }
    for k, v in glossary.items():
        print(f"{k.capitalize()}: {v}")


def exercise5():
    rivers = {
        "nile": "egypt",
        "amazon": "brazil",
        "mississippi": "mississippi",
    }
    for k, v in rivers.items():
        print(f"The {k.capitalize()} runs through {v.capitalize()}.")
    for river in rivers.keys():
        print(river)
    for country in rivers.values():
        print(country)


def exercise6():
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }
    potential = ["arden", "aarsh", "barnan", "brahm", "jen"]
    for name in potential:
        if name in favorite_languages.keys():
            print("Thank you for taking the poll.")
        else:
            print("Please take our poll.")


if __name__ == "__main__":
    runall(import_module(__name__), "exercise")
