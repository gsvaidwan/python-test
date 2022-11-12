import matplotlib.pyplot as plt
import seaborn_test as sns

# loading dataset
data = sns.load_dataset("iris")
print(data)

# draw lineplot
sns.lineplot(x="sepal_length", y="sepal_width", data=data)

plt.show()




import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("iris")

# draw lineplot
sns.lineplot(x="sepal_length", y="sepal_width", data=data)

# setting the x limit of the plot
plt.ylim(2)

plt.show()




import seaborn as sns
import matplotlib.pyplot as plt

# load the tips dataset present by default in seaborn
tips = sns.load_dataset('tips')
sns.set_style('white')

# make a countplot
sns.countplot(x ='sex', data = tips)
plt.show()





import seaborn as sns
import matplotlib.pyplot as plt

# load the tips dataset present by default in seaborn
tips = sns.load_dataset('tips')
sns.set_style('darkgrid')

# make a countplot
sns.countplot(x ='sex', data = tips)
plt.show()




import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
plt.figure(figsize =(5,10))
sns.countplot(x ='sex', data = tips)
plt.show()




import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
sns.set_context('poster', font_scale = 0.5)
sns.countplot(x ='sex', data = tips, palette ='coolwarm')
plt.show()




import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("iris")

# draw lineplot
sns.lineplot(x="sepal_length", y="sepal_width", data=data)

# Removing the spines
sns.despine()
plt.show()






import seaborn
import matplotlib.pyplot as plt

# loading of a dataframe from seaborn
df = seaborn.load_dataset('tips')

# Form a facetgrid using columns with a hue
graph = seaborn.FacetGrid(df, col ="sex", hue ="day")
# map the above form facetgrid with some attributes
graph.map(plt.scatter, "total_bill", "tip", edgecolor ="w").add_legend()
# show the object
plt.show()




import seaborn
import matplotlib.pyplot as plt

# loading of a dataframe from seaborn
df = seaborn.load_dataset('tips')

# Form a facetgrid using columns with a hue
graph = seaborn.FacetGrid(df, row ='smoker', col ='time')
# map the above form facetgrid with some attributes
graph.map(plt.hist, 'total_bill', bins = 15, color ='orange')
# show the object
plt.show()




import seaborn
import matplotlib.pyplot as plt
# use to set style of background of plot
seaborn.set(style="whitegrid")

# loading data-set
tip = seaborn.load_dataset("tips")
seaborn.boxplot(x ='tip', y ='day', data = tip)
plt.show()