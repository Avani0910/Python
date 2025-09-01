def list_to_integer(lst):
    # Convert each number to string, join them, then convert back to integer
    return int("".join(map(str, lst)))

# Example usage
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
print("Single integer:", list_to_integer(my_list))

