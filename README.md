# cymh-wait-times
Modelling CYMH wait times using linear regression in python

## Introduction
This project intends to model average wait time for first service based on the number of clients recieving their first service in python using linear regression.
The motivation of this project is to demonstrate my ability to use python for data analysis.

# Part one
## Downloading the data
I got the data for this project from figure 3.02 on [this page](https://mcfd.gov.bc.ca/reporting/services/child-and-youth-mental-health/performance-indicators) from the [MCFD Reporting Portal](https://mcfd.gov.bc.ca/reporting/services).

**Average Days to First CYMH Service**
|Service Delivery Area|CYMH Clients Receiving Their First Clinical Service, Fiscal 2017/2018|Number of Clients that Had No Wait|Average Number of Days to First Service|
|----------------|----|---|---|
|Coast/North Shore|786|129|50.6|
|East Fraser|1,135|230|75.5|
|Kootenays|642|173|44.5|
|North Central|318|26|103.9|
|North Fraser|996|320|54.9|
|North Vancouver Island|923|57|55.4|
|Northeast|421|245|27.7|
|Northwest|429|149|45.7|
|Okanagan|1,454|132|63.2|
|South Fraser|995|175|87.5|
|South Vancouver Island|1,151|220|65.8|
|Thompson Cariboo Shuswap|1,012|374|34.0|
|Vancouver/Richmond||||	

I then stripped the commas and changed the names to classifiers 0-11 to make the data more easily computer readable (as outlined in data_dictionary.txt) and put the data into data.txt.

## Plotting the data
To get intuitions on data it is often useful to plot it. To plot data in python I am using the matplotlib pyplot. Installation instructions for which can be found [here](https://matplotlib.org/users/installing.html).
I made the python script plot.py to show me a scatter plot and a bar chart of Average wait times vs. Number of new clients.

## Scatter plot
**Average wait time in days vs Number of new clients**
![Average wait time in days vs Number of new clients](https://github.com/joelrussellcohen/cymh-wait-times/blob/main/saved_images/scatter_plot.png?raw=true)

As you can see from this graph, the service delivery area's kind of follow a linear trend. However there are a few outliers - note the dot in the top left corner.

## Bar chart
**Average wait time in days and number of new clients / 10 per service area**
![Average wait time in days and number of new clients / 10 per service area](https://github.com/joelrussellcohen/cymh-wait-times/blob/main/saved_images/combined_bar.png?raw=true)

I initially plotted this graph without scaling the number of new clients but the difference between the bars made it hard to read. Scaled down you can see that service delivery area #3, north central as is reffered to in the [data dictionary](https://github.com/joelrussellcohen/cymh-wait-times/blob/main/data/data_dictionary.txt), has disproportionatly long wait times when compared to the volume of new clients for other service areas.

