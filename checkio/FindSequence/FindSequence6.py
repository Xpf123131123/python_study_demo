REPEATING_VALUE = 4

def checkio(matrix):
    # Empty list to analyze repeating values
    string_list = []
    # Add all rows and columns
    string_list.extend([val for val in matrix])
    for offset in range(len(matrix)):
        string_list.append([j[offset] for i, j in enumerate(matrix)])
    # Add all matrix diagonals >= 4
    for offset in range(-(len(matrix)) + REPEATING_VALUE, len(matrix) - REPEATING_VALUE + 1):
        string_list.append([row[i+offset] for i, row in enumerate(matrix) if 0 <= i+offset < len(row)])
        string_list.append([row[-i - 1 - offset] for i, row in enumerate(matrix) if 0 <= i + offset < len(row)])
    # Check for repeating values (>= 4) in string_list array
    # Just try to find substring not to work with indexes
    for line_val in string_list:
        for val in line_val:
            if ''.join(([str(val)]*REPEATING_VALUE)) in ''.join(str(x) for x in line_val):
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