# Code for pands_project
# Author: Marcella Morgan


# Importing libaries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import sys

# Reading in the iris dataset
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

#  Outputting a summary of each variable to a single text file:

sys.stdout = open("summary.txt", 'w')

print ("Summary of Dataset:")

print (df.head)
print (df.tail)

print ("Summary of Values")

print(df.describe())

print ("Inspecting types")


print (df.dtypes)


# Converting data to numpy arrays

# sepal length
slen = df["sepal_length"]. to_numpy()

# sepal width
swidth = df["sepal_width"]. to_numpy()

# petal length
plen = df["petal_length"]. to_numpy()

# petal width
pwidth = df["petal_width"]. to_numpy()

# Histograms

plt.title('Histogram of Sepal Length')
plt.hist(slen)
plt.savefig("Sepal-lenght.png")
plt.close()

plt.title('Histogram of Sepal Width')
plt.hist(swidth)
plt.savefig("Sepal-width.png")
plt.close()

plt.title('Histogram of petal Length')
plt.hist(plen)
plt.savefig("Petal-lenght.png")
plt.close()

plt.title('Histogram of Petal Width')
plt.hist(pwidth)
plt.savefig("Petal-Width.png")
plt.close()



plt.title('Scatterplot of Petal Width and Petal length')
plt.plot(plen, pwidth, 'x')
plt.savefig("Petal_Width and Petal_length.png")
plt.close()

plt.title('Scatterplot of Sepal Width and Sepal length')
plt.plot(slen, swidth, 'x')
plt.savefig("Sepal_Width and Sepal_length.png")
plt.close()

plt.title('Scatterplot of Petal Width and Sepal length')
plt.plot(slen, pwidth, 'x')
plt.savefig("Petal_Width and Sepal_length.png")
plt.close()

plt.title('Scatterplot of Sepal Width and Petal length')
plt.plot(plen, swidth, 'x')
plt.savefig("Sepal_Width and Petal_length.png")
plt.close()


'''
# Axis labels

plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')

# Title

plt.title ('Iris Data Set')
plt.show()

'''