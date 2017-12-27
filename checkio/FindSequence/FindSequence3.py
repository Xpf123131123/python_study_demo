def checkio(matrix):
    length = len(matrix)
    seq_min_len = 4

    def check_sequence(sy, sx, dy, dx):
        seq_lengths = [0]
        prev = matrix[sy][sx]
        while 0 <= sy < length and 0 <= sx < length:
            if matrix[sy][sx] == prev:
                seq_lengths[-1] += 1
                if seq_lengths[-1] >= seq_min_len:
                    return True
            else:
                seq_lengths.append(1)
                prev = matrix[sy][sx]

            sy += dy
            sx += dx

        return False

    # (start cell(y ,x), next cell direction(y, x), (sequence check directions(y, x)))
    routes = [
        [(0, 0), (1, 0), ((0, 1), (1, 1), (-1, 1))],
        [(0, 0), (0, 1), ((1, 0), (1, 1))],
        [(1, length - 1), (1, 0), ((1, -1),)],
    ]
    for start_cell, next_cell, directions in routes:
        y, x = start_cell
        while y < length and x < length:
            for direc in directions:
                if check_sequence(y, x, direc[0], direc[1]):
                    return True
            y += next_cell[0]
            x += next_cell[1]

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