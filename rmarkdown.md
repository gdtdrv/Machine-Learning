Spatio-temporal prediction of ambulance calls
================

Dissertation project was done in cooperation with the North West Ambulance Service.

Project supervisors are Dr Anastasios Noulas from New York University and Dr Andrew Titman from Lancaster University.

### Exploratory Data Analysis

##### Clear weekly pattern for some types of problems

It is examined if the calls related to certain type of problems have stable temporal behavior through the year. This is tested by plotting the number of calls for each month in terms of hour of the week. It can be seen that there is a clear temporal pattern, which doesn't have monthly variations.

![](rmarkdown_files/figure-markdown_github/pressure-1.png)

##### Strong connection between human activities and ambulance calls

Normalised urban activity frequencies versus ambulance call frequencies. Check-ins at nightlife places such as Pubs present a strong alignment over time with Assault related ambulance calls. Hour 0 represents Monday 0-1am.

![](rmarkdown_files/figure-markdown_github/unnamed-chunk-1-1.png)

##### Some type of problems share temporal and spatial pattern

Analysing where and when calls from various types of problem occur, it turned out that some of them happen at the same place and at the same time.

![](E:/Job%20applications/gery/Documents/rmarkdown_files/figure-markdown_github/23m.png)

![](E:/Job%20applications/gery/Documents/rmarkdown_files/figure-markdown_github/25m.png)

##### Decomposition

Decompostion of time series showed trend, seasonality and mulitplicative relationship between them.

![](rmarkdown_files/figure-markdown_github/unnamed-chunk-2-1.png)

### Methods
