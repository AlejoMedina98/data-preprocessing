import pandas as pd
# Import numpy to read NaN values on the pd dataframe
import numpy as np

df = pd.read_csv('train.csv')

print(df.head(25))

# Remove missed data using dropna function
# axis 0 = Horizontally
# axis 1 = Vertically
# subset = ["column_name"] only applies for this column
# inplace = True, modifies the dataframe

df.dropna(axis = 0, inplace=True, subset=["Parch"])

print(df.head(25))

# How to replace values in the dataframe
# using .replace funtcion

print(df["Age"])
print(df["Age"].mean()) # Get the average in that column
# Define the value you will use to replace NaN values
promedio = 30

# Replace and use inplace to save on dataframe
df["Age"].replace(np.nan, promedio, inplace=True)

print(df["Age"])