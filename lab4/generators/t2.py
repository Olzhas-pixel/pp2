def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i
n = int(input("Enter a number for even number generator: "))
print("Even numbers:")
print(",".join(str(num) for num in even_numbers(n)))