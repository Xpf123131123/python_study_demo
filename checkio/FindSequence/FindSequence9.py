def checkio(matrix):
    _len = len(matrix)

    verticals = [[m[i] for m in matrix] for i in range(_len)]

    diagonals = [[matrix[_len - 1 - i + j][j] for j in range(i + 1)] for i in range(_len)] + \
                [[matrix[j][_len - i + j] for j in range(i)] for i in range(_len - 1, 0, -1)] + \
                [[matrix[j][i - j] for j in range(i + 1)] for i in range(_len)] + \
                [[matrix[_len - i + j][_len - 1 - j] for j in range(0, i)] for i in range(_len - 1, 0, -1)]

    for elem in diagonals + verticals + matrix:
        if len(elem) >= 4:
            for digit in range(10):
                if str(digit) * 4 in ''.join(str(i) for i in elem):
                    return True

    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
    assert checkio([
        [1, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 2, 1, 1, 4],
        [4, 6, 5, 1, 1, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
    print('you win')