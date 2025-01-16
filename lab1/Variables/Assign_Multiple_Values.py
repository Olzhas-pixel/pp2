#Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
x, y, z = "sdsa", " dassdada" , "dewrew"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:
x = y = z = 0
print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

success = ["eat" , "sleap" , "work" , "repeat"]
a , b , c , d = success
print(a , b , c , d)

