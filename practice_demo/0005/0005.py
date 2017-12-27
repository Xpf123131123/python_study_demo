"""
第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

"""

from PIL import Image
import sys, os


# 文件地址
filePath = os.path.realpath(__file__)
# 文件所在目录
dirPath = os.path.dirname(__file__)


imageList = []
for dirName, subdirList, fileList in os.walk(dirPath):
    for file in fileList:
        imageList.append(file)


size = (128, 128)


def convertFilesToJPEG(imageList):
    # 替换文件后缀
    for infile in imageList:
        f, e = os.path.splitext(infile)
        outfile = f + '.jpg'
        print(infile)
        if infile != outfile:
            try:
                Image.open(infile).save(outfile)
            except IOError:
                print('cannot convert', infile)
    pass

def createJPEGThumbnails(imageList):
    # 缓存文件
    for infile in imageList:
        outfile = os.path.splitext(infile)[0] + '.thumbnail'
        if infile != outfile:
            try:
                im = Image.open(infile)
                im.thumbnail(size)
                im.save(outfile, 'JPEG')
            except IOError:
                print('cannot create thumbnail for', infile)
    pass

def identifyImageFiles(imageList):
    for infile in imageList:
        try:
            with Image.open(infile) as im:
                print(infile, im.format, "%dx%d" % im.size, im.mode)
        except IOError:
            pass

