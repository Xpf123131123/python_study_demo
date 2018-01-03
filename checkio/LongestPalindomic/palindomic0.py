"""

获取字符串中最长的回文
效率

"""


def longest_palindomic(text):
    '''
    将字符串从大到小,从左到右切片，对每一个切片进行判断是否是回文，如果是则直接返回
    eg: abcdefghh
        abcdefghh
        abcdefgh
        bcdefghh
        ...
        ...
        a
        b
        c
        ...
        h
    :param text:
    :return:
    '''
    for i in range(len(text), 0, -1):
        for j in range(len(text) - i + 1):
            s = text[j:j + i]
            if s == s[::-1]:
                return s



if __name__ == '__main__':
    assert longest_palindomic('abcdefghh') == 'hh'
    assert longest_palindomic('abcdefghhgfedcba') == 'abcdefghhgfedcba'
    pass