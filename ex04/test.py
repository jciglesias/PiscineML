import numpy as np
from prediction import predict_

x = np.arange(1,6)
# Example 1:
theta1 = np.array([[5], [0]])
print(f"Example 1:\n{predict_(x, theta1)}")
# Ouput:
# array([[5.], [5.], [5.], [5.], [5.]])
# Do you remember why y_hat contains only 5’s here?
# Example 2:
theta2 = np.array([[0], [1]])
print(f"Example 2:\n{predict_(x, theta2)}")
# Output:
# array([[1.], [2.], [3.], [4.], [5.]])
# Do you remember why y_hat == x here?
# Example 3:
theta3 = np.array([[5], [3]])
print(f"Example 3:\n{predict_(x, theta3)}")
# Output:
# array([[ 8.], [11.], [14.], [17.], [20.]])
# Example 4:
theta4 = np.array([[-3], [1]])
print(f"Example 4:\n{predict_(x, theta4)}")
# Output:
# array([[-2.], [-1.], [ 0.], [ 1.], [ 2.]])