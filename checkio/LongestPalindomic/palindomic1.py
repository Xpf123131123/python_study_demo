def longest_palindromic(text):
    if text == '':
        return ''

    if text == text[::-1]:
        return text

    return max(
        sorted(
            [
                longest_palindromic(text[1:]),
                longest_palindromic(text[:-1])
            ],
            key=lambda x: text.find(x)
        ),
        key=lambda x: len(x)
    )


import re

r = re.findall(r'[o]{3}', 'baooorrrrrrrrrrrrrrr')
r = re.split(r'[o]{3}', 'baooorrrrrrrrrrrrrrr')
print(r)

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
    assert longest_palindromic("abc") == "a", "The A"
    assert longest_palindromic("") == "", "The A"