import pandas as pd

# Declare where the data sources is located
# and read it as a dataframe saved on "df" variable
url = 'train.csv'
df = pd.read_csv(url)

# Change your headings names by using the command:
# The array should have same items as your dataframe
# df.columns = ["Column 1 name", "Column 2 name", "etc"]

print("This is the heading in the dataframe:")
print(df.head(0))

# Print the datatypes in your dataframe
print("These are the datatypes of each column in the dataframe:")
print(df.dtypes)

# Print head by using: 
#df.head()

# Print tails by using:
#df.tail()

# Statistical analysis
# This function does not describe "object" types
print(df.describe())


# If you want to describe "object" types, use this cmd:
print(df.describe(include="all"))

# Export a dataframe to a csv:
# df.to_csv('your_new_file.csv')

#Visualize an overall dataframe info:
print(df.info())