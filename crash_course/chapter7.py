from util import runall
from importlib import import_module


def exercise4():
    while True:
        response = input("Enter a pizza topping or quit: ")
        if response.lower() == "quit":
            break
        else:
            print(f"{response.capitalize()} has been added to your pizza.")


def exercise5():
    while True:
        response = input("Please enter your age: ")
        if not str.isdigit(response):
            print("Please enter a valid number.")
            continue
        age = int(response)
        if age < 3:
            print("Your ticket is free.")
        elif 3 <= age <= 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")


def exercise6():
    iterations = 0
    while iterations < 10:
        iterations += 1
        response = input("Please enter your age: ")
        if response.lower() == "quit":
            break
        if not str.isdigit(response):
            print("Please enter a valid number.")
            continue
        age = int(response)
        if age < 3:
            print("Your ticket is free.")
        elif 3 <= age <= 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")


def exercise7():
    while True:
        print("Infinte loop")


if __name__ == "__main__":
    runall(import_module(__name__), "exercise")
