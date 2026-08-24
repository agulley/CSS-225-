# Andre Gulley
# Milestone 3 - Adventure Game
# Chapter 2
# 8-23-2026


import random

knight = "gore"
medieval_knight = "gore"

if knight == medieval_knight:
    print("slay the dragon.")
else:
    print("get equip.")

dice_roll = random.randint(1, 6)
print(f"defeat the dragon: {dice_roll}")

names = ["gore", "gargoyles", "dragon"]
names.insert(1, "gore")
print(names)

