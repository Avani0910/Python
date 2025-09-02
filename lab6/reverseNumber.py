# Program to reverse a number

# Input number from user
num = int(input("Enter a number: "))

# Work with absolute value to handle negatives
n = abs(num)

# Reverse the number
reverse_num = 0
while n > 0:
    digit = n % 10
    reverse_num = reverse_num * 10 + digit
    n //= 10

# Restore sign if number was negative
if num < 0:
    reverse_num = -reverse_num

print("Original number:", num)
print("Reversed number:", reverse_num)
