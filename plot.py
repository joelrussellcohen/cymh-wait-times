import matplotlib.pyplot as pyplot
import numpy as np

# Extract the raw data from the text file
f = open('./data/data.txt')
data_raw = f.read().strip()
data_raw = data_raw.split('\n')
data_raw = [t.split() for t in data_raw]

for i in range(len(data_raw)):
    for j in range(len(data_raw[i])):
        data_raw[i][j] = float(data_raw[i][j])
f.close()

# Transform raw data into numpy array
data = np.array(data_raw)

# Store the columns we want to plot into their own variables
x = data[:,1] # x is the number of new clients
y = data[:,3] # y is the average wait time in days for new clients

# Plot the data as a scatter plot

pyplot.plot(x, y, 'ro')
pyplot.ylabel('Average wait time (days)')
pyplot.xlabel('Number of new clients')
pyplot.savefig('./saved_images/scatter_plot.png', bbox_inches='tight', pad_inches=0.2)
pyplot.show()

# Plot the data as a bar graph
sdvs = data[:,0] # Service delivery areas
scale_factor = 10 # Factor by which we are scaling number of new clients
x_scaled = x / scale_factor

pyplot.bar(sdvs, x_scaled, width=0.25)
pyplot.bar([s + 0.3 for s in sdvs], y, width=0.25)

pyplot.ylabel('Number of new clients / 10\nAverage wait time in days for new clients')
pyplot.xlabel('Service Delivery Area #')
pyplot.xticks(sdvs)

pyplot.savefig('./saved_images/combined_bar.png', bbox_inches='tight', pad_inches=0.2)
pyplot.show()
