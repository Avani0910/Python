# Program to calculate the product of digits of a number

# Input number from user
num = int(input("Enter a number: "))

# Work with the absolute value (to handle negative numbers)
n = abs(num)

product = 1

# If number is 0, product should be 0
if n == 0:
    product = 0
else:
    while n > 0:
        digit = n % 10
        product *= digit
        n //= 10

print("Original number:", num)
print("Product of digits:", product)
