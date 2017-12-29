import random
import string
"""
第 0001 题： 做为 Apple Store App 独立开发者，
你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
"""

"""
思路: 根据时间生成
"""

def produce(count, length):
    arr = []
    choice = string.ascii_letters + "0123456789"
    for i in range(count):
        ran = ''
        for j in range(length):
            ran += random.choice(choice)
        if ran in arr:
            i -= 1
        else:
            arr.append(ran)

    print(arr)
    pass

if __name__ == '__main__':
    produce(200, 20)
