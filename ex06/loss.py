import numpy as np
import math

def loss_elem_(y, y_hat):
    """
    Description:
    Calculates all the elements (y_pred - y)^2 of the loss function.
    Args:
    y: has to be an numpy.array, a vector.
    y_hat: has to be an numpy.array, a vector.
    Returns:
    J_elem: numpy.array, a vector of dimension (number of the training examples,1).
    None if there is a dimension matching problem between X, Y or theta.
    None if any argument is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    if all(isinstance(a, np.ndarray) for a in [y, y_hat]):
        dif = []
        for x in range(len(y_hat)):
            dif.append([math.pow(y_hat[x] - y[x], 2)])
        return np.array(dif)
    return None
def loss_(y, y_hat):
    """
    Description:
    Calculates the value of loss function.
    Args:
    y: has to be an numpy.array, a vector.
    y_hat: has to be an numpy.array, a vector.
    Returns:
    J_value : has to be a float.
    None if there is a dimension matching problem between X, Y or theta.
    None if any argument is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    if all(isinstance(x, np.ndarray) for x in [y, y_hat]):
        dif = loss_elem_(y,y_hat)
        return dif.sum() / (2 * len(y))
    return None
