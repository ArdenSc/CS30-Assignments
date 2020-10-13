from util import runall
from importlib import import_module


def exercise1():
    class Restaurant:
        def __init__(self, restaurant_name: str, cuisine_type: str):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"{self.restaurant_name} is serving {self.cuisine_type}.")

        def open_restaurant(self):
            print(f"{self.restaurant_name} is now open.")

    restaurant = Restaurant("McDonalds", "Fast Food")
    print(restaurant.restaurant_name)
    print(restaurant.cuisine_type)
    restaurant.describe_restaurant()
    restaurant.open_restaurant()


def exercise2():
    class Restaurant:
        def __init__(self, restaurant_name: str, cuisine_type: str):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"{self.restaurant_name} is serving {self.cuisine_type}.")

        def open_restaurant(self):
            print(f"{self.restaurant_name} is now open.")

    restaurant1 = Restaurant("McDonalds", "Fast Food")
    restaurant1.describe_restaurant()
    restaurant2 = Restaurant("Wasabi", "Sushi")
    restaurant2.describe_restaurant()
    restaurant3 = Restaurant("Taco Bell", "Mexican")
    restaurant3.describe_restaurant()


def exercise3():
    class User:
        def __init__(self, first_name: str, last_name: str):
            self.first_name = first_name
            self.last_name = last_name

        def describe_user(self):
            print(f"The user's name is {self.first_name} {self.last_name}.")

        def greet_user(self):
            print(f"Welcome {self.first_name}!")

    user1 = User("Arden", "Sinclair")
    user1.describe_user()
    user1.greet_user()
    user2 = User("Aarsh", "Shah")
    user2.describe_user()
    user2.greet_user()


def exercise4():
    class Restaurant:
        def __init__(self,
                     restaurant_name: str,
                     cuisine_type: str,
                     number_served: int = 0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.number_served = number_served

        def describe_restaurant(self):
            print(f"{self.restaurant_name} is serving {self.cuisine_type}.")

        def open_restaurant(self):
            print(f"{self.restaurant_name} is now open.")

        def set_number_served(self, number_served: int):
            self.number_served = number_served

        def increment_number_served(self, newly_served: int):
            self.number_served += newly_served

    restaurant = Restaurant("McDonalds", "Fast Food")
    print(restaurant.number_served)
    restaurant.number_served = 2
    print(restaurant.number_served)
    restaurant.set_number_served(4)
    print(restaurant.number_served)
    restaurant.increment_number_served(3)
    print(restaurant.number_served)


def exercise5():
    class User:
        login_attempts = 0

        def __init__(self, first_name: str, last_name: str):
            self.first_name = first_name
            self.last_name = last_name

        def describe_user(self):
            print(f"The user's name is {self.first_name} {self.last_name}.")

        def greet_user(self):
            print(f"Welcome {self.first_name}!")

        def increment_login_attempts(self):
            self.login_attempts += 1

        def reset_login_attempts(self):
            self.login_attempts = 0

    user = User("Arden", "Sinclair")
    user.increment_login_attempts()
    user.increment_login_attempts()
    user.increment_login_attempts()
    print(user.login_attempts)
    user.reset_login_attempts()
    print(user.login_attempts)


if __name__ == "__main__":
    runall(import_module(__name__), "exercise")
