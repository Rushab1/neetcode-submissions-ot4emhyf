import numpy as np
from numpy.typing import NDArray
from typing import List


class Solution:
    def forward(self, x: NDArray[np.float64], weights: List[NDArray[np.float64]], biases: List[NDArray[np.float64]]) -> NDArray[np.float64]:
        # x: 1D input array
        # weights: list of 2D weight matrices
        # biases: list of 1D bias vectors
        # Apply ReLU after each hidden layer, no activation on output layer
        # return np.round(your_answer, 5)

        y = x

        def activate(y: NDArray[np.float64]):
            return np.maximum(0, y)


        for i, w in enumerate(weights):
            z = np.dot(y, w) + biases[i]
            y = activate(z)

        return np.round(y, 5)