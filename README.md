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
