def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

print("Squares from 5 to 10:")
for num in squares(5, 10):
    print(num, end=" ")
print("\n")