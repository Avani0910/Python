# b. Write a Python program to plot two or more lines on same plot with suitable legends of each line.

import matplotlib.pyplot as plt

# Data for plotting
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]   # Line 1
y2 = [1, 4, 9, 16, 25]  # Line 2
y3 = [2, 3, 5, 7, 11]   # Line 3

# Plotting multiple lines
plt.plot(x, y1, label="Line 1: y=2x")
plt.plot(x, y2, label="Line 2: y=x^2")
plt.plot(x, y3, label="Line 3: Prime numbers")

# Adding labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Multiple Lines on Same Plot")

# Adding legend
plt.legend()

# Display plot
plt.show()
