# Program to solve the equation z = (x+y)*(x+y) - 2*x*y
# This equation simplifies to z = x^2 + y^2 (because (x+y)^2 - 2xy = x^2 + y^2)

# Taking input from the user
x = float(input("Enter value of x: "))
y = float(input("Enter value of y: "))

# Calculating z
z = (x + y) * (x + y) - 2 * x * y

# Printing the result
print("The value of z is:", z)
