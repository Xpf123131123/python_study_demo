from functools import reduce


def longest_palindromic(text):
    is_palindromic = lambda t: reduce(lambda x, y: x and y, [True] + [t[i] == t[-1 - i] for i in range(len(t) // 2)])

    lenght = len(text)
    for i in range(lenght):
        for j in range(i + 1):
            subtext = text[j:lenght - i + j]
            if is_palindromic(subtext): return subtext
    return ""


if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"