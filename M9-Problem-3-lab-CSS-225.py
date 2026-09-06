# Andre Gulley
# 9-5-2026

# The Problem-3 Number and Description

# A while loop, ask the user to enter a number.


# Initialize an empty list to store the numbers
numbers_list = []

# Continue looping as long as the sum of the list is 100 or less
while sum(numbers_list) <= 100:
    # Ask the user for input and convert it to a float (or int)
    user_input = float(input("Enter a number: "))

    # Append the entered number to the list
    numbers_list.append(user_input)

# Print the final results once the sum exceeds 100
print("\nThe sum has exceeded 100!")
print(f"Numbers entered: {numbers_list}")
print(f"Final sum: {sum(numbers_list)}")

