# Iris Dataset

<div style="text-align: center;">

![Image of Iris](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Iris_%28plant%29.jpg/463px-Iris_%28plant%29.jpg)
</div>

This is the repository containing my project for the Programming and Scripting module of the [Higher Diploma in Science in Data Analytics given by ATU Galway-Mayo](https://www.gmit.ie/higher-diploma-in-science-in-computing-in-data-analytics). My lecturer was [Andrew Beatty](https://github.com/andrewbeattycourseware?tab=overview&from=2022-12-01&to=2022-12-31). The project is an anlysis of the famous [Iris dataset](https://archive.ics.uci.edu/dataset/53/iris).

To create this repository, I installed Python using [Anaconda](https://www.anaconda.com/download), and I used [Visual Studio Code](https://code.visualstudio.com/) as a text editor and terminal.

## Background on the Iris Dataset

The Iris Dataset was created by the British statistician and biologist Ronald Fisher in 1936. It contains measurements of various features of iris flowers, including sepal length, sepal width, petal length, and petal width and contains 150 samples of iris, with 50 samples from each of three species: setosa, versicolor, and virginica. Fisher's work highlights how the dataset can be used to demonstrate various statistical techniques and so the Iris Dataset has become a classic in the field of statistical analysis, serving as a benchmark for testing classification algorithms.

The Iris dataset is perfect for beginners in data analytics because it's simple and has a clear real-world application. We can visualise the flowers and understand why it's useful to study them. With features like the sepal and petal measurements, it's great for practicing classification and clustering techniques. And along with these quantative variables we get a qualitative one too - species.

## Python Libraries

<details><summary>Pandas</summary><br>
Pandas is a powerful data manipulation and analysis library, offering data structures like DataFrame for handling structured data effectively.</details><br>
<details><summary>Matplotlib</summary><br>
Matplotlib is a versatile plotting library that provides a MATLAB-like interface for creating a wide range of static, interactive, and animated visualizations.</details><br>
<details><summary>Seaborn</summary><br>
Seaborn is built on top of Matplotlib and provides a high-level interface for drawing attractive and informative statistical graphics.</details><br>
<details><summary>NumPy</summary><br>
NumPy is the fundamental package for scientific computing in Python, providing support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions.</details><br>
<details><summary>Warnings</summary><br>
The warnings module is used to handle warning messages, and warnings.filterwarnings('ignore') suppresses these warnings to improve the clarity of the output.</details><br>

## Summary and Pandas

I downloaded the dataset from [here](https://archive.ics.uci.edu/dataset/53/iris) as Andrew suggested, but this dataset did not come with headers. So I instead used the dataset from [Michael Waskon's github](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv). Initially I used the method where I read the data by linking to the url - Ian showed us how to do this, but I decided to download the dataset as if there were any issues with accessing github my code would not work.

For the summary.txt file I used the sys.stdout function to write the file. I then used pandas functions to summarise the data. The tricky part of this was the layout of the text file. Becasue the layout would be created by the python program I had less control over where text was placed. I used print() to print empty lines between each element.

The pandas functions were useful for filtering the data. I filtered the data by species and created numpy arrays for each variable. I also used the groupby function to get the mean of each variable for each species.

## Histograms

First I made a histogram for each variable using pyplot. Then, becasue I was interested in looking at the distribution of each species I used Seaborn's histplot function.

The tricky part here was understanding the difference between stateless and stateful plots. When I wanted to plot the four seaborn histograms on the same figure I needed to create a stateless plot so that I could control how many axes there were. But then I wasn't able to use the displot function that I had used for the Penguin project. Because displot works with stateful plots. I had to use the histplot function instead. This also made it a bit more clear the difference between plt and ax when using pyplot. When you use plt it creates the figure for you. But ax creates the axes only. So you have to create the figure first.

## Scatterplots

I used Seaborn's pairplot function here that is very straigtforward to use and doesn't require any filtering of data.

I then wanted to look at a best fit line to see how correlation petal and sepal width and lenght were. And I wanted these to be on the same figure. I used Seaborn's lmplot function for this. However I ran into the same issue as I did earlier. lmplot would not accept the ax parameter becasue it creates a stateful plot. 

# Correlation

Best fit line:

# I wanted to put these best fit lines on the same figure but lmplot does not support the 'ax' parameter I used earlier. 
# So this is another eg of stateful v stateless plots. 
# So I did some research and found that regplot would work with the 'ax' parameter but not with the 'hue'! So it woul
# So I used the filtered pandas 




One of the things that happened when I was making these plots was after I figured out how to make the plots and they were working and I was tidying up the presentation I changed the file name of the image and it was too long. But I didn't know that was causing the file to not save. It was saving as a txt file. I spent literal hours trying to figure out what had happened that my plots were no longer saving. And that was all it was - the filename was too long!

## Links

Dataset:

https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

https://archive.ics.uci.edu/dataset/53/iris 

https://stackoverflow.com/questions/23464138/downloading-and-accessing-data-from-github-python

Markdown:

https://gist.github.com/citrusui/07978f14b11adada364ff901e27c7f61 

https://markdown.land/markdown-center

Pandas:

https://www.geeksforgeeks.org/pandas-groupby/

https://pandas.pydata.org/docs/user_guide/10min.html#min

https://stackoverflow.com/questions/44881307/pandas-how-to-hide-the-header-when-the-output-need-header-as-a-condition-to-filt

https://stackoverflow.com/questions/76533178/corr-results-in-valueerror-could-not-convert-string-to-float

https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/


figures and axes:
https://python-charts.com/matplotlib/title/?utm_content=cmp-true
https://stackoverflow.com/questions/12444716/how-do-i-set-the-figure-title-and-axes-labels-font-size

Histogram:

https://www.geeksforgeeks.org/how-to-plot-a-histogram-with-various-variables-in-matplotlib-in-python/

https://www.geeksforgeeks.org/matplotlib-pyplot-subplots-in-python/


Heatmap:

https://seaborn.pydata.org/generated/seaborn.heatmap.html
https://seaborn.pydata.org/tutorial/color_palettes.html
https://www.practicalpythonfordatascience.com/ap_seaborn_palette#spring-spring-r


Best fit line:
https://seaborn.pydata.org/generated/seaborn.regplot.html












