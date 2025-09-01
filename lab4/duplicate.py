# c. Write a Python program to remove duplicates from a list. 

def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example usage
my_list = [1, 2, 3, 2, 4, 1, 5, 3]
print("Original list:", my_list)
print("List after removing duplicates:", remove_duplicates(my_list))
