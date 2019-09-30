import pandas as pd

url = 'train.csv'
df = pd.read_csv(url)

print(df.head(25))

# Generate a new dataframe replacing all categorical variables
# with numerical variables, use drop_first=True to remove first result
dummines = pd.get_dummies(df, columns=["Sex"], drop_first=True)

print(dummines.head(25))