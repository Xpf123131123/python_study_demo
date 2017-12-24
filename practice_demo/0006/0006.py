"""
第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

"""



import os
import sys

demoPath = '/Users/pengfeixu/PycharmProjects/python_study_demo'

fileList = []
pycFileList = []
democount = 0
spacecount = 0
commentcount = 0

for dirPath, subdirPath, filePath in os.walk(demoPath):
    # print('目录结构', dirPath)
    # print('子目录结构', subdirPath) # 是一个数组，包含了当前目录下的所有子目录
    # print('文件',  filePath) # 是一个数组，包含了当前目录下的所有文件(不包含子目录中的文件)
    for file in filePath:
        if file.endswith('.py'):# or file.endswith('.java') or file.endswith('.js')
            fileList.append('{}/{}'.format(dirPath, file))
        elif file.endswith('.pyc'):
            pycFileList.append('{}/{}'.format(dirPath, file))
        else:
            # print('文件过滤: ', dirPath.join(file))
            pass




# filelist 统计



for file in fileList:
    # print('======================================================')
    if file.endswith('/__init__.py'):
        # print('__init__.py 文件过滤')
        continue

    try:
        with open(file) as f:
            for line in f:
                if line == '\n': # 空行只有\n
                    spacecount += 1
                    # print('--------')
                elif line.startswith('#'):
                    commentcount += 1
                    # print('******** : ' + line)
                else:
                    democount += 1
                    if '#' in line: # 同时包含代码和注释
                        commentcount += 1
                    # print('0000000 : ' + line)

    except IOError:
        print('cannot open file')
    except Exception as ex:
        print(ex)


print(fileList)
print('代码行数:', democount)
print('注释行数:', commentcount)
print('空行行数:', spacecount)


# pyc filelist 统计
















