# Andre Gulley

# 8-30-2026

# Not sure what it does, just add numbers. This is a lot of code that gose nowhere.



def check_dragon_battle(sword_charge, shield_energy):
    print(f"--- Battle Stats: Sword={sword_charge}, Shield={shield_energy} ---")

   
    print("Version 1 (Original with 'not'):")
    if not ((sword_charge >= 0.90) and (shield_energy >= 100)):
        print("Your attack has no effect, the dragon fries you to a crisp!")
    else:
        print("The dragon crumples in a heap. You rescue the gorgeous princess!")


    print("\nVersion 2 (De Morgan's Laws Applied):")
    if (sword_charge < 0.90) or (shield_energy < 100):
        print("Your attack has no effect, the dragon fries you to a crisp!")
    else:
        print("The dragon crumples in a heap. You rescue the gorgeous princess!")


    print("\nVersion 3 (Swapped If/Else Branches):")
    if (sword_charge >= 0.90) and (shield_energy >= 100):
        print("The dragon crumples in a heap. You rescue the gorgeous princess!")
    else:
        print("Your attack has no effect, the dragon fries you to a crisp!")



check_dragon_battle(sword_charge=0.75, shield_energy=120)

print("\n" + "="*40 + "\n")

# Scenario B: Requirements ARE met (Victory!)
check_dragon_battle(sword_charge=0.95, shield_energy=105)

