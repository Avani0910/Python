# c. Write a Python function program to count a number of digits in a number.


def count_digits(num):
    # Handle negative numbers
    num = abs(num)
    
    # Special case for 0
    if num == 0:
        return 1
    
    count = 0
    while num > 0:
        num //= 10   # Remove the last digit
        count += 1
    return count


# --- Main program ---
n = int(input("Enter a number: "))
print(f"Number of digits in {n} is: {count_digits(n)}")
