# Arden Sinclair
# CS30 - P1Q1
# Sept. 16, 2020
# Makes various modifications to two inventories stored in lists
# and prints out information about the changes made.

# Both inventories start empty
playerInventory = ["Map"]
enemyInventory = ["Sword", "Shield", "Gun"]

# Print the item the player starts with
print(f"The player has a {playerInventory[0]}")
print(playerInventory)

# Add a sword to the end of the player inventory
playerInventory.append("Sword")
print(f"The player got a {playerInventory[1]}!")
print(playerInventory)

# Add a shield to the middle of the player inventory
playerInventory.insert(1, "Shield")
print(f"The player has picked up a {playerInventory[1]}.")
print(playerInventory)

# Remove the last item in the player inventory
del playerInventory[2]
print("The item in the player's last slot broke!")
print(playerInventory)

# Remove the first item in the player inventory
print(f"The player dropped their {playerInventory.pop(0)}.")
print(playerInventory)

# Remove the shield from the player inventory
removedItem = "Shield"
playerInventory.remove(removedItem)
print(f"The player lost their {removedItem}.")
print(playerInventory)

# Determine how many items are in the player inventory
print(f"There are {len(playerInventory)} \
items remaining in the player inventory.")

# Print the items the enemy starts with
print(f"The enemy has a {enemyInventory[0]}, \
{enemyInventory[1]}, and {enemyInventory[2]}.")
print(enemyInventory)

# Temporarily sort the enemy inventory
print("For a moment, the enemy's inventory was sorted.")
print(sorted(enemyInventory))

# Show that the inventory hasn't changed
print("It went back to normal.")
print(enemyInventory)

# Permanantly sort the enemy inventory
enemyInventory.sort()
print("The enemy inventory was sorted.")
print(enemyInventory)

# Reverse the order of the enemy inventory
enemyInventory.reverse()
print("The enemy inventory got reversed.")
print(enemyInventory)

# Determine how many items are in the enemy inventory
print(f"There are {len(enemyInventory)} \
items remaining in the enemy inventory.")
