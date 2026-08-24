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
