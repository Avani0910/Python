# f. Find common items from two lists. 

def find_common(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print("List 1:", list1)
print("List 2:", list2)
print("Common items:", find_common(list1, list2))
