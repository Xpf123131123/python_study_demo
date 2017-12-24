"""
第 0008 题： 一个HTML文件，找出里面的正文。

第 0009 题： 一个HTML文件，找出里面的链接
"""

import urllib.request
import re


# 正则表达式
# 获取body内的信息
re_getBody = r'<body.*?>.*?</body>'
# 获取超链接内的网址
re_getHref = r'<a.*?href="(.*?)".*?>'
# 获取所有http开头的网页
re_getHTTP = r'(http:.*?)"'

# https:www.baidu.com
url = 'http://www.baidu.com/'
# url = 'http://blog.csdn.net/htdeyanlei/article/details/50866307'

def get_html_with_url(url):
    html = urllib.request.urlopen(url).read()
    return html

def saveHTMLToFile(filename, html):
    if not filename or not html:
        print('CANNOT READ FILENAME OR HTML!!!')
        return False

    writeSuccess = True
    try:
        with open(filename.replace('/', '_') + '.html', 'wb') as f:
            f.write(html)
    except IOError:
        writeSuccess = False
        print('CANNOT WRITE FILE TO FILEPATH!!!')

    return writeSuccess

def getHTMLBodyContent(html):
    start = html.find('<body')
    end = html.find('</body>')
    if not start or not end:
        print('CANNOT FIND BODY CONTENT WITH INPUT ELEMENT!!!')
        return None
    return html[start: end + 7]

html = get_html_with_url(url)
html = html.decode('utf-8')



bodys = re.findall(re_getBody, html, re.S)
# print(bodys[-1])
urls = re.findall(re_getHref, html, re.S)

# for url in urls:
#     print(url)

urls1 = re.findall(re_getHTTP, html, re.S)

for url in urls1:
    print(url)

body = getHTMLBodyContent(html)
# print(body)

#
# print(start, end)

# htmlPath = 'baidu.html'
# str = ''
# with open(htmlPath, 'rb') as f:
#     for line in f:
#        # str += ''.join(line)
#         print(line)
#
# print(str)



