import matplotlib.pyplot as plt
import numpy as np

def plot(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a vector of dimension m * 1.
    y: has to be an numpy.array, a vector of dimension m * 1.
    theta: has to be an numpy.array, a vector of dimension 2 * 1.
    Returns:
    Nothing.
    Raises:
    This function should not raise any Exceptions.
    """
    if all(isinstance(a, np.ndarray) for a in [x,y,theta]):
        # m, b = np.polyfit(x,y,1)
        m, b = theta[1], theta[0]
        tmp = []
        for i in x:
            tmp.append(m*i+b)
        plt.plot(x, tmp)
        plt.scatter(x, y)
        plt.show()
