import matplotlib.pyplot as pyplot
import numpy as np
from plot import scatter_plot


def normal_equation(x, y):
    x = np.column_stack((np.ones(x.size), x)) # Add ones column to X
    x_transpose = np.transpose(x)
    theta = np.matmul(np.matmul(np.linalg.inv(np.matmul(x_transpose,x)),x_transpose),y) # (X'*X)-1Xy
    return theta

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

    # Turn the data into a numpy array
    data = np.array(data_raw)

    # Extract the client numbers and average wait times
    client_num = data[:,1]
    average_wait = data[:, 3]

    # Plot the number of functions vs the average wait time
    scatter_plot(client_num,average_wait,ylabel='Average wait time (days)', xlabel='Number of new clients', show=False)

    # Get the theta values from the for linear regression from the normal equation
    theta = normal_equation(client_num, average_wait)

    # Plot the hypotheses against the scatter plot
    line = np.linspace(0, np.max(client_num), 1000)
    pyplot.plot(line, line*theta[1] + theta[0])
    pyplot.text(50, 50, 'y = %fx + %f' % (theta[1], theta[0]))

    # Uncomment the following line to save the image
    # pyplot.savefig('./saved_images/linear_fit.png')
    pyplot.show()