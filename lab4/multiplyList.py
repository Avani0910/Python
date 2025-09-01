def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage
my_list = [2, 3, 4, 5]
print("The product of all items in the list is:", multiply_list(my_list))
