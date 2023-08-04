import numpy as np
from tools import add_intercept

def predict_(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a vector of dimension m * 1.
    theta: has to be an numpy.array, a vector of dimension 2 * 1.
    Returns:
    y_hat as a numpy.array, a vector of dimension m * 1.
    None if x and/or theta are not numpy.array.
    None if x or theta are empty numpy.array.
    None if x or theta dimensions are not appropriate.
    Raises:
    This function should not raise any Exceptions.
    """
    if parse(x, theta):
        tmp = add_intercept(x)
        ret = [[0] for _ in range(len(x))]
        for i in range(len(tmp)):
            for j in range(len(theta)):
                ret[i][0] += tmp[i][j] * theta[j][0]
        return np.array(ret)
    return None

@staticmethod
def parse(x, theta) -> bool:
    if isinstance(x, np.ndarray) and isinstance(theta, np.ndarray) and len(x) and len(theta) == 2:
        for j in theta:
            if not isinstance(j[0], (np.integer, float)):
                print(type(j[0]))
                return False
        for i in x:
            if not isinstance(i[0], (np.integer, float)):
                print(type(i))
                return False
        return True
    return False
