import matplotlib.pyplot as pyplot
import numpy as np
import pandas as pd

# Function scatter_plot
# Plot the data as a scatter plot
# Inputs:
# x - an array-like object that will be plotted with y along the horizontal axis
# y - an array-like object that will be plotted with x along the vertical axis
# filename - if specified, a string which contains the path to save the plot image to
# xlabel - if specified, a string which denotes the x label of the plot
# ylabel - if specified, a string which denotes the y label og the plot
# title - if specified, a string which denotes the title of the plot
# show - default: True, if show=False, suppresses display of the function
# Returns: none
def scatter_plot(x, y, filename=None, xlabel=None, ylabel=None, title=None, show=True):
    pyplot.plot(x, y, 'ro')
    pyplot.xlabel(xlabel)
    pyplot.ylabel(ylabel)
    if filename:
        pyplot.savefig(filename, bbox_inches='tight', pad_inches=0.2)
    if show:
        pyplot.show()

# Function combined_bar
# Plot the data as a scatter plot
# x - an m dimentional array-like object which sets the horizontal positions of the bar graphs
# y - an m, n dimentional array-like object which is represents a list of data to plot against x
# filename - if specified, a string which contains the path to save the plot image to
# xlabel - if specified, a string which denotes the contents of the x-axis
# ylabel - if specified, a string list of strings which denote the labels for the bars
# title - if specified, a string which denotes the title of the plot
# show - default: True, if show=False, suppresses display of the function
# Returns: None
def combined_bar(x, y_list, filename=None, xlabel=None, ylabel=None, title=None, width=0.25, show=True):
    for i in range(len(y_list[0,:])):
        pyplot.bar([s + i*width for s in x], y_list[:,i], width=width)
    pyplot.xlabel(xlabel)

    if(ylabel and type(ylabel) is not str):
        ylabel_str = ''
        for label in ylabel:
            ylabel_str += '%s\n' % label
        ylabel_str = ylabel_str[:-1]
        pyplot.ylabel(ylabel_str)
    else:
        pyplot.ylabel(ylabel)

    pyplot.title(title)

    if filename:
        pyplot.savefig(filename, bbox_inches='tight', pad_inches=0.2)
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
    bars = np.column_stack((x_scaled, y))
    ylabels = ['Number of new clients / 10', 'Average wait time in days for new clients']
    xlabel = 'Service Delivery areas'

    combined_bar(sdas, bars, xlabel=xlabel, ylabel=ylabels, show=False)
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