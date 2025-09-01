# b. Write a Python program to get the largest number from a list. 

def find_largest(numbers):
    largest = numbers[0]  # assume first element is the largest
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Example usage
my_list = [25, 78, 12, 98, 56, 43]
print("The largest number in the list is:", find_largest(my_list))
