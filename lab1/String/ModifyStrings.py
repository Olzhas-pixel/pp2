a="Hello, world!"
a=a.lower()
print(a)

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


# The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J")) #//output: Jello, World!

# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.

# Example
# The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']