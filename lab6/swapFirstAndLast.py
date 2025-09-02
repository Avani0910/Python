# Program to swap the first and last digits of a number

# Input number from user
num = int(input("Enter a number: "))
num_str = str(num)

# If number has only 1 digit, no swapping needed
if len(num_str) == 1:
    swapped = num_str
else:
    # Swap first and last digits
    swapped = num_str[-1] + num_str[1:-1] + num_str[0]

# Convert back to integer
swapped_num = int(swapped)

print("Original number:", num)
print("Number after swapping first and last digits:", swapped_num)
