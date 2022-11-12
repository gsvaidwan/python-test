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