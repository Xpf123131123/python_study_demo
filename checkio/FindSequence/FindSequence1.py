def checkio(matrix):
    print(len(matrix))
    m = matrix
    print(m)

    for i in range(len(matrix) - 1):
        for j in range(len(matrix) - 3):
            if m[i][j] == m[i][j + 1] == m[i][j + 2] == m[i][j + 3]:
                return True  # -----

    for i in range(len(matrix) - 3):
        for j in range(len(matrix) - 1):
            if m[i][j] == m[i + 1][j] == m[i + 2][j] == m[i + 3][j]:
                return True  # |||||

    for i in range(len(matrix) - 2):
        for j in range(len(matrix) - 2):
            if m[i][j] == m[i + 1][j + 1] == m[i + 2][j + 2] == m[i + 3][j + 3]:
                return True  # \\\\\\\\

    for i in range(len(matrix) - 2):
        for j in range(len(matrix) - 2):
            if m[i][len(matrix) - (1 + j)] == m[i + 1][len(matrix) - (2 + j)] == m[i + 2][len(matrix) - (3 + j)] == \
                    m[i + 3][len(matrix) - (4 + j)]:
                return True  # //////////
    # replace this for solution
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