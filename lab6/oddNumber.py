# a. Write a Python program to print all odd numbers between 1 to 100 using a while loop.



num = 1   # starting number

while num <= 100:
    if num % 2 != 0:   # check if odd
        print(num, end=" ")
    num += 1
