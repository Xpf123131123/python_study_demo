def is_palidrom(substr):
    return substr == substr[::-1]


def find_palidroms(substr, length):
    r = len(substr) - length
    return [substr[i:i + r] for i in range(length + 1) if is_palidrom(substr[i:i + r])]


def longest_palindromic(text):
    for length in range(len(text)):
        palidroms = find_palidroms(text, length)
        if palidroms:
            return palidroms[0]

if __name__ == '__main__':
    assert longest_palindromic("1") == "1", "digit one"
    assert longest_palindromic("abc") == "a", "one 'A'"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"