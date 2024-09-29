import math

def calculate_area_circle(radius):
    return math.pi * (radius ** 2)

def print_area(shape, area):
    print(f"The area of the {shape} is: {area}")

radius = 3
area = calculate_area_circle(radius)
print_area("circle", area)