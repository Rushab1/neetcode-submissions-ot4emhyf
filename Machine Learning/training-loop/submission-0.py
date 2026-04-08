import numpy as np
from numpy.typing import NDArray
from typing import Tuple


class Solution:
    def __init__(self):
        self.w = np.zeros(1)
        self.b = 0

    def forward(self, X, y):
        return np.dot(X, self.w) + self.b

    def loss(self, y_hat, y):
        l = np.linalg.norm(y_hat - y) ** 2
        l /= len(y)
        return l

    def gradient(self, y_hat, y):
        # dl/dw = dl/dy_hat * dy_hat/ dw
        N = len(y)

        dl_dyhat = 2/N * (y_hat - y)
        dl_dw = np.dot(np.transpose(X), dl_dyhat)
        dl_db = np.sum(dl_dyhat)

        return dl_dw, dl_db

    def backward(self, dl_dw, dl_db, lr):
        self.w -= lr * dl_dw
        self.b -= lr * dl_db
        
    def epoch(self, X, y, lr):
        y_hat = self.forward(X, y)
        dl_dw, dl_db = self.gradient(y_hat, y)
        self.backward(dl_dw, dl_db, lr)

    def train(self, X: NDArray[np.float64], y: NDArray[np.float64], epochs: int, lr: float) -> Tuple[NDArray[np.float64], float]:
        # X: (n_samples, n_features)
        # y: (n_samples,) targets
        # epochs: number of training iterations
        # lr: learning rate
        #
        # Model: y_hat = X @ w + b
        # Loss: MSE = (1/n) * sum((y_hat - y)^2)
        # Initialize w = zeros, b = 0

        N = len(X)
        F = len(X[0])
        self.w = np.zeros([F, 1])
        y = np.reshape(y, (-1, 1))
        for epoch in range(epochs):
            self.epoch(X, y, lr)
        
        w, b = self.w, self.b

        return (np.round(w[0], 5), round(b, 5))
        

