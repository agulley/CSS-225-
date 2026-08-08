# Area of a circle
import math

radius_input = input('Enter the radius: ')
radius = float(radius_input)

# Calculation
area = math.pi * (radius ** 2)

# print nice Job
print(f"The area of the circle is {area:.2f}")