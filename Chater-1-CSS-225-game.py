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
