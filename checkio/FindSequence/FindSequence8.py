from itertools import groupby


def check_sequence(l):
    gr = [list(j) for i, j in groupby(l)]
    gr.sort(key=len)
    if len(gr[-1]) >= 4:
        return True
    return False


def diagonals(L):
    """
    http://stackoverflow.com/a/31373955/190597 (unutbu)
    >>> L = array([[ 0,  1,  2],
                   [ 3,  4,  5],
                   [ 6,  7,  8],
                   [ 9, 10, 11]])

    >>> diagonals(L)
    [[9], [6, 10], [3, 7, 11], [0, 4, 8], [1, 5], [2]]
    """
    h, w = len(L), len(L[0])
    return [[L[h - p + q - 1][q]
             for q in range(max(p - h + 1, 0), min(p + 1, w))]
            for p in range(h + w - 1)]


def antidiagonals(L):
    """
    >>> L = array([[ 0,  1,  2],
                   [ 3,  4,  5],
                   [ 6,  7,  8],
                   [ 9, 10, 11]])

    >>> antidiagonals(L)
    [[0], [3, 1], [6, 4, 2], [9, 7, 5], [10, 8], [11]]
    """
    h, w = len(L), len(L[0])
    return [[L[p - q][q]
             for q in range(max(p - h + 1, 0), min(p + 1, w))]
            for p in range(h + w - 1)]


def checkio(matrix):
    matrix_len = len(matrix)
    vertical = [[matrix[i][ii] for i in range(matrix_len)] for ii in range(matrix_len)]
    vertical = [check_sequence(i) for i in vertical]
    horizontal = [check_sequence(matrix[i]) for i in range(matrix_len)]
    diagonal = [check_sequence(i) for i in diagonals(matrix)]
    anty_d = [check_sequence(i) for i in antidiagonals(matrix)]

    if any(diagonal):
        return True
    if any(anty_d):
        return True
    if any(vertical):
        return True
    if any(horizontal):
        return True
    return False