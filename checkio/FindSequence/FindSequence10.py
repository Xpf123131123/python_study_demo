def checkio(matrix):
    # find all unique FindSequence in matrix
    elements = (set([m for n in matrix for m in n]))

    # string that will have every row, column and diagonal apended to
    _list = ''

    for h in range(len(matrix)):
        _list += '.'

        # find all rows
        for v in range(len(matrix[0])):
            _list += str(matrix[h][v])
        _list += '.'

        # find all columns
        for v in range(len(matrix[0])):
            _list += str(matrix[v][h])
        _list += '.'

        # find all diagonals one way
        for v in range(len(matrix[0])):
            _list += '.'
            for n in range(len((matrix))):
                for m in range(len(matrix[0])):
                    if h - v == n - m:
                        _list += str(matrix[n][m])

        # find all diagonals the other way
        for v in range(len(matrix[0])):
            _list += '.'
            for n in range(len((matrix))):
                for m in range(len(matrix[0])):
                    if h + v == n + m:
                        _list += str(matrix[n][m])

    # check if unique FindSequence in matrix can be found in _list
    for e in elements:
        if str(e) * 4 in _list:
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