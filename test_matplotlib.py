# importing matplotlib module
from matplotlib import pyplot as plt

# x-axis values
x = [5, 2, 9, 4, 7]

# Y-axis values
y = [10, 5, 8, 4, 2]

# Function to plot
plt.plot(x,y)

# function to show the plot
plt.show()



import matplotlib.pyplot as plt
l = ['Python', 'C++', 'Ruby', 'Java']
sizes = [215, 130, 245, 210]
# Plot
plt.pie(sizes, labels=l,autopct='%1.1f%%', shadow=True, startangle=180)
# plt.axis('equal')
plt.show()



import matplotlib.pyplot as plt
x =[25.0,25.0,27.0,4,5,6,78]

y =[6.2,6.6,6.5,3.4,6,6.5,9]
plt.scatter(x, y, c ="red")

# To show the plot
plt.show()


import matplotlib.pyplot as plt

# dataset-1
x1 = [89, 43, 36, 36, 95, 10,
	66, 34, 38, 20]

y1 = [21, 46, 3, 35, 67, 95,
	53, 72, 58, 10]

# dataset2
x2 = [26, 29, 48, 64, 6, 5,
	36, 66, 72, 40]

y2 = [26, 34, 90, 33, 38,
	20, 56, 2, 47, 15]

plt.scatter(x1, y1, c ="blue",
			linewidths = 2,
			marker ="s",
			edgecolor ="green",
			s = 50)

plt.scatter(x2, y2, c ="yellow",
			linewidths = 2,
			marker ="^",
			edgecolor ="red",
			s = 200)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


import pandas as pd
from matplotlib import pyplot as plt
csv_new1=pd.read_csv("D:\\PYTHON-TRAINING\\PANDAS-DEMO\\raw-data\\nba.csv", usecols=[0])
csv_new1.head()

csv_new2=pd.read_csv("D:\\PYTHON-TRAINING\\PANDAS-DEMO\\raw-data\\nba.csv", usecols=[8])
csv_new2.head()

x = csv_new1

y = csv_new2

# Function to plot
plt.plot(x,y)

# function to show the plot
plt.show()


import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.axis([0, 6, 0, 20])
plt.show()


import matplotlib.pyplot as plt

# year contains the x-axis values
# and e-india & e-bangladesh
# are the y-axis values for plotting

year = [1972, 1982, 1992, 2002, 2012]
e_india = [100.6, 158.61, 305.54, 394.96, 724.79]
e_bangladesh = [10.5, 25.21, 58.65, 119.27, 274.87]

# plotting of x-axis(year) and
# y-axis(power consumption)
# with different colored labels of two countries

plt.plot(year, e_india, color ='orange',
		label ='India')

plt.plot(year, e_bangladesh, color ='g',
		label ='Bangladesh')

# naming of x-axis and y-axis
plt.xlabel('Years')
plt.ylabel('Power consumption in kWh')

# naming the title of the plot
plt.title('Electricity consumption per capita\
of India and Bangladesh')

plt.legend()
plt.show()

dict = {'c':30,'c++':45, 'python':69,'r':56,'java':50}




import matplotlib.pyplot as plt
dict = {'c':30,'c++':45, 'python':69,'r':56,'java':50}
x=dict.keys()
y=dict.values()
x
y

plt.bar(x,y)
plt.show()

plt.bar(courses, values, color ='maroon',
		width = 0.4)


import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.axis([0, 6, 0, 20])
plt.show()

import matplotlib.pyplot as plt

# year contains the x-axis values
# and e-india & e-bangladesh
# are the y-axis values for plotting

year = [1972, 1982, 1992, 2002, 2012]
e_india = [100.6, 158.61, 305.54, 394.96, 724.79]
e_bangladesh = [10.5, 25.21, 58.65, 119.27, 274.87]

# plotting of x-axis(year) and
# y-axis(power consumption)
# with different colored labels of two countries

plt.plot(year, e_india, color ='orange',
		label ='India')

plt.plot(year, e_bangladesh, color ='g',
		label ='Bangladesh')

# naming of x-axis and y-axis
plt.xlabel('Years')
plt.ylabel('Power consumption in kWh')

# naming the title of the plot
plt.title('Electricity consumption per capita\
of India and Bangladesh')

plt.legend()
plt.show()


# import matplotlib.pyplot as plt
# dict = {'m':30,'c':45, 'e':69,'p':56,'h':50}
# x=dict.keys()
# y=dict.values()
# x
# y
# plt.title('Marks obtained of this student in this Year')
# plt.legend(x,y)
# plt.show()

import matplotlib.pyplot as plt
marks={'math':10,'chem':18,'phy':15,'bio':12,'eng':17}
n=marks.keys()
m=marks.values()
plt.bar(n,m)
plt.show()



import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.arange(0.0, 2.0, 0.01)
# print(x)
y = 1 + np.sin(2 * x)
z = 14-np.tan(4+x)
# Creating 6 subplots and unpacking the output array immediately
# fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3,2)
fig, ((ax1, ax2,ax3),( ax4,ax5, ax6)) = plt.subplots(2,3)
ax1.plot(x, y, color="orange")
ax2.plot(x, z, color="green")
ax3.plot(z, y, color="blue")
ax4.plot(y, z, color="magenta")
ax5.plot(x, y, color="black")
ax6.plot(x, y, color="red")
plt.show()




import numpy as np
import matplotlib.pyplot as plt

# create data
x=np.array([1, 2, 3, 4])

# making subplots
fig, ax = plt.subplots(2, 2)

# set data with subplots and plot
ax[0, 0].plot(x, x)
ax[0, 1].plot(x, x*2)
ax[1, 0].plot(x, x*x)
ax[1, 1].plot(x, x*x*x)

# set the title to subplots
ax[0, 0].set_title("Linear")
ax[0, 1].set_title("Double")
ax[1, 0].set_title("Square")
ax[1, 1].set_title("Cube")

# set spacing
fig.tight_layout()
plt.show()



import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

x1 = [1, 2, 3, 4, 5, 6]
y1 = [45, 34, 30, 45, 50, 38]
y2 = [36, 28, 30, 40, 38, 48]

labels = ["student 1", "student 2"]

fig.suptitle(' Student marks in different subjects ', fontsize=30)

# Creating the sub-plots.
l1 = ax1.plot(x1, y1, 'o-', color='g')
l2 = ax2.plot(x1, y2, 'o-')

fig.legend([l1, l2], labels=labels,
		loc="upper left")
# plt.subplots_adjust(left=0.9)

plt.show()



# import pandas as pd
# import matplotlib.pyplot as plt
# csv_new1=pd.read_csv("D:\\PYTHON\\py_prac\\data1.csv", usecols=[0])
# csv_new1.head()
# csv_new2=pd.read_csv("D:\\PYTHON\\py_prac\\data1.csv", usecols=[8])
# csv_new2.head()

# x = csv_new1
# y = csv_new2

# # Function to plot
# plt.plot(x,y)

# # function to show the plot
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
data = pd.read_csv("nba.csv")
d=data.head(5)
x1=d.Name
y1=d.Age
y2=d.Weight
labels = ["Age", "Weight"]

l1 = ax1.plot(x1, y1, 'o-')
l2 = ax2.plot(x1, y2, 'o-')

fig.legend([l1, l2], labels=labels,
		loc="upper left")

plt.show()
