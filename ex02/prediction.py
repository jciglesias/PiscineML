import numpy as np

def simple_predict(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
    y_hat as a numpy.ndarray, a vector of dimension m * 1.
    None if x or theta are empty numpy.ndarray.
    None if x or theta dimensions are not appropriate.
    Raises:
    This function should not raise any Exception.
    """
    if parse(x, theta):
        y = []
        for xi in x:
            y.append(theta[0] + theta[1] * xi)
        return np.array(y)
    return None

@staticmethod
def parse(x, theta) -> bool:
    if isinstance(x, np.ndarray) and isinstance(theta, np.ndarray) and len(x) and len(theta) == 2:
        for j in theta:
            if not isinstance(j, np.integer):
                return False
        for i in x:
            if not isinstance(i, np.integer):
                return False
        return True
    return False
