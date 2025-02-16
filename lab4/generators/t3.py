def divisible(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
print("\nNumbers divisible by 3 and 4 up to 50:")
for num in divisible(50):
    print(num, end=" ")
print("\n")