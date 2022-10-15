# importing pandas module
import pandas as pd

# importing regex module
# import re
	
# making data frame
data = pd.read_csv("nba.csv")
	
# removing null values to avoid errors
data.dropna(inplace = True)

# calling describe method
desc = data["Name"].describe()

# display
print(desc)