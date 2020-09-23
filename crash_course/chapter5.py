from util import runall
from importlib import import_module


def exercise1():
    number = 10
    print("Is number equal to 10? I think it is.")
    print(number == 10)

    print("Is number less than 5? I think not.")
    print(number < 5)

    print("Is number greater than 5? I think it is.")
    print(number > 5)

    print("Is number greater than or equal to 15? I think not.")
    print(number >= 15)

    print("Is number less than or equal to 10? I think it is.")
    print(number <= 10)

    print("Is number not equal to 20? I think it is not.")
    print(number != 20)

    word = "banana"
    print('Is word equal to "apple"? I think not')
    print(word == "apple")

    print('Is word not equal to "tomato"? I think it is.')
    print(word != "tomato")

    list = ["apple", "banana"]

    print('Is word equal to "orange" and on the list? I think not.')
    print(word == "orange" and word in list)

    print('Is "Banana" in lowercase on the list? I think it is.')
    print(word.lower() in list)

    print('Is "orange" or "pickle" on the list? I think not.')
    print("orange" in list or "pickle" in list)

    print('Is pickle not on the list? I think it is not.')
    print("pickle" not in list)


def exercise2():
    print("Completed in exercise1")


def exercise3():
    alien_color = "green"
    if alien_color == "green":
        print("You earned 5 points!")

    alien_color = "red"
    if alien_color == "green":
        print("You earned 5 points!")


def exercise4():
    alien_color = "green"
    if alien_color == "green":
        print("You earned 5 points for shooting the alien!")
    else:
        print("You earned 10 points!")

    alien_color = "yellow"
    if alien_color == "green":
        print("You earned 5 points for shooting the alien!")
    else:
        print("You earned 10 points!")


def exercise5():
    alien_color = "green"
    if alien_color == "green":
        print("You earned 5 points.")
    elif alien_color == "yellow":
        print("You earned 10 points.")
    else:
        print("You earned 15 points.")

    alien_color = "yellow"
    if alien_color == "green":
        print("You earned 5 points.")
    elif alien_color == "yellow":
        print("You earned 10 points.")
    else:
        print("You earned 15 points.")

    alien_color = "red"
    if alien_color == "green":
        print("You earned 5 points.")
    elif alien_color == "yellow":
        print("You earned 10 points.")
    else:
        print("You earned 15 points.")


def exercise6():
    age = 17
    if age < 2:
        print("You are a baby.")
    elif 2 <= age < 4:
        print("You are a toddler")
    elif 4 <= age < 13:
        print("You are a kid.")
    elif 13 <= age < 20:
        print("You are a teenager.")
    elif 20 <= age < 65:
        print("You are an adult.")
    else:
        print("You are an elder.")


def exercise7():
    favorite_fruits = ["watermelon", "strawberry", "orange"]
    if "banana" in favorite_fruits:
        print("You really like banana!")
    if "watermelon" in favorite_fruits:
        print("You really like watermelon!")
    if "orange" in favorite_fruits:
        print("You really like orange!")
    if "kiwi" in favorite_fruits:
        print("You really like kiwi!")
    if "peach" in favorite_fruits:
        print("You really like peach!")


def exercise8():
    usernames = ["admin", "arden", "aarsh", "barnan", "brahm"]
    for user in usernames:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")


def exercise9():
    usernames = []
    if len(usernames) == 0:
        print("We need to find some users!")
    for user in usernames:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")


def exercise10():
    current_users = ["admin", "arden", "aarsh", "barnan", "brahm"]
    new_users = ["joe", "jack", "jeff", "arden", "aarsh"]
    for user in new_users:
        if user in current_users:
            print(f"{user} is already in use. Please try another name.")
        else:
            print(f"{user} is available.")


def exercise11():
    numbers = range(1, 10)
    for number in numbers:
        if number == 1:
            print(f"{number}st")
        elif number == 2:
            print(f"{number}nd")
        elif number == 3:
            print(f"{number}rd")
        else:
            print(f"{number}th")


def exercise12():
    print("All exercises have been formatted correctly.")


def exercise13():
    print("""\
If statements could be used to validate user input, check if an item exists
in a database, or check if stock exists for an online store.\
""")


if __name__ == "__main__":
    runall(import_module(__name__), "exercise")
