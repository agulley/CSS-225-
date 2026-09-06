# Andre Gulley
# 9-5-2026

# The Problem-1

# An infinite loop that prints “Infinite”


# Problem1Infinite.py
# This script runs until the user enters 1

while True:
    print("Infinite")

    # Prompt the user for input
    user_input = input("Enter '1' to stop, or press Enter to continue: ")

    # Check if the user entered 1
    if user_input == "1":
        print("Stopping the loop.")
        break  # This exits the while loop completely


