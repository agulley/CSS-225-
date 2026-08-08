#  Wonderful holiday leaving on day
start_day = int(input("Enter start day: "))

# Nights
length = int(input("Enter length: "))

return_home = (start_day + length) % 7
print(return_home)
