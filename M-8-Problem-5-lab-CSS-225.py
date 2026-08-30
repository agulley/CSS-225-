# Andre Gulley

# 8-30-2026

# Task 1, Task 2, Task 3.

def check_task_readiness(character, task_name, required_items, forbidden_debuffs):
    missing_items = [
        item for item in required_items
        if item not in character.weapons
    ]

    active_debuffs = [
        debuff for debuff in forbidden_debuffs
        if debuff in character.weaknesses
    ]

    if missing_items:
        print(f"{character.nickname} is not ready to {task_name}.")
        print("Missing:", ", ".join(missing_items))
    elif active_debuffs:
        print(f"{character.nickname} is not ready to {task_name}.")
        print("Forbidden debuffs:", ", ".join(active_debuffs))
    else:
        print(f"{character.nickname} is ready to {task_name}!")


class Character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses


player1 = Character(
    "Alex",
    ["rope", "coat", "first aid kit", "pan", "groceries", "pen", "paper", "idea"],
    []
)

check_task_readiness(
    player1,
    "Climb a mountain",
    ["rope", "coat", "first aid kit"],
    ["slow"]
)

check_task_readiness(
    player1,
    "Cook a meal",
    ["pan", "groceries"],
    ["small"]
)

check_task_readiness(
    player1,
    "Write a book",
    ["pen", "paper", "idea"],
    ["confusion"]
)