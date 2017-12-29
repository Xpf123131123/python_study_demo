import numpy as np
import re
def checkio(matrix):
    row = len(matrix)

    for x in range(row):
        horizontal = "".join(map(str,matrix[x]))
        vertical = "".join(map(str,np.transpose(matrix)[x]))
        diagonal_right = "".join([str(x) for x in np.diag(matrix, x)])
        diagonal_left = "".join([str(x) for x in np.diag(matrix, -1 * x)])
        diagonal_right_r = "".join([str(x) for x in np.diag(np.fliplr(matrix), x)])
        diagonal_left_r = "".join([str(x) for x in np.diag(np.fliplr(matrix), -1 * x)])

        if not re.search(r'(.)\1\1\1+', horizontal) is None or \
           not re.search(r'(.)\1\1\1+', vertical) is None or \
           not re.search(r'(.)\1\1\1+', diagonal_right) is None or \
           not re.search(r'(.)\1\1\1+', diagonal_left) is None or \
           not re.search(r'(.)\1\1\1+', diagonal_right_r) is None or \
           not re.search(r'(.)\1\1\1+', diagonal_left_r) is None:
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