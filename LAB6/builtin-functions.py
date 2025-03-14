from functools import reduce
import time
import math

# 1. Multiply all numbers in a list using builtin function
def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

# 2. Count uppercase and lowercase letters in a string
def count_case(s):
    upper_case = sum(1 for c in s if c.isupper())
    lower_case = sum(1 for c in s if c.islower())
    return upper_case, lower_case

# 3. Check if a string is palindrome
def is_palindrome(s):
    return s == s[::-1]

# 4. Invoke square root function after specific milliseconds
def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)  # Convert milliseconds to seconds
    return math.sqrt(number)

# 5. Check if all elements in a tuple are True
def all_true(t):
    return all(t)

# Sample usage:
if __name__ == "__main__":
    # Test multiply_list
    print("Product of list:", multiply_list([1, 2, 3, 4, 5]))
    
    # Test count_case
    upper, lower = count_case("Hello World")
    print(f"Uppercase: {upper}, Lowercase: {lower}")
    
    # Test is_palindrome
    print("Is palindrome:", is_palindrome("madam"))
    
    # Test delayed_sqrt
    num, delay = 25100, 5000
    print(f"Square root of {num} after {delay} milliseconds is {delayed_sqrt(num, delay)}")
    
    # Test all_true
    print("All elements true:", all_true((True, True, False)))
