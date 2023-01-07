# Sea Level Predictor
You will analyze a dataset of the global average sea level change since 1880. You will use the data to predict the sea level change through year 2050.
<br><br>
Use the data to complete the following tasks:
<br><br>
* Use Pandas to import the data from `epa-sea-level.csv`.
* Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axix.
* Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
* Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
* The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.

<br><br>
Sample of what the data looks like:
<br>
| Year |CSIRO Adjusted Sea Level	| Lower Error Bound	| Upper Error Bound |	NOAA Adjusted Sea Level |
| :---: | :---: | :---: | :---: | :---: |
1880 |	0	| -0.952755905 |	0.952755905 |	
1881	| 0.220472441	| -0.732283464 |	1.173228345 |	
1882 |	-0.440944881 |	-1.346456692 |	0.464566929	|
1883 |	-0.232283464 |	-1.129921259 |	0.66535433 |	
1884 |	0.590551181 |	-0.283464567 |	1.464566928	|
1885 |	0.531496062 |	-0.330708661	| 1.393700786 |	
