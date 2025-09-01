# b. Write a NumPy program to reverse an array (the first element becomes the last).

import numpy as np

# Create an example array
arr = np.array([1, 2, 3, 4, 5])

# Reverse the array
reversed_arr = arr[::-1]

print("Original array:", arr)
print("Reversed array:", reversed_arr)
