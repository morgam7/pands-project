# Code for pands_project
# Author: Marcella Morgan

# Data frames

import pandas as pd
# Plotting

import matplotlib.pyplot as plt
# Fetching iris dataset from a url

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')


# Taking a quick look

df

# Inspect types

df.dtypes
# Description of dataset

df.describe()
# Converting data to numpy arrays

# sepal length
slen = df["sepal_length"]. to_numpy()

# sepal width
swidth = df["sepal_width"]. to_numpy()

# petal length
plen = df["petal_length"]. to_numpy()

# petal width
pwidth = df["petal_width"]. to_numpy()



# Making a simple plot

plt.plot(plen, pwidth, 'x') # 'x' variable here displays points as xs

# Axis labels

plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')

# Title

plt.title ('Iris Data Set')
plt.show()