import pandas as pd

# Create a dictionary
data = {'a': 100, 'b': 200, 'c': 300, 'd': 400}

print("Dictionary:")
print(data)

# Convert dictionary to Pandas Series
series = pd.Series(data)

print("\nPandas Series:")
print(series)
