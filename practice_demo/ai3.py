import numpy as np

def nonlin(x, deriv=False):
    if (deriv==True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# output dataset
y = np.array([[0, 0, 1, 1]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

syn0 = 2 * np.random.random((3, 1)) - 1
print(syn0)

for iter in range(10000):
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))

    l1_error = y - l1

    l1_delta = l1_error * nonlin(l1, True)

    syn0 += np.dot(l0.T, l1_delta)

print("Output After Training:")
print(l1)
print(np.atleast_2d([1,2,3]))

"""
X	输入数据集，形式为矩阵，每 1 行代表 1 个训练样本。
y	输出数据集，形式为矩阵，每 1 行代表 1 个训练样本。
l0	网络第 1 层，即网络输入层。
l1	网络第 2 层，常称作隐藏层。
syn0	第一层权值，突触 0 ，连接 l0 层与 l1 层。
*	逐元素相乘，故两等长向量相乘等同于其对等元素分别相乘，结果为同等长度的向量。
–	元素相减，故两等长向量相减等同于其对等元素分别相减，结果为同等长度的向量。
x.dot(y)	若 x 和 y 为向量，则进行点积操作；若均为矩阵，则进行矩阵相乘操作；若其中之一为矩阵，则进行向量与矩阵相乘操作。
"""

"""
输入为x   输出为y
预测输出为l
隐藏层l1 l2 l3 l4 

x     l1      l2       l3       l
  syn0    syn1    syn2     syn3

l1 = x * syn0 * sig     

l2 = l1 * syn1 * sig    l1_error = div * (l2_error * syn2) l1_delta = l1_error * l1

l3 = l2 * syn2 * sig    l2_error = div * (l3_error * syn3) l2_delta = l2_error * l2

l = l3 * syn3 * sig     l3_error = (y - l)   l3_delta = div *  l3_error * l3

delta = l3_error * l3

syn3 = syn3 + (v) * div(l) * (y - l) * l3 


"""

l = [1, 2, 3, 4]
l_arr = np.atleast_2d(l)


print(l_arr.shape[1])

