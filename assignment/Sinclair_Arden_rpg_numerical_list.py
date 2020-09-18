# Arden Sinclair
# CS30 P1Q1
# Sept. 18, 2020
# An example program that takes normal lists and
# prints them as formatted numerical lists.


def num_list(name, list):
    """Prints numerical list with one item per line.

    Args:
        name: The name of the list.
        list: The list of values.
    """
    print(f"{name}:")
    for index, value in enumerate(list):
        print(f"{index + 1}: {value.capitalize()}")


# Define the lists.
player_weapons = ["sword", "dagger", "club"]
player_armour = ["helmet", "chestplate", "leggings", "boots"]

# Print the lists unformatted.
print(player_weapons)
print(player_armour)

# Print the lists as a formatted numerical list.
num_list('Player Weapons', player_weapons)
num_list("Player Armour", player_armour)
