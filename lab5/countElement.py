# a. Write a Python program to Count the occurrences of an element in a tuple.

# Define a tuple
my_tuple = (1, 2, 3, 2, 4, 2, 5, 3, 2)

# Element to count
element = 2

# Count occurrences using tuple's count() method
count = my_tuple.count(element)

print(f"The element {element} appears {count} times in the tuple.")
