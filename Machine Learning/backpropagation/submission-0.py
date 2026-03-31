import numpy as np
from numpy.typing import NDArray
from typing import Tuple


class Solution:
    def backward(self, x: NDArray[np.float64], w: NDArray[np.float64], b: float, y_true: float) -> Tuple[NDArray[np.float64], float]:
        # x: 1D input array
        # w: 1D weight array
        # b: scalar bias
        # y_true: true target value
        #
        # Forward: z = dot(x, w) + b, y_hat = sigmoid(z)
        # Loss: L = 0.5 * (y_hat - y_true)^2
        # Return: (dL_dw rounded to 5 decimals, dL_db rounded to 5 decimals)
        
        z = np.dot(x, w) + b
        y_hat = 1 / (1 + np.exp(-z))

        # y = 1/1 + np.exp(-(Wx + b))
        # L = 0.5(y_hat-y_t)^2
        # dL = ...
        # = (y_hat - yt) * dy_hat 
        # = (y_hat - yt) * (-1 / (1 + np.exp(-z)) ^ 2 * d(np.exp(-z))
        # = - (y_hat - yt) / (1 + np.exp(-z)) ^ 2 * np.exp(-z) * (- dz) = ...

        gradient_common = (y_hat - y_true) / np.pow(1 + np.exp(-z), 2) * np.exp(-z)

        # dz/dw = x, dz/db = 1 
        dl_dw = gradient_common * x
        dl_db = gradient_common    
        return np.round(dl_dw, 5), round(dl_db, 5)