import math

# 1. Convert degrees to radians
def degrees_to_radians(deg):
    return deg * (math.pi / 180)

degree = 15
print("Input degree:", degree)
print("Output radian:", round(degrees_to_radians(degree), 6))


# 2. Calculate the area of a trapezoid
def trapezoid_area(height, base1, base2):
    return (base1 + base2) * height / 2

height = 5
base1 = 5
base2 = 6
print("\nHeight:", height)
print("Base, first value:", base1)
print("Base, second value:", base2)
print("Expected Output:", trapezoid_area(height, base1, base2))


# 3. Calculate the area of a regular polygon
def polygon_area(sides, side_length):
    return (sides * side_length ** 2) / (4 * math.tan(math.pi / sides))

sides = 4
side_length = 25
print("\nInput number of sides:", sides)
print("Input the length of a side:", side_length)
print("The area of the polygon is:", polygon_area(sides, side_length))


# 4. Calculate the area of a parallelogram
def parallelogram_area(base, height):
    return base * height

base = 5
height = 6
print("\nLength of base:", base)
print("Height of parallelogram:", height)
print("Expected Output:", parallelogram_area(base, height))
