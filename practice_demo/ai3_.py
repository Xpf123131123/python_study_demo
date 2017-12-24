import numpy as np

X = [[1, 2, 3, 4],
     [3, 3, 4, 5]]

X = np.atleast_2d(X)

# 随机产生一个
i = np.random.randint(X.shape[0])
print(i)

a = [X[i]]
print(a)