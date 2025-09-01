# e. Write a NumPy program to find the memory size of a NumPy array.

import numpy as np

# Create an example array
arr = np.array([1, 2, 3, 4, 5])

# Calculate memory size
memory_size = arr.size * arr.itemsize

print("Memory size of the array in bytes:", memory_size)
