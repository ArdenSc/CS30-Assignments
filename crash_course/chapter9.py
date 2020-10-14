from typing import List
from util import runall
from importlib import import_module
from random import randint, choice


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


def exercise6():
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

    class IceCreamStand(Restaurant):
        def __init__(self,
                     restaurant_name: str,
                     cuisine_type: str,
                     number_served: int = 0,
                     flavors: List[str] = []):
            super().__init__(restaurant_name, cuisine_type, number_served)
            self.flavors = flavors

        def list_flavors(self):
            print("Available flavors:")
            for flavor in self.flavors:
                print(f"- {flavor}")

    ics = IceCreamStand("DQ", "Ice Cream", flavors=["Vanilla", "Chocolate"])
    ics.list_flavors()


def exercise7():
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

    class Admin(User):
        def __init__(self,
                     first_name: str,
                     last_name: str,
                     privileges: List[str] = []):
            super().__init__(first_name, last_name)
            self.privileges = privileges

        def show_privileges(self):
            print("Available privileges:")
            for privilege in self.privileges:
                print(f"- {privilege}")

    arden = Admin("Arden", "Sinclair",
                  ["can add post", "can delete post", "can ban user"])
    arden.show_privileges()


def exercise8():
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

    class Privileges():
        def __init__(self, privileges: List[str] = []):
            self.privileges = privileges

        def show_privileges(self):
            print("Available privileges:")
            for privilege in self.privileges:
                print(f"- {privilege}")

    class Admin(User):
        def __init__(self, first_name: str, last_name: str,
                     privileges: Privileges):
            super().__init__(first_name, last_name)
            self.privileges = privileges

    privileges = Privileges(
        ["can add post", "can delete post", "can ban user"])
    arden = Admin("Arden", "Sinclair", privileges)
    arden.privileges.show_privileges()


def exercise9():
    class Car:
        """A simple attempt to represent a car."""
        def __init__(self, make: str, model: str, year: int):
            self.make = make
            self.model = model
            self.year = year
            self.odometer_reading: int = 0

        def get_descriptive_name(self):
            long_name = f"{self.year} {self.make} {self.model}"
            return long_name.title()

        def read_odometer(self):
            print(f"This car has {self.odometer_reading} miles on it.")

        def update_odometer(self, mileage: int):
            if mileage >= self.odometer_reading:
                self.odometer_reading = mileage
            else:
                print("You can't roll back an odometer!")

        def increment_odometer(self, miles: int):
            self.odometer_reading += miles

    class Battery:
        """A simple attempt to model a battery for an electric car."""
        def __init__(self, battery_size: int = 75):
            """Initialize the battery's attributes."""
            self.battery_size = battery_size

        def describe_battery(self):
            """Print a statement describing the battery size."""
            print(f"This car has a {self.battery_size}-kWh battery.")

        def get_range(self):
            """Print a statement about the range this battery provides."""
            if self.battery_size == 75:
                range = 260
            elif self.battery_size == 100:
                range = 315
            else:
                range = "unknown"
            print(f"This car can go about {range} miles on a full charge.")

        def upgrade_battery(self):
            if self.battery_size != 100:
                self.battery_size = 100

    class ElectricCar(Car):
        """Represent aspects of a car, specific to electric vehicles."""
        def __init__(self, make: str, model: str, year: int):
            """Initialize attributes of the parent class."""
            super().__init__(make, model, year)
            self.battery = Battery()

    my_tesla = ElectricCar('tesla', 'model s', 2019)
    my_tesla.battery.get_range()
    my_tesla.battery.upgrade_battery()
    my_tesla.battery.get_range()


def exercise13():
    class Die:
        def __init__(self, sides: int = 6):
            self.sides = sides

        def roll_die(self):
            print(randint(1, self.sides))

    die = Die()
    for _ in range(10):
        die.roll_die()
    die = Die(10)
    for _ in range(10):
        die.roll_die()
    die = Die(20)
    for _ in range(10):
        die.roll_die()


def exercise14():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
    winning_ticket = []
    for _ in range(4):
        winning_ticket.append(str(choice(data)))
    print("Any ticket matching these numbers and/or letters wins:")
    print(' '.join(winning_ticket))


def exercise15():
    def get_winning_ticket() -> List[str]:
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
        winning_ticket = []
        for _ in range(4):
            winning_ticket.append(str(choice(data)))
        return winning_ticket

    my_ticket = get_winning_ticket()
    i = 0
    while True:
        i += 1
        winning_ticket = get_winning_ticket()
        for value in my_ticket:
            if value not in winning_ticket:
                break
        else:
            break
    print(f"It took {i} loops to get a winning ticket.")


if __name__ == "__main__":
    runall(import_module(__name__), "exercise")
