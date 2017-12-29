from itertools import chain, repeat
import re


def checkio(matrix):
    n = len(matrix)
    for row in chain(
            (zip(range(n), repeat(k)) for k in range(n)),
            (zip(repeat(k), range(n)) for k in range(n)),
            (zip(range(n), range(k, n)) for k in range(n - 3)),
            (zip(range(n), range(k, n)) for k in range(n - 3)),
            (zip(range(k, n), range(n)) for k in range(1, n - 3)),
            (zip(range(n), reversed(range(k, n))) for k in range(n - 3)),
            (zip(range(k, n), reversed(range(n))) for k in range(1, n - 3))):
        if re.findall(r'(\d)\1{3}',
                      ''.join(str(matrix[i][j]) for i, j in row)):
            return True
    else:
        return False