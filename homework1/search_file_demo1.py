# !/bin/env Python3
# -*- encoding=UTF-8 -*-
# author : xpf
# search files with input keywords
# 根据关键字搜索当前目录下的文件

import sys
import os

# 文件地址
filePath = os.path.realpath(__file__)
# 文件所在目录
dirPath = os.path.dirname(__file__)

# 忽略某些文件
def ignoreFile(*ignore):
    def new_func(func):
        def new(keywords, list):
            list1 = []
            for file in list:
                i = 0
                for ig in ignore:
                    if ig in file:
                        break
                    else:
                        i += 1
                        if i == len(ignore):
                            list1.append(file)
            return func(keyWords, list1)
        return new
    return new_func


def getDirTrees(rootPath):
    list = []
    for dirName, subdirList, fileList in os.walk(rootPath):
        list.append(dirName)
        for fname in fileList:
            list.append(fname)
    return list

# 搜索时忽略.csh .sh文件
@ignoreFile('.csh', '.sh')
def getResultWithKeyAndList(keywords, list):
    if keywords and list:
        result = []
        for file in list:
            if keyWords in file:
                result.append(file)
        return result
    else:
        return []


if __name__ == '__main__':
    keyWords = input('请输入您要搜索的关键字：')
    list = getDirTrees('d:\\Git') # 地址写死了， 可以改成当前目录下的文件dirPath
    result = getResultWithKeyAndList(keyWords, list)
    print(len(result))
    print(result)


    """文件地址及目录获取方法"""
    '''
    print("当前文件地址: " + filePath)
    print("当前文件所在目录: " + dirPath)
    print("__file__ = " + __file__)
    print("os.path.realpath(__file__) = " + os.path.realpath(__file__))
    print("os.path.dirname(__file__) = " + os.path.dirname(__file__))
    print("os.path.split(__file__) = " + os.path.split(__file__)[0])
    print("os.path.abspath(__file__) = " + os.path.abspath(__file__))
    print("os.getcwd() = " + os.getcwd())
    print("sys.path[0] = " + sys.path[0])
    print("sys.argv[0] = " + sys.argv[0])
    '''
