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


def exercise10():
    numbers = [n**3 for n in range(1, 11)]
    print("The first three itmes in the list are:")
    print(numbers[:2])
    print("Three items from the middle of the list are:")
    print(numbers[2:5])
    print("The last three itmes in the list are:")
    print(numbers[-3:])


def exercise11():
    pizzas = ["pepperoni", "all dressed", "meat lovers"]
    for pizza in pizzas:
        print(f"I like {pizza} pizza.")
    print(f"My favorite pizza is {pizzas[0]}")
    print(f"My second favorite is {pizzas[1]}")
    print(f"My third favorite pizza is {pizzas[2]}")
    print("I really love pizza!")
    friend_pizzas = pizzas[:]
    pizzas.append("ham and pineapple")
    friend_pizzas.append("cheese")
    print("My favorite pizzas are:")
    for pizza in pizzas:
        print(pizza)
    print("My friend's favorite pizzs are:")
    for pizza in friend_pizzas:
        print(pizza)


if __name__ == "__main__":
    runall(import_module(__name__), "exercise")
