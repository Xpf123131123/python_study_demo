# Returns true if the all elements are the same
def checkline(matrix, x, y, dx, dy):
    el = matrix[x][y]
    for i in range(1, 4):
        if el != matrix[x + i * dx][y + i * dy]:
            return False

    return True


# Returns true if the square 4x4 has the line with the same elements
def checkSquare(matrix, x, y):
    for i in range(0, 4):
        # Check horizontal lines
        if checkline(matrix, x + i, y, 0, 1):
            return True
        # Check vertical lines
        if checkline(matrix, x, y + i, 1, 0):
            return True

    # Check diagonals
    if checkline(matrix, x, y, 1, 1):
        return True

    if checkline(matrix, x + 3, y, -1, 1):
        return True


