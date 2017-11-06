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

mateData = [[0 for k in range(0, 13)] for i in range(0, 5)]

for k in list:
    mateData[int(k / 13)][int(k % 13)] += 1

print(mateData)

