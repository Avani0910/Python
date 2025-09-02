# b. Write a Python program to find the sum of all natural numbers between 1 to n.

# Take input from user
n = int(input("Enter a positive integer: "))

# Check if the number is valid
if n <= 0:
    print("Please enter a positive integer greater than 0.")
else:
    # Method 1: Using formula
    total = n * (n + 1) // 2
    print(f"Sum of natural numbers from 1 to {n} is (using formula): {total}")

    # Method 2: Using loop
    total_loop = 0
    for i in range(1, n + 1):
        total_loop += i
    print(f"Sum of natural numbers from 1 to {n} is (using loop): {total_loop}")
