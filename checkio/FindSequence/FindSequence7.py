def checkio(mx):
    def check_row(row):
        """
        Check one row
        """
        for item in row:
            for inx in range(len(row) - 3):
                if len(set(row[inx: inx + 4])) == 1:  # three equals make set of one
                    return True
        return False

    def hz_check(data):
        """
        Check horizontal rows
        """
        for row in data:
            if check_row(row):
                return True
        return False

    def ve_check(data):
        """
        Check vertical columns
        """
        for col in range(len(data)):
            column = [data[row][col] for row in range(len(data))]
            if check_row(column):
                return True
        return False

    def diag_check(data):
        """
        Check all diagonals
        """
        for inx in range(len(data) - 2):
            diag_main_and_down = [data[row][row - inx] for row in range(inx, len(data))]
            if check_row(diag_main_and_down):
                return True

        for inx in range(len(data) - 3):
            diag_up = [data[row][row + inx + 1] for row in range(len(data) - inx - 1)]
            if check_row(diag_up):
                return True
        return False

    def mirror_mx_up(data):
        """
        Mirror up in order to check diagonals again
        """
        lst = list(data)
        lst.reverse()
        return lst

    # let's try
    return any([hz_check(mx),
                ve_check(mx),
                diag_check(mx),
                diag_check(mirror_mx_up(mx))])

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