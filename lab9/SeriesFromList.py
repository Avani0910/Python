import pandas as pd
import numpy as np

# 1. Create a Pandas Series from a list
list_data = [10, 20, 30, 40, 50]
series_from_list = pd.Series(list_data)
print("Series from List:")
print(series_from_list)

# 2. Create a Pandas Series from a NumPy array
array_data = np.array([100, 200, 300, 400, 500])
series_from_array = pd.Series(array_data)
print("\nSeries from NumPy Array:")
print(series_from_array)

# 3. Create a Pandas Series from a dictionary
dict_data = {'a': 1000, 'b': 2000, 'c': 3000}
series_from_dict = pd.Series(dict_data)
print("\nSeries from Dictionary:")
print(series_from_dict)
