import pandas as pd

# Create two Pandas Series
s1 = pd.Series([10, 20, 30, 40, 50])
s2 = pd.Series([2, 4, 6, 8, 10])

print("First Series:")
print(s1)

print("\nSecond Series:")
print(s2)

# Addition
print("\nAddition of two Series:")
print(s1 + s2)

# Subtraction
print("\nSubtraction of two Series:")
print(s1 - s2)

# Multiplication
print("\nMultiplication of two Series:")
print(s1 * s2)

# Division
print("\nDivision of two Series:")
print(s1 / s2)
