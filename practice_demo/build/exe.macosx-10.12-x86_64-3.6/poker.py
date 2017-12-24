# encoding:utf-8
import random

list = []
count = 17
for i in range(0, count):
    if len(list) >= 17: break
    k = random.randint(0, 53)
    if k not in list:
        count -= 1
        list.append(k)
print(list)


# abs() 绝对值函数
a = abs(-1)
print(a) # 1

# all() 判断对象包含的元素是否全部为真，返回一个bool值，全部为真则true，否则为false
b = all(list)
print(b) # False

# any() 判断对象包含的元素是否有真，返回一个bool 有为true，无为false
c = any(list)
print(c) # True

# ascii() 返回Ascii
d = ascii('学习')
print(d) # '\u5b66\u4e60'

# bin() 传入一个数字，返回对应的二进制
e = bin(10)
print(e) # 0b1010
f = bin(0x11)
print(f) # 0b10001

# bool()
g = bool(e)
print(g) # True

# bytearray() 返回一个byte数组
h = bytearray(list)
print(h) # bytearray(b'2.\x02\x15\x11\x1c4\x06\x1d\x18\x08\x0c\x00 \x01')

#
import sys, math

def hash_fraction(m,n):
    P = sys.hash_info.__module__

    while m % P == n % P == 0:
        m, n = m // P, n // P

    if n % P == 0:
        hash_value = sys.hash_info.inf
    else:
        hash_value = (abs(m) % P) * pow(n, P - 2, P) % P
    if m < 0:
        hash_value = -hash_value
    if hash_value == -1:
        hash_value = -2
    return hash_value

def hash_float(x):
    if math.isnan(x):
        return sys.hash_info.nan
    elif math.isinf(x):
        return sys.hash_info.inf if x > 0 else -sys.hash_info.inf
    else:
        return hash_fraction(*x.as_integer_ratio())

























# mateData = [[0 for k in range(0, 13)] for i in range(0, 5)]
#
# for k in list:
#     mateData[int(k / 13)][int(k % 13)] += 1
#
# # print()
#
# list[1] = 0
#
# print(all(list))
#
# class A:
#     def __init__(self):
#         self.name = 'xpf'
#         self.age = 20
#
# def all_def(iter):
#     for obj in iter:
#         if not obj:
#             return False
#     return True
#
# a = A()
#
# s = 'xpfskdlsslds'
#
# for i in ascii(s):
#     print(i)
#
# # print(all(a))
#
# b = bin(10)
# print(b)
#
# bool([b])
#
# f = (not list) or s
# print(f)
# # and 判断是否都对，如果第一个为false，则返回false（第一个），否则判断第二个
# q = list and ''
# print(q)


