# Program to find the first and last digits of a number

# Input number from user
num = int(input("Enter a number: "))

# Find last digit
last_digit = num % 10

# Find first digit
first_digit = num
while first_digit >= 10:
    first_digit //= 10

# Output results
print("First digit:", first_digit)
print("Last digit:", last_digit)
