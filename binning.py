import pandas as pd
import numpy as np

url = 'train.csv'
dataframe = pd.read_csv(url)

# Lets bin the column age by years
# using the method cut()

bins = [0, 5, 12, 18, 36, 60, 100]
labels = ["1", "2", "3", "4", "5", "6"]


# Replace NaN ages with the average age
dataframe["Age"].replace(np.nan, dataframe["Age"].mean(), inplace=True)

# Print before the change
print(dataframe["Age"].head(25))

# Bin the column age using the bins and labels declared before
dataframe["Age"] = pd.cut(dataframe["Age"], bins, labels=labels)

# Print again to see the changes
print(dataframe["Age"].head(25))
