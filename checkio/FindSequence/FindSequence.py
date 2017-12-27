from collections import namedtuple

LengthBundle = namedtuple('LengthBundle', 'value west northwest north northeast')


OFFSETS = {
    'west': (0, -1),
    'northwest':( -1, -1),
    'north': (-1, 0),
    'northeast': (-1, 1),
}


def checkio(matrix, line_length=4):

    # line_lengths is a matrix containing line lengths ending at the given cell
    line_lengths = [[] for _ in range(len(matrix))]
    def length_at_cell(value, r, c, direction):
        'Retrieve a value from the solution matrix, or none if out of bounds'
        ro, co = OFFSETS[direction]
        r += ro
        c += co
        if r >= 0 and 0 <= c < len(matrix) and line_lengths[r][c].value == value:
            return getattr(line_lengths[r][c], direction) + 1
        return 1

    for ri, row in enumerate(matrix):
        for ci, cell in enumerate(row):
            left = length_at_cell(cell, ri, ci, 'west')
            topleft = length_at_cell(cell, ri, ci, 'northwest')
            top = length_at_cell(cell, ri, ci, 'north')
            topright = length_at_cell(cell, ri, ci, 'northeast')
            s = LengthBundle(cell, left, topleft, top, topright)
            if any(x == line_length for x in s[1:]):
                return True
            line_lengths[ri].append(s)
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