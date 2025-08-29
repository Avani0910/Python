# Write a Python function that evaluates the mathematical functions
# f(x)=cos(2x),f^' (x)=-2 sin⁡(2x),and f^'' (x)=-4 cos⁡(2x). 
# Return these three values. Write out the results of these values for x=π

import math 
x = float(input("Enter the value of x :" ))
a = math.cos(2*x)
b = (-2)*math.sin(2*x)
c = (-4)*math.cos(2*x)
print("f(x) = \n",a)
print("f'(x) = \n",b)
print("f''(x) = \n",c)


