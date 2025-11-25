import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    "age": [20, 25, None, 30, None]
})

# Fill missing values with the mean of the column
df["age"] = df["age"].fillna(df["age"].mean())

print(df)
