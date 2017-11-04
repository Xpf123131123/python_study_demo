def reverse(text):
    return text[::-1]

def isHuiWen(text):
    text1 = ''
    for item in text:
        if item >= 'a' and item <= 'z':
            text1 += item
        if item >= 'A' and item <= 'Z':
            text1 += item

    print(text1)
    return text1 == reverse(text1)


text = input('输入内容，判断是否回文:')

if isHuiWen(text):
    print('{} is hui wen'.format(text))
else:
    print('{} is not hui wen'.format(text))
