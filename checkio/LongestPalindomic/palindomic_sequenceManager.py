from difflib import SequenceMatcher


def longest_palindromic(text):
    match = SequenceMatcher(None, text, text[::-1]).find_longest_match(0, len(text), 0, len(text))

    return text[match[0]:match[0] + match[2]]


if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"