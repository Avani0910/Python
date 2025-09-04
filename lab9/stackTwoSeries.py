import pandas as pd

# Create two Series
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([5, 6, 7, 8])

print("First Series:")
print(s1)

print("\nSecond Series:")
print(s2)

# Stack vertically (row-wise)
vertical_stack = pd.concat([s1, s2])
print("\nStacked Vertically (Row-wise):")
print(vertical_stack)

# Stack horizontally (column-wise)
horizontal_stack = pd.concat([s1, s2], axis=1)
print("\nStacked Horizontally (Column-wise):")
print(horizontal_stack)
