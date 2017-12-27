import itertools

def longest_palindromic(text):
    lp, lp_len = '', 0
    for start, stop in itertools.combinations(range(len(text) + 1), 2):
        ss = text[start:stop]  # substring
        if (len(ss) > lp_len) and (ss == ss[::-1]):
            lp, lp_len = ss, len(ss)
    return lp

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"