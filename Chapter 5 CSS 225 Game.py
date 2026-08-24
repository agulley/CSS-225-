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

