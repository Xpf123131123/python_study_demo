"""
第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。
"""
import re

Path = 'EnglishWord.txt'

with open(Path, 'rb') as f:
    str = f.read()
    arr = str.split()
    print(arr)
    words = {}
    for word in arr:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1


    print(words)

