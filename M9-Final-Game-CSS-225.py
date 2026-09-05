# Andre Gulley
# Milestone 3 - Adventure Game
# Chapter 1
# 8-23-2026



import random

knight = "gore"
medieval_knight = "gore"

if knight == medieval_knight:
    print("Take task.")
else:
    print("Get equip.")

print("\nYou enter the Haunted Woods and climb the volcano...")
print("You retrieved the crystal holding the dragon's power!")

print("\n--- The Dragon Battle ---")
slay_dragon = random.randint(1, 6)
print(f"You rolled a: {slay_dragon}")

if slay_dragon >= 4:
    print("Success! You used the sword and crystal to slay the dragon!")
else:
    print("The dragon attacks! You must retreat and try again.")

print("\n--- Village Hero List ---")
names = ["Arthur", "Lancelot", "Galahad"]
print(f"Original list: {names}")

names.insert(1, "gore")
print(f"Updated list: {names}")


# Andre Gulley
# Milestone 3 - Adventure Game
# Chapter 4
# 8-23-2026

import random


knight = "medieval_knight"
gore = knight

if gore == "medieval_knight":
    print("slay gargoyles.")
else:
    print("gargoyles win.")

fight_gargoyles = random.randint(1, 6)
print(f"continues task: {fight_gargoyles}")


names = ["gore", "gargoyles", "woods"]
names.insert(1, "gore")
print(names)

# Andre Gulley
# Milestone 3 - Adventure Game
# Chapter 4
# 8-23-2026

import random


knight = "medieval_knight"
gore = knight

if gore == "medieval_knight":
    print("slay gargoyles.")
else:
    print("gargoyles win.")


fight_gargoyles = random.randint(1, 6)
print(f"continues task: {fight_gargoyles}")


names = ["gore", "gargoyles", "woods"]
names.insert(1, "gore")
print(names)

# Andre Gulley
# Milestone 3 - Adventure Game
# Chapter 4
# 8-23-2026

import random


knight = "medieval_knight"
gore = knight

if gore == "medieval_knight":
    print("slay gargoyles.")
else:
    print("gargoyles win.")

fight_gargoyles = random.randint(1, 6)
print(f"continues task: {fight_gargoyles}")


names = ["gore", "gargoyles", "woods"]
names.insert(1, "gore")
print(names)

# Andre Gulley
# Milestone 3 - Adventure Game
# Chapter 5
# 8-23-2026

import random

gore = "medieval_knight"

if gore == "medieval_knight":
    print("avoiding snake bites.")
else:
    print("bitten by snakes.")
    dice_roll = random.randint(1, 6)
    print(f"he continues a: {dice_roll}")

names = ["gore", "dragon", "volcano"]
names.insert(1, "core")
print(names)

# Andre Gulley
# Milestone 3 - Adventure Game
# Chapter 6
# 8-23-2026

import random

knight = "gore"

medieval_knight = "gore"

if knight == medieval_knight:
    print("Slay dragon.")
else:
    print("Dragon kills knight.")

the_dragon = random.randint(1, 6)

print(f"Task over: {the_dragon}")

names = ["gore", "dragon", "snakes"]

names.insert(1, "gore")

print(names)

# Andre Gulley
# Milestone 3 - Adventure Game
# Chapter 7
# 8-23-2026

import random


knight = "gore"

if knight == "medieval_knight":
    print("slayed the dragon.")
else:
    print("returned the crystal.")

    slayed = random.randint(1, 6)


    print(f"dragon kills gore: {slayed}")

names = ["gore", "retrieved the crystal", "crystal back to the empire"]


names.insert(1, "gore")

print(names)


