from tkinter import E
import numpy as np
import matplotlib.pyplot as plt

X = np.array(sorted(np.random.rand(20) * 30)).reshape(-1, 1)
y = X.flatten() + np.random.normal(loc=0.0, scale=5.0, size=20) + 5

plt.scatter(X.flatten(), y)
plt.show()

X_norm = (X - X.mean()) / X.std()
y_norm = (y - y.mean()) / y.std()

plt.scatter(X_norm.flatten(), y_norm)
plt.show()

class LinearRegression:
    def __init__(self, lr, iters):
        self.lr = lr
        self.iters = iters

    def predict(self, X):
        return np.dot(self.W, X.T) + self.b

    def fit(self, X, y):
        self.W = np.zeros((1, X.shape[1]))
        self.b = np.zeros((X.shape[1], 1))
        for i in range(self.iters):
            residuals = self.update_weights(X, y)
            print(f'after iteration {i+1} sum of squared residuals {residuals}')
        return self

    def update_weights(self, X, y):
        yp = self.predict(X)
        # calculate error
        e = y - yp
        # gradient calculation
        dW = (1 / X.shape[0]) * np.dot((-2 * e), X)
        db = (1 / X.shape[0]) * np.sum(-2 * e, axis=1, keepdims=True)
        # update weights and bias
        self.W = self.W - (self.lr * dW)
        self.b = self.b - (self.lr * db)
        # calculate the sum of square residuals
        return np.sum(e**2)

lr = LinearRegression(0.000001, 1000)
lr.fit(X, y)
ypred = lr.predict(X).flatten()
print(lr.W, lr.b)
plt.scatter(X.flatten(), y)
plt.plot(X.flatten(), ypred)
plt.show()


lr = LinearRegression(0.01, 1000)
lr.fit(X_norm, y_norm)
ypred = lr.predict(X_norm).flatten()
print(lr.W, lr.b)
plt.scatter(X_norm.flatten(), y_norm)
plt.plot(X_norm.flatten(), ypred)
plt.show()