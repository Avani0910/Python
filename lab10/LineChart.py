# a. Write a Python program to draw a line with suitable label in the x axis, y axis and a title.

import matplotlib.pyplot as plt 
# data to display on plots 
x = [5,2,6] 
y = [4,7,3] 
plt.plot(x, y)
plt.title("Line Chart")
# Adding the legends
plt.legend(["Line"])
plt.show()
