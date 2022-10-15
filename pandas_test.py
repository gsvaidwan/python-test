import pandas as pd
 
# importing numpy as np
import numpy as np
 
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
 
# creating a dataframe from dictionary
df = pd.DataFrame(dict)
print(df)
 
# filling missing value using fillna()  
print(df.fillna(0))
# print(df)

import pandas as pd
 
# importing numpy as np
import numpy as np
 
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score':[52, 40, 80, 98],
        'Fourth Score':[np.nan, np.nan, np.nan, 65]}
 
# creating a dataframe from dictionary

df = pd.DataFrame(dict)
print(df)
# using dropna() function  
print(df.dropna())

import pandas as pd
# Define a dictionary containing Students data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
	'Height': [5.1, 6.2, 5.1, 5.2],
	'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# Declare a list that is to be converted into a column
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']

# Using 'Address' as the column name
# and equating it to the list
df['Address'] = address

# Observe the result
print(df)




# importing pandas module
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name" )
print(data)
# dropping passed columns
data.drop(["Team", "Weight"], axis = 1, inplace = True)

# display
print(data)



import pandas as pd

# dataframe of height and weight football players
df = pd.DataFrame({
    'Height': [167, 175, 170, 186, 190, 188, 158, 169, 183, 180],
    'Weight': [65, 70, 72, 80, 86, 94, 50, 58, 78, 85],
    'Team': ['A', 'A', 'B', 'B', 'B', 'C', 'A', True, 'B', 'C']
})

# display the dataframe
print(df)

df.drop(df.index[df['Team'] == True], inplace=True)
print(df)


# importing Pandas library
import pandas as pd
# print(pd.read_csv("pokemon.csv"))

# import os
# print(os.getcwd())

# pd.read_csv(filepath_or_buffer = "pokemon.csv")

# makes the passed rows header
# print(pd.read_csv("pokemon.csv", header =[0]))

# # make the passed column as index instead of 0, 1, 2, 3....
# print(pd.read_csv("pokemon.csv", index_col ='Type'))

# uses passed cols only for data frame
print(pd.read_csv("pokemon.csv", usecols =["Type"]))




import pandas as pd

# list of name, degree, score
nme = ["aparna", "nikhil", "sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]

# dictionary of lists
dict = {'name': nme, 'degree': deg, 'score': scr}
	
df = pd.DataFrame(dict)

# saving the dataframe
df.to_csv('file-67.csv')



import pandas as pd

# list of name, degree, score
nme = ["aparna", "pankaj", "sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]

# dictionary of lists
dict = {'name': nme, 'degree': deg, 'score': scr}
	
df = pd.DataFrame(dict)

# saving the dataframe
df.to_csv('file219.csv', header=False, index=False)



import pandas as pd

# making data frame
data = pd.read_csv("nba.csv")

# calling head() method
# storing in new variable
data_top = data.head()
data_tail = data.tail(3)

# display
print(data_top)
print(data_tail)



import pandas as pd

# making data frame
data = pd.read_csv("nba.csv")

# number of rows to return
n = 9

# creating series
series = data["Name"]

# returning top n rows
top = series.head(n)


# display
print(top)

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