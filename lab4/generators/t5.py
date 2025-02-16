def countdown(n):
    for i in range(n, -1, -1):
        yield i
print("Countdown from 10:")
for num in countdown(10):
    print(num, end=" ")
print("\n")