# Code for pands_project
# Author: Marcella Morgan

# Importing libaries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import sys
import warnings
warnings.filterwarnings('ignore')

# Reading in the iris dataset
df = pd.read_csv('iris.csv')

# Summary using Pandas:

# Writing a summary of each variable to a single text file:
sys.stdout = open("summary.txt", 'w')

print ("Summary of Dataset:")
print ()
print ("First 5 lines:")
print (df.head()) 
print ("Last 5 lines:")
print (df.tail())
print ()
print ("Inspecting types:")
print ()
print (df.dtypes)
print ()
print ("Summary of Variables:")
print ()
print (df.describe())
print ()
print ("Number of each Species:")
print ()
print (df["species"].value_counts())
print ()

# Filtering dataset by variable and converting to numpy arrays to be used later.
slen = df["sepal_length"]. to_numpy()
swidth = df["sepal_width"]. to_numpy()
plen = df["petal_length"]. to_numpy()
pwidth = df["petal_width"]. to_numpy()

# Using groupby function to get the mean of the variables of each species.
print("Mean of each variable by species:")
print()
print(df.groupby("species").mean())


'''
# Histograms:

# Pyplot:
# I will use pyplot to make the histograms
# Writing a function to make a histogram and name elements
def histogram(var, name, colour): 
        plt.hist(var, alpha = 0.45, color = colour) # alpha parameter defines transparancy of histogram 
        plt.title(f"Histogram of {name}") # Using function to insert name
        plt.xlabel(f"{name} (cm)")
        plt.ylabel("Count")
        plt.savefig(f"{name} Histogram")
        plt.close() # Closing here or else the function will place each new histogram over the previous on the same axis.
                    # And I don't want to do this here but the transparency parameter would come in handy if I did.

# Inputitng arguments using subsets I made earlier with pandas
histogram(swidth, "Sepal Width", 'blue')
histogram(plen, "Petal Length", 'green')
histogram(pwidth, "Petal Width", 'orange')
histogram(slen, "Sepal Length", 'red')


# Seaborn:
# I want to see how the species differ across the variables so I will use Seaborn's histplot function. This will allow me to represent 
# the categroical variable 'species' with the 'hue' parameter.
# I will also display all four histograms on the same figure.

# Creating a stateless plot here that will allow me to choose number of axes 
fig, axes = plt.subplots(2, 2)  
# Making figure bigger to see all four plots clearly
fig.set_figwidth(12)
fig.set_figheight(8) 

# Using histplot function with ax parameter to put all four histograms on same figure
# .set_title lets me title each histogram 
sns.histplot(data = df, x = swidth, hue = "species", ax=axes[0,0]).set_title("Sepal Width (cm)")
sns.histplot(data = df, x = slen, hue = "species", ax=axes[0,1]).set_title("Sepal Length (cm)")   
sns.histplot(data = df, x = pwidth, hue = "species", ax=axes[1,0]).set_title("Petal Width (cm)")
sns.histplot(data = df, x = plen, hue = "species", ax=axes[1,1]).set_title("Petal Length (cm)")
plt.savefig("Histograms with Species")
plt.close()


# Scatterplots:

# Using Seaborn library to make the scatterplots with very handy pairplot function. This also 
# makes a KDE of each variable.
# The 'corner' parameter cuts of the repeated scatterplots. Using 'hue' again to display species.
# And anchoring the legend in a nicer position than the default
sns.pairplot(data=df, hue="species", corner=True).legend.set_bbox_to_anchor((.61, .6))
plt.savefig("Scatterplots with Species")
plt.close()

'''
# Best Fit Line:

# I was interested in looking at the correlation between sepal length and petal length and sepal width and petal width
# in each of the species.
# I made a scatter plot with a best fit line using the lmplot fucntion in Seaborn. 
# I indicating species with 'hue'

fig, axes = plt.subplots()
sns.lmplot(x="sepal_length", y="petal_length", data=df, hue="species").set_titles("Sepal Length and Petal Length")
plt.savefig("Sepal Length and Petal Length")
plt.close()

sns.lmplot(x='sepal_width', y="petal_width", data=df, hue="species").set_titles("Sepal Width and Petal Width")
plt.savefig("Sepal Width and Petal Width")
plt.close()



