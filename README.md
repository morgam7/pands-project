# Iris Dataset

<div style="text-align: center;">

![Image of Iris](https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5)
</div>

This is the repository containing my project for the Programming and Scripting module of the [Higher Diploma in Science in Data Analytics given by ATU Galway-Mayo](https://www.gmit.ie/higher-diploma-in-science-in-computing-in-data-analytics). My lecturer was [Andrew Beatty](https://github.com/andrewbeattycourseware?tab=overview&from=2022-12-01&to=2022-12-31). The project is an analysis of the famous [Iris dataset](https://archive.ics.uci.edu/dataset/53/iris).

To create this repository, I installed Python using [Anaconda](https://www.anaconda.com/download), and I used [Visual Studio Code](https://code.visualstudio.com/) as a text editor and terminal.

## Why this Project is useful

This is the first module of a two year course and I have no previous experience coding or working with datasets. So it is unlikely I will be adding much to the Iris dataset literature! But this project might be useful for people who are just starting out with data analytics. Or for future students of ATU's data analytics course. It might help with figuring out how to tackle the project.

## Background on the Iris Dataset

The Iris Dataset was created by the British statistician and biologist Ronald Fisher in 1936. It contains measurements of various features of iris flowers, including sepal length, sepal width, petal length, and petal width and contains 150 samples of iris, with 50 samples from each of three species: setosa, versicolor, and virginica. Fisher's work highlights how the dataset can be used to demonstrate various statistical techniques and so the Iris Dataset has become a classic in the field of statistical analysis, serving as a benchmark for testing classification algorithms.

The Iris dataset is perfect for beginners in data analytics because it's simple and has a clear real-world application. We can visualise the flowers and understand why it's useful to study them. With features like the sepal and petal measurements, it's great for practicing classification and clustering techniques. And along with these quantitative variables we get a qualitative one too - species.

## Python Libraries

<details><summary>Pandas</summary><br>
Pandas is a powerful data manipulation and analysis library, offering data structures like DataFrame for handling structured data effectively.</details><br>
<details><summary>Matplotlib</summary><br>
Matplotlib is a versatile plotting library that provides a MATLAB-like interface for creating a wide range of static, interactive, and animated visualizations.</details><br>
<details><summary>Seaborn</summary><br>
Seaborn is built on top of Matplotlib and provides a high-level interface for drawing attractive and informative statistical graphics.</details><br>
<details><summary>sys</summary><br>
The sys module in Python is a handy tool that provides access to system-specific parameters and functions. It helps you interact with the Python interpreter, access command line arguments, manage module search paths, and more.</details><br>
<details><summary>Warnings</summary><br>
The warnings module is used to handle warning messages, and warnings.filterwarnings('ignore') suppresses these warnings to improve the clarity of the output.</details><br>

## Dataset

I downloaded the dataset from [here](https://archive.ics.uci.edu/dataset/53/iris) as Andrew suggested, but this dataset did not come with headers. So I instead used the dataset from [Michael Waskom’s github](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv). Initially I used the method where I read the data by linking to the url - Ian showed us how to do this, but I decided to download the dataset as if there were any issues with accessing github my code would not work.

## Summary and Pandas

For the summary.txt file I used the [sys.stdout](https://docs.python.org/3/library/sys.html#sys.stdout) function to write the file. The tricky part of this was the layout of the text file. Because the layout would be created by the python program I had less control over where text was placed. I used print() to print empty lines between each element.

I then used pandas functions to summarise the data. The pandas functions were useful for filtering the data. I filtered the data by species and variable. I also used the [groupby()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html) function to get the mean of each variable for each species. 

I also used the [corr()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html) function to find the correlation between the variables of each species using Pearson’s correlation coefficient. I had an issue here where the function would not work because of the species column which contains categorical values. So I filtered the dataset to get one with only the numerical values. Then I found out that I could use the [numeric_only parameter](https://stackoverflow.com/questions/76533178/corr-results-in-valueerror-could-not-convert-string-to-float) which was a neater way to do it.

### Links that helped:

https://stackoverflow.com/questions/23464138/downloading-and-accessing-data-from-github-python

https://pandas.pydata.org/docs/user_guide/10min.html#min

https://learnpython.com/blog/how-to-summarize-data-in-python/

https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/

https://www.w3schools.com/python/pandas/pandas_correlations.asp

https://stackoverflow.com/questions/76533178/corr-results-in-valueerror-could-not-convert-string-to-float

https://stackoverflow.com/questions/13872049/print-empty-line

## Histograms

First I made a histogram for each variable using pyplot. Then, because I was interested in looking at each species separately, I made histograms using Seaborn's [histplot function](https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn-histplot). This allowed me to use the [hue parameter](https://www.statology.org/seaborn-histogram-hue/) to separate the species.

The tricky part here was understanding the difference between axes level and figure level plotting functions. When I wanted to plot the four seaborn histograms on the same figure I needed to create an empty figure so that I could control how many axes there were. But then I wasn't able to use the [displot function](https://seaborn.pydata.org/generated/seaborn.displot.html) that I had used for the Penguin project I did for Ian's course. Displot is a figure level function, so it creates the figure as it creates the plot. So I had to use the histplot function instead. And use pyplot to create the figure.

### Reading the plots:

The individual histograms didn't really tell me much. When they were separated out into species I could see that there was a standard distribution across all the variables in each species, which would be expected. 

Looking at the Petal Length and Petal Width histogram there is a clear separation between the Setosas and the two other species. So petal length and petal width could be used to classify the Setosas. You could safely say that if an iris has a petal length of less than 2.5cm and a petal width of less than .75cm then the flower is likely a setosa.

Another thing to take away from the petal histograms is how much narrower the distribution was with the Setosas. So they are more uniform in petal size.

### Links that helped:

https://www.geeksforgeeks.org/how-to-plot-a-histogram-with-various-variables-in-matplotlib-in-python/

https://www.geeksforgeeks.org/matplotlib-pyplot-subplots-in-python/

https://www.geeksforgeeks.org/matplotlib-pyplot-hist-in-python/

https://seaborn.pydata.org/tutorial/function_overview.html

https://www.w3schools.com/python/matplotlib_subplot.asp

https://www.w3schools.com/python/matplotlib_subplot.asp

## Scatterplots

I used [Seaborn's pairplot function](https://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn-pairplot) here to make the scatterplots. It also made four KDE plots for each of the variables. The pairplot function is very straightforward to use and doesn't require any filtering of data. The only tricky thing was figuring out how to place the legend as the default positioned the legend in an awkward way.

### Reading the Plots:

Looking at the scatterplots it is clear that the species cluster in most of the variables, with there being a very clear demarcation with the Setosas. The petal variables are the most useful for classification as there was more of an overlap with the sepal variables. Also the scatterplots clearly show that that setosas are the smallest flowers except when it comes to sepal width. Across all other variables the Setosas are the smallest with the Versicolor being the next biggest with the Virginica being the largest.

So the scatterplots backed up the findings from the histograms.

### Links that helped:

https://www.geeksforgeeks.org/data-visualization-with-pairplot-seaborn-and-pandas/?ref=lbp

https://stackoverflow.com/questions/27019079/move-seaborn-plot-legend-to-a-different-position

## Best Fit Line:

Next I looked at the correlation between the variables of each species. I thought it would be interesting to see if there was any correlation between the length and width of the petals. Do they get longer as they get wider? So I made a scatter plot with a best fit line for the petal variables. I used [Seaborn's lmplot function](https://seaborn.pydata.org/generated/seaborn.lmplot.html) to do this and the handy 'hue' parameter to distinguish between species. 

I wanted to look the correlation of the other variables also. And I wanted to see if I could put these plots on the same figure. However I ran into the same issue as I did earlier with the histograms. lmplot would not accept the 'ax' parameter because it is a figure level function. It works with [FacetGrid](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid) and the [regplot function](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot) to make the figure and the axes at the same time.

So I decided to use regplot with the pyplot fig function to make a four-axes figure plotting the correlation between each of the variables. But while regplot works with the 'ax' parameter it does not work with the 'hue'! So I wasn't able to represent each species. So I used the filtered pandas datasets I made earlier to make three four axes figures, one for each of the species. 

This ended up being a bit of unnecessary work but it was really useful to get a sense of how each function comes with its own limitations. And I also gained a bit more understanding of the difference between stateful and stateless plots.

### Reading the Plots:

So do the petals get wider as they get longer? It looks like the answer is yes for the Versicolors. Not so much for the Virginicas. As for the Setosas, when I was looking at just the Implot plot with all the three species together, I initially thought that there was a strong correlation for the Setosas too.

However when I looked at the replot plots for the Setosas, where the datapoints are more spread out, the correlation does not seem to be there. So the way the data is represented - even just how tightly the datapoints are bunched together, can affect how the plots are read. So this was an interesting thing to learn and something to be wary of.

Looking further at the replot plots I can see there is a strong correlation between sepal length and width for the Setosas. And sepal length and petal length with the Versicolors.

### Links that helped:

https://datagy.io/python-pearson-correlation

https://datagy.io/seaborn-regplot-lmplot/

https://www.w3schools.com/python/python_ml_linear_regression.asp

https://python-charts.com/correlation/scatter-plot-regression-line-seaborn/

## Heatmap:

Another way to look at correlation is to use a Heatmap. I used Seaborn's very straightforward [heatmap function](https://seaborn.pydata.org/generated/seaborn.heatmap.html#seaborn-heatmap) and the Pearson’s correlation co-efficient that I made earlier with pandas. I made a heatmap for all species together and then one for each species. And I spent far too long playing around with the different colour palettes!

### Reading the Plots:

The heatmaps backed up the findings of the best fit line plots. It was useful to have the Pearson correlation co-efficient value in each cell. It backed up the finding that there is about the same amount of correlation between petal length and width with the Setosas and Virginicas, even though looking at the Implot plot it would appear to be more with the Setosas.

### Links that Helped:

https://seaborn.pydata.org/generated/seaborn.heatmap.html

https://seaborn.pydata.org/tutorial/color_palettes.html

https://www.practicalpythonfordatascience.com/ap_seaborn_palette#spring-spring-r

https://stackabuse.com/ultimate-guide-to-heatmaps-in-seaborn-with-python/

## Conclusion

In summary, my analysis of the Iris dataset revealed clear differences between the three Iris species, with Setosas standing out due to their distinct sepal and petal measurements. Setosas were particularly easy to identify because of their smaller petal length and width. Using heatmaps and best fit lines, we visualized these differences effectively. This analysis highlights why the Iris dataset is a classic example for learning about data analysis.

### Other Links that Helped:

https://python-charts.com/matplotlib/title

https://stackoverflow.com/questions/12444716/how-do-i-set-the-figure-title-and-axes-labels-font-size

https://datagy.io/matplotlib-title/

https://www.geeksforgeeks.org/change-plot-size-in-matplotlib-python/

https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html

https://gist.github.com/citrusui/07978f14b11adada364ff901e27c7f61 - Dropdown menu

https://markdown.land/markdown-center



























