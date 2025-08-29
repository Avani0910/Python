# b.Make a simplest possible Python program that calculates and prints the value of the formula
# y=6x^2+4sin(x)

import math
x = float(input("Enter the value of x : "))
y = 6*pow(x,2) + 4*math.sin(math.radians(x))
print(y)

