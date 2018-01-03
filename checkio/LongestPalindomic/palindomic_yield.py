def substrings(string):
    l = len(string)
    for n in range(l, 0, -1):
        for i in range(l - n + 1):
            yield string[i:n+i]

def longest_palindromic(string):
    return next(sub for sub in substrings(string) if sub == sub[::-1])


if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
    assert longest_palindromic("abc") == "a", "The A"
    assert longest_palindromic("") == "", "The A"