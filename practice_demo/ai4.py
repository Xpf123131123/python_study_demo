import numpy as np

###########非线性转化函数及其导数#############
# 激活函数
def tanh(x):
    return np.tanh(x)
# 激活函数的导数
def tanh_deriv(x):
    return 1.0 - np.tanh(x) * np.tanh(x)

# 激活函数1
def logistic(x):
    return 1 / (1 + np.exp(-x))
# 激活函数1的导数
def logistic_derivative(x):
    return logistic(x) * (1 - logistic(x))

class NeuralNetwork:
    def __init__(self, layers, activation='tanh'):
        if activation == 'tanh':
            self.activation = tanh
            self.activation_deriv = tanh_deriv
        elif activation == 'logistic':
            self.activation = logistic
            self.activation_deriv = logistic_derivative

        # 初始化权值函数
        self.weights = []
        for i in range(1, len(layers) - 1):
            self.weights.append((2 * np.random.random((layers[i - 1] + 1, layers[i] + 1)) - 1) * 0.25)
            self.weights.append((2 * np.random.random((layers[i] + 1, layers[i + 1])) - 1) * 0.25)


    def fit(self, X, y, learning_rate=0.2,epochs=1000):
        X = np.atleast_2d(X)
        # print(X)
        temp = np.ones([X.shape[0], X.shape[1] + 1])
        temp[:, 0:-1] = X
        # print(X)
        X = temp
        y = np.array(y)

        for k in range(epochs):
            i = np.random.randint(X.shape[0])
            a = [X[i]]
            for l in range(len(self.weights)):
                print('a : ', a)
                print('l : ', l)
                a.append(self.activation(np.dot(a[l], self.weights[l])))
            error = y[i] - a[-1]
            deltas = [error * self.activation_deriv(a[-1])]

            for l in range(len(a) - 2, 0, -1):
                deltas.append(deltas[-1].dot(self.weights[l].T) * self.activation_deriv(a[l]))
            deltas.reverse()

            for i in range(len(self.weights)):
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)

    def predict(self, x):
        x = np.array(x)
        temp = np.ones(x.shape[0] + 1)
        temp[0: -1] = x
        a = temp
        for l in range(0, len(self.weights)):
            a = self.activation(np.dot(a, self.weights[l]))
        return a


if __name__ == '__main__':
    nn = NeuralNetwork([3, 3, 1], 'logistic')
    x = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
    y = np.array([1, 0, 0, 1])
    nn.fit(x, y, 0.1, 1000)
    for i in [[0, 0, 1], [0,1, 1], [1, 0, 1], [1, 1, 1]]:
        # print(i)
        print(i, nn.predict(i))