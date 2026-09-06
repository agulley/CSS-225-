# Andre Gulley
# 9-5-2026

# The Problem-4 Number and Description

# A while loop, ask the user to enter a number.


# Initialize the list and the counter
tens = []
counter = 0

# Loop until the counter reaches 50
while counter <= 50:
    # Check if the counter is divisible by 10
    if counter % 10 == 0:
        tens.append(counter)

    # Increment the counter
    counter += 1

# Confirm and print the results
print("The 'tens' list contains:", tens)

