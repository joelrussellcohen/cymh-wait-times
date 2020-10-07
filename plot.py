import matplotlib.pyplot as pyplot
import numpy as np
import pandas as pd

# Plot the data as a scatter plot
def scatter_plot(x, y, filename=None, xlabel=None, ylabel=None, show=True):
    pyplot.plot(x, y, 'ro')
    pyplot.xlabel(xlabel)
    pyplot.ylabel(ylabel)
    if filename:
        pyplot.savefig('./saved_images/%s' % filename, bbox_inches='tight', pad_inches=0.2)
    if show:
        pyplot.show()

if __name__ == "__main__":
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

    # To save the scatter plot, set filename='name.png'
    scatter_plot(x,y,filename=None, ylabel='Average wait time (days)', xlabel='Number of new clients')


    # Plot the data as a bar graph
    sdas = data[:,0] # Service delivery areas
    scale_factor = 10 # Factor by which we are scaling number of new clients
    x_scaled = x / scale_factor

    pyplot.bar(sdas, x_scaled, width=0.25)
    pyplot.bar([s + 0.3 for s in sdas], y, width=0.25)

    pyplot.ylabel('Number of new clients / 10\nAverage wait time in days for new clients')
    pyplot.xlabel('Service Delivery Area #')
    pyplot.xticks(sdas)

    # Uncomment to the next comment to save the plot
    #pyplot.savefig('./saved_images/combined_bar.png', bbox_inches='tight', pad_inches=0.2)
    pyplot.show()

    # Plot the ratio of average wait time per number of new clients to each service delivery area as a bar graph
    ytox = [y[i]/x[i] for i in range(0,x.size)]
    
    df = pd.DataFrame({'sdas':sdas, 'ytox':ytox})
    df = df.sort_values('ytox')
    #print(df_sorted)
    #pyplot.bar('sdas','ytox',data=df_sorted)
    fig, ax = pyplot.subplots()
    df.plot(kind='bar', x='sdas', y='ytox', ax=ax)
    pyplot.ylabel('Average wait time in days for new clients : Number of new clients')
    pyplot.xlabel('Service Delivery Area #')
    #pyplot.xticks(sdas)
    
    pyplot.savefig('./saved_images/time_per_client', bbox_inches='tight', pad_inches=0.2)
    pyplot.show()