# Code for pands_project
# Author: Marcella Morgan
# Code to analyse the Iris dataset for my project for the Programming and Scripting module of the Higher Diploma 
# in Science in Data Analytics given by ATU Galway-Mayo.

# Importing libaries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

# Filtering dataset by variable to be used later.
slen = df["sepal_length"]
swidth = df["sepal_width"]
plen = df["petal_length"]
pwidth = df["petal_width"]

# Filtering dataset by species to be used later.
# I can filter the species column using a string - the name of each species
setosa = df[df['species'] =="setosa"]
versicolor = df[df['species'] =="versicolor"]
virginica = df[df['species'] =="virginica"]

# Filtering out the categorical variable. I needed to do this to make the corr() function work. But I ended up using the 
# numeric_only parameter instead which was neater.
numeric_data=df[["sepal_length","sepal_width","petal_length","petal_width"]] 
print("Quantitative Variables Only:")
print()
print(numeric_data)
print()

# Using groupby function to get the mean of the variables of each species.
print("Mean of each variable by species:")
print()
print(df.groupby("species").mean())
print()

# Using corr() function to get pearson's correlation for the variables.
# I need add the (numeric_only=True) parameter so it will disregard the speices column. This is a recent change in pandas.
print("Pearson's Correlation for each variable:")
print()
print(df.corr(method='pearson', numeric_only=True))
print()
correlation=df.corr(method='pearson', numeric_only=True) #labeling this to make it easier later when I make heatmap

# Making a pearson's correlation for each of the species to use later:
corr_setosa = setosa.corr(method='pearson', numeric_only=True)
corr_versicolor = versicolor.corr(method='pearson', numeric_only=True)
corr_virginica = virginica.corr(method='pearson', numeric_only=True)

# Histograms:

# Pyplot:
# I will use pyplot to make the histograms
# Writing a function to make a histogram and name elements
def histogram(var, name, colour): 
        plt.hist(var, alpha = 0.45, color = colour) # alpha parameter defines transparancy of histogram 
        plt.title(f"Histogram of {name}") # Using function to insert name
        plt.xlabel(f"{name} (cm)")
        plt.ylabel("Count")
        plt.savefig(f"Histogram of {name}")
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

# Creating the figure here will allow me to choose number of axes using plt.subplots()
fig, axes = plt.subplots(2, 2)  
# Making figure bigger to see all four plots clearly
fig.set_figwidth(12)
fig.set_figheight(12) 
fig.suptitle("Histograms with Species", fontsize=20) # I'm able to change font size of title here

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
pairplot = sns.pairplot(data=df, hue="species", corner=True).legend.set_bbox_to_anchor((.61, .6))
plt.savefig("Scatterplots with Species")
plt.close()

# Best Fit Line:

# I want to look at the correlation between the variables.
# I made a scatter plot with a best fit line using the lmplot function in Seaborn.
# Indicating species with 'hue'

sns.lmplot(x='petal_length', y="petal_width", data=df, hue="species").figure.suptitle("Petal Length and Petal Width")
plt.savefig("Best fit Petal Length and Width")
plt.close()

# I wanted to put these best fit lines on the same figure but lmplot does not support the 'ax' parameter I used earlier
# with the histograms 
# So I used regplot which works with the 'ax' parameter. But not with 'hue'! 
# So I used the species dataset I filtered ealier to make best fit lines for each species.

def regplot(var, name): 
    fig, axes = plt.subplots(2, 2)  
    fig.set_figwidth(12)
    fig.set_figheight(12) 
    fig.suptitle(f"Best Fit Line {name}",fontsize=20) 
    sns.regplot(data = var, x='petal_length', y="petal_width", ax=axes[0,0]).set_title("Petal Width/Height (cm)")
    sns.regplot(data = var, x='petal_length', y="sepal_width", ax=axes[0,1]).set_title("Petal Width/Sepal Height (cm)")
    sns.regplot(data = var, x='sepal_length', y="petal_width", ax=axes[1,0]).set_title("Sepal Width/Petal Height (cm)")
    sns.regplot(data = var, x='sepal_length', y="sepal_width", ax=axes[1,1]).set_title("Sepal Width/Height (cm)")
    plt.savefig(f"Best Fit {name}")
    plt.close()

regplot(setosa, "Setosa")
regplot(versicolor, "Versicolor")
regplot(virginica, "Virginica")

# Heatmap:

# Another way to visaulise correlation is to make a heatmap. 
 #I want to make four heatmaps and put them on the same figure:
fig, axes = plt.subplots(2, 2)  
fig.set_figwidth(16)
fig.set_figheight(16)
fig.suptitle("Heatmaps", fontsize=20)
# Seaborn again came in handy with its heatmap function. I used the pearson's correlation I did earlier.
# The 'cmap' parameter changes the colours. 
# The correlation values are printed in the boxes using 'annot' parameter.
sns.heatmap(correlation, cmap = "PuBu", ax=axes[0,0], linecolor = 'white', linewidths = 1, annot=True).set_title("All Species")
 # This is one barbie would like.
sns.heatmap(corr_setosa, cmap = "PuRd", ax=axes[0,1], linecolor = 'white', linewidths = 1, annot=True).set_title("Setosa")
# Adding the other species
sns.heatmap(corr_versicolor, cmap = "BuGn", ax=axes[1,0], linecolor = 'white', linewidths = 1, annot=True).set_title("Versicolor")
sns.heatmap(corr_virginica, cmap = "YlOrBr", ax=axes[1,1], linecolor = 'white', linewidths = 1, annot=True).set_title("Virginica")
plt.savefig("Heatmap")
plt.close()


