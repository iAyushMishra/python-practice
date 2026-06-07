"""Calculate the area of a circle."""

import math


def calculate_area(radius):
    return math.pi * radius ** 2


try:
    radius = float(input("Enter radius: "))

    if radius < 0:
        print("Radius cannot be negative.")
    else:
        area = calculate_area(radius)
        print(f"Area = {area:.2f}")
except ValueError:
    print("Please enter a valid number.")
