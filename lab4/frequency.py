# d. Write a Python program to get the frequency of elements in a list. 

def get_frequency(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

# Example usage
my_list = [1, 2, 2, 3, 4, 3, 2, 5, 1, 4, 4]
print("Original list:", my_list)
print("Frequency of elements:", get_frequency(my_list))
