mylist = ["apple", "banana", "cherry"]

# Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)

# List Length
# To determine how many items a list has, use the len() function:

# Example
# Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]


# What is the data type of a list?

mylist = ["apple", "banana", "cherry"]
print(type(mylist))


# Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Example
# Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Example
# Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# This example returns the items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
